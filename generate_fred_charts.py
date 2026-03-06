#!/usr/bin/env python3
"""
Generate interactive Plotly charts from FRED data
Styled with pink/magenta theme to match victoria peng's website
"""

import requests
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
import os

# Configuration
API_KEY = os.getenv('FRED_API_KEY', '171f88a5b22f07908b08c933d0bb0b2e')  # Set via environment variable
BASE_URL = "https://api.stlouisfed.org/fred/series/observations"
OUTPUT_DIR = "dashboard/charts"

# Create output directory if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Theme colors (matching main site)
COLORS = {
    'primary': '#ff59a6',      # Pink
    'secondary': '#ff1bad',    # Magenta
    'dark': '#444',            # Dark gray text
    'light': '#fff',           # Light background
    'border': '#ff99c8',       # Light pink
    'hover': '#fff5fb'         # Very light pink
}

# FRED Series to fetch
SERIES = [
    {
        'id': 'CPIAUCSL',
        'title': 'CPI – Last Five Years',
        'ylabel': 'Index (1982-1984=100)',
        'file': 'cpi.html'
    },
    {
        'id': 'UNRATE',
        'title': 'Unemployment Rate',
        'ylabel': 'Percent',
        'file': 'unemployment.html'
    },
    {
        'id': 'GS10',
        'title': '10-Year Treasury Yields',
        'ylabel': 'Percent',
        'file': 'treasury_10y.html'
    },
    {
        'id': 'TB3MS',
        'title': '3-Month Treasury Rates',
        'ylabel': 'Percent',
        'file': 'treasury_3m.html'
    }
]

def fetch_fred_data(series_id):
    """Fetch data from FRED API"""
    params = {
        'series_id': series_id,
        'api_key': API_KEY,
        'file_type': 'json',
        'limit': 120  # Last ~10 years
    }
    
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        
        if 'observations' in data:
            df = pd.DataFrame(data['observations'])
            df['date'] = pd.to_datetime(df['date'])
            df['value'] = pd.to_numeric(df['value'], errors='coerce')
            df = df.dropna(subset=['value'])
            return df.sort_values('date')
    except Exception as e:
        print(f"Error fetching {series_id}: {e}")
    
    return None

def create_chart(df, title, ylabel, filename):
    """Create an interactive Plotly chart with custom styling"""
    if df is None or df.empty:
        print(f"Skipping {filename} - no data")
        return
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=df['date'],
        y=df['value'],
        mode='lines',
        line=dict(
            color=COLORS['primary'],
            width=2.5
        ),
        fill='tozeroy',
        fillcolor=f"rgba(255, 89, 166, 0.1)",  # Transparent pink
        hovertemplate='<b>%{x|%Y-%m-%d}</b><br>Value: %{y:.2f}<extra></extra>',
        name=title
    ))
    
    fig.update_layout(
        title={
            'text': title,
            'font': {'size': 18, 'color': COLORS['primary'], 'family': 'Verdana, sans-serif'},
            'x': 0.5,
            'xanchor': 'center'
        },
        xaxis=dict(
            title=dict(text='Date', font=dict(size=12, color=COLORS['dark'])),
            showgrid=True,
            gridwidth=1,
            gridcolor='rgba(255, 153, 200, 0.2)',
            tickfont=dict(size=10, color=COLORS['dark'])
        ),
        yaxis=dict(
            title=dict(text=ylabel, font=dict(size=12, color=COLORS['dark'])),
            showgrid=True,
            gridwidth=1,
            gridcolor='rgba(255, 153, 200, 0.2)',
            tickfont=dict(size=10, color=COLORS['dark'])
        ),
        plot_bgcolor=COLORS['light'],
        paper_bgcolor=COLORS['light'],
        font=dict(family='Verdana, sans-serif', size=11, color=COLORS['dark']),
        hovermode='x unified',
        margin=dict(l=60, r=40, t=60, b=60),
        height=480,
        showlegend=False
    )
    
    # Save as HTML
    filepath = os.path.join(OUTPUT_DIR, filename)
    fig.write_html(filepath, include_plotlyjs='cdn')
    print(f"✓ Generated {filepath}")

def main():
    """Fetch all FRED data and generate charts"""
    print(f"🔄 Generating FRED charts with pink/magenta theme...")
    print(f"API Key: {'SET' if API_KEY != 'YOUR_API_KEY' else 'NOT SET (set FRED_API_KEY env var)'}\n")
    
    for series in SERIES:
        print(f"📊 Fetching {series['id']}...")
        df = fetch_fred_data(series['id'])
        
        if df is not None:
            create_chart(df, series['title'], series['ylabel'], series['file'])
        else:
            print(f"✗ Failed to fetch {series['id']}")
    
    print(f"\n✨ Done! Charts saved to {OUTPUT_DIR}/")
    print("\nUpdate dashboard/index.html to reference these files:")
    for series in SERIES:
        print(f"  - {series['title']}: charts/{series['file']}")

if __name__ == '__main__':
    main()
