# service-ai
By school 30 from Nighniy Novgorod 

#### Для запуска нужен Python 3.x

# [RU]
#### 1. Установка библиотек
* Откройте командную строку(cmd) в дирректории с программой
* Введите
```sh
pip install -r requirements.txt
```
* Поздравляю, вы установили все нужные для работы библиотеки :)
***
#### 2. Настройка системы
* Откройте файл config.py
* Вы увидите такое содержание
```sh
MCHS_SERVER_ENABLED = False
MCHS_SERVER_ADDRESS = "http://api.mchs.ru"
MCHS_REQUEST_HEADERS = {"access_token": ""}
MCHS_REQUEST_METHOD = "POST"
```
* MCHS_SERVER_ENABLED - Включена ли отправка на сервер МЧС (Boolean)
* MCHS_SERVER_ADDRESS = Стрка с адресом сервера API мтч
* MCHS_REQUEST_HEADERS = Заголовки (Python dictionary)
* MCHS_REQUEST_METHOD = метод запросв (POST, GET, и т.д)
***

#### 3. Запуск
* Введите в командной строке (в корне приложения)
```sh
python run.py
```
* Готово

