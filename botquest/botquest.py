import logging
import emoji
from aiogram import Bot, Dispatcher, executor, types
from os import getenv
from sys import exit
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

import time
import asyncio
from tkinter import *
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
TOKEN = "5015439752:AAH4QQ35AVshBYcSWgAdtLjOUubnxaXGz4Y"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot,storage = MemoryStorage())
logging.basicConfig(level=logging.INFO)

window = Tk()
window.title("bot construct")


class InputUserData(StatesGroup):
    start = State()
    step_2 = State()
    raspr = State()
    lab_raspr = State()
class Stages(StatesGroup):
    malevich = State()
    kazan = State()
    step3 = State()
    step4 = State()
    waiting =State()
    waiting1 =State()
    waiting2 =State()
    waiting3 =State()
    waiting4 =State()
    waiting5 =State()
    waiting6 =State()
    waiting7 =State()
    waiting8 =State()
    waiting9 =State()

    final = State()
class Stages_lab(StatesGroup):
    step_1 = State()
    step_2 = State()
    step_3 = State()
    step_4 = State()
    step_5 = State()
    step_6 = State()
    step_7 = State()
    waiting =State()
    waiting1 =State()
    waiting2 =State()
    waiting3 =State()
    waiting4 =State()
    waiting5 =State()
    waiting6 =State()
    waiting7 =State()
    waiting8 =State()
    waiting9 =State()
    vr = State()
    waiting_game = State()
    waiting_video = State()
    waiting_game1 = State()
    waiting_video1 = State()
    waiting_game2 = State()
    waiting_video2 = State()
    waiting_game3 = State()
    waiting_video3 = State()
    waiting_game4 = State()
    waiting_video4 = State()
    waiting_game5 = State()
    waiting_video5 = State()
    waiting_game6 = State()
    waiting_video6 = State()
route = {}
lab_route = {}


@dp.message_handler(commands="start",state="*")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    await message.answer(emoji.emojize(':wave:',use_aliases=True) + "Привет! Я верный помощник профессора Ломанштейна-МакБрауни - Искусственный Нейронный Жизнерадостный Интеллект, сокращенно - ИНЖИ!" +emoji.emojize(':robot:',use_aliases=True))
    await asyncio.sleep(4)
    await message.answer("Я вижу что он смог найти здесь помощь!")
    await asyncio.sleep(4)
    await message.answer("Прошу, введите секретный код от профессора, чтобы я мог точно знать, что вы друзья.",reply_markup=keyboard)
    await asyncio.sleep(4)
    await InputUserData.start.set()

kodes = ["1567","2784","3048","4650"]
@dp.message_handler(text=kodes,state=InputUserData.start, content_types=types.ContentTypes.TEXT)
async def any_text_message(message: types.Message, state: FSMContext):

    async with state.proxy() as user_data:
    # Здесь user_data является хранилищем (а точнее словарем), куда можно сохранять определенные данные и вытаскивать если нужно в любой момент
        user_data[message.chat.id] = message.text.replace('\n',' ')
        global route
        route[message.chat.id]=user_data[message.chat.id]
        lbl = Label(window, text=route)
        lbl.grid(column=0, row=0)


    await state.finish()
    async with state.proxy() as data:
        data[message.chat.id] = 0
    async with state.proxy() as data:
        data[message.chat.id] = 0
    await message.answer(emoji.emojize(':thumbsup:',use_aliases=True)+"Здорово! Теперь с вашей помощью мы с профессором можем попробовать починить машину времени и вернуться домой!")
    await asyncio.sleep(4)
    await message.answer("Мне нужен ключ, с помощью которого я смогу подключиться к сети Сколково и узнать что можно использовать для восстановления машины времени.")
    await asyncio.sleep(4)
    await message.answer("Части ключа спрятаны здесь в Атриуме, нам нужно их найти.")
    await asyncio.sleep(4)
    await message.answer(emoji.emojize(':face_with_monocle:',use_aliases=True)+"Но для начала мы должны осмотреться.")
    await asyncio.sleep(4)
    await message.answer(emoji.emojize(':information_source:',use_aliases=True)+"Сколково очень большое место, тут легко заблудиться.")
    await asyncio.sleep(4)
    await message.answer("Три ключевых ориентира в Технопарке:")
    await asyncio.sleep(4)
    await message.answer("Атриум — это большой холл в здании Технопарка Сколково. Здесь мы сейчас и находимся.\n\nЯдра — огромные шары для удобства ориентирования внутри большого Атриума. По этим шарам гости Сколково могут находить необходимые помещения, мероприятия, лаборатории.\n\nКаспулы — стеклянные аудитории, в которых проходят конференции, мастер-классы, мероприятия.")
    await asyncio.sleep(4)
    await message.answer("Я помогу вам с поисками.")
    await asyncio.sleep(4)
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Да!", callback_data="yes"))
    await message.answer("Готовы?",reply_markup=keyboard)
    await InputUserData.raspr.set()
@dp.callback_query_handler(text="yes",state=InputUserData.raspr)
async def send_random_value(call: types.CallbackQuery,state: FSMContext):
    def cod_creator(x):
        x = int(x)
        if x == 1567:
            x = 1234
        elif x == 2784:
            x = 2341
        elif x == 3048:
            x = 3412
        elif x ==4650:
            x = 4123
        result = []
        while x > 0:
            result.append(x % 10)
            x //= 10
        result.reverse()
        result.append(0)
        return result
    global route
    print(call.message.chat.id)
    a = cod_creator(route[call.message.chat.id])
    print(a)
    async with state.proxy() as data:
        number = data[call.message.chat.id]
    print(number)
    if a[number] == 1:
        await call.message.answer("Вычисляю маршрут...")
        await Stages.malevich.set()
        await asyncio.sleep(4)
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Вперед!", callback_data="step"))
        await call.message.answer("Нашел!",reply_markup=keyboard)
        await asyncio.sleep(4)
    elif a[number]== 2:
        await call.message.answer("Вычисляю маршрут...")
        await Stages.kazan.set()
        await asyncio.sleep(4)
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Вперед!", callback_data="step"))
        await call.message.answer("Нашел!",reply_markup=keyboard)
        await asyncio.sleep(4)
    elif a[number] ==3:
        await call.message.answer("Вычисляю маршрут...")
        await Stages.step3.set()
        await asyncio.sleep(4)
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Вперед!", callback_data="step"))
        await call.message.answer("Нашел!",reply_markup=keyboard)
        await asyncio.sleep(4)
    elif a[number] ==4:
        await call.message.answer("Вычисляю маршрут...")
        await Stages.step4.set()
        await asyncio.sleep(4)
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Вперед!", callback_data="step"))
        await call.message.answer("Нашел!",reply_markup=keyboard)
        await asyncio.sleep(4)
    elif a[number] == 0:
        await call.message.answer("Вычисляю маршрут...")
        await Stages.final.set()
        await asyncio.sleep(4)
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Вперед!", callback_data="step"))
        await call.message.answer("Нашел!",reply_markup=keyboard)
    elif a[number] == 9:
        await call.message.answer("Ребята! Я обнаружил в Атриуме одну очень интересную штуку! Мы можем увидеться с вами и поиграть!")
        await asyncio.sleep(4)
        await call.message.answer("Вам нужно найти капсулу с названием  Portal Tech. Она находится недалеко от Ядра 2.")
        await asyncio.sleep(4)
        await call.message.answer("Когда дойдете до нужного места, сообщите мне секретный код, чтобы я понял что пришли вы, а не какие-то злодеи. Код должен находиться где-то рядом с капсулой.")
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Вперед!", callback_data="step"))
        await asyncio.sleep(4)
        await Stages.waiting.set()


@dp.message_handler(text="7653",state=Stages.waiting)
async def any_text_message(message: types.Message,state: FSMContext):
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(types.InlineKeyboardButton(text="Едем дальше", callback_data="yes"))
            await message.answer("Теперь нужно пройти дальше в противоположную от входа сторону, слева вы увидите большую светящуюся вывеску Portal Sсreen. Спросите сотрудника или помощников ученого, они объяснят, как можно поиграть со мной. Когда закончите - жмите кнопку.",reply_markup=keyboard)
            await InputUserData.raspr.set()
            async with state.proxy() as data:
                    data[message.chat.id] +=1
#Этапы
@dp.callback_query_handler(text="step",state=Stages.malevich)
async def send_random_value(call: types.CallbackQuery,state: FSMContext):
    await call.message.answer(emoji.emojize(':nerd_face:',use_aliases=True)+"Расположение Сколково выбрано не случайно.")
    await asyncio.sleep(4)
    await call.message.answer("В этих местах любил бывать известный художник начала XX века.")
    await asyncio.sleep(4)
    await call.message.answer("Из-за крушения я забыл, что это за художник.")
    await asyncio.sleep(4)
    await call.message.answer("Кажется, в его фамилии и зашифрована часть ключа.")
    await asyncio.sleep(4)
    await call.message.answer(emoji.emojize(':play_button:')+ "В Атриуме есть капсула, названная в его честь. Названия или номера капсул обычно находятся на табличках сверху.")
    await asyncio.sleep(4)
    await call.message.answer(emoji.emojize(":bell:")+("Найдите капсулу с его фамилией и напишите ее."))
    await asyncio.sleep(4)
    await Stages.waiting1.set()
word = ["Malevich","Малевич","малевич","malevich"]
@dp.message_handler(text=word,state=Stages.waiting1)
async def any_text_message(message: types.Message,state: FSMContext):
  
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Едем дальше", callback_data="yes"))
        await message.answer("Да, точно!")
        await asyncio.sleep(4)
        await message.answer("Я нашел в вашем времени интересную вещь! Есть мой друг бот, который с помощью нейронной сети может нарисовать картину, похожую на картину Казимира Малевича.")
        await asyncio.sleep(4)
        await message.answer("Попробуйте создать свою картину в его стиле:\n\n — Откройте моего бота-друга: @sber_rudalle_xl_bot;\n — Напишите “Малевич” и еще 2-3 слова, которые первыми пришли тебе в голову;\n — Через 1-2 минуты ваша картина будет готова!")
        await asyncio.sleep(5)
        await message.answer(emoji.emojize(':white_check_mark:',use_aliases=True)+"Вот часть ключа: 8",reply_markup=keyboard)
        await InputUserData.raspr.set()
        async with state.proxy() as data:
                data[message.chat.id] +=1

@dp.callback_query_handler(text="step",state=Stages.kazan)
async def send_random_value(call: types.CallbackQuery,state: FSMContext):
    await call.message.answer(emoji.emojize(':woman_scientist:')+"Важнейшим этапом в разработке новых технологий является презентация этой самой технологии.")
    await asyncio.sleep(4)
    await call.message.answer("Для этих презентаций инженеры и учёные используют большие залы, чтобы каждый мог увидеть, о чем они говорят.")
    await asyncio.sleep(4)
    await call.message.answer(emoji.emojize(':play_button:')+"В Сколково это зал Казан. Дно этого зала выглядит как огромная блестящая кастрюля на ножках.")
    await asyncio.sleep(4)
    await call.message.answer("В этом зале презентовали как-то и меня.")
    await asyncio.sleep(4)
    await call.message.answer("Ну, вернее презентуют, если говорить о вашем времени.")
    await asyncio.sleep(4)
    await call.message.answer("По моим подсчетам, в этом месте находится часть ключа.")
    await asyncio.sleep(4)
    await call.message.answer(emoji.emojize(':bell:')+("Осмотритесь и напишите номер ядра, возле которого располагается основание зала.\nНапомню, Ядро - это большой шар, который вы увидите, если поднимете голову вверх."))
    await asyncio.sleep(4)
    await Stages.waiting2.set()
chislo=["1","2","1 ядро","2 ядро","1 ядро","2 Ядро","1 Ядро"]
@dp.message_handler(text=chislo,state=Stages.waiting2)
async def any_text_message(message: types.Message,state: FSMContext):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Едем дальше", callback_data="yes"))
    await message.answer(emoji.emojize(':white_check_mark:',use_aliases=True)+"Да, точно! Вот часть ключа: 9",reply_markup=keyboard)
    await InputUserData.raspr.set()
    async with state.proxy() as data:
            data[message.chat.id] +=1
@dp.callback_query_handler(text="step",state=Stages.step3)
async def send_random_value(call: types.CallbackQuery,state: FSMContext):
    await call.message.answer("Территория Сколково очень большая, поэтому здесь просто заблудиться.")
    await asyncio.sleep(4)
    await call.message.answer("Чтобы те кто приехал сюда не терялись, архитекторы придумали огромные шары для навигации — Ядра.")
    await asyncio.sleep(4)
    await call.message.answer("Вы уже их видели, правда?")
    await asyncio.sleep(4)
    await call.message.answer(emoji.emojize(':play_button:')+"Возле такого вот Ядра 5 есть робот, мой прототип, он приветствует всех гостей Сколково.")
    await asyncio.sleep(4)
    await call.message.answer("Можно считать, что это мой пра-пра-пра…  в общем, дедушка.")
    await asyncio.sleep(4)
    await call.message.answer(emoji.emojize(':bell:')+"Пожалуйста, найдите его и узнайте, как его зовут.")
    await asyncio.sleep(4)
    await call.message.answer("В его имени зашифрована часть ключа, я смогу расшифровать её. Напишите его имя.")
    await asyncio.sleep(4)
    await Stages.waiting3.set()
word1 = ["Промобот","промобот","promobot","Promobot"]
@dp.message_handler(text=word1,state=Stages.waiting3)
async def any_text_message(message: types.Message,state: FSMContext):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Едем дальше", callback_data="yes"))
    await message.answer(emoji.emojize(':white_check_mark:',use_aliases=True)+"Расшифровал! Ещё одна часть ключа: 6",reply_markup=keyboard)
    await InputUserData.raspr.set()
    async with state.proxy() as data:
            data[message.chat.id] +=1
@dp.callback_query_handler(text="step",state=Stages.step4)
async def send_random_value(call: types.CallbackQuery,state: FSMContext):
    await call.message.answer("В Сколково трудятся лучшие учёные и инженеры России. \nОни приезжают сюда со всех уголков нашей страны. \nЧтобы им было проще добираться до Сколково, был спроектирован специальный транспортный хаб, в который и прибывают поезда со специалистами.")
    await asyncio.sleep(4)
    await call.message.answer("Нам нужны координаты этого транспортного хаба.\nВ них содержится часть ключа.")
    await asyncio.sleep(4)
    await call.message.answer("Здесь, в Атриуме, найдите интерактивную карту Сколково.\nНажмите на экран и активируйте ее.\n\n" +emoji.emojize(':bell:')+"На этой карте вам нужно найти большой Транспортный хаб и узнать его название.\n" + emoji.emojize(':backhand_index_pointing_right:')+"Подсказка: \nИнтерактивная карта находится недалеко от ядра 4. \nВсе построенные и действующие здания подсвечены зелёным цветом, на них можно нажать и посмотреть, что еще интересного есть в Сколково.")
    await asyncio.sleep(4)
    await asyncio.sleep(4)
    await Stages.waiting4.set()
word2 = ["Orbion","orbion","орбион","Орбион"]
@dp.message_handler(text=word2,state=Stages.waiting4)
async def any_text_message(message: types.Message,state: FSMContext):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Едем дальше", callback_data="yes"))
    await message.answer(emoji.emojize(':white_check_mark:',use_aliases=True)+"Все верно! Я нашел еще одну часть ключа: 5",reply_markup=keyboard)
    await InputUserData.raspr.set()
    async with state.proxy() as data:
            data[message.chat.id] +=1
@dp.callback_query_handler(text="step",state=Stages.final)
async def any_text_message(call: types.CallbackQuery,state: FSMContext):
    await call.message.answer(emoji.emojize(':white_check_mark:',use_aliases=True)+"Теперь чтобы я подключился к сети Сколково вам нужно ввести все части ключа в той последовательности, что вы получили.")
    await asyncio.sleep(4)
    await InputUserData.step_2.set()

#Этапы

lab_kodes = ["8965","9658","6589","5896"]
@dp.message_handler(text=lab_kodes,state=InputUserData.step_2, content_types=types.ContentTypes.TEXT)
async def any_text_message(message: types.Message, state: FSMContext):
    async with state.proxy() as user_data:
    # Здесь user_data является хранилищем (а точнее словарем), куда можно сохранять определенные данные и вытаскивать если нужно в любой момент
        user_data[message.chat.id] = message.text.replace('\n',' ')
        global lab_route
        lab_route[message.chat.id]=user_data[message.chat.id]
        print("marshrut",lab_route)
        await state.finish()
    async with state.proxy() as lab_data:
        lab_data[message.chat.id] = 0

    await message.answer("Я смог подключиться к сети Сколково и кое-что узнать.")
    await asyncio.sleep(4)
    await message.answer("Оказывается, даже в вашем времени есть очень интересные технологии! Я нашел лаборатории, которые, возможно, смогут нам помочь.")
    await asyncio.sleep(4)
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Да!", callback_data="yes"))
    await message.answer("Ты готов?",reply_markup=keyboard)
    await InputUserData.lab_raspr.set()
@dp.callback_query_handler(text="yes",state=InputUserData.lab_raspr)
async def send_random_value(call: types.CallbackQuery,state: FSMContext):
    def cod_creator(x):
        x = int(x)
        if x == 8965:
            x = 1235
        elif x == 9658:
            x = 2351
        elif x == 6589:
            x = 3512
        elif x ==5896:
            x = 5123
        else:
            print("route error")
        result = []
        while x > 0:
            result.append(x % 10)
            x //= 10
        result.reverse()
        result.append(0)
        return result
    global lab_route
    print(call.message.chat.id)
    a = cod_creator(lab_route[call.message.chat.id])
    print(a[0])
    print("lab_route", a)
    async with state.proxy() as lab_data:
        number = lab_data[call.message.chat.id]

    if a[number] == 1:
        await call.message.answer("Вычисляю маршрут")
        print(a[number])
        await Stages_lab.step_1.set()
        await asyncio.sleep(4)
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Вперед!", callback_data="step_lab"))
        await call.message.answer("Нашел!",reply_markup=keyboard)
        await asyncio.sleep(4)
    elif a[number]== 2:
        await call.message.answer("Вычисляю маршрут")
        await Stages_lab.step_2.set()
        await asyncio.sleep(4)
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Вперед!", callback_data="step_lab"))
        await call.message.answer("Нашел!",reply_markup=keyboard)
        await asyncio.sleep(4)
    elif a[number] ==3:
        await call.message.answer("Вычисляю маршрут")
        await Stages_lab.step_3.set()
        await asyncio.sleep(4)
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Вперед!", callback_data="step_lab"))
        await call.message.answer("Нашел!",reply_markup=keyboard)
        await asyncio.sleep(4)
    elif a[number] ==4:
        await call.message.answer("Вычисляю маршрут")
        await Stages_lab.step_4.set()
        await asyncio.sleep(4)
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Вперед!", callback_data="step_lab"))
        await call.message.answer("Нашел!",reply_markup=keyboard)
        await asyncio.sleep(4)
    elif a[number] == 5:
        await call.message.answer("Вычисляю маршрут")
        await Stages_lab.step_5.set()
        await asyncio.sleep(4)
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Вперед!", callback_data="step_lab"))
        await call.message.answer("Нашел!",reply_markup=keyboard)
    elif a[number] == 9:
        await call.message.answer("Ребята! Я обнаружил в Атриуме одну очень интересную штуку! Мы можем увидеться с вами и поиграть!")
        await asyncio.sleep(4)
        await call.message.answer("Вам нужно найти капсулу с названием  Portal Tech. Она находится недалеко от Ядра 2.")
        await asyncio.sleep(4)
        await call.message.answer("Когда вы дойдете до нужного места, сообщите мне секретный код, чтобы я понял что пришли вы, а не какие-то злодеи.")
        await asyncio.sleep(4)
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Вперед!", callback_data="step_lab"))
        await call.message.answer(" а не какие-то злодеи.",reply_markup=keyboard)
        await asyncio.sleep(4)
        await Stages_lab.vr.set()
    elif a[number] == 0:
        await call.message.answer("Спасибо, что вы помогли мне загрузить все нужные данные в память, теперь мы с профессором сможем восстановить систему и корабль.\n\nВозвращайтесь в капсулу из которой вы стартовали, чтобы попрощаться с профессором, а сразу после этого мы с ним займемся восстановлением наших систем.")
    else:
        print("route error")
#Инновакс ПОМЕНЯТЬ

@dp.callback_query_handler(text="step_lab",state=Stages_lab.step_1)
async def send_random_value(call: types.CallbackQuery,state: FSMContext):
    await call.message.answer("Я обнаружил здесь выставку, технологии которой могут помочь мне восстановить систему навигации космического корабля и облегчить весь процесс починки.")
    await asyncio.sleep(4)
    await call.message.answer("Она расположена рядом с капсулой виртуальной реальности Portal Tech.")
    await asyncio.sleep(4)
    await call.message.answer("На первый взгляд там расположены обычные картины, но в каждой из них есть секрет. Ваш сопровождающий поможет вам раскрыть его.")
    await asyncio.sleep(4)
    await call.message.answer("Чтобы пройти первичную дешифровку, введите название картины с серыми шестеренками. Напишите его на русском.")
    await asyncio.sleep(4)
    await Stages_lab.waiting5.set()

@dp.message_handler(text="Река времени",state=Stages_lab.waiting5)
async def any_text_message(message: types.Message,state: FSMContext):
    await message.answer("Отлично! Это выставка AR-картин autstraction art! Я получил новые данные!")
    await asyncio.sleep(4)
    await message.answer("Хм-м, похоже что они засекречены.")
    await asyncio.sleep(4)
    await message.answer("Пожалуйста, помогите мне их расшифровать. Выполните это задание, в конце будет секретный код. Он поможет нам расшифровать необходимые данные про лабораторию Инновакс.")
    await asyncio.sleep(4)
    await message.answer("Игра проходится в режиме Gyro. \nДля перемещения вперед-назад используйте стрелки слева внизу экрана. \nДля прыжка - стрелку справа внизу экрана. \nУ вас есть 3 жизни.")
    await asyncio.sleep(4)
    await message.answer("https://edu.cospaces.io/QEW-HYM\nКод игры:QEW-HYM")
    await asyncio.sleep(4)
    await Stages_lab.waiting_game1.set()

@dp.message_handler(text="2354",state=Stages_lab.waiting_game1)
async def any_text_message(message: types.Message,state: FSMContext):
    await message.answer("Ура! Вот что мне удалось узнать:")
    await asyncio.sleep(4)
    await message.answer("Технологии AR используются в медицине, инжерии, обучении и многих других областях.")
    await asyncio.sleep(4)
    await message.answer("Но я все еще не могу понять, поможет ли эта технология нам. Посмотрите видео и загрузите необходимые данные в мою память.")
    await asyncio.sleep(4)
    await message.answer("https://www.youtube.com/watch?v=5qQt_yIz0p8")
    await asyncio.sleep(4)
    await message.answer(emoji.emojize(":bell:")+("Что такое AR?"))
    await asyncio.sleep(4)
    await Stages_lab.waiting_video1.set()

@dp.message_handler(text="Дополненная реальность",state=Stages_lab.waiting_video1)
async def any_text_message(message: types.Message,state: FSMContext):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Едем дальше", callback_data="yes"))
    await message.answer("Отлично! Теперь я смогу сделать замену сломанным деталям нашего корабля и восстановить навигационную систему!",reply_markup=keyboard)
    await InputUserData.lab_raspr.set()
    async with state.proxy() as lab_data:
        lab_data[message.chat.id] +=1

#Vr
@dp.message_handler(text="7653",state=Stages_lab.vr)
async def any_text_message(message: types.Message,state: FSMContext):
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(types.InlineKeyboardButton(text="Едем дальше", callback_data="yes"))
            await message.answer("Поехали! Когда закончите - жмите кнопку",reply_markup=keyboard)
            await InputUserData.lab_raspr.set()
            async with state.proxy() as lab_data:
                lab_data[message.chat.id] +=1



#Аврора

@dp.callback_query_handler(text="step_lab",state=Stages_lab.step_2)
async def send_random_value(call: types.CallbackQuery,state: FSMContext):

    await asyncio.sleep(4)
    await call.message.answer("При крушении повредилась часть корабля, отвечающая за полёт. Но я кое-что узнал:")
    await asyncio.sleep(4)
    await call.message.answer("В вашем времени уже идет разработка беспилотных и летающих автомобилей, возможно, эти технологии помогут восстановить и наши системы.")
    await asyncio.sleep(4)
    await call.message.answer("Вам нужно найти капсулу с этим проектом. Она расположена недалеко от 5 ядра.")
    await asyncio.sleep(4)
    await call.message.answer("Чтобы пройти первичную дешифровку, необходимо узнать название проекта летающих мотоциклов. Скорее всего оно написано на нескольких моделях, поэтому придется осмотреть их все.")
    await asyncio.sleep(4)
    await Stages_lab.waiting6.set()
hui = ["Ховерсерф","HOVERSURF","hoversurf","Hoversurf"]
@dp.message_handler(text=hui,state=Stages_lab.waiting6)
async def any_text_message(message: types.Message,state: FSMContext):
    await asyncio.sleep(4)
    await message.answer("Отлично, получены новые данные!")
    await asyncio.sleep(4)
    await message.answer("Хм-м, похоже что они засекречены.")
    await asyncio.sleep(4)
    await message.answer("Пожалуйста, помогите мне их расшифровать. Выполните это задание, в конце будет секретный код. Он поможет нам расшифровать необходимые данные про проект HOVERSURF.")
    await asyncio.sleep(4)
    await message.answer("https://edu.cospaces.io/NUD-ZGY\nКод игры: NUD-ZGY")
    await asyncio.sleep(4)
    await Stages_lab.waiting_game2.set()

@dp.message_handler(text="3275",state=Stages_lab.waiting_game2)
async def any_text_message(message: types.Message,state: FSMContext):
    await asyncio.sleep(4)
    await message.answer("Ура! вот что мне удалось узнать:")
    await asyncio.sleep(4)
    await message.answer("Первая модель ховербайка Scorpion 1 была представлена в 2016 году на конференции в Сколково и с тех пор стремительно развивается.")
    await asyncio.sleep(4)
    await message.answer("Основатель проекта говорит, что чтобы научиться управлять ховербайком, неподготовленному человеку понадобится около пары часов. А для того, кто уже умеет управлять мотоциклом, процесс займёт десять минут.")
    await asyncio.sleep(4)
    await message.answer("Кроме ховербайка разратываются еще проекты грузовых дронов и летающего такси.")
    await asyncio.sleep(4)
    await message.answer("Ховербайк уже использует вместо машин полиция Дубая, а аэротакси выедет, точнее, вылетит, на маршрут уже в 2025 году.")
    await asyncio.sleep(4)
    await message.answer("Но мне не хватает данных для того чтобы я мог использовать эти технологии. Пожалуйста, посмотрите видео и загрузите их в мою память.")
    await asyncio.sleep(4)
    await message.answer("https://www.youtube.com/watch?v=dEU4sBbxMzY")
    await asyncio.sleep(4)
    await message.answer(emoji.emojize(":bell:")+("Какую максимальную скорость сможет развивать аэротакси? Напишите цифру."))
    await asyncio.sleep(4)
    await Stages_lab.waiting_video2.set()
@dp.message_handler(text="200",state=Stages_lab.waiting_video2)
async def any_text_message(message: types.Message,state: FSMContext):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Едем дальше", callback_data="yes"))
    await message.answer("Вау! В вашем времени эти технологии уже развиваются, поэтому с их помощью мы сможем починить систему корабля, отвечающую за полет!",reply_markup=keyboard)
    await InputUserData.lab_raspr.set()
    async with state.proxy() as lab_data:
        lab_data[message.chat.id] +=1

#Овизион
@dp.callback_query_handler(text="step_lab",state=Stages_lab.step_3)
async def send_random_value(call: types.CallbackQuery,state: FSMContext):

    await call.message.answer("При крушении часть систем космического корабля заблокировалась.")
    await asyncio.sleep(4)
    await call.message.answer("И даже если я все починю, мы не сможем улететь из-за этого блока.")
    await asyncio.sleep(4)
    await call.message.answer("Доступ к данным Сколково заблокирован.")
    await asyncio.sleep(4)
    await call.message.answer("Но вот что я смог узнать:")
    await asyncio.sleep(4)
    await call.message.answer("Инженеры Сколково создали специальную систему распознавания лиц. Если я узнаю, как ученые управляют доступом к системе, я смогу вспомнить, как можно разблокировать автоматическую блокировку корабля, которая включилась при крушении.")
    await asyncio.sleep(4)
    await call.message.answer("Чтобы найти эту лабораторию, вам нужно:\n\n — найти Ядро 6;\n — перед турникетами будет стоять Терминал контроля доступа в лаборатории. Вы можете попробовать пройти внутрь, но если вашего лица нет в базе данных Сколково - система вас не пропустит.")
    await asyncio.sleep(4)
    await call.message.answer("Для того чтобы пройти первичную дешифровку, необходимо найти где-то поблизости секретный код Терминала лаборатории.")
    await asyncio.sleep(4)
    await Stages_lab.waiting7.set()
@dp.message_handler(text="3854",state=Stages_lab.waiting7)
async def any_text_message(message: types.Message,state: FSMContext):
    await message.answer("Супер! Это Терминал лаборатории Ovision! Я получил новые данные!")
    await asyncio.sleep(4)
    await message.answer("Хм-м, похоже что они засекречены.")
    await asyncio.sleep(4)
    await message.answer("Пожалуйста, помогите мне их расшифровать. Выполните это задание, в конце будет секретный код. Он поможет нам расшифровать необходимые данные про лабораторию Ovision.")
    await asyncio.sleep(4)
    await message.answer("https://edu.cospaces.io/MUU-QPK\nКод игры:MUU-QPK")
    await asyncio.sleep(4)
    await Stages_lab.waiting_game3.set()
@dp.message_handler(text="7926",state=Stages_lab.waiting_game3)
async def any_text_message(message: types.Message,state: FSMContext):
    await message.answer("Ура! Вот что мне удалось узнать:")
    await asyncio.sleep(4)
    await message.answer("OVISION — российский разработчик, который основывается на распознавании лиц. По научному это называется биометрией. Система распознавания лиц - самый удобный и быстрый способ установления личности человека.")
    await asyncio.sleep(4)
    await message.answer("Представьте будущее, в котором можно будет просто проходить в метро, оплачивать покупки и делать еще кучу обычных дел, не задумываясь о ключах, карточках и документах.")
    await asyncio.sleep(4)
    await message.answer("Миссия OVISION — приблизить это будущее.")
    await asyncio.sleep(4)
    await message.answer("Мне нужны еще некоторые данные. Я нашел видеоролик, который поможет вам узнать нужную информацию.")
    await asyncio.sleep(4)
    await message.answer("https://youtu.be/2BnLPNN6SXE")
    await asyncio.sleep(4)
    await message.answer(emoji.emojize(":bell:")+("На каком максимальном расстоянии может распознавать камера Терминала? Ответ дайте в метрах."))
    await asyncio.sleep(4)
    await Stages_lab.waiting_video3.set()


@dp.message_handler(text="2",state=Stages_lab.waiting_video3)
async def any_text_message(message: types.Message,state: FSMContext):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Едем дальше", callback_data="yes"))
    await message.answer("Здорово! Теперь профессор сможет разблокировать всю систему управления в машине времени с помощью биометрии!",reply_markup=keyboard)
    await InputUserData.lab_raspr.set()
    async with state.proxy() as lab_data:
        lab_data[message.chat.id] +=1


#Лоретт
@dp.callback_query_handler(text="step_lab",state=Stages_lab.step_4)
async def send_random_value(call: types.CallbackQuery,state: FSMContext):
    await call.message.answer("О нет! Поднялась вьюга!")
    await asyncio.sleep(4)
    await call.message.answer("А при аварии пострадала система безопасности навигации!")
    await asyncio.sleep(4)
    await call.message.answer("Я не смогу проложить безопасный путь до дома.")
    await asyncio.sleep(4)
    await call.message.answer("Но вот что я узнал:")
    await asyncio.sleep(4)
    await call.message.answer("Деду Морозу очень нелегко в Новогоднюю ночь. Может подняться внезапная сильная снежная буря, или случайный салют может задеть сани Дедушки, или ещё какая-нибудь неприятность. Для того чтобы Дедушка не потерялся, учёные Сколково разработали для него особый навигационный прибор, который помогает ему найти верный путь до каждого ребёнка.")
    await asyncio.sleep(4)
    await call.message.answer("Прибор также учитывает все преграды на пути и строит маршрут в обход неприятностям. А строит маршрут этот прибор благодаря специальным спутникам, которые и разрабатывают в этой лаборатории. ")
    await asyncio.sleep(4)
    await call.message.answer("Если я узнаю, как работает этот прибор для Дедушки, я смогу безопасно добраться до Сколково.")
    await asyncio.sleep(4)
    await call.message.answer("Чтобы найти эту лабораторию, вам нужно:")
    await asyncio.sleep(4)
    await call.message.answer("— найти Ядро 4;\n— с помощью секретной карточки-пропуска пройти через турникеты;\n— по лестнице спуститься на Этаж -1;\n— как выйдете с лестницы, повернуть налево;\n— с помощью секретной карточки-пропуска открыть дверь и пройти к секретным лабораториям; \n— найти помещение лаборатории №…")
    await asyncio.sleep(4)
    await call.message.answer("Чтобы пройти первичную дешифровку, необходимо узнать секретный код лаборатории.")
    await asyncio.sleep(4)
    await Stages_lab.waiting8.set()
@dp.message_handler(text="1077",state=Stages_lab.waiting8)
async def any_text_message(message: types.Message,state: FSMContext):
    await message.answer("Отлично! Это лаборатория Лоретт! Я получил новые данные!")
    await asyncio.sleep(4)
    await message.answer("Хм-м, похоже что они засекречены.")
    await asyncio.sleep(4)
    await message.answer("Пожалуйста, помогите мне их расшифровать. Выполни это задание, в конце будет секретный код. Он поможет нам расшифровать необходимые данные про лабораторию Лоретт.")
    await asyncio.sleep(4)
    await message.answer("Сслыки на игру тоже никто не сделал, ну короче тут вы идете в коспейс , ответ 1234567 если чо")
    await asyncio.sleep(4)
    await Stages_lab.waiting_game4.set()
@dp.message_handler(text="1234567",state=Stages_lab.waiting_game4)
async def any_text_message(message: types.Message,state: FSMContext):
    await message.answer("Ура! вот что мне удалось узнать:")
    await asyncio.sleep(4)
    await message.answer("https://www.youtube.com/watch?v=adclrJgpJWg&ab_channel=LoReTT")
    await asyncio.sleep(4)
    await message.answer("Пожалуйста, загрузите эти данные в мою память!")
    await asyncio.sleep(4)
    await message.answer("Сколько приблизительно было спутников на орбите земли в 2020 году?")
    await asyncio.sleep(4)
    await Stages_lab.waiting_video4.set()


@dp.message_handler(text="2700",state=Stages_lab.waiting_video4)
async def any_text_message(message: types.Message,state: FSMContext):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Едем дальше", callback_data="yes"))
    await message.answer("Спасибо вам, ребята! Команда 🦸‍♀️🦸! Теперь я смогу без проблем добраться домой!",reply_markup=keyboard)
    await InputUserData.lab_raspr.set()
    async with state.proxy() as lab_data:
        lab_data[message.chat.id] +=1

#Моторика
@dp.callback_query_handler(text="step_lab",state=Stages_lab.step_5)
async def send_random_value(call: types.CallbackQuery,state: FSMContext):
    await asyncio.sleep(4)
    await call.message.answer("Боюсь, даже если найти все детали для починки, своими руками профессор их не сможет заменить.")
    await asyncio.sleep(4)
    await call.message.answer("Кажется, я нашел часть информации о лаборатории, которая сможет нам помочь.")
    await asyncio.sleep(4)
    await call.message.answer("Вам нужно найти капсулу, в которой можно увидеть настоящие изделия этой лаборатории - протезы рук. По моим данным, капсула находится где-то между Ядром 3 и Ядром 1.")
    await asyncio.sleep(4)
    await call.message.answer("Чтобы пройти первичную дешифровку, необходимо ввести секретный код, который вы увидите у себя под ногами.")
    await asyncio.sleep(4)
    await Stages_lab.waiting9.set()

@dp.message_handler(text="2789",state=Stages_lab.waiting9)
async def any_text_message(message: types.Message,state: FSMContext):
     await message.answer("Отлично! Это лаборатория Моторика! Я получил новые данные!")
     await asyncio.sleep(4)
     await message.answer("Хм-м, похоже что они засекречены.")
     await asyncio.sleep(4)
     await message.answer("Пожалуйста, помогите мне их расшифровать. Выполните это задание, в конце будет секретный код. Он поможет нам расшифровать необходимые данные про лабораторию Моторика.")
     await asyncio.sleep(4)
     await message.answer("https://edu.cospaces.io/QCW-GYR\nКод игры:QCW-GYR")
     await asyncio.sleep(4)
     await Stages_lab.waiting_game5.set()
@dp.message_handler(text="9033",state=Stages_lab.waiting_game5)
async def any_text_message(message: types.Message,state: FSMContext):
    await asyncio.sleep(4)
    await message.answer("Я смог подключиться к системе и узнать немного о разработках этой лаборатории:")
    await asyncio.sleep(4)
    await message.answer("Моторика с 2014 года исследует и разрабатывает технологии на стыке медицины и робототехники. Сейчас они выпускают два типа протезов: активные тяговые протезы Киби и бионические протезы Инди и Манифесто. Протезы подходят для детей и взрослых с ампутациями верхних конечностей на уровне кисти и предплечья.")
    await asyncio.sleep(4)
    await message.answer("В настоящее время они проводят пилотное тестирование новой реабилитационной платформы на базе виртуальной реальности.")
    await asyncio.sleep(4)
    await message.answer("Мне не хватает данных для того чтобы понять, подходят ли нам технологии этой лаборатории. Посмотрите видео и загрузите информацию в мою память.")
    await asyncio.sleep(4)
    await message.answer("https://youtu.be/g1J8d9etBxk")
    await asyncio.sleep(4)
    await message.answer("Сколько недель изготавливается протез?")
    await asyncio.sleep(4)
    await Stages_lab.waiting_video5.set()
@dp.message_handler(text="3",state=Stages_lab.waiting_video5)
async def any_text_message(message: types.Message,state: FSMContext):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Едем дальше", callback_data="yes"))
    await message.answer("Как же это здорово! Всего за три недели в этой лаборатории делают протезы, которые помогают множеству людей. Возможно, мы сможем придумать, как можно использовать эти технологии! Давайте посмотрим на эту лабораторию. Доверьтесь вашему помощнику, и он покажет вам место, где изготавливают такие протезы.",reply_markup=keyboard)
    async with state.proxy() as lab_data:
         lab_data[message.chat.id] +=1
    await InputUserData.lab_raspr.set()



@dp.message_handler(lambda message: message.text,state="*")
async def process_gender_invalid(message: types.Message):
    return await message.reply("Не все мои системы в норме, я не понял, что вы сказали. Возможно вы допустили ошибку.")






if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
    window.mainloop()
