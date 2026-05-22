# Проект асинхронного парсинга PEP

## Описание проекта

scrapy_parser_pep - асинхронный парсер документов PEP на базе Scrapy.

Проект позволяет:
- собирать данные обо всех документах PEP
- получать номер, название и статус каждого PEP
- сохранять список всех PEP в CSV-файл
- подсчитывать количество PEP по каждому статусу
- сохранять сводку по статусам в отдельный CSV-файл
- формировать итоговую строку Total с общим количеством PEP
- использовать Scrapy Items для хранения данных
- использовать Scrapy Feeds для экспорта списка PEP
- использовать Pipeline для формирования сводки по статусам


## Технологии

В проекте используются:

- Python 3.12
- Scrapy
- Twisted
- Lxml
- CSS-селекторы
- XPath-селекторы
- Pytest
- Flake8


## Запуск проекта

### 1. Клонировать репозиторий

```bash
git clone <URL_репозитория>
```

```bash
cd scrapy_parser_pep
```

### 2. Создать и активировать виртуальное окружение

```bash
python3 -m venv venv
```

#### Linux/macOS

```bash
source venv/bin/activate
```

#### Windows

```bash
source venv/Scripts/activate
```

### 3. Установить зависимости

```bash
python -m pip install --upgrade pip
```

```bash
pip install -r requirements.txt
```

## Запуск парсера

Парсер запускается командой:

```bash
scrapy crawl pep
```

После запуска в директории results/ создаются два CSV-файла:

* `pep_ДатаВремя.csv`
* `status_summary_ДатаВремя.csv`

## Файл со списком PEP

Файл `pep_ДатаВремя.csv` содержит список всех документов PEP.

В файле есть три столбца:

| Номер | Название  | Статус |
|-------|---|--|
| 0001  |  PEP Purpose and Guidelines | Active |
| 0008  |  Style Guide for Python Code | Active |
| 0020  |  The Zen of Python | Active |

## Файл со сводкой по статусам

Файл `status_summary_ДатаВремя.csv` содержит количество PEP по каждому статусу.

Пример файла:

| Статус   | Количество |
|----------|------------|
| Active   | 38         |
| Final    | 355        |
| Rejected | 130        |
| Draft    | 44         |
| Total    | 726        |

## Проверка проекта

Запуск тестов

```bash
python -m pytest
```

```bash
python -m flake8 pep_parse
```
## Автор

Владислав Шилов