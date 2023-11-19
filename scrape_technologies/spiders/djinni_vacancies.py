import scrapy
from scrapy.http import Response

from .check_technologies import check_technologies


class BooksSpider(scrapy.Spider):
    name = "djinni_spider"
    allowed_domains = ["djinni.co"]
    start_urls = ["https://djinni.co/jobs/?primary_keyword=Python&exp_rank=junior"]

    @staticmethod
    def scrape_single_vacancy(response: Response) -> dict:
        yield {
            "Title": response.css(".col > h1::text").get().strip(),
            "Technologies": check_technologies(response.css(".row-mobile-order-2 > .mb-4").get())
        }

    def parse(self, response: Response, **kwargs) -> dict:
        for vacancy in response.css(".list-jobs__item"):
            vacancy_url = vacancy.css(".job-list-item__link::attr(href)").get()
            yield response.follow(vacancy_url, callback=self.scrape_single_vacancy)

