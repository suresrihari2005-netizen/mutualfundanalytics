# Data Dictionary

## nav_history

| Column | Type | Description |
|----------|----------|----------|
| amfi_code | Integer | Fund code |
| date | Date | NAV date |
| nav | Float | Net Asset Value |

## investor_transactions

| Column | Type | Description |
|----------|----------|----------|
| investor_id | Text | Investor ID |
| transaction_date | Date | Transaction date |
| amfi_code | Integer | Fund code |
| transaction_type | Text | SIP/Lumpsum/Redemption |
| amount_inr | Float | Transaction amount |

## scheme_performance

| Column | Type | Description |
|----------|----------|----------|
| amfi_code | Integer | Fund code |
| scheme_name | Text | Scheme name |
| return_1yr_pct | Float | 1-year return |
| return_3yr_pct | Float | 3-year return |
| return_5yr_pct | Float | 5-year return |
| expense_ratio_pct | Float | Expense ratio |