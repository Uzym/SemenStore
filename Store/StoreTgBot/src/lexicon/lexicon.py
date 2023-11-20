from aiogram.types import BotCommand
from emoji import emojize

BOT_NAME = "Telegram Store Admin Bot"
BOT_DESCRIPTION = ("Данный бот служит для работы администрации магазина")
BOT_SHORT_DESCRIPTION = "Telegram Store Admin"

START_COMMAND = "start"
HELP_COMMAND = "help"
FIRMS_COMMAND = "firms"
NEW_FIRM_COMMAND = "new_firm"
CATEGORIES_COMMAND = "categories"
NEW_CATEGORY_COMMAND = "new_category"
SERIES_COMMAND = "series"
NEW_SERIES_COMMAND = "new_series"

COMMANDS = [
    BotCommand(command=START_COMMAND, description="перейти в главное меню"),
    BotCommand(command=HELP_COMMAND, description="открыть справку"),
    BotCommand(command=FIRMS_COMMAND, description="управление фирмами"),
    BotCommand(command=NEW_FIRM_COMMAND, description="создать фирму"),
    BotCommand(command=CATEGORIES_COMMAND, description="управление категориями"),
    BotCommand(command=NEW_CATEGORY_COMMAND, description="создать категорию"),
    BotCommand(command=SERIES_COMMAND, description="управление сериями"),
    BotCommand(command=NEW_SERIES_COMMAND, description="создать серию")
]

LEXICON: dict[str, str] = {
    "main_window": emojize(":up_arrow: Главное меню"),
    "get_me": emojize(":factory_worker: Мой аккаунт"),
    "back": emojize(":BACK_arrow: Назад"),
    "cancel": emojize(":stop_sign: Отменить"),
    "main_menu_button": emojize(":up_arrow: Главное меню"),
    "help_button": emojize(":red_question_mark: Помощь"),
    "ok": emojize(":green_circle: Подтвердить"),
    "add": emojize(":plus: Добавить"),
    "update": emojize(":memo: Изменить"),
    "start": "",
    "help": BOT_DESCRIPTION,
    "not_found": "Данный элемент не найден",
    "loading": "Выполняется запрос",
    "bad_input": "Неправильный ввод",
    "select_title": emojize(":blue_book: Задать название"),
    "select_description": emojize(":open_book: Задать описание"),
    "select_discount": emojize(":shopping_cart: Задать скидку"),
    "input_title": emojize(":pencil: Введите название"),
    "input_description": emojize(":pencil: Введите описание"),
    "input_discount": emojize(":pencil: Введите скидку"),
    "update_title": emojize(":pencil: Обновить название"),
    "update_description": emojize(":pencil: Обновить описание"),
    "update_discount": emojize(":pencil: Обновить скидку"),
    "search": emojize(":magnifying_glass: Поиск"),
    "search_firms": emojize(":magnifying_glass_tilted_right: Поиск фирм"),
    "firms_list": emojize(":memo: Список фирм"),
    "firm": emojize(":trade_mark: Фирма"),
    "create_firm": emojize(":plus: Создать фирму"),
    "add_photo": emojize(":framed_picture: Добавить фото"),
    "delete_photo": emojize(":wastebasket: Удалить фото"),
    "send_photo": emojize(":sparkler: Отправьте фото (как фото а не как файл)"),
    "complete": emojize(":check_mark_button: Завершить"),
    "update_firm": emojize(":pencil: Изменить фирму"),
    "delete_firm": emojize(":wastebasket: Удалить фирму"),
    "search_categories": emojize(":magnifying_glass_tilted_right: Поиск категорий"),
    "categories_list": emojize(":memo: Список категорий"),
    "category": emojize(":trade_mark: Категория"),
    "create_category": emojize(":plus: Создать категорию"),
    "update_category": emojize(":pencil: Изменить категорию"),
    "delete_category": emojize(":wastebasket: Удалить категорию"),
    "search_series": emojize(":magnifying_glass_tilted_right: Поиск серий"),
    "series_list": emojize(":memo: Список серий"),
    "series": emojize(":trade_mark: Серия"),
    "create_series": emojize(":plus: Создать серию"),
    "update_series": emojize(":pencil: Изменить серию"),
    "delete_series": emojize(":wastebasket: Удалить серию"),
}
