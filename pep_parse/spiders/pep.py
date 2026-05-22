"""Паук для парсинга документов PEP."""

import re

import scrapy

from pep_parse.constants import (
    PEP_LINK_SELECTOR,
    PEP_STATUS_SELECTOR,
    PEP_TITLE_SELECTOR,
)
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    """Паук для сбора информации о документах PEP."""

    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        """Собирает ссылки на страницы документов PEP."""
        pep_links = response.css(
            PEP_LINK_SELECTOR
        ).getall()

        for pep_link in pep_links:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        """Парсит страницу PEP и формирует Item."""
        title = response.css(PEP_TITLE_SELECTOR).get(default='').strip()
        status = response.xpath(PEP_STATUS_SELECTOR).get(default='').strip()
        number = re.search(r'pep-(\d+)', response.url).group(1)

        name = title.replace(f'PEP {int(number)} – ', '')

        yield PepParseItem(
            number=number,
            name=name,
            status=status,
        )
