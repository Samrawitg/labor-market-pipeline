# U.S. Labor Market Analysis Pipeline

An end-to-end ETL pipeline analyzing U.S. labor market trends from 2022-2024 
using data from the Bureau of Labor Statistics, Federal Reserve (FRED), 
and BLS Occupational Employment & Wage Statistics.

## Dashboard
[View on Tableau Public](https://public.tableau.com/app/profile/samrawit.anteneh/viz/USLaborMarketAnalysis2022-2024/USLMADashboard?publish=yes)

## Project Overview
This project builds a fully automated data pipeline that extracts data from 
multiple government APIs and flat files, transforms and joins them into a 
unified dataset, loads them into PostgreSQL, and visualizes key labor market 
insights in Tableau.

## Key Findings
- Construction unemployment shows strong seasonal spikes every January due 
  to weather-related slowdowns, while professional services maintained the 
  lowest unemployment rates throughout the period
- Workers experienced real purchasing power losses in early 2023 when 
  inflation outpaced wage growth, before wages recovered by mid-2023
- National job openings declined significantly from their 2022 peak, falling 
  below the period average by September 2023
- Database Architects lead data-adjacent roles at $135,980 median annual wage, 
  while business and operations analyst roles range from $85,000-$100,000

## Data Sources
- **BLS API** — monthly unemployment rates by industry (6 sectors, 2022-2024)
- **FRED API** — macro indicators including job openings, average hourly 
  earnings, CPI, and unemployment rate
- **BLS OEWS** — occupational employment and wage statistics (809 occupations)

## Tech Stack
- Python (pandas, requests, sqlalchemy, matplotlib)
- PostgreSQL + DBeaver
- Tableau Public
- Git + GitHub

## Pipeline Architecture
Extract → Transform → Load, orchestrated by a single pipeline.py script

- extract_bls.py — pulls unemployment data from BLS API
- extract_fred.py — pulls macro indicators from FRED API  
- extract_oews.py — loads occupational wage data from flat file
- transform.py — cleans, joins, and engineers features across all three sources
- load.py — loads processed data into PostgreSQL
- pipeline.py — runs the full ETL pipeline end to end

## How to Run
1. Clone the repo
2. Create a virtual environment: python3 -m venv venv
3. Install dependencies: pip install -r requirements.txt
4. Add your API keys to a .env file (see .env.example)
5. Run the pipeline: cd scripts && python3 pipeline.py

## Project Structure
labor_pipeline/
  data/
    raw/          # extracted source files
    processed/    # cleaned, joined datasets
  notebooks/      # exploration and EDA notebooks
  scripts/        # ETL pipeline scripts
  sql/            # analytical SQL queries