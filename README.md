# 📈 Djinni Vacancies Scraper and Statistics Generator
## 👀 Overview
This Python application is designed to scrape job vacancies from Djinni, a popular job board for IT professionals, and generate statistics based on job positions categorized as junior, middle, senior, and an overall summary of required technologies.

## 🌟 Features
- Web Scraping: Utilizes the Scrapy framework to crawl Djinni and extract relevant job vacancy information, including job title, required technologies, and experience level (junior, middle, senior).

- Data Processing: Processes the scraped data to extract required technologies and categorizes job positions into junior, middle, and senior levels.

- Statistics Generation: Generates statistics for each experience level (junior, middle, senior) and an overall summary of the required technologies.

- Visualization: Creates bar plots to visually represent the technology requirements for each

## 🚀 Getting Started
Execute the following commands:
```shell
git clone https://github.com/Barsh4ec/python-technologies-overview.git
python -m venv venv
source venv/bin/activate # or venv\Scripts\activate in Windows
pip install -r requirements.txt
python main.py
```
After running **main.py** all the vacancies will be scraped and statistics charts will be created.
You can find results in [this](/analytics) folder.

## 💻 Example
### Overall Statistics
![image](/analytics/overall_vacancies.png)

### Junior Statistics
![image](/analytics/junior_vacancies.png)

### Middle Statistics
![image](/analytics/middle_vacancies.png)

### Senior Statistics
![image](/analytics/senior_vacancies.png)
