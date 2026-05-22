"""Экспортёры данных проекта."""

from scrapy.exporters import CsvItemExporter

from pep_parse.constants import PEP_CSV_FIELDS


class PepCsvItemExporter(CsvItemExporter):
    """CSV-экспортёр с русскими заголовками."""

    def start_exporting(self):
        """Записывает русские заголовки в CSV-файл."""
        if self.include_headers_line:
            self.csv_writer.writerow(PEP_CSV_FIELDS.values())
            self._headers_not_written = False
