import scrapy
from urllib.parse import urlparse
from Site_parse.loaders import InfoLoader
from scrapy.extensions.closespider import CloseSpider


class HabrParseSpider(scrapy.Spider):
    name = 'Habr_parse'
    allowed_domains = ['habr.com']
    start_urls = ['https://habr.com/ru/']
    url_div = urlparse(start_urls[0])
    counter = 1

    def parse(self, response, **kwargs):

        for url_next_page in response.xpath('//a[@id="next_page"]/@href'):
            next_page = self.url_div.scheme + '://' + self.url_div.netloc + url_next_page.get()
            yield response.follow(next_page, callback=self.parse)

        for url_post in response.xpath('//a[@class="post__title_link"]/@href'):
            self.counter += 1
            if self.counter < 56:
                print(f'Обработана {self.counter}-я ссылка')
                yield response.follow(url_post, callback=self.parse_news_info)
            else:
                raise CloseSpider('Количество статей 55.')

    def parse_news_info(self, response, **kwargs):

        item_elements = {
            'page_header': response.xpath('//span[@class="post__title-text"]/text()').get(),
            'page_url': response.url,
            'page_text': response.xpath('//div[@id="post-content-body"]/descendant::text()[not(parent::code)]').getall(),
            'page_tags': response.xpath('//dl[@class="post__tags"][1]//li/a/text()').getall()
        }

        info_loader = InfoLoader(response=response)

        for key, value in item_elements.items():
            info_loader.add_value(key, value)

        yield info_loader.load_item()
