import json
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(
    dbname="hh_central_asia",
    user="postgres",
    password=os.getenv("DB_PASSWORD"),
    host="localhost"
)
cur = conn.cursor()

def load_vacancy(v, source_keyword):
    try:

        employer = v.get("employer") or {}
        emp_id = employer.get("id")
        if emp_id:
            cur.execute("""
                INSERT INTO employers (id, name, url, trusted)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (id) DO NOTHING
            """, (
                emp_id,
                employer.get("name"),
                employer.get("url"),
                employer.get("trusted", False)
            ))
        
        salary = v.get("salary") or {}
        salary_from = salary.get("from")
        salary_to = salary.get("to")
        salary_currency = salary.get("currency")

        area = v.get("area") or {}
        area_name = area.get("name")

        experience = (v.get("experience") or {}).get("name")
        employment = (v.get("employment") or {}).get("name")
        schedule = (v.get("schedule") or {}).get("name")

        cur.execute("""
            INSERT INTO vacancies (id, name, employer_id, area_name, salary_from, 
                                   salary_to, salary_currency, experience, 
                                   employment, schedule, published_at, source_keyword)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (id) DO NOTHING
        """, (
            v.get("id"),
            v.get("name"),
            emp_id,
            area_name,
            salary_from,
            salary_to,
            salary_currency,
            experience,
            employment,
            schedule,
            v.get("published_at"),
            source_keyword
        ))

        for skill in v.get("key_skills", []):
            cur.execute("""
                INSERT INTO skills (vacancy_id, skill)
                VALUES (%s, %s)
            """, (v.get("id"), skill.get("name")))

    except Exception as e:
        print(f"Ошибка вакансии {v.get('id')}: {e}")
        conn.rollback()
        return False
    return True

if __name__ == "__main__":
    raw_dir = "data/raw"
    total = 0
    skipped = 0

    for filename in sorted(os.listdir(raw_dir)):
        if not filename.endswith(".json"):
            continue

        keyword = filename.replace(".json", "").replace("_", " ")
        filepath = os.path.join(raw_dir, filename)

        with open(filepath, encoding="utf-8") as f:
            vacancies = json.load(f)

        loaded = 0
        for v in vacancies:
            ok = load_vacancy(v, keyword)
            if ok:
                loaded += 1
            else:
                skipped += 1

        conn.commit()
        total += loaded
        print(f"{filename}: загружено {loaded}/{len(vacancies)}")

    print(f"\nИТОГО загружено: {total} | пропущено: {skipped}")
    cur.close()
    conn.close()