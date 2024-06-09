# 1. FastAPI - Установка и запуск
## Установка библиотек
1) Создать виртуальное окружение
```
python -m .venv .venv
```
2) Активировать виртуальное окружение
```
source .venv/bin/activate
```
3) Установить fastapi
```
pip install fastapi
```
Для установки всех  (?) зависимостей использовать fastapi[all]
```
pip install fastapi[all]
```
## Создание минимального приложения
Для `main.py`
1) Объявить переменную
```python
app = FastAPI()
```
2) Создать функцию, которая возвращает что-либо
```python
def hello():
    ...
    return 'Hello World!'
```
3) Повесить декоратор с роутом и методом запрсоа
```python
@app.get('/')
def hello():
    ...
    return 'Hello World!'
```
## Запуск приложения
```
uvicorn main:app --reload
```
`uvicorn` — библиотека, позволяющая запустить свой собственный веб-сервер

`main:app` — путь до переменной приложения FastAPI

`--reload` — флаг перезапуска вебсервера при внесении любых изменений

Для запуска приложенения с возможнсотями poetry
1) Перенести main.py внутрь директории пакета
2) В `pyproject.toml` добавить строчку кастомной команды
```
[tool.poetry.scripts]
start = "my_package.main:start"
```
3) В `main.py` добавить функцию запуска `start`
```python
def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("my_package.main:app", host="0.0.0.0", port=8000, reload=True)
```
4) Запустить кастомной командой
```
poetry run start
```


## Документация API
Документация генерируется автоматически и доступна по двум ссылкам
`/doc` и `/redoc`