# Бот по работе с заданиями.

Данный сайт сделан в качестве тестового задания.

## Запуск

Проект предполагает наличие установленного Python. 

1. Установить зависимости

```commandline
pip install -r requirements.txt
```

2. Создать базы данных с именем site в PostgreSQL

```commandline
sudo -u postgres psql
postgres=# createbase tasks;
```

3. Запуск файла

```commandline
flask run
```
