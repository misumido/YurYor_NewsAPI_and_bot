from aiogram.fsm.state import State, StatesGroup

class News(StatesGroup):
    title_st = State()
    text_st = State()
