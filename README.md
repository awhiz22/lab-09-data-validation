# 🧪 Lab — Can You Trust This Dataset?

## Overview

You have been given a dataset containing e-commerce sales data.

Your manager has already used this dataset to report revenue metrics to leadership.

Your job is to determine:

> **Can this dataset be trusted for analysis?**

---

## Objectives

By completing this lab, you will:

- Identify common data-quality issues
- Write validation checks using pandas
- Use assertions to enforce data rules
- Build a data-quality report
- Create an analysis-ready dataset
- Compare results before and after validation

---

## Dataset

You will work with a dataset called `sales.csv`.

This dataset may contain:

- Missing values  
- Duplicate records  
- Invalid numeric values  
- Inconsistent categories  
- Outliers  
- Invalid dates  

---

## Instructions

### 🔹 Part 1 — Initial Analysis

Calculate the following:

- Total revenue  
- Average order value  
- Revenue by status  

Then answer:

> Do you trust these results? Why or why not?

---

### 🔹 Part 2 — Identify Data Issues

Investigate the dataset and identify any issues.

Consider:

- Missing values  
- Duplicate IDs  
- Invalid values (negative revenue, zero quantity)  
- Inconsistent categories  
- Suspicious values  

Document your findings.

---

### 🔹 Part 3 — Create Validation Checks

Create new columns that flag issues in the dataset.

Examples:

- Missing customer IDs  
- Duplicate order IDs  
- Negative revenue  
- Invalid quantities  
- Invalid status values  
- Future dates  

---

### 🔹 Part 4 — Summarize Data Quality Issues

Create a summary showing how many issues exist for each validation check.

---

### 🔹 Part 5 — Assertions

Write assertions that enforce data-quality rules.

Example rules:

- Order IDs must be unique  
- Revenue must be non-negative  
- Quantity must be greater than zero  

Run your assertions.

> What happens? Why?

---

### 🔹 Part 6 — Create a Clean Dataset

Create a new dataset that excludes problematic rows.

Explain your decisions:

- What did you remove?
- Why?

---

### 🔹 Part 7 — Re-run Analysis

Recalculate:

- Total revenue  
- Average order value  
- Revenue by status  

Compare results before and after cleaning.

> What changed?

---

### 🔹 Part 8 — Data Quality Report

Create a data-quality report that includes:

- Counts of each issue  
- Summary statistics  
- Category breakdowns  

---

## Reflection Questions

- Which data issue had the biggest impact on results?
- What assumptions did you make during cleaning?
- What risks exist if data validation is skipped?

---

## Deliverables

- Completed notebook
- Clean dataset
- Data-quality report
- Written answers to reflection questions