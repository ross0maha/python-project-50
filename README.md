### Hexlet tests and linter status:
[![Actions Status](https://github.com/ross0maha/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/ross0maha/python-project-50/actions)
[![Actions Status](https://github.com/ross0maha/python-project-50/actions/workflows/main.yml/badge.svg)](https://github.com/ross0maha/python-project-50/actions)
[![Test Coverage](https://api.codeclimate.com/v1/badges/b8b78a830576323a7457/test_coverage)](https://codeclimate.com/github/ross0maha/python-project-50/test_coverage)
[![Maintainability](https://api.codeclimate.com/v1/badges/b8b78a830576323a7457/maintainability)](https://codeclimate.com/github/ross0maha/python-project-50/maintainability)

# Вычислитель отличий

## Описание

"Вычислитель отличий" — это CLI-приложение для сравнения файлов в форматах JSON и YAML и отображения отличий между ними. В проекте реализованы обход, преобразование и формирование абстрактного синтаксического дерева (AST), и он написан в функциональном стиле.

## Возможности

- Поддержка JSON и YAML
- Формирование и работа с AST
- Анализ и сравнение входных файлов
- Вывод различий в удобочитаемом формате
- Работа через CLI
- Анализ входных параметров и создание справки

## Установка

1. Склонируйте репозиторий:
```bash
git clone <https://github.com/ross0maha/python-project-50.git>
cd python-project-50
```
2. Установите Poetry, если еще не установлен:   
```bash
pip install poetry
```
3. Установите зависимости:
```bash
poetry install
```
4. Установите приложение:
```bash
make build
make package-install
```

## Использование

Запустите приложение для сравнения двух файлов:

```bash
genndiff path/to/file1 path/to/file2
```

Пример:

```bash
genndiff examples/file1.json examples/file2.yaml
```

Для получения справки используйте флаг `-h` или `--help`:

```bash
genndiff --help
```

Вывод может быть произведен в следующих форматах:

- stylish (по умолчанию)
- plain
- json


![asciicast](demo.gif)