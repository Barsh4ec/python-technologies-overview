import scrapy
from scrapy.http import Response

from .check_technologies import check_technologies


class BooksSpider(scrapy.Spider):
    name = "djinni_spider"
    allowed_domains = ["djinni.co"]
    start_urls = [
        "https://djinni.co/jobs/?primary_keyword=Python&exp_rank=junior",
        "https://djinni.co/jobs/?primary_keyword=Python&exp_rank=middle",
        "https://djinni.co/jobs/?primary_keyword=Python&exp_rank=senior",
    ]

    @staticmethod
    def get_rank(url: str) -> str:
        if "junior" in url:
            return "Junior"
        if "middle" in url:
            return "Middle"
        if "senior" in url:
            return "Senior"

    def scrape_single_vacancy(self, response: Response) -> dict:
        left_technologies = check_technologies(response.css(".row-mobile-order-2 > .mb-4").get())

        right_technologies = check_technologies(
            ", ".join(
                response.css('.job-additional-info--item-text span[class=""]::text').getall()
            )
        )
        technologies = list(set(left_technologies + right_technologies))
        yield {
            "Title": response.css(".col > h1::text").get().strip(),
            "Technologies": technologies,
            "Rank": self.get_rank(response.url)
        }

    def parse(self, response: Response, **kwargs) -> dict:
        for vacancy in response.css(".list-jobs__item"):
            vacancy_url = vacancy.css(".job-list-item__link::attr(href)").get()
            yield response.follow(vacancy_url, callback=self.scrape_single_vacancy)

        next_page = response.css(".pagination li:nth-last-child(1) > .page-link::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

