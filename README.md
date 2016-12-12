# тест таск для izhevsknet

Без каких-либо внешних зависимостей; raw BaseHttpServer из built-in питона.

### убедитесь, что в системе стоит python2.7.*

#Шаги:
----
##db
> `sudo yum install MySQL-python` (rpm-based) OR
> `sudo apt-get install MySQL-python` (deb-based)

----
##скормите установку бд и таблиц (от `root`):
> `#: mysql -u root -p < test.sql`,
введите пароль для администратора бд

----
##настройки
> Хранятся в `config.json`, настройки для `mysql` predefined.

----
##запуск
> в терминале (от `root`)
> `#: python test_server.py` запустит веб-сервер на locahost:<port>, значение порта в конфиге

http://localhost:80/
