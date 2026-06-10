import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from cleaner import to_usd, categorize_role, calc_salary_avg


# --- to_usd ---

def test_to_usd_usd():
    assert to_usd(1000, 'USD') == 1000.0

def test_to_usd_kzt():
    assert to_usd(500000, 'KZT') == 1000.0

def test_to_usd_uzs():
    assert to_usd(12987012, 'UZS') == 1000.0

def test_to_usd_none_amount():
    assert to_usd(None, 'USD') is None

def test_to_usd_none_currency():
    assert to_usd(1000, None) is None

def test_to_usd_unknown_currency():
    assert to_usd(1000, 'XYZ') is None


# --- categorize_role ---

def test_categorize_data_analyst():
    assert categorize_role('data analyst') == 'Data Analyst'

def test_categorize_data_engineer():
    assert categorize_role('data engineer') == 'Data Engineer'

def test_categorize_ml():
    assert categorize_role('machine learning engineer') == 'Data Scientist / ML'

def test_categorize_russian():
    assert categorize_role('аналитик данных') == 'Data Analyst'

def test_categorize_none():
    assert categorize_role(None) == 'Other'

def test_categorize_unknown():
    assert categorize_role('java developer') == 'Other'


# --- calc_salary_avg ---

def test_salary_avg_both():
    assert calc_salary_avg(1000, 2000) == 1500.0

def test_salary_avg_only_from():
    assert calc_salary_avg(1000, None) == 1000

def test_salary_avg_only_to():
    assert calc_salary_avg(None, 2000) == 2000

def test_salary_avg_none():
    assert calc_salary_avg(None, None) is None