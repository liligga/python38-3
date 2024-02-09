from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from keyboards.free_lesson_courses_kb import free_lesson_courses_kb


# FSM - Finite State Machine, конечный автомат
class FreeLessonReg(StatesGroup):
    name = State()
    age = State()
    email = State()
    course = State()


free_lesson_reg_router = Router()

@free_lesson_reg_router.message(Command("free_lesson"))
async def start_reg(message: types.Message, state: FSMContext):
    await state.set_state(FreeLessonReg.name)
    await message.answer("Ответьте на несколько вопросов, чтобы записаться на бесплатный урок. Для завершения введите /stop")
    await message.answer("Как вас зовут?")


@free_lesson_reg_router.message(Command("stop"))
async def stop_reg(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Спасибо за уделенное время, приходите позже!")


@free_lesson_reg_router.message(FreeLessonReg.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(f"Спасибо, {message.text}")
    await state.set_state(FreeLessonReg.age)
    await message.answer("Сколько вам лет?")


@free_lesson_reg_router.message(FreeLessonReg.age)
async def process_age(message: types.Message, state: FSMContext):
    age = message.text
    if not age.isdigit():
        await message.answer("Возраст должен быть числом")
    elif int(age) < 14 or int(age) > 65:
        await message.answer("Возраст должен быть от 14 до 65")
    else:
        await state.update_data(age=message.text)
        await state.set_state(FreeLessonReg.email)
        await message.answer("Ведите Ваш email")


@free_lesson_reg_router.message(FreeLessonReg.email)
async def process_email(message: types.Message, state: FSMContext):
    await state.update_data(email=message.text)
    await state.set_state(FreeLessonReg.course)
    await message.answer("Какое направление Вам подходит?", reply_markup=free_lesson_courses_kb())


@free_lesson_reg_router.message(FreeLessonReg.course)
async def process_course(message: types.Message, state: FSMContext):
    remove_kb = types.ReplyKeyboardRemove()
    await state.update_data(course=message.text)
    await message.answer("Спасибо", reply_markup=remove_kb)
    data = await state.get_data()
    # save to DataBase
    await message.answer(f"Ваши дданные: {data}")
    await state.clear()
