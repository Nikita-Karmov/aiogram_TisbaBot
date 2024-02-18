from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command

user_private_router = Router()


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Ку,этот бот поможет тебе узнать твоё расписание")


@user_private_router.message(Command('date'))
async def menu_cmd(message: types.Message):
    await message.answer("выбери день недели!:")


@user_private_router.message(Command('monday'))
async def menu_cmd(message: types.Message):
    await message.answer("ФИЗКУЛЬТУРА  с 14-00 в олимпе (выходной!!)")


@user_private_router.message(Command('tuesday'))
async def menu_cmd(message: types.Message):
    await message.answer("1 пара (9:30-10.50)-Технология разработки и защиты баз данных ауд.111|\n"
                         "2 пара (11:00-12:20)-Технология разработки и защиты баз данных ауд. 111|\n"
                         "3 пара (12:50-14:10)-Теория вероятности и математическая статистика ауд.404")


@user_private_router.message(Command('wednesday'))
async def menu_cmd(message: types.Message):
    await message.answer("1 пара (9:30-10.50)-Иностранный язык ауд. 114-409|\n"
                         "2 пара (11:00-12:20)-Разработка программных модулей ауд. 402|\n"
                         "3 пара (12:50-14:10)-Обеспечение качества  функционирования компьютерных систем ауд.108")


@user_private_router.message(Command('thursday'))
async def menu_cmd(message: types.Message):
    await message.answer("1 пара (8.00-9.20)-Поддержка и тестирование программных модулей ауд. 402\n"
                         "2 пара (9.25-10.45)-Обеспечение качества  функционирования компьютерных систем  ауд. 111\n"
                         "3 пара (10.50-12.10)-Архитектура аппаратных средств СЕМЁНЁВ!!!! ауд.101\n"
                         "4 пара (12.15-13.35)-Поддержка и тестирование программных модулей ауд.111")


@user_private_router.message(Command('friday'))
async def menu_cmd(message: types.Message):
    await message.answer("1 пара (12:50-14:10)-Внедрение и пдрж программного обеспечения компьютерных  ауд. 108|\n"
                         "2 пара (14:20-15:40)-Обеспечение качества функционирования компьютерных систем ауд. 114|\n"
                         "3 пара (15:50-17:10)-Основы алгоритмизации и программирования ауд.111")


@user_private_router.message(Command('saturday'))
async def menu_cmd(message: types.Message):
    await message.answer("1 пара (8.00-9.20)-Поддержка и тестирование программных модулей ауд. 402|\n"
                         "2 пара (9.25-10.45)-Обеспечение качества  функционирования компьютерных систем  ауд. 111|\n"
                         "3 пара (10.50-12.10)-Архитектура аппаратных средств СЕМЁНЫЧЕВ!!!! ауд.101|\n"
                         "4 пара (12.15-13.35)-Поддержка и тестирование программных модулей ауд.111")


@user_private_router.message(Command('sunday'))
async def menu_cmd(message: types.Message):
    await message.answer("пися и попа")


@user_private_router.message(Command('donat'))
async def start_cmd(message: types.Message):
    await message.answer("деньги за тисбу сюда 5536914188548550")


@user_private_router.message(F.text)
async def start_cmd(message: types.Message):
    await message.answer("я тупой бот тисби могу воспринимать только команды, но ты можешь выбрать команды из этого"
                         " списка: /monday /tuesday /wednesday /thursday /friday /saturday /sunday")


@user_private_router.message(F.photo)
async def start_cmd(message: types.Message):
    await message.answer("я тупой бот тисби могу воспринимать только команды, но ты можешь выбрать команды из этого "
                         "списка: /monday /tuesday /wednesday /thursday /friday /saturday /sunday")


@user_private_router.message(F.sticker)
async def start_cmd(message: types.Message):
    await message.answer("я тупой бот тисби могу воспринимать только команды, но ты можешь выбрать команды из этого "
                         "списка: /monday /tuesday /wednesday /thursday /friday /saturday /sunday")

# @user_private_router.message(F.text, F.text.lower().contains('дни недели'))
# async def start_cmd(message: types.Message):
#      await message.answer("выбери один из этих дней: /monday /Tuesday /Wednesday /Thursday /Friday /Saturday /Sunday")
