# Mutual Fund Analytics - Analyst Guide

## Introduction

This guide explains how to use the Mutual Fund Analytics project.

---

## Prerequisites

- Python 3.x
- Virtual Environment
- Required packages installed

---

## Running the ETL Pipeline

```bash
python src/etl/loader.py
python src/etl/normaliser.py
python src/etl/validator.py
```

---

## Running Analytics

```bash
python src/analytics/valuation.py
python src/analytics/clustering.py
python src/analytics/cluster_statistics.py
```

---

## Running the API

```bash
uvicorn src.api.main:app --reload
```

API URL:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

## Running the Dashboard

```bash
streamlit run src/dashboard/app.py
```

---

## Running Tests

```bash
pytest tests -v
```

---

## Output Files

The generated reports are available in the `output/` folder.

Examples:

- company_tearsheet.pdf
- cluster_labels.csv
- portfolio_stats.csv
- capital_allocation_report.csv

---

## Project Completed Successfully