import telebot

from itertools import permutations

bot = telebot.TeleBot("6030378910:AAGgA5TsEQZbWz1I0fzYiL4dgV9gFiGCWz8")

file = open(r"C:\all_projects\new_anagram_words_bot\singular.txt",
            encoding='utf-8')

words = file.read().split()


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message,
                 f"\t\t\t\t\tПривет {message.from_user.first_name}.\t Я анагармм_бот.\t Я помогу тебе составить слова из введенных букв. "
                 f" \tВведите русские буквы в одну строку без пробелов, регистр "
                 f"не имеет значения.")


@bot.message_handler(commands=['app'])
def application(message):
    msg = bot.reply_to(message, message.text)
    bot.register_next_step_handler(msg, review)


def review(message):
    user_letters = message.text
    sort_alphabet = sorted(user_letters)
    sort_alphabet = ''.join(sort_alphabet)

    empty_list = []
    revers_char = permutations(sort_alphabet)

    for val in revers_char:
        val = ''.join(val)
        empty_list.append(val)

    def length_words(n):
        variable = []
        for i in permutations(sort_alphabet, r=n):
            variable.append(i)

        list_length = []
        for i in variable:
            str_11 = ''.join(i)
            list_length.append(str_11)

        list_length_finally = []
        for i in list_length:
            if i in words:
                list_length_finally.append(i.title())
                set_list = set(list_length_finally)
                long_word = ' '.join(set_list)
        # print(f'Слова из {n} букв:', long_word)
        return long_word

    x = len(user_letters)
    while x > 3:
        length_words(x)
        x -= 1

    test_variable_8 = length_words(8)
    test_variable_7 = length_words(7)
    test_variable_6 = length_words(6)
    test_variable_5 = length_words(5)
    test_variable_4 = length_words(4)
    test_variable_3 = length_words(3)

    @bot.message_handler(commands=['8'])
    def start(message):
        bot.send_message(message.chat.id, test_variable_8)

    @bot.message_handler(commands=['7'])
    def start(message):
        bot.send_message(message.chat.id, test_variable_7)

    @bot.message_handler(commands=['6'])
    def start(message):
        bot.send_message(message.chat.id, test_variable_6)

    @bot.message_handler(commands=['5'])
    def start(message):
        bot.send_message(message.chat.id, test_variable_5)

    @bot.message_handler(commands=['4'])
    def start(message):
        bot.send_message(message.chat.id, test_variable_4)

    @bot.message_handler(commands=['3'])
    def start(message):
        bot.send_message(message.chat.id, test_variable_3)


bot.polling()
