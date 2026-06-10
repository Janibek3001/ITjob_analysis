def to_usd(amount, currency):
    """Конвертирует зарплату в USD"""
    exchange_rates = {
        'USD': 1,
        'KZT': 0.0020,
        'UZS': 0.000077,
        'KGS': 0.011,
        'RUR': 0.011,
        'EUR': 1.08
    }
    if amount is None or currency is None:
        return None
    rate = exchange_rates.get(currency)
    if rate is None:
        return None
    return round(amount * rate, 2)


def categorize_role(keyword):
    """Категоризирует вакансию по роли"""
    if keyword is None:
        return 'Other'
    keyword = str(keyword).lower()
    if any(x in keyword for x in ['data analyst', 'аналитик данных', 'sql analyst', 'bi analyst']):
        return 'Data Analyst'
    elif any(x in keyword for x in ['data engineer', 'инженер данных', 'etl']):
        return 'Data Engineer'
    elif any(x in keyword for x in ['data scientist', 'machine learning', 'ml engineer', 'ai engineer', 'nlp']):
        return 'Data Scientist / ML'
    elif any(x in keyword for x in ['business analyst', 'бизнес аналитик', 'product analyst', 'продуктовый']):
        return 'Business / Product Analyst'
    elif any(x in keyword for x in ['tableau', 'power bi']):
        return 'BI Developer'
    elif 'data architect' in keyword:
        return 'Data Architect'
    else:
        return 'Other'


def calc_salary_avg(salary_from, salary_to):
    """Считает среднее значение зарплаты"""
    if salary_from is not None and salary_to is not None:
        return round((salary_from + salary_to) / 2, 2)
    elif salary_from is not None:
        return salary_from
    elif salary_to is not None:
        return salary_to
    return None