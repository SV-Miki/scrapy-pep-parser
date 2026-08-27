# Scrapy PEP Parser

Асинхронный парсер документов PEP, реализованный на Scrapy.

Парсер получает список PEP с официального сайта Python, переходит на страницу каждого документа и собирает:

- номер PEP
- название
- текущий статус

После завершения работы формируются два CSV-файла: полный список документов и сводная статистика по статусам.

## Возможности

- асинхронный сбор данных со страниц PEP
- извлечение данных с помощью CSS- и XPath-селекторов
- экспорт полного списка PEP в CSV
- подсчёт количества документов по каждому статусу
- формирование итоговой строки `Total`
- автоматическое создание файлов с датой и временем запуска


## Структура проекта

```text
scrapy_parser_pep/
├── pep_parse/
│   ├── spiders/
│   │   └── pep.py
│   ├── items.py
│   ├── pipelines.py
│   ├── exporters.py
│   ├── constants.py
│   └── settings.py
├── results/
├── tests/
├── requirements.txt
└── scrapy.cfg
```

## Как устроен проект

Основной Spider получает ссылки на документы с главной страницы PEP и обрабатывает каждую страницу отдельно.

Данные одного документа сохраняются в `Scrapy Item` со следующими полями:

- `number`
- `name`
- `status`

Для формирования результатов используются два механизма Scrapy:

- `Feeds` экспортирует полный список PEP в CSV
- `Pipeline` подсчитывает количество документов по статусам и создаёт сводный CSV

Структура обработки данных:

```text
peps.python.org
       ↓
   PepSpider
       ↓
 PepParseItem
    ↙       ↘
 Scrapy     Pipeline
 Feeds
   ↓           ↓
pep_*.csv   status_summary_*.csv
```

## Технологии

- Python 3.12
- Scrapy
- CSS selectors
- XPath
- pytest
- Flake8

## Установка

Клонировать репозиторий:

```bash
git clone git@github.com:SV-Miki/scrapy_parser_pep.git
cd scrapy_parser_pep
```

Создать виртуальное окружение:

```bash
python3 -m venv venv
```

Активировать его.

### Linux / macOS

```bash
source venv/bin/activate
```

### Windows PowerShell

```powershell
venv\Scripts\Activate.ps1
```

### Windows Command Prompt

```cmd
venv\Scripts\activate.bat
```

Установить зависимости:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Запуск

Запустить Spider:

```bash
scrapy crawl pep
```

После завершения работы в директории `results/` создаются два файла:

```text
pep_<дата-время>.csv
status_summary_<дата-время>.csv
```

### Список PEP

Файл `pep_<дата-время>.csv` содержит данные обо всех найденных документах:

| Номер | Название                    | Статус |
|-------|-----------------------------|--------|
| 0001  | PEP Purpose and Guidelines  | Active |
| 0008  | Style Guide for Python Code | Active |
| 0020  | The Zen of Python           | Active |

### Сводка по статусам

Файл `status_summary_<дата-время>.csv` содержит количество документов каждого статуса:

| Статус | Количество |
|--------|-----------:|
| Active |        ... |
| Final  |        ... |
| Draft  |        ... |
| Total  |        ... |

Количество документов зависит от текущего состояния каталога PEP на момент запуска парсера.

## Проверка проекта

Запустить тесты:

```bash
pytest
```

Проверить код с помощью Flake8:

```bash
flake8 pep_parse
```

## Автор

Владислав Шилов
