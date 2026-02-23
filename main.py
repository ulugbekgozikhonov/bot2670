from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command 
from aiogram.fsm.context import FSMContext
import logging 
from state import RegisterState
from database import create_table, insert_user, get_user

from aiogram.client.session.aiohttp import AiohttpSession

logging.basicConfig(level=logging.INFO)

PROXY_URL = 'http://proxy.server:3128'
BOT_TOKEN = "8090071919:AAFfkerj0nWL-i9l_J_so4rM8F390EyBKsc"

session = AiohttpSession(proxy=PROXY_URL)
bot = Bot(token=BOT_TOKEN, session=session)



dp = Dispatcher()


@dp.message(Command("start"))
async def start_handler(message: types.Message, state: FSMContext):
    id = message.from_user.id
    user = get_user(id)
    if user:
        await message.answer(f"Xush kelibsiz {user[1]}!")
    else:
        await message.answer("Welcome to bot")
        await message.answer("Ismingizni kiriting")
        await state.update_data(id=id)
        await state.set_state(RegisterState.ism)


@dp.message(RegisterState.ism)
async def ism_handler(message:types.Message, state: FSMContext):
    ism = message.text 
    await state.update_data(ism=ism)
    await message.answer("Yoshingizni kiriting")
    await state.set_state(RegisterState.yosh)


@dp.message(RegisterState.yosh)
async def yosh_handler(message:types.Message, state: FSMContext):
    yosh = message.text 
    await state.update_data(yosh=yosh)
    await message.answer("Davlatingizni kiriting")
    await state.set_state(RegisterState.davlat)


@dp.message(RegisterState.davlat)
async def davlat_handler(message:types.Message, state: FSMContext):
    davlat = message.text 
    await state.update_data(davlat=davlat)
    await message.answer("Millatingizi kiriting")    
    await state.set_state(RegisterState.millat)


@dp.message(RegisterState.millat)
async def millat_handler(message:types.Message, state: FSMContext):
    millat = message.text 
    await state.update_data(millat=millat)
    data = await state.get_data()
    insert_user(data)
    await message.answer("Malumotlar saqlandi ✅")    
    await state.clear()  


async def main():
    create_table()
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio 
    asyncio.run(main()) 
