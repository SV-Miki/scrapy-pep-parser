"""Константы проекта парсера PEP."""

from pathlib import Path

# Директории и шаблоны имён файлов.
BASE_DIR = Path(__file__).parent.parent
RESULTS_DIR = 'results'
PEP_FILE_NAME = 'pep_%(time)s.csv'
STATUS_SUMMARY_FILE_NAME = 'status_summary_{datetime}.csv'


# Поля Item.
FIELD_NUMBER = 'number'
FIELD_NAME = 'name'
FIELD_STATUS = 'status'


# Заголовки CSV-файлов.
PEP_CSV_FIELDS = {
    FIELD_NUMBER: 'Номер',
    FIELD_NAME: 'Название',
    FIELD_STATUS: 'Статус',
}
STATUS_SUMMARY_HEADER = ('Статус', 'Количество')


# Настройки CSV-экспорта.
CSV_FORMAT = 'csv'
DEFAULT_ENCODING = 'utf-8'
FEED_OVERWRITE = True


# CSS- и XPath-селекторы для парсинга PEP.
PEP_LINK_SELECTOR = 'a[href^="pep-"]::attr(href)'
PEP_TITLE_SELECTOR = 'h1.page-title::text'
PEP_STATUS_SELECTOR = (
    '//dt[contains(normalize-space(), "Status")]'
    '/following-sibling::dd[1]//text()'
)


# Служебные значения.
TOTAL_STATUS = 'Total'
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'


# Настройки Scrapy.
PEP_PARSE_PIPELINE = 'pep_parse.pipelines.PepParsePipeline'
PEP_CSV_EXPORTER = 'pep_parse.exporters.PepCsvItemExporter'
