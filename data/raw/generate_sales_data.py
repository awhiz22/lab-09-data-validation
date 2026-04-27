"""
generate_sales_data.py

Generates a messy e-commerce sales dataset for a data validation lab.
"""

import pandas as pd
import numpy as np


def generate_sales_data(n=300, seed=42):
    np.random.seed(seed)

    sales = pd.DataFrame({
        "order_id": np.arange(1000, 1000 + n),
        "customer_id": np.random.randint(1, 80, size=n),
        "product_id": np.random.randint(200, 230, size=n),
        "revenue": np.round(np.random.normal(loc=200, scale=75, size=n), 2),
        "quantity": np.random.randint(1, 6, size=n),
        "unit_price": np.round(np.random.normal(loc=50, scale=15, size=n), 2),
        "status": np.random.choice(
            ["Complete", "Cancelled", "Returned"],
            size=n,
            p=[0.72, 0.18, 0.10]
        ),
        "payment_method": np.random.choice(
            ["Credit Card", "Debit Card", "PayPal", "Gift Card"],
            size=n
        ),
        "region": np.random.choice(
            ["West", "East", "South", "Midwest"],
            size=n
        )
    })

    sales["order_date"] = pd.to_datetime("2023-01-01") + pd.to_timedelta(
        np.random.randint(0, 365, size=n), unit="D"
    )

    # --------------------------------------------------
    # Obvious data-quality issues
    # --------------------------------------------------

    duplicate_indices = np.random.choice(sales.index, size=12, replace=False)
    sales.loc[duplicate_indices, "order_id"] = sales.loc[duplicate_indices, "order_id"] - 1

    neg_revenue_indices = np.random.choice(sales.index, size=8, replace=False)
    sales.loc[neg_revenue_indices, "revenue"] = -abs(sales.loc[neg_revenue_indices, "revenue"])

    zero_quantity_indices = np.random.choice(sales.index, size=6, replace=False)
    sales.loc[zero_quantity_indices, "quantity"] = 0

    missing_customer_indices = np.random.choice(sales.index, size=12, replace=False)
    sales.loc[missing_customer_indices, "customer_id"] = np.nan

    future_date_indices = np.random.choice(sales.index, size=6, replace=False)
    sales.loc[future_date_indices, "order_date"] = pd.to_datetime("2035-01-01")

    outlier_indices = np.random.choice(sales.index, size=5, replace=False)
    sales.loc[outlier_indices, "revenue"] *= 25

    # --------------------------------------------------
    # Messy categorical issues
    # --------------------------------------------------

    status_noise = [
        "complete",
        " COMPLETE ",
        "completed",
        "Cancelled ",
        "CANCELLED",
        "return",
        "Returned ",
        "unknown"
    ]

    status_indices = np.random.choice(sales.index, size=25, replace=False)
    sales.loc[status_indices, "status"] = np.random.choice(status_noise, size=25)

    payment_noise = [
        "credit card",
        "CreditCard",
        " CREDIT CARD ",
        "paypal",
        "Pay Pal",
        "giftcard",
        "Unknown"
    ]

    payment_indices = np.random.choice(sales.index, size=20, replace=False)
    sales.loc[payment_indices, "payment_method"] = np.random.choice(payment_noise, size=20)

    region_noise = [
        "west",
        "WEST ",
        "east",
        " south ",
        "Mid-West",
        "Northeast",
        None
    ]

    region_indices = np.random.choice(sales.index, size=18, replace=False)
    sales.loc[region_indices, "region"] = np.random.choice(region_noise, size=18)

    # --------------------------------------------------
    # Hidden edge cases
    # --------------------------------------------------

    # 1. Revenue does not match quantity * unit_price
    mismatch_indices = np.random.choice(sales.index, size=20, replace=False)
    sales.loc[mismatch_indices, "revenue"] = np.round(
        sales.loc[mismatch_indices, "revenue"] * np.random.uniform(0.5, 1.8, size=20),
        2
    )

    # 2. Unit price is negative or zero
    bad_price_indices = np.random.choice(sales.index, size=6, replace=False)
    sales.loc[bad_price_indices[:3], "unit_price"] = 0
    sales.loc[bad_price_indices[3:], "unit_price"] = -abs(sales.loc[bad_price_indices[3:], "unit_price"])

    # 3. Cancelled orders still have large positive revenue
    cancelled_revenue_indices = sales[sales["status"] == "Cancelled"].sample(
        n=min(8, (sales["status"] == "Cancelled").sum()),
        random_state=seed
    ).index

    sales.loc[cancelled_revenue_indices, "revenue"] = np.round(
        np.random.uniform(150, 600, size=len(cancelled_revenue_indices)),
        2
    )

    # 4. Returned orders have quantity but no negative/adjusted revenue
    returned_indices = sales[sales["status"] == "Returned"].sample(
        n=min(6, (sales["status"] == "Returned").sum()),
        random_state=seed + 1
    ).index

    sales.loc[returned_indices, "revenue"] = np.round(
        np.random.uniform(100, 500, size=len(returned_indices)),
        2
    )

    # 5. Duplicate full rows, not just duplicate IDs
    full_duplicate_rows = sales.sample(n=5, random_state=seed + 2)
    sales = pd.concat([sales, full_duplicate_rows], ignore_index=True)

    # 6. Whitespace in column names
    sales = sales.rename(columns={
        "payment_method": "payment_method ",
        "region": " region"
    })

    # 7. A numeric-looking column stored as strings
    string_revenue_indices = np.random.choice(sales.index, size=10, replace=False)
    sales.loc[string_revenue_indices, "revenue"] = sales.loc[string_revenue_indices, "revenue"].astype(str)

    # 8. A few revenue values with dollar signs
    dollar_indices = np.random.choice(sales.index, size=5, replace=False)
    sales.loc[dollar_indices, "revenue"] = "$" + sales.loc[dollar_indices, "revenue"].astype(str)

    # 9. A few impossible customer IDs
    bad_customer_indices = np.random.choice(sales.index, size=4, replace=False)
    sales.loc[bad_customer_indices, "customer_id"] = -1

    # 10. A few invalid product IDs
    bad_product_indices = np.random.choice(sales.index, size=4, replace=False)
    sales.loc[bad_product_indices, "product_id"] = 9999

    return sales


if __name__ == "__main__":
    df = generate_sales_data()
    df.to_csv("sales.csv", index=False)
    print("sales.csv generated successfully.")