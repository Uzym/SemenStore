import operator
import logging

from aiogram.types import CallbackQuery, Message

from aiogram_dialog import Window, DialogManager
from aiogram_dialog.widgets.kbd import Select, Group, ScrollingGroup, Button, Row, Cancel
from aiogram_dialog.widgets.text import Format, Const
from aiogram_dialog.widgets.input import MessageInput

from src.lexicon import LEXICON
from src.services import FirmService
from src.states.states import Firm


firm_service = FirmService()
logger = logging.getLogger()


async def firm_create_go_back_button(callback: CallbackQuery, button: Button, manager: DialogManager, **kwargs):
    await manager.switch_to(Firm.firm_create)


firm_create_go_back_button = Button(
    text=Const("Назад"),
    id="firms_create_go_back",
    on_click=firm_create_go_back_button
)


async def firm_create_title_param_button(callback: CallbackQuery, button: Button, manager: DialogManager, **kwargs):
    await manager.switch_to(Firm.firm_create_title_param)


async def firm_create_title_param(message: Message, message_input: MessageInput, manager: DialogManager):
    manager.dialog_data['title'] = message.text
    await manager.switch_to(Firm.firm_create)


firm_create_title_param_button = Button(
    text=Const("Задать название"),
    id="firms_search_filter_title",
    on_click=firm_create_title_param_button
)

firm_create_title_param_window = Window(
    Const("Введите название фирмы"),
    MessageInput(firm_create_title_param),
    Row(firm_create_go_back_button, Cancel(Const(LEXICON["cancel"]))),
    state=Firm.firm_create_title_param
)


async def firm_create_description_param_button(callback: CallbackQuery, button: Button, manager: DialogManager, **kwargs):
    await manager.switch_to(Firm.firm_create_description_param)


async def firm_create_description_param(message: Message, message_input: MessageInput, manager: DialogManager):
    manager.dialog_data['description'] = message.text
    await manager.switch_to(Firm.firm_create)


firm_create_description_param_button = Button(
    text=Const("Задать описание"),
    id="firms_search_filter_description",
    on_click=firm_create_description_param_button
)

firm_create_description_param_window = Window(
    Const("Введите описание фирмы"),
    MessageInput(firm_create_description_param),
    Row(firm_create_go_back_button, Cancel(Const(LEXICON["cancel"]))),
    state=Firm.firm_create_description_param
)


async def firm_create_discount_param_button(callback: CallbackQuery, button: Button, manager: DialogManager, **kwargs):
    await manager.switch_to(Firm.firm_create_discount_param)


async def firm_create_discount_param(message: Message, message_input: MessageInput, manager: DialogManager):
    manager.dialog_data['discount'] = float(message.text)
    await manager.switch_to(Firm.firm_create)


firm_create_discount_param_button = Button(
    text=Const("Задать скидку"),
    id="firms_search_filter_discount",
    on_click=firm_create_discount_param_button
)

firm_create_discount_param_window = Window(
    Const("Введите скидку"),
    MessageInput(firm_create_discount_param),
    Row(firm_create_go_back_button, Cancel(Const(LEXICON["cancel"]))),
    state=Firm.firm_create_discount_param
)


async def firm_create(callback: CallbackQuery, button: Button, manager: DialogManager):
    await manager.switch_to(Firm.firm)


firm_create_button = Button(
    text=Const("Создать фирму"),
    id="firm_create",
    on_click=firm_create
)


firm_create_window = Window(
    Const("Создать фирму"),
    Group(
        firm_create_title_param_button,
        firm_create_description_param_button,
        firm_create_discount_param_button,
        firm_create_button,
        firm_create_go_back_button,
        Cancel(Const(LEXICON["cancel"]))
    ),
    state=Firm.firm_create
)


async def firm_create_getter(dialog_manager: DialogManager, **kwargs):
    title = None
    if 'title' in dialog_manager.dialog_data.keys():
        title = dialog_manager.dialog_data['title']
    description = None
    if 'description' in dialog_manager.dialog_data.keys():
        description = dialog_manager.dialog_data['description']
    discount = None
    if 'discount' in dialog_manager.dialog_data.keys():
        discount = dialog_manager.dialog_data['discount']
    firm_data = await firm_service.create_firm(title=title, description=description, discount=discount)
    data = [
        (firm_data.title, firm_data.description, firm_data.discount, str(firm_data.firm_id)) # TODO пересчет скидки
    ]
    return {
        "firms": data
    }


firm_create_result_window = Window(
    Format("Фирма"),
    Group(
        Select(
            text=Format("{item[0]}\n{item[1]}\n{item[2]}"),
            item_id_getter=operator.itemgetter(1),
            items="firm",
            id="firm_i"
        ),
        id="firm",
        width=1,
    ),
    Cancel(Const("Завершить")),
    state=Firm.firm,
    getter=firm_create_getter
)


create_firm_windows = [firm_create_title_param_window, firm_create_description_param_window, 
                       firm_create_window, firm_create_discount_param_window,
                       firm_create_result_window]
