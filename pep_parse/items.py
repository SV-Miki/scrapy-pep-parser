"""Items для парсера PEP."""

import scrapy


class PepParseItem(scrapy.Item):
    """Item для хранения данных одного документа PEP."""

    number = scrapy.Field()
    name = scrapy.Field()
    status = scrapy.Field()
