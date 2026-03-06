# FRED Charts Setup

## Quick Start

This generates interactive Plotly charts from the Federal Reserve Economic Data (FRED) API and integrates them into your dashboard.

### 1. Get a FRED API Key

1. Go to https://fred.stlouisfed.org/docs/api/
2. Register for a free account
3. Create an API key (instant)
4. Copy your 32-character API key

### 2. Set Environment Variable

```bash
export FRED_API_KEY="your_32_character_api_key_here"
```

Or add to your shell profile (~/.zshrc or ~/.bash_profile):
```bash
export FRED_API_KEY="your_32_character_api_key_here"
```

### 3. Generate Charts

```bash
python generate_fred_charts.py
```

This creates interactive Plotly charts styled with your pink/magenta theme and saves them to `dashboard/charts/`.

### 4. Deploy

```bash
git add dashboard/charts/
git commit -m "Add generated FRED charts"
git push origin main
```

## What Gets Generated

- `dashboard/charts/cpi.html` – Consumer Price Index (inflation)
- `dashboard/charts/unemployment.html` – Unemployment Rate
- `dashboard/charts/treasury_10y.html` – 10-Year Treasury Yields
- `dashboard/charts/treasury_3m.html` – 3-Month Treasury Rates

## Styling

Charts use your site's color scheme:
- **Primary**: #ff59a6 (pink)
- **Secondary**: #ff1bad (magenta)
- **Font**: Verdana
- **Theme**: Light background with dotted grid

## Update Schedule

Run `python generate_fred_charts.py` periodically (monthly/quarterly) to refresh data. You can automate this with:

```bash
# Add to crontab for monthly updates
0 0 1 * * cd ~/projects/mochi-site && export FRED_API_KEY="..." && python generate_fred_charts.py && git add dashboard/charts && git commit -m "Auto-update FRED charts" && git push origin main
```

## Dependencies

- requests
- pandas
- plotly

Install via: `pip install -r requirements_charts.txt`
