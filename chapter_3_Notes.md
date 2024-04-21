# Financial Statements Analysis and Models

Contents:

* [Short Term Measures](#Short-Term-Measures)
* [Long Term Measures](#Long-Term-Measures)
* [Asset Management](#Asset-Management-Measures)
* [Profitability Measures](#Profitability-Measures)
* [Market Value Measures](#Market-Value-Measures)
* [Internal Growth Rate](#Internal-Growth-Rate)
* [Sustainable Growth Rate](#Sustainable-Growth-Rate)

## Short Term Measures

The primary concern of these ratios is to assess the ability of the firm to pay its bills over the short run without undue stress.  These ratios focus on current assets and current liabilities.

**Current Assets**

```python
current_ratio = current_assets / current_liabilities
```

**Acid Drop Ratio**

```python
acid_drop_ratio = (current_assets - inventory) / current_liabilities
```

**Cash Ratio**

```python
current_ratio = cash / current_liabilities
```

## Long Term Measures

These are intended to address the firm's long-run ability to meet its obligations.  These ratios are sometimes called financial leverage ratios.

**Total Debt Ratio**

Takes into account all debts of all maturities to all creditors.

```python
total_debt_ratio = (total_assets - total_liabilities) / total_assets
```

**Debt-Equity Ratio**

```python
debt_equity_ratio = total_debt / total_equity
```

**Equity Multiplier**

```python
equity_multiplier = total_assets / total_liabilities
```

**Times Interest Earned**

```python
times_interest_earned = EBIT / interest
```

**Cash Coverage Ratio**

```python
cash_coverage = (EBIT + depreciation_amortization) / interest
```

## Asset Management

This measures are sometimes called `Asset Management`, `Utilization Ratios` or `Turnover Ratios`.  What these measures are intended to describe is how efficiently, or intensively, a firm uses its assets to generate sales.

### Inventory Turnover Ratios

These provide indications of how fast a company can sell its products.

**Inventory Turnover Ratio**

```python
inventory_turnover_ratio = cost_of_goods_sold / avg_inventory
```

**Days' Sales in Inventory**

```python
days_sales_in_inventory = 365 / inventory_turnover_ratio 
```

### Receivable Turnover Ratios

These measures how fast the company the company can collect on credit sales.

**Receivable Turnover Ratio**

```python
receivable_turnover_ratio = credit_sales / avg_accounts_receivable
```

**Days' Sales in Receivable**

```python
days_sales_in_receivable = 365 / receivable_turnover_ratio 
```

**Total Asset Turnover**

```python
total_asset_turnover = sales / total_assets
```

## Profitability Ratios


## Internal Growth Rate

The internal growth rate is the maximum growth rate that can be achieved with no external financing of any kind.  This is called "internal" because this is  the rate a firm can maintain with internal financing only.

The internal growth rate is computed as: `igr = (ROA * b) / (1 - ROA * b)`

Where:

ROA = Return on Assets
b = Retention Ratio

## Sustainable Growth Rate

  The sustainable growth rate is the maximum growth rate a firm can achieve with no external equity financing while it maintains a constant debt-equity ratio.

 Reasons for not wanting external financing:

* New equity sales can be expensive.
* Current owners don't want new owners.
* Current owners don't want to contribute additional equity.

The sustainable growth rate is computed as: `sgr = (ROE * b) / (1 - ROE * b)`

Where:

ROE = Return on Equity
b = Retention Ratio
