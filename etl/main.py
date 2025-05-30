from etl.fetch_trending import fetch_trending_repos
from etl.save_repos import save_to_db

if __name__ == "__main__":
    for period in ["daily", "weekly", "monthly"]:
        data = fetch_trending_repos(period)
        save_to_db(data, period)
