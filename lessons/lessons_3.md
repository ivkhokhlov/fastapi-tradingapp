# 3. Валидация данных с Pydantic

## Зачем нужна валидация данных
- Обеспечивает корректность данных, отправляемых клиентом.
- Гарантирует, что сервер может обработать и вернуть данные в нужном формате.
- Позволяет избежать ошибок при обработке неверных данных.

## Реализация валидации данных с помощью Pydantic
### Создание моделей

```python
  from pydantic import BaseModel

  class Trade(BaseModel):
      id: int
      user_id: int
      currency: str
      side: str
      price: float
      amount: float
 ```

### Использование моделей в эндпоинтах
```python
@app.post('/trades/')
def add_trades(trades: List[Trade]):
    fake_trades.extend(trades)
    return {"status": "success", "data": fake_trades}
```
### Обработка ошибок валидации

Пример ошибки валидации:

При отправке неверного типа данных (например, строки вместо числа) Pydantic возвращает понятное сообщение об ошибке.

```json

    {
        "loc": ["body", "amount"],
        "msg": "value is not a valid float",
        "type": "type_error.float"
    }
```

### Дополнительные правила валидации

Настройка полей:

```python
from pydantic import Field

class Trade(BaseModel):
    id: int
    user_id: int
    currency: str
    side: str
    price: float = Field(..., gt=0)
    amount: float
```

Устанавливает, что цена должна быть больше нуля.

### Опциональные поля и вложенные модели

Пример опционального поля:

```python
from typing import Optional
class User(BaseModel):
    id: int
    role: str
    name: str
    degree: Optional[List[Degree]] = None
```
### Вложенные модели
```python
class Degree(BaseModel):
    id: int
    date_awarded: datetime
    type: str

class User(BaseModel):
    id: int
    role: str
    name: str
    degrees: List[Degree]
```

### Валидация данных, отправляемых клиенту

Использование модели ответа:

```python
@app.get('/users/', response_model=List[User])
def get_users():
    return fake_users
```

Вывод

Pydantic упрощает процесс валидации данных в FastAPI, обеспечивая корректность данных и улучшая взаимодействие между клиентом и сервером. Использование моделей позволяет легко управлять сложными структурами данных и предоставляет гибкие возможности для обработки ошибок.