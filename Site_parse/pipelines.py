# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from prettytable import PrettyTable


class SiteParsePipeline:
    def process_item(self, item, HabrParseSpider):

        x = PrettyTable(max_table_width=150)
        x.field_names = ["page_url", "page_header", "page_text", "page_tags"]
        x.align['page_text'] = 'l'
        x._min_width = {"page_url": 25, "page_header": 30, "page_text": 65, "page_tags": 30}
        x._max_width = {"page_url": 25, "page_header": 30, "page_text": 65, "page_tags": 30}

        x.add_row([item['page_url'], item['page_header'], item['page_text'].replace(' ', ' ').replace('\r\n', ' '), item['page_tags']])

        with open('../parse_result.txt', 'a') as file:
            file.write(x.get_string())
