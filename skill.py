from datetime import datetime
from threading import Thread
import random
import os
import webbrowser

import wikipedia
import subprocess
import soundcard as sc

import variable
import text_to_speech as tts
import config


wikipedia.set_lang('ru')
curdir = os.path.dirname(__file__)


# Базовые команды
def response_not_recognized_true() -> None:
    with open(os.path.join(curdir, 'files/not_recognized.txt'), 'w') as response_recognized_file:
        response_recognized_file.write('1')
    variable.response_recognized_update()


def response_not_recognized_false() -> None:
    with open(os.path.join(curdir, 'files/not_recognized.txt'), 'w') as response_recognized_file:
        response_recognized_file.write('0')
    variable.response_recognized_update()


def get_wikipedia_info(text) -> None:
    try:
        # Удаление лишних слов из запроса
        text_list = text.split()
        text_list = [i for i in text_list if i not in config.wikipedia_word_tuple]
        text = ' '.join(text_list)
        # Ищем информацию на википедии
        info = wikipedia.summary(text, sentences=5)
        tts.audio_playback(config.wikipedia_tuple_true[random.randint(0, len(config.wikipedia_tuple_true) - 1)])
        tts.audio_playback(info)
    except:
        tts.audio_playback(
            config.wikipedia_tuple_false[random.randint(0, len(config.wikipedia_tuple_false) - 1)])


def def_time() -> None:
    time_local = datetime.now()
    time_now = 'сейчас '
    hour = {
        1: ' один час',
        2: ' два часа',
        3: ' три часа',
        4: ' четыре часа',
        5: ' пять часов',
        6: ' шесть часов',
        7: ' семь часов',
        8: ' восемь часов',
        9: ' девять часов',
        10: ' десять часов',
        11: ' одиннадцать часов',
        12: ' двенадцать часов',
        14: ' четырнадцать часов',
        15: ' пятнадцать часов',
        16: ' шестнадцать часов',
        17: ' семнадцать часов',
        18: ' восемнадцать часов',
        19: ' девятнадцать часов',
        20: ' двадцать часов',
        21: ' двадцать один час',
        22: ' двадцать два часа',
        23: ' двадцать три часа',
        24: ' двадцать четыре часа'
    }
    minute = {
        1: 'одна минута',
        2: 'две минуты',
        3: 'три минуты',
        4: 'четыре минуты',
        5: 'пять минут',
        6: 'шесть минут',
        7: 'семь минут',
        8: 'восемь минут',
        9: 'девять минут',
        10: 'десять минут',
        11: 'одиннадцать минут',
        12: 'двенадцать минут',
        13: 'тринадцать минут',
        14: 'четырнадцать минут',
        15: 'пятнадцать минут',
        16: 'шестнадцать минут',
        17: 'семнадцать минут',
        18: 'восемнадцать минут',
        19: 'девятнадцать минут',
        20: 'двадцать минут',
        21: 'двадцать одна минута',
        22: 'двадцать две минуты',
        23: 'двадцать три минуты',
        24: 'двадцать четыре минуты',
        25: 'двадцать пять минут',
        26: 'двадцать шесть минут',
        27: 'двадцать семь минут',
        28: 'двадцать восемь минут',
        29: 'двадцать девять минут',
        30: 'тридцать минут',
        31: 'тридцать одна минута',
        32: 'тридцать две минуты',
        33: 'тридцать три минуты',
        34: 'тридцать четыре минуты',
        35: 'тридцать пять минут',
        36: 'тридцать шесть минут',
        37: 'тридцать семь минут',
        38: 'тридцать восемь минут',
        39: 'тридцать девять минут',
        40: 'сорок минут',
        41: 'сорок одна минута',
        42: 'сорок две минуты',
        43: 'сорок три минуты',
        44: 'сорок четыре минуты',
        45: 'сорок пять минут',
        46: 'сорок шесть минут',
        47: 'сорок семь минут',
        48: 'сорок восемь минут',
        49: 'сорок девять минут',
        50: 'пятьдесят минут',
        51: 'пятьдесят одна минута',
        52: 'пятьдесят две минуты',
        53: 'пятьдесят три минуты',
        54: 'пятьдесят четыре минуты',
        55: 'пятьдесят пять минут',
        56: 'пятьдесят шесть минут',
        57: 'пятьдесят семь минут',
        58: 'пятьдесят восемь минут',
        59: 'пятьдесят девять минут',
        60: 'шестьдесят минут'
    }
    time_now += hour[time_local.hour]
    time_now += ' '
    time_now += minute[time_local.minute]

    tts.audio_playback(time_now)


def data_time() -> None:
    dt = datetime.now()
    date = ''
    date += 'Сегодня '
    date += config.weekday[dt.weekday()] + ', '

    num_date = {1: 'первое',
                2: 'второе',
                3: 'третье',
                4: 'четвёртое',
                5: 'пятое',
                6: 'шестое',
                7: 'седьмое',
                8: 'восьмое',
                9: 'девятое',
                10: 'десятое',
                11: 'одиннадцатое',
                12: 'двенадцатое',
                13: 'тринадцатое',
                14: 'четырнадцатое',
                15: 'пятнадцатое',
                16: 'шестнадцатое',
                17: 'семнадцатое',
                18: 'восемнадцатое',
                19: 'девятнадцатое',
                20: 'двадцатое',
                21: 'двадцать первое',
                22: 'двадцать второе',
                23: 'двадцать третье',
                24: 'двадцать четвёртое',
                25: 'двадцать пятое',
                26: 'двадцать шестое',
                27: 'двадцать седьмое',
                28: 'двадцать восьмое',
                29: 'двадцать девятое',
                30: 'тридцатое',
                31: 'тридцать первое'}

    date += num_date[int(dt.day)] + ' '
    date += config.month[dt.month - 1]
    tts.audio_playback(date)


def open_browser() -> None:
    webbrowser.open_new_tab('open_browser_ru.html')
    tts.audio_playback('Браузер открыт')

def search_micro() -> list:
    return [device.name for device in sc.all_microphones()]


# Ответные фразы
def hi() -> None:
    tts.audio_playback(config.hi_tuple[random.randint(0, len(config.hi_tuple) - 1)])


def goodbye() -> None:
    tts.audio_playback(config.goodbye_tuple[random.randint(0, len(config.goodbye_tuple) - 1)])


def how_are_you() -> None:
    tts.audio_playback(config.how_are_you_tuple[random.randint(0, len(config.how_are_you_tuple) - 1)])


def well_done() -> None:
    tts.audio_playback(config.well_done_tuple[random.randint(0, len(config.well_done_tuple) - 1)])


def fool() -> None:
    tts.audio_playback(config.fool_tuple[random.randint(0, len(config.fool_tuple) - 1)])


def what_can_you() -> None:
    text = 'я умею:'
    text += ' говорить текущее время и дату.'
    text += ' искать информацию на википедии.'
    text += ' запускать сайты и программы.'
    text += ' а также запускать браузер'
    tts.audio_playback(text)


def change_time_record(num: str) -> None:
    try:
        int(num)
        if int(num) > 0:
            with open(os.path.join(curdir, 'files/record_time.txt'), 'w') as record_time_file:
                record_time_file.write(str(num))
            variable.time_record_update()
        else:
            variable.error_text_output = 'Число должно быть больше 0'
    except ValueError:
        variable.error_text_output = 'Число должно быть больше 0'


# Открытие программ
def def_program_one() -> None:
    def program() -> None:
        try:
            subprocess.call(variable.program_one_path)
            tts.audio_playback('программа запущена')
        except:
            tts.audio_playback('не удалось запустить программу. проверьте правельность путей')
    Thread(target=program).start()



def def_program_two() -> None:
    def program() -> None:
        try:
            subprocess.call(variable.program_two_path)
            tts.audio_playback('программа запущена')
        except:
            tts.audio_playback('не удалось запустить программу. проверьте правельность путей')
    Thread(target=program).start()


def def_program_three() -> None:
    def program() -> None:
        try:
            subprocess.call(variable.program_three_path)
            tts.audio_playback('программа запущена')
        except:
            tts.audio_playback('не удалось запустить программу. проверьте правельность путей')
    Thread(target=program).start()


def def_program_four() -> None:
    def program() -> None:
        try:
            subprocess.call(variable.program_four_path)
            tts.audio_playback('программа запущена')
        except:
            tts.audio_playback('не удалось запустить программу. проверьте правельность путей')
    Thread(target=program).start()




# Открытие сайтов
def def_site_one() -> None:
    webbrowser.open(variable.site_one_link)


def def_site_two() -> None:
    webbrowser.open(variable.site_two_link)


def def_site_three() -> None:
    webbrowser.open(variable.site_three_link)


def def_site_four() -> None:
    webbrowser.open(variable.site_four_link)


# Добавление сайтов
def def_site_add_one(name: str, link: str) -> None:
    site_list = name.split('; ')
    add_name_str = ''
    for i in site_list:
        add_name_str += f'{i}\n'
    with open(os.path.join(curdir, 'files/dict/websites/site_one_name.txt'), 'w') as name_file:
        name_file.write(add_name_str)
    with open(os.path.join(curdir, 'files/dict/websites/site_one_link.txt'), 'w') as link_file:
        link_file.write(link)
    variable.link_update()
    config.data_set_update()
    variable.vect_update()


def def_site_add_two(name: str, link: str) -> None:
    site_list = name.split('; ')
    add_name_str = ''
    for i in site_list:
        add_name_str += f'{i}\n'
    with open(os.path.join(curdir, 'files/dict/websites/site_two_name.txt'), 'w') as name_file:
        name_file.write(add_name_str)
    with open(os.path.join(curdir, 'files/dict/websites/site_two_link.txt'), 'w') as link_file:
        link_file.write(link)
    variable.link_update()
    config.data_set_update()
    variable.vect_update()


def def_site_add_three(name: str, link: str) -> None:
    site_list = name.split('; ')
    add_name_str = ''
    for i in site_list:
        add_name_str += f'{i}\n'
    with open(os.path.join(curdir, 'files/dict/websites/site_three_name.txt'), 'w') as name_file:
        name_file.write(add_name_str)
    with open(os.path.join(curdir, 'files/dict/websites/site_three_link.txt'), 'w') as link_file:
        link_file.write(link)
    variable.link_update()
    config.data_set_update()
    variable.vect_update()


def def_site_add_four(name: str, link: str) -> None:
    site_list = name.split('; ')
    add_name_str = ''
    for i in site_list:
        add_name_str += f'{i}\n'
    with open(os.path.join(curdir, 'files/dict/websites/site_four_name.txt'), 'w') as name_file:
        name_file.write(add_name_str)
    with open(os.path.join(curdir, 'files/dict/websites/site_four_link.txt'), 'w') as link_file:
        link_file.write(link)
    variable.link_update()
    config.data_set_update()
    variable.vect_update()


# Добавление программ
def def_program_add_one(name: str, path: str) -> None:
    # Изменение имени
    name = name.lower()
    name_list = name.split('; ')
    add_name_str = ''
    for i in name_list:
        add_name_str += f'{i}\n'
    with open(os.path.join(curdir, 'files/dict/programs/program_one_name.txt'), 'w') as name_file:
        name_file.write(add_name_str)
    # Изменение пути
    with open(os.path.join(curdir, 'files/dict/programs/program_one_path.txt'), 'w') as path_file:
        path_file.write(path)
    variable.path_update()
    config.data_set_update()
    variable.vect_update()


def def_program_add_two(name: str, path: str) -> None:
    # Изменение имени
    name = name.lower()
    name_list = name.split('; ')
    add_name_str = ''
    for i in name_list:
        add_name_str += f'{i}\n'
    with open(os.path.join(curdir, 'files/dict/programs/program_two_name.txt'), 'w') as name_file:
        name_file.write(add_name_str)
    # Изменение пути
    with open(os.path.join(curdir, 'files/dict/programs/program_two_path.txt'), 'w') as path_file:
        path_file.write(path)
    variable.path_update()
    config.data_set_update()
    variable.vect_update()


def def_program_add_three(name: str, path: str) -> None:
    # Изменение имени
    name = name.lower()
    name_list = name.split('; ')
    add_name_str = ''
    for i in name_list:
        add_name_str += f'{i}\n'
    with open(os.path.join(curdir, 'files/dict/programs/program_three_name.txt'), 'w') as name_file:
        name_file.write(add_name_str)
    # Изменение пути
    with open(os.path.join(curdir, 'files/dict/programs/program_three_path.txt'), 'w') as path_file:
        path_file.write(path)
    variable.path_update()
    config.data_set_update()
    variable.vect_update()


def def_program_add_four(name: str, path: str) -> None:
    # Изменение имени
    name = name.lower()
    name_list = name.split('; ')
    add_name_str = ''
    for i in name_list:
        add_name_str += f'{i}\n'
    with open(os.path.join(curdir, 'files/dict/programs/program_four_name.txt'), 'w') as name_file:
        name_file.write(add_name_str)
    # Изменение пути
    with open(os.path.join(curdir, 'files/dict/programs/program_four_path.txt'), 'w') as path_file:
        path_file.write(path)
    variable.path_update()
    config.data_set_update()
    variable.vect_update()


def change_micro_device(num_dev: int) -> None:
    with open('files/change_micro.txt', 'w') as micro_file:
        micro_file.write(f'{num_dev}')
    variable.vosk_update()


def reset():
    with open('files/not_recognized.txt') as not_recognized_file_read:
        if not not_recognized_file_read.read() == 'True' or not_recognized_file_read.read() == '':
            with open('files/not_recognized.txt', 'w') as not_recognized_file_write:
                not_recognized_file_write.write('')
    with open('files/game_file/record.txt') as record_file_read:
        try:
            int(record_file_read.read())
        except ValueError:
            with open('files/game_file/record.txt', 'w') as record_file_write:
                record_file_write.write('0')
    with open('files/change_micro.txt') as micro_file:
        try:
            if int(micro_file.read()) > len(search_micro()):
                if len(search_micro()) >= 1:
                    with open('files/game_file/record.txt', 'w') as record_file_write:
                        record_file_write.write('1')
                        variable.stt_record = True
                elif len(search_micro()) == 0:
                    variable.stt_record = False
        except ValueError:
            with open('files/game_file/record.txt', 'w') as record_file_write:
                record_file_write.write('1')
    with open('files/record_time.txt') as record_file:
        try:
            int(record_file.read())
        except ValueError:
            with open('files/game_file/record.txt', 'w') as record_file:
                record_file.write('7')
