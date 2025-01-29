import os
import time

import vosk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import sounddevice as sd

import config


# Запись голоса
record = True

# Работа цикла для записи голоса
cycle_record = True
text = ''
voice_period_1 = time.time()
voice_period_2 = time.time()
error_text_output = ''

run_micro_up_say = False
one_say_error_micro = True
stt_record = True
curdir = os.path.dirname(__file__)

def path_update() -> None:
    global program_one_path
    global program_two_path
    global program_three_path
    global program_four_path

    with open(os.path.join(curdir, 'files/dict/programs/program_one_path.txt')) as one_path_file:
        program_one_path = one_path_file.read()
    with open(os.path.join(curdir, 'files/dict/programs/program_two_path.txt')) as two_path_file:
        program_two_path = two_path_file.read()
    with open(os.path.join(curdir, 'files/dict/programs/program_three_path.txt')) as three_path_file:
        program_three_path = three_path_file.read()
    with open(os.path.join(curdir, 'files/dict/programs/program_four_path.txt')) as four_path_file:
        program_four_path = four_path_file.read()


path_update()


def time_record_update() -> None:
    global record_time_run

    with open(os.path.join(curdir, 'files/record_time.txt'), 'r') as record_file:
        record_time_run = int(record_file.read())

time_record_update()

def link_update() -> None:
    global site_one_link
    global site_two_link
    global site_three_link
    global site_four_link

    with open(os.path.join(curdir, 'files/dict/websites/site_one_link.txt')) as one_link_file:
        site_one_link = one_link_file.read()
    with open(os.path.join(curdir, 'files/dict/websites/site_two_link.txt')) as two_link_file:
        site_two_link = two_link_file.read()
    with open(os.path.join(curdir, 'files/dict/websites/site_three_link.txt')) as three_link_file:
        site_three_link = three_link_file.read()
    with open(os.path.join(curdir, 'files/dict/websites/site_four_link.txt')) as four_link_file:
        site_four_link = four_link_file.read()


link_update()


def vect_update() -> None:
    global vectorizer
    global vectors
    global clf
    # Обучение матрицы на data_set модели
    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform(list(config.data_set.keys()))

    clf = LogisticRegression()
    clf.fit(vectors, list(config.data_set.values()))

    del config.data_set


vect_update()


def vosk_update() -> None:
    global model
    global samplerate
    global blocksize
    global dtype
    global micro_device

    model = vosk.Model(os.path.join(curdir, "model"))
    device = sd.default.device  # <--- по умолчанию
    samplerate = int(sd.query_devices(device[0], 'input')['default_samplerate'])  # получаем частоту микрофона
    blocksize = 8000
    dtype = 'int16'
    with open(os.path.join(curdir, 'files/change_micro.txt'), 'r') as micro_file:
        micro_device = int(micro_file.read())


vosk_update()

# Обновление ответной фразы на (случай случае если фраза не распознно)
def response_recognized_update():
    global response_recognized
    with open(os.path.join(curdir, 'files/not_recognized.txt'), 'r') as response_recognized_file:
        response_recognized = bool(int(response_recognized_file.read()))


response_recognized_update()
