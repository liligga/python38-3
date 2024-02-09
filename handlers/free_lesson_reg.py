from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


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
    await message.answer("Как вас зовут?")


@free_lesson_reg_router.message(FreeLessonReg.name)
async def process_name(message: types.Message, state: FSMContext):
    await message.answer(f"Спасибо, {message.text}")