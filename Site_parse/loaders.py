from itemloaders.processors import TakeFirst, MapCompose
from scrapy.loader import ItemLoader
from .items import InfoItem


class InfoLoader(ItemLoader):
    default_item_class = InfoItem
    page_header_in = ' '.join
    page_header_out = TakeFirst()
    page_url_in = ' '.join
    page_url_out = TakeFirst()
    page_text_in = ' '.join
    page_text_out = TakeFirst()
    page_tags_in = '\n'.join
    page_tags_out = TakeFirst()
