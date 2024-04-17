Бот возвращает цену на определённое количество валюты (евро, доллар или рубль). Выполнено

При написании бота необходимо использовать библиотеку pytelegrambotapi. Выполнено

Человек должен отправить сообщение боту в виде <имя валюты, цену которой он хочет узнать> <имя валюты, в которой надо узнать цену первой валюты> <количество первой валюты>. Выполнено

При вводе команды /start или /help пользователю выводятся инструкции по применению бота. Выполнено

При вводе команды /values должна выводиться информация о всех доступных валютах в читаемом виде. Выполнено

Для получения курса валют необходимо использовать любое удобное API и отправлять к нему запросы с помощью библиотеки Requests. Выполнено

Для парсинга полученных ответов использовать библиотеку JSON. Выполнено

При ошибке пользователя (например, введена неправильная или несуществующая валюта или неправильно введено число) вызывать собственно написанное исключение APIException с текстом пояснения ошибки. Выполнено

Текст любой ошибки с указанием типа ошибки должен отправляться пользователю в сообщения. Выполнено

Для отправки запросов к API описать класс со статическим методом get_price(), который принимает три аргумента и возвращает нужную сумму в валюте:
имя валюты, цену на которую надо узнать, — base;
имя валюты, цену в которой надо узнать, — quote;
количество переводимой валюты — amount. Выполнено

Токен Telegram-бота хранить в специальном конфиге (можно использовать .py файл). Выполнено

Все классы спрятать в файле extensions.py. Выполнено