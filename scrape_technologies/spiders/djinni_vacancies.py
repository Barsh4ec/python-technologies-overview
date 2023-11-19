import scrapy
from scrapy.http import Response


class BooksSpider(scrapy.Spider):
    name = "djinni_spider"
    allowed_domains = ["djinni.co"]
    start_urls = ["https://djinni.co/jobs/"]

    def parse(self, response: Response, **kwargs) -> dict:
        ...
