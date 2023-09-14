# Конвертация валют по REST API
## Содержание
* [Описание](#description)
* [Установка и настройка](#install)
  * [Перед тем, как начать](#install-python)
  * [Клонирование репозитория](#install-git)
  * [Получение доступа к API](#install-rapidapi)
  * [Файл .env](#install-env)
  * [Установка Docker](#install-docker)
  * [Запуск](#install-start)
* [Состав страниц сайта](#pages)
  * [Документация Swagger](#page-swagger)
  * [Конвертация валют по REST API](#page-rest)
* [Используемые библиотеки](#utils)

<a name="description"></a>
## Описание
Сервис по запросу через API принимает две валюты и сумму, которую переводит по актуальному курсу.

<a name="install"></a>
## Установка и настройка
<a name="install-python"></a>
### Перед тем, как начать
* Проверьте, что у вас установлен `Python` и есть виртуальное пространство

<a name="install-git"></a>
### Клонирование репозитория
* Перейдите в папку проекта и выполните команду в консоли `git clone`, чтобы скопировать файлы репозитория
```
git clone https://github.com/PanicNyan/conversion_rest_api.git
```

<a name="install-rapidapi"></a>
### Получение доступа к API
* Создайте аккаунт на [rapidapi.com](https://rapidapi.com "Переход на сайт rapidapi.com")
* Получите подписку (можно выбрать бесплатную) на сервис [Currency Converter by API-Ninjas](https://rapidapi.com/apininjas/api/currency-converter-by-api-ninjas/ "Переход к сервису API")
* Сохраните полученные KEY и HOST сервиса

<a name="install-env"></a>
### Файл .env
* Скопируйте файл `.env.template` или его содержимое и сохраните под именем нового файла `.env`
* Укажите данные в файле `.env`
  * Секретный ключ проекта в переменную **SECRET_KEY**
  * Режим Debug в проекте (значение «1» обозначает True, при значении «0» будет False) в переменную **DJANGO_DEBUG**
  * Дополнительные IP-адреса через запятую без пробелов в переменную **ALLOWED_HOSTS**
  * Ключ сайта API сервиса с rapidapi в переменную **RAPID_API_KEY**
  * Хост сайта API сервиса с rapidapi, в переменную **RAPID_API_HOST**
```
SECRET_KEY="Секретный ключ Django"
DJANGO_DEBUG=Включение/выключение DEBUG (1 или 0)
ALLOWED_HOSTS="Список адресов, через запятую"
RAPID_API_KEY="Ключ подключения к API сайта"
RAPID_API_HOST="Хост подключения к API сайта"
```

<a name="install-docker"></a>
### Установка Docker
* Если Docker не был установлен ранее, то проведите стандартную установку [Docker](https://docker.com "Переход на сайт docker.com")
* Соберите образ проекта в Docker командой в консоли
```
docker compose build
```

<a name="install-start"></a>
### Запуск
* Запустите контейнеры Docker командой
```
docker compose up
```
* Откройте в браузере страницу сервиса по адресу `http://127.0.0.1:8000/`

<a name="pages"></a>
## Состав страниц сайта
<a name="page-swagger"></a>
### Документация Swagger
В документацию можно попасть после запуска проекта по адресу http://127.0.0.1:8000/api/schema/swagger.

<a name="page-rest"></a>
### Конвертация валют по REST API
После запуска проекта доступен по адресу http://127.0.0.1:8000/api/rates?from=USD&to=RUB&value=1.
\
Под GET-запросы «from» и «to» можно указать свои валюты, если не указан «value», то по умолчанию используется значение «1».

<a name="utils"></a>
## Используемые библиотеки
asgiref==3.7.2\
attrs==23.1.0\
certifi==2023.7.22\
charset-normalizer==3.2.0\
Django==4.2.5\
djangorestframework==3.14.0\
drf-spectacular==0.26.4\
idna==3.4\
inflection==0.5.1\
jsonschema==4.19.0\
jsonschema-specifications==2023.7.1\
python-dotenv==1.0.0\
pytz==2023.3.post1\
PyYAML==6.0.1\
referencing==0.30.2\
requests==2.31.0\
rpds-py==0.10.3\
sqlparse==0.4.4\
uritemplate==4.1.1\
urllib3==2.0.4\