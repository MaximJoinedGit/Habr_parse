from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from Site_parse import settings
from Site_parse.spiders.Habr_parse import HabrParseSpider
import datetime
from os import path

if __name__ == '__main__':

    with open('../parse_result.txt', 'w') as new_file:
        new_file.write(f'Парсинг статей на Habr от {datetime.datetime.now()}. Количество статей - 55.\n\n')

    crawl_settings = Settings()
    crawl_settings.setmodule(settings)
    crawl_proc = CrawlerProcess(settings=crawl_settings)
    crawl_proc.crawl(HabrParseSpider)
    crawl_proc.start()
