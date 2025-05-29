from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

async def main_menu_bt():
    buttons = [
        [KeyboardButton(text="🗞️Добавить новость")]
        ]
    kb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=buttons)
    return kb
async def main_menu_in():
    buttons = [
        [InlineKeyboardButton(text="🗞️Добавить новость", callback_data="add_news")]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=buttons)
    return kb
async def publish_in(id):
    buttons = [
        [InlineKeyboardButton(text="✅Опубликовать", callback_data=f"publish_{id}")]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=buttons)
    return kb

async def delete_in(message_id):
    buttons = [
        [InlineKeyboardButton(text="🗑️Удалить", callback_data=f"delete_{message_id}")]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=buttons)
    return kb
async def for_deleted_in():
    buttons = [
        [InlineKeyboardButton(text="Данная новость была удалена", callback_data="none")]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=buttons)
    return kb
async def cancel_bt():
    buttons = [
        [KeyboardButton(text="❌Отменить")]
    ]
    kb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=buttons)
    return kb