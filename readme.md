# Порядок работы приложения по парсингу Google таблиц и отправки сообщений в группу Telegram

## Требования к парсингу Google таблиц

Для корректного парсинга Google таблицы нужно:
1. Создать приложение в центре разработки Google
2. Для приложения разрешить использование API Google диска и Google таблиц
3. Создать сервисную учетную запись
4. Сохранить API токен в json файл. Файл размеситить рядом с файлом .env. Указать название файла с токеном в .env файле.
5. Предоставить доступ к нужной таблице для созданной сервисной учетной записи стандартными средствами Google таблиц

Данное приложение заточено под определенные правила ведения информации в Google таблице.

1. Имя таблицы может быть любым. Основное условие, что имя таблицы должно быть правильно указано в .env файле.
2. Информация о сотрудниках и возможных вариантах поздравлений разнесена по разным страницам таблицы. Имена страниц
также задаются через .env файл
3. Данные о сотрудниках должны вестись в структурированном виде. Первая строка таблицы должна представлять собой 
заголовки полей (Name, Surename, Birthday)
4. Формат даты дня рождения dd/mm/yyyy
5. Перечень поздравлений должен идти сплошным списком, без заголовков. Одно поздравление на одной строке.

## Требования к настройке Telegram бота

1. Группа для которой необходимо активировать функцию поздравления сотрудников должна быть публичной.
2. Бот должен быть включен в состав этой группы. Боту должны быть предоставлены права администратора на группу.

## Общие требования

Перед использованием приложения необходимо установить зависимости из файла requirements.txt и соответствующием образом
отредаткировать .env файл.