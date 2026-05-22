"""Pipeline для формирования сводки по статусам PEP."""

import csv
import datetime as dt
from collections import Counter

from pep_parse.constants import (
    BASE_DIR,
    DATETIME_FORMAT,
    DEFAULT_ENCODING,
    FIELD_STATUS,
    RESULTS_DIR,
    STATUS_SUMMARY_FILE_NAME,
    STATUS_SUMMARY_HEADER,
    TOTAL_STATUS,
)


class PepParsePipeline:
    """Pipeline для подсчёта количества PEP по статусам."""

    def open_spider(self, spider):
        """Инициализирует счётчик статусов при запуске паука."""
        self.status_counter = Counter()

    def process_item(self, item, spider):
        """Обрабатывает Item и увеличивает счётчик статуса."""
        status = item[FIELD_STATUS]
        self.status_counter[status] += 1
        return item

    def close_spider(self, spider):
        """Создаёт CSV-файл со сводкой по статусам PEP."""
        results_dir = BASE_DIR / RESULTS_DIR
        results_dir.mkdir(exist_ok=True)

        now = dt.datetime.now()
        now_formatted = now.strftime(DATETIME_FORMAT)
        file_name = STATUS_SUMMARY_FILE_NAME.format(
            datetime=now_formatted
        )
        file_path = results_dir / file_name

        with open(
            file_path,
            mode='w',
            encoding=DEFAULT_ENCODING,
            newline='',
        ) as file:
            writer = csv.writer(file)
            writer.writerow(STATUS_SUMMARY_HEADER)
            writer.writerows(self.status_counter.items())
            writer.writerow(
                (TOTAL_STATUS, sum(self.status_counter.values()))
            )
