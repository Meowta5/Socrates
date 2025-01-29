
import os
import pprint

curdir = os.path.dirname(__file__)

# Тригеры
TRIGGER = {'сократ', 'сократик', 'сократушка', 'сократище', 'секрет', 'секретик', 'секретушка', 'секретеще'}

# Дни
weekday = ('понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье')
month = ('января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября',
             'декабря')

# Википедия
wikipedia_tuple_true = ('Вот что мне удалось найти', 'Вот что я нашел', 'Вот что я смог найти',
                          'Вот что мне удалось найти по итогу поиска',
                          'Вот что я обнаружил в результате поиска')

wikipedia_tuple_false = ('Не удалось получить информацию из Википедии', 'Не удалось найти информацию из Википедии')

wikipedia_word_tuple = ('найди', 'поищи', 'ищи', 'единой', 'пожалуйста', 'плиз', 'на', 'в', 'внутри', 'википедия',
                       'википедии', 'сократ')


# Прослушка команд начата
lister_tuple = ('я вас слушаю',)

# Не распознана команда
response_recognized_tuple = ('не удалось распознать команду', 'команда не распознана', 'повторите запрос, команда не распознана. сэр')

# Для включения
open_program_tuple = ('включи', 'включай', 'запусти', 'запускай', 'открой', 'открывай', 'активируй', 'пуск')

# Полувнекомандные фразы
hi_tuple = ('привет', 'здравия желаю', 'здравствуйте', 'приветствую', 'добрый день', 'привет', 'здравия желаю', 'здравствуйте',
            'приветствую', 'добрый день', '')

how_are_you_tuple = ('хорошо', 'замечательно', 'круто', 'нормально', 'пойдет', 'бывало и лучше')

well_done_tuple = ('приму к сведению', 'вас понял', 'так точно', 'окей', 'к вашим услугам сэр')

fool_tuple = ('очень тонкое замечание, сэр', 'вас понял')

goodbye_tuple = ('до свидания', 'до включения', 'гудбай')

# Датасет
def data_set_update():
    global data_set
    data_set = {
        "найди на википедии": "get_wikipedia_info",
        "поищи на википедии": "get_wikipedia_info",
        "ищи на википедии": "get_wikipedia_info",
        "пожалуйста найди на википедии": "get_wikipedia_info",
        "сколько сейчас время": "def_time",
        "сколько время": "def_time",
        "который час": "def_time",
        "сколько сейчас часов": "def_time",
        "сколько сейчас времени": "def_time",
        "какое сегодня число": "data_time",
        "какая сегодня дата": "data_time",
        "какой сегодня день": "data_time",
        "какой сегодня день недели": "data_time",
        "который день": "data_time",
        "который день недели": "data_time",
        "которое число": "data_time",
        "какое число": "data_time",
        "а какое сегодня число": "data_time",
        "а какое число": "data_time",
        "открой браузер": "open_browser",
        "запусти браузер": "open_browser",
        "включи браузер": "open_browser",
        "открой хром": "open_browser",
        "открой гугл хром": "open_browser",
        "открой гугл": "open_browser",
        "что ты умеешь": "what_can_you",
        "какие есть команды": "what_can_you",
        "какие у тебя есть команды": "what_can_you",
        "какие есть функции": "what_can_you",
        "какие у тебя навыки": "what_can_you",
        "что ты можешь делать": "what_can_you",
        "какие у тебя способности": "what_can_you",
        "что входит в твои умения": "what_can_you",
        "какие у тебя компетенции": "what_can_you",
        "что ты в состоянии сделать": "what_can_you",
        "какие у тебя профессиональные качества": "what_can_you",
        "что ты можешь предложить": "what_can_you",
        "какие у тебя таланты": "what_can_you",
        "что ты умеешь и можешь выполнить": "what_can_you",
        "как ты": "how_are_you",
        "как поживаешь": "how_are_you",
        "как поживаете": "how_are_you",
        "как сам": "how_are_you",
        "как настроение": "how_are_you",
        "как делишки": "how_are_you",
        "как жизнь молодая и веселая": "how_are_you",
        "как идут дела": "how_are_you",
        "как ты там": "how_are_you",
        "ты молодец": "well_done",
        "ты умница": "well_done",
        "ты молодчина": "well_done",
        "ты красавчик": "well_done",
        "ты гений": "well_done",
        "ты талант": "well_done",
        "ты профессионал": "well_done",
        "ты герой": "well_done",
        "ты великолепно": "well_done",
        "ты выше всяких похвал": "well_done",
        "молодец": "well_done",
        "умница": "well_done",
        "молодчина": "well_done",
        "красавчик": "well_done",
        "гений": "well_done",
        "талант": "well_done",
        "профессионал": "well_done",
        "герой": "well_done",
        "великолепно": "well_done",
        "выше всяких похвал": "well_done",
        "ты глупый": "fool",
        "ты тупой": "fool",
        "ты недалекий": "fool",
        "ты бестолковый": "fool",
        "ты тормоз": "fool",
        "ты дурачок": "fool",
        "ты болван": "fool",
        "ты тупица": "fool",
        "ты олень": "fool",
        "ты дебил": "fool",
        "ты идиот": "fool",
        "ты балбес": "fool",
        "глупый": "fool",
        "недалекий": "fool",
        "бестолковый": "fool",
        "тормоз": "fool",
        "дурачок": "fool",
        "болван": "fool",
        "тупица": "fool",
        "тупой": "fool",
        "олень": "fool",
        "дебил": "fool",
        "идиот": "fool",
        "балбес": "fool",
        "здравствуй": "hi",
        "здравствуйте": "hi",
        "добрый день": "hi",
        "доброе утро": "hi",
        "приветствую": "hi",
        "салют": "hi",
        "хай": "hi",
        "ку": "hi",
        "здорово": "hi",
        "привет": "hi",
        "до свидания": "goodbye",
        "всего хорошего": "goodbye",
        "до встречи": "goodbye",
        "прощай": "goodbye",
        "бывай": "goodbye",
        "счастливо": "goodbye",
        "до скорого": 'goodbye',
        "пока": 'goodbye'
    }

    def program_add(func_name: str, path: str) -> list:
        with open(os.path.join(curdir, path), 'r') as file:
            program_list = []
            for el in file:
                program_list.append(el[:-1])
            program_key_list = []
            program_meanig = []
            for program_el in program_list:
                for open_program_el in open_program_tuple:
                    program_key_list.append(f'{open_program_el} {program_el}')
                    program_meanig.append(func_name)
            program_return = [program_key_list, program_meanig]
            if file.read() != '' or file.read() != ' ' or file.read() != '\n':
                return program_return

    program_one = program_add(func_name='def_program_one', path='files/dict/programs/program_one_name.txt')
    program_two = program_add(func_name='def_program_two', path='files/dict/programs/program_two_name.txt')
    program_three = program_add(func_name='def_program_three', path='files/dict/programs/program_three_name.txt')
    program_four = program_add(func_name='def_program_four', path='files/dict/programs/program_four_name.txt')

    program_one_key = program_one[0]
    program_one_meaning = program_one[1]

    program_two_key = program_two[0]
    program_two_meaning = program_two[1]

    program_three_key = program_three[0]
    program_three_meaning = program_three[1]

    program_four_key = program_four[0]
    program_four_meaning = program_four[1]

    site_one = program_add(func_name='def_site_one', path='files/dict/websites/site_one_name.txt')
    site_two = program_add(func_name='def_site_two', path='files/dict/websites/site_two_name.txt')
    site_three = program_add(func_name='def_site_three', path='files/dict/websites/site_three_name.txt')
    site_four = program_add(func_name='def_site_four', path='files/dict/websites/site_four_name.txt')

    site_one_key = site_one[0]
    site_one_meaning = site_one[1]

    site_two_key = site_two[0]
    site_two_meaning = site_two[1]

    site_three_key = site_three[0]
    site_three_meaning = site_three[1]

    site_four_key = site_four[0]
    site_four_meaning = site_four[1]

    for key, meaning in zip(program_one_key, program_one_meaning):
        data_set[key] = meaning
    for key, meaning in zip(program_two_key, program_two_meaning):
        data_set[key] = meaning
    for key, meaning in zip(program_three_key, program_three_meaning):
        data_set[key] = meaning
    for key, meaning in zip(program_four_key, program_four_meaning):
        data_set[key] = meaning
    for key, meaning in zip(site_one_key, site_one_meaning):
        data_set[key] = meaning
    for key, meaning in zip(site_two_key, site_two_meaning):
        data_set[key] = meaning
    for key, meaning in zip(site_three_key, site_three_meaning):
        data_set[key] = meaning
    for key, meaning in zip(site_four_key, site_four_meaning):
        data_set[key] = meaning

    pprint.pprint(data_set)

data_set_update()
