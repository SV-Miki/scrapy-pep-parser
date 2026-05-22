"""Настройки Scrapy-проекта pep_parse."""

from pathlib import Path

from pep_parse.constants import (
    CSV_FORMAT,
    DEFAULT_ENCODING,
    FEED_OVERWRITE,
    FIELD_NAME,
    FIELD_NUMBER,
    FIELD_STATUS,
    PEP_CSV_EXPORTER,
    PEP_FILE_NAME,
    PEP_PARSE_PIPELINE,
    RESULTS_DIR,
)


BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'

ROBOTSTXT_OBEY = True

BASE_DIR = Path(__file__).parent.parent
RESULTS_PATH = BASE_DIR / RESULTS_DIR
RESULTS_PATH.mkdir(exist_ok=True)

ITEM_PIPELINES = {
    PEP_PARSE_PIPELINE: 300,
}

FEEDS = {
    f'{RESULTS_DIR}/{PEP_FILE_NAME}': {
        'format': CSV_FORMAT,
        'fields': [
            FIELD_NUMBER,
            FIELD_NAME,
            FIELD_STATUS,
        ],
        'overwrite': FEED_OVERWRITE,
        'encoding': DEFAULT_ENCODING,
    },
}

FEED_EXPORTERS = {
    CSV_FORMAT: PEP_CSV_EXPORTER,
}
