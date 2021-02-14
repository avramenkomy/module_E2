!!! Внимание, отправка писем идет через mail.ru, чтобы заработало на локальном сервере необходимо указать переменные окружения:
SECRET_KEY = <ваш SECRET_KEY для Django>
EMAIL_HOST_USER = имя Вашего почтового ящика на mail.ru в формате <example@mail.ru>
EMAIL_HOST_PASSWORD = пароль для Вашего почтового ящика

1. Клонировать проект git clone https://github.com/avramenkomy/module_E2.git
2. Установить requirements.txt - pip install -r requirements.txt
3. Указать переменные среды
4. Запустить локальный сервер - python manage.py runserver
5. Доступны формы отправки сообщения с задержкой по времени в секундах и форма отправки трех сообщений с возможностью установки различной задержки по времени
    !!!При отправки нескольких писем необходимо заполнить все три формы !!!
    обработка невалидных форм не предумотрена