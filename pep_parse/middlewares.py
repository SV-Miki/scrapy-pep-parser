"""Middleware проекта pep_parse."""

from scrapy import signals


class PepParseSpiderMiddleware:
    """Spider middleware проекта."""

    @classmethod
    def from_crawler(cls, crawler):
        """Создаёт middleware и подключает сигнал открытия паука."""
        spider_middleware = cls()
        crawler.signals.connect(
            spider_middleware.spider_opened,
            signal=signals.spider_opened,
        )
        return spider_middleware

    def process_spider_input(self, response, spider):
        """Обрабатывает входящий response."""
        return None

    def process_spider_output(self, response, result, spider):
        """Возвращает результаты работы паука."""
        yield from result

    def process_spider_exception(self, response, exception, spider):
        """Обрабатывает исключения паука."""
        return None

    def process_start_requests(self, start_requests, spider):
        """Обрабатывает стартовые запросы."""
        yield from start_requests

    def spider_opened(self, spider):
        """Логирует открытие паука."""
        spider.logger.info(f'Spider opened: {spider.name}')


class PepParseDownloaderMiddleware:
    """Downloader middleware проекта."""

    @classmethod
    def from_crawler(cls, crawler):
        """Создаёт middleware и подключает сигнал открытия паука."""
        downloader_middleware = cls()
        crawler.signals.connect(
            downloader_middleware.spider_opened,
            signal=signals.spider_opened,
        )
        return downloader_middleware

    def process_request(self, request, spider):
        """Обрабатывает исходящий request."""
        return None

    def process_response(self, request, response, spider):
        """Возвращает полученный response."""
        return response

    def process_exception(self, request, exception, spider):
        """Обрабатывает исключения загрузчика."""
        return None

    def spider_opened(self, spider):
        """Логирует открытие паука."""
        spider.logger.info(f'Spider opened: {spider.name}')
