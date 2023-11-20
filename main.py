import subprocess
from datetime import datetime

import pandas as pd
import matplotlib.pyplot as plt


subprocess.run(["scrapy", "crawl", "djinni_spider", "-O", "vacancies.csv"])

ranks = ["Junior", "Middle", "Senior", "Overall"]
vacancies = pd.read_csv("vacancies.csv")

for rank in ranks:
    if not rank == "Overall":
        rank_vacancies = vacancies[vacancies["Rank"] == f"{rank}"]
    else:
        rank_vacancies = vacancies

    technologies_df = rank_vacancies["Technologies"].str.split(",", expand=True)
    technologies_stacked = technologies_df.stack().reset_index(level=1, drop=True)
    technology_counts = technologies_stacked.value_counts()

    technologies = technology_counts.index

    plt.figure(figsize=(12, 6))
    plt.bar(technologies, technology_counts)
    plt.title(f"{rank} Vacancies requirements({datetime.now().date()})")
    plt.xlabel("Technology")
    plt.xticks(rotation=45)
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(f"analytics/{rank.lower()}_vacancies.png", dpi=300)
