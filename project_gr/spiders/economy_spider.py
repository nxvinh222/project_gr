import scrapy
from ..items.vneconomy_items import VneconomyItems

class EconomySpider(scrapy.Spider):
    name = 'economy'
    page_number = 2
    start_urls = [
        'https://vneconomy.vn/tieu-diem.htm'
    ]
    def parse(self, response, **kwargs):

        items = VneconomyItems()

        all_news = response.css('.story.story--featured.story--timeline')

        for news in all_news:
            title = news.css('.story__title a::attr(title)').extract()
            content = news.css('.story__summary::text').extract()
            time = news.css('.story__meta time::text').extract()

            items['title'] = title
            items['content'] = content
            items['time'] = time

            yield items

        next_page = 'https://vneconomy.vn/tieu-diem.htm?trang=' + str(EconomySpider.page_number) + ''
        if EconomySpider.page_number <= 11:
            EconomySpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)