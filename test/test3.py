from telebot import TeleBot, types
import dotenv
import os
import string

print(type(string.digits))


# path = os.path.dirname(__file__)
# norm_path = os.path.normpath(path)
# print(os.path.isfile('Как_подготовиться_к_тренировке.jpg'))
# print(os.getcwd())


dotenv.load_dotenv()

my_secret = os.environ.get('TELEGRAM_TOKEN')
ADMIN_USER_ID = os.environ.get('ADMIN_ID')

bot = TeleBot(my_secret)

exercises = {
    'Кардио': 1000,
    'Силовая тренировка': 2000,
    'Йога': 1500,
    'Растяжка': 1200
}

user_data = {}

# Функция для обработки команды /start
def start_handler(message):
    welcome_message = "Добро пожаловать!"
    bot.send_message(message.chat.id, welcome_message)
    show_exercises_menu(message)

# Функция для отображения меню с тренировками
def show_exercises_menu(message):
    markup = types.InlineKeyboardMarkup()
    for exercise, price in exercises.items():
        button_text = exercise + " - " + str(price) + "руб."
        markup.add(types.InlineKeyboardButton(button_text, callback_data=exercise))
    bot.send_message(message.chat.id, "Пожалуйста, выберите тренировку:", reply_markup=markup)

# Обработчик выбора вида тренировки
def exercise_selected(call):
    exercise = call.data
    user_data[call.message.chat.id] = {'exercise': exercise}
    bot.send_message(call.message.chat.id, "Вы выбрали" + " - " + exercise +
                     "\nДля записи на тренировку, введите ваш номер телефона:")
    bot.register_next_step_handler(call.message, get_phone_number)

# Функция для запроса номера телефона
def get_phone_number(message):
    phone_number = message.text
    # check_phone_number = all(list(map(lambda x: x in string.digits, phone_number)))
    # if not check_phone_number or len(phone_number) < 11:
    #     bot.send_message(message.chat.id, 'dedededededed')
    #     exercise_selected(message)
    user_data[message.chat.id]['phone_number'] = phone_number
    bot.send_message(message.chat.id, "Введите желаемую дату и время для занятия:")
    bot.register_next_step_handler(message, get_date_time)

# Функция для запроса даты и времени
def get_date_time(message):
    date_time = message.text
    user_data[message.chat.id]['date_time'] = date_time
    # Отправка уведомлений пользователю и тренеру
    exercise = user_data[message.chat.id]['exercise']
    phone_number = user_data[message.chat.id]['phone_number']
    bot.send_message(message.chat.id, "Спасибо! Вы хотите записаться на " + exercise + " на " + date_time +
                     "\nЯ свяжусь с вами по номеру " + phone_number + " для уточнения возможности записи.")
    bot.send_message(ADMIN_USER_ID, "Новая запись:\nТренировка: " + exercise +
                     "\nДата и время: " + date_time + "\nТелефон: " + phone_number)
    send_notification(message)


def send_notification(message):
    text = 'Ознакомьтесь, пожалуйста, с памяткой о подготовке к тренировке'
    with open('./Как_подготовиться_к_тренировке.jpg', 'rb') as file:
        bot.send_photo(message.chat.id, file, caption=text)
    # bot.send_photo(message.chat.id, open('./test/Как_подготовиться_к_тренировке.jpg', 'rb'))





# Регистрация обработчиков
bot.register_message_handler(start_handler, commands=['start'])
bot.register_callback_query_handler(exercise_selected, func=lambda call: call.data in exercises.keys())
bot.register_message_handler(get_phone_number, content_types=['contact'])

# Запуск бота
bot.infinity_polling(none_stop=True)