# 🛠️ Tech Trends ETL Pipeline

This repository contains the ETL (Extract, Transform, Load) service for **Tech Trends Explorer**. It collects, processes, and stores trending GitHub data daily to support the analytics and visualizations on the frontend.

## 🔧 Tech Stack

- **Language**: Python
- **Database**: PostgreSQL (hosted on Supabase)
- **Deployment**: Render (as a Cron Job)
- **Data Source**: [GitHub Trending](https://github.com/trending)

## ⚙️ How It Works

1. **Extract**: Scrapes trending repositories from GitHub based on daily/weekly/monthly time spans.
2. **Transform**: Parses metadata such as programming languages, descriptions, keywords, and stars.
3. **Load**: Saves cleaned data to PostgreSQL, overwriting the previous day's data.


## 🕒 Scheduled Execution

This ETL runs daily via [Render Cron Job](https://render.com/docs/cronjobs). It ensures that the database always contains the latest GitHub trending data.

## 📥 Environment Variables

| Variable            | Description                         |
|---------------------|-------------------------------------|
| `DATABASE_URL`      | Supabase/PostgreSQL connection URL  |

Set these in your Render cron job's environment settings.

## 🚀 Running Locally

```bash
pip install -r requirements.txt
python main.py
```

