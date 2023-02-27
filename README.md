### Тестирование UI-интерфейса сайта https://demoqa.com/

- Создать окружение:
> python -m venv venv
- Активировать окружение:
> source venv/Scripts/activate
- Установить зависимости:
> pip install -r requirements.txt
- Для запуска тестов выполнить команду:
> pytest

#### Для запуска тестов в firefox-browser, необходимо поменять значение браузера на "firefox" в файле tests/config.json.