from aiogram.fsm.state import State, StatesGroup

 
class RegisterState(StatesGroup):
    ism = State()
    yosh = State()
    davlat = State()
    millat = State()
    