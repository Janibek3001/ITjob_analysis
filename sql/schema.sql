CREATE TABLE employers (
    id VARCHAR(20) PRIMARY KEY,
    name VARCHAR(255),
    url VARCHAR(255),
    trusted BOOLEAN
);

CREATE TABLE vacancies (
    id VARCHAR(20) PRIMARY KEY,
    name VARCHAR(255),
    employer_id VARCHAR(20) REFERENCES employers(id),
    area_name VARCHAR(100),
    salary_from INTEGER,
    salary_currency VARCHAR(10),
    experience VARCHAR(50),
    employment VARCHAR(50),
    schedule VARCHAR(50),
    published_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT now()
);

CREATE TABLE skills(
    id SERIAL PRIMARY KEY,
    vacancy_id VARCHAR(20) REFERENCES vacancies(id),
    skill VARCHAR(100)
)