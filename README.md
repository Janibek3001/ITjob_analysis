# HH Central Asia — IT Labor Market Analysis

Анализ рынка data-вакансий в Центральной Азии на основе данных hh.ru.

## 📊 Что исследовали

- 1300+ вакансий по Казахстану, Узбекистану и Кыргызстану
- Роли: Data Analyst, Data Engineer, Data Scientist, Business Analyst, BI Developer
- Навыки, зарплаты, опыт, топ работодатели

## 🔍 Главные инсайты

**Города:**
- Алматы лидирует — 600 вакансий
- Ташкент второй — 378
- Астана третья — 221

**Зарплаты (медиана, USD/месяц):**
| Роль | Зарплата |
|------|----------|
| Data Scientist / ML | $1,250 |
| Data Engineer | $1,200 |
| Business / Product Analyst | $1,100 |
| Data Analyst | $1,000 |
| BI Developer | $895 |

**Зарплата по опыту:**
| Опыт | Зарплата |
|------|----------|
| Без опыта | $540 |
| 1–3 года | $950 |
| 3–6 лет | $1,400 |
| 6+ лет | $2,000 |

**Топ технические навыки:** SQL, Python, Power BI, Docker, PostgreSQL, Git, ETL

**Топ работодатели:** Ipotekabank, Beeline, Kaspi.kz, Andersen, BI Group

## 🛠 Стек

- **Python** — сбор и анализ данных (requests, pandas, matplotlib)
- **PostgreSQL** — хранение данных
- **hh.ru API** — источник данных
- **pytest** — тесты

## 📁 Структура

hh-central-asia/
├── data/
│   ├── raw/          # сырые JSON с API
│   └── processed/    # очищенные данные
├── notebooks/
│   ├── 02_cleaning.ipynb
│   ├── 03_skills.ipynb
│   └── 04_salary.ipynb
├── src/
│   ├── parser.py     # сбор данных с hh.ru API
│   ├── loader.py     # загрузка в PostgreSQL
│   └── cleaner.py    # очистка и нормализация
├── tests/
│   └── test_cleaner.py
└── reports/          # графики

## 🚀 Запуск

```bash
git clone https://github.com/USERNAME/hh-central-asia
cd hh-central-asia
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python src/parser.py   # сбор данных
python src/loader.py   # загрузка в БД
jupyter notebook       # анализ
```
