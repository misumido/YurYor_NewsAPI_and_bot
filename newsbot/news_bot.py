from aiogram import Router, F
import os
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message,CallbackQuery, ReplyKeyboardRemove
from newsbot.buttons import *
import newsbot.states as states
from configs import TELEGRAM_CHANNEL_ID, PHOTO_DIR
from random import randint
from database.newsservice import *
bot_router = Router()
admin_id = 305896408
channel_id = int(TELEGRAM_CHANNEL_ID)
@bot_router.message(CommandStart())
async def start(message: Message):
    user_id = message.from_user.id
    if user_id == admin_id:
        await message.bot.send_message(user_id, "Хотите создать новость?", reply_markup= await main_menu_in())
@bot_router.callback_query(F.data.in_(["add_news", "none"]))
async def call_backs(query: CallbackQuery, state: FSMContext):
    await state.clear()
    if query.data == "add_news":
        await query.bot.delete_message(chat_id=query.from_user.id, message_id=query.message.message_id)
        await query.bot.send_message(chat_id=query.from_user.id, text="Напишите заголовок новости",
                                     reply_markup=await cancel_bt())
        await state.set_state(states.News.title_st)
    elif query.data == "none":
        await query.message.bot.answer_callback_query(query.id, text="Данная новость была удалена",
                                                      show_alert=True)
@bot_router.callback_query(lambda call: "publish_" in call.data)
async def publish(query: CallbackQuery):
    news_id = int(query.data.replace("publish_", ""))
    channel_message = await query.bot.copy_message(chat_id=channel_id, from_chat_id=query.from_user.id,
                                 message_id=query.message.message_id)
    await query.bot.edit_message_reply_markup(chat_id=query.from_user.id, message_id=query.message.message_id,
                                              reply_markup=await delete_in(channel_message.message_id))
    publish_news_db(news_id, channel_message.message_id)

@bot_router.callback_query(lambda call: "delete_" in call.data)
async def again(query: CallbackQuery):
    message_id = int(query.data.replace("delete_", ""))
    await query.bot.delete_message(chat_id=channel_id, message_id=message_id)
    await query.bot.edit_message_reply_markup(chat_id=query.from_user.id, message_id=query.message.message_id,
                                              reply_markup=await for_deleted_in())
    delete_news_db(message_id)

@bot_router.message(states.News.title_st)
async def title(message: Message, state: FSMContext):
    user_id = message.from_user.id
    if message.text:
        if message.text == "❌Отменить":
            await message.bot.send_message(user_id, "Действия отменены", reply_markup= ReplyKeyboardRemove())
            await state.clear()
        else:
            await message.bot.send_message(user_id, "Отправьте текст новости, либо фотографию с описанием",
                                           reply_markup=await cancel_bt())
            await state.set_data({"title": message.text})
            await state.set_state(states.News.text_st)
    else:
        await message.bot.send_message(user_id, "Формат сообщения не поддерживается")

@bot_router.message(states.News.text_st)
async def change_greeting(message: Message, state: FSMContext):
    user_id = message.from_user.id
    data = await state.get_data()
    title = data.get("title")
    if message.text == "❌Отменить":
        await message.bot.send_message(user_id, "Действия отменены", reply_markup=ReplyKeyboardRemove())
        await state.clear()
    elif message.text:
        id = add_news_db(title=title, text=message.text)
        await message.bot.send_message(user_id, text=f"<b>{title}</b>\n{message.text}", parse_mode="html",
                                       reply_markup=await publish_in(id))
        await state.clear()
    elif message.photo:
        photo = message.photo[-1]
        file_name = f"photo_{randint(1,1000000000)}_{photo.file_id}.jpg"
        file_path = os.path.join(PHOTO_DIR, file_name)
        file = await message.bot.get_file(photo.file_id)
        await message.bot.download_file(file.file_path, destination=file_path)
        id = add_news_db(title=title, text=message.caption, photo=file_name)
        caption = message.caption if message.caption else ""
        await message.bot.copy_message(chat_id=user_id, from_chat_id=message.from_user.id,
                                       message_id=message.message_id,
                                       caption=f"<b >{title}</b>\n{caption}",
                                       parse_mode="html",
                                       reply_markup=await publish_in(id))
        await state.clear()
    else:
        await message.bot.send_message(user_id, "Формат сообщения не поддерживается")






