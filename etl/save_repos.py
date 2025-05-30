from etl.db import get_connection

def save_to_db(repos, time_span):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM trending_repositories WHERE time_span = %s AND fetched_at::date = CURRENT_DATE",
        (time_span,)
    )

    for r in repos:
        cur.execute(
            "INSERT INTO trending_repositories ("
            "repo_name, repo_url, description, language, "
            "language_color, stars_total, forks, stars_growth, "
            "time_span, fetched_at"
            ") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (
                r["repo_name"], r["repo_url"], r["description"], r["language"],
                r["language_color"], r["stars_total"], r["forks"], r["stars_growth"],
                r["time_span"], r["fetched_at"]
            )
        )

    conn.commit()
    cur.close()
    conn.close()
