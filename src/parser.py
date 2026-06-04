import requests
import json
import time
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.hh.ru"
HEADERS = {
    "User-Agent":"job_analyze/1.0",
    "Authorization": f"Bearer {os.getenv('HH_ACCESS_TOKEN')}"
}


def get_vacancies(text, per_page=100):
    vacancies = []
    page = 0

    while True:
        params = {
            "text": text,
            "per_page": per_page,
            "page": page
        }

        response = requests.get(f"{BASE_URL}/vacancies", headers=HEADERS, params=params)
        data = response.json()

        if "items" not in data or len(data["items"]) == 0:
            break

        vacancies.extend(data["items"])
        print(f"[{text}] Страница {page + 1} — собрано {len(vacancies)} вакансий")

        if page >= min(data["pages"] - 1, 19):
            break

        page += 1
        time.sleep(0.5)

    return vacancies

def get_vacancy_detail(vacancy_id):
    """Получает полные данные одной вакансии включая навыки"""
    response = requests.get(f"{BASE_URL}/vacancies/{vacancy_id}", headers=HEADERS)
    time.sleep(0.3)
    return response.json()

def save_raw(data, filename):
    os.makedirs("/home/janibekabdurakhimov/Projects/hh_central_asia/data/raw/", exist_ok=True)
    with open(f"/home/janibekabdurakhimov/Projects/hh_central_asia/data/raw//{filename}", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Сохранено: /home/janibekabdurakhimov/Projects/hh_central_asia/data/raw//{filename}")

if __name__ == "__main__":
    keywords = [
        # Data Analytics
        "data analyst",
        "аналитик данных",
        "BI analyst",
        "business analyst",
        "бизнес аналитик",
        "product analyst",
        "продуктовый аналитик",
    
        # Data Engineering
        "data engineer",
        "инженер данных",
        "ETL developer",
        "data architect",
    
        # Data Science & ML
        "data scientist",
        "machine learning engineer",
        "ML engineer",
        "AI engineer",
        "NLP engineer",
    
        # Related
        "SQL analyst",
        "tableau developer",
        "power bi developer",
    ]

    for keyword in keywords:
        print(f"\n--- Собираем: {keyword} ---")
        vacancies = get_vacancies(keyword)

        detailed = []
        for i, v in enumerate(vacancies):
            detail = get_vacancy_detail(v["id"])
            detailed.append(detail)
            print(f"  Детали: {i+1}/{len(vacancies)}", end='\r')
        
        filename = keyword.replace(" ", "_") + ".json"
        save_raw(detailed, filename)