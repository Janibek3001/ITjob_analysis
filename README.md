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
├── notebooks/
│   ├── 01_edu.ipynb      # Exploratory Data Analysis
│   ├── 02_cleaning.ipynb # Очистка данных
│   ├── 03_skills.ipynb   # Анализ навыков
│   └── 04_salary.ipynb   # Анализ зарплат
├── reports/              # Графики (PNG)
│   ├── cities.png
│   ├── roles.png
│   ├── salary_by_city.png
│   ├── salary_by_experience.png
│   ├── salary_by_role.png
│   ├── skills_by_role.png
│   ├── top_employers.png
│   └── top_tech_skills.png
├── src/
│   ├── parser.py         # Сбор данных с hh.ru API
│   ├── loader.py         # Загрузка в PostgreSQL
│   └── cleaner.py        # Очистка и нормализация
├── tests/
│   └── test_cleaner.py
├── README.md
└── REPORTS.md   
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
