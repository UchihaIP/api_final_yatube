# API Yatube
## Описание проекта 

Yatube - это социальная сеть выраженная в виде API,
 в которой реализованы возможности: публиковать и смотреть записи, 
 оставлять комментарии, а так же подписываться на понравившихся авторов.
## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```bash
  git clone https://github.com/UchihaIP/api_final_yatube.git 
  cd kittygram
```
Cоздать и активировать виртуальное окружение:
```bash
  python3 -m venv env 
  source env/bin/activate
```
Установить зависимости из файла requirements.txt:
```bash
  python3 -m pip install --upgrade pip
  pip install -r requirements.txt
```
Выполнить миграции:
```bash
  python3 manage.py migrate
```
Запустить проект:
```bash
  python3 manage.py runserver
```
## API Reference

#### Получение публикаций

```http
  GET /api/v1/posts/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `limit` | `integer` | Количество публикаций на страницу |
| `offset` | `integer` | Номер страницы после которой начинать выдачу |

#### Получение публикации по id

```http
  GET /api/v1/posts/{id}/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `integer` | **Required**. id публикации |

#### Создание публикации

```http
  POST /api/v1/posts/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `text`      | `string` | **Required**. Tекст публикации |
| `image`      | `string or null` | Фото публикации |
| `group`      | `integer or null` | id сообщества |


#### Получение JWT-токена

```http
  POST /api/v1/jwt/create/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `username`      | `string` | **Required** |
| `password`      | `string` | **Required** |




## Tech Stack

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)

## Author

- [Рифат Хасанов](https://github.com/UchihaIP)


## 🔗 Links
[![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/lawlietLL)
[![linkedin](https://img.shields.io/badge/вконтакте-%232E87FB.svg?&style=for-the-badge&logo=vk&logoColor=white)](https://vk.com/itsmyrevolution)
