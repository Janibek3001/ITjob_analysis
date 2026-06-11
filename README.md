# HH Central Asia — IT Labor Market Analysis
Анализ рынка data-вакансий в Центральной Азии на основе данных hh.ru.
> 📊 Полный аналитический отчет доступен в [REPORTS.md](REPORTS.md).

## Что исследовали

- 1300+ вакансий по Казахстану, Узбекистану и Кыргызстану
- Роли: Data Analyst, Data Engineer, Data Scientist, Business Analyst, BI Developer
- Навыки, зарплаты, опыт, топ работодатели


## 🛠 Стек

- **Python** — сбор и анализ данных (requests, pandas, matplotlib)
- **PostgreSQL** — хранение данных
- **hh.ru API** — источник данных
- **pytest** — тесты

## 📁 Структура


```
ITjob_analysis/
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
```

## 🚀 Запуск

```bash
git clone https://github.com/Janibek3001/ITjob_analysis
cd ITjob_analysis
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python src/parser.py   # сбор данных
python src/loader.py   # загрузка в БД
jupyter notebook       # анализ
```
