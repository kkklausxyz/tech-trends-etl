import requests
from bs4 import BeautifulSoup
from datetime import datetime

def fetch_trending_repos(since="daily"):
    url = f"https://github.com/trending?since={since}"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/117.0.0.0 Safari/537.36"
        )
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    repo_items = soup.find_all("article", class_="Box-row")

    repos = []
    for repo in repo_items:
        name_tag = repo.find("h2", class_="h3")
        if not name_tag or not name_tag.a:
            continue

        repo_name = name_tag.a.get_text(strip=True).replace(" ", "")
        repo_url = f"https://github.com{name_tag.a['href']}"

        description_tag = repo.find("p", class_="col-9 color-fg-muted my-1 pr-4")
        description = description_tag.text.strip() if description_tag else ""

        lang_tag = repo.find("span", itemprop="programmingLanguage")
        language = lang_tag.text.strip() if lang_tag else None

        color_tag = repo.find("span", class_="repo-language-color")
        language_color = color_tag["style"].split(":")[-1].strip() if color_tag else None

        stars_tag = repo.find("a", href=lambda x: x and x.endswith("/stargazers"))
        forks_tag = repo.find("a", href=lambda x: x and x.endswith("/forks"))
        stars_total = int(stars_tag.text.strip().replace(",", "").replace("K", "000")) if stars_tag else 0
        forks = int(forks_tag.text.strip().replace(",", "").replace("K", "000")) if forks_tag else 0

        stars_growth = 0
        stars_growth_tags = repo.find_all("span", class_="d-inline-block float-sm-right")
        growth_key = {
            "daily": "stars today",
            "weekly": "stars this week",
            "monthly": "stars this month"
        }[since]

        for tag in stars_growth_tags:
            if tag and tag.text and growth_key in tag.text:
                stars_growth = int(tag.text.strip().split()[0].replace(",", ""))
                break

        repos.append({
            "repo_name": repo_name,
            "repo_url": repo_url,
            "description": description,
            "language": language,
            "language_color": language_color,
            "stars_total": stars_total,
            "forks": forks,
            "stars_growth": stars_growth,
            "time_span": since,
            "fetched_at": datetime.utcnow()
        })

    return repos
