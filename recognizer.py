import time
import numpy as np

from sklearn.metrics.pairwise import cosine_similarity

import variable
import config
from skill import *
import text_to_speech as tts


def recognize(text, vectorizer, clf, vectors):
    print('рекогнайзер запущен')
    # Вычисляем время когда была сказана команда
    variable.voice_period_2 = time.time()
    text = text.lower()
    # Вычисляем прошло ли n секунд, если да то проверяем наличие тригера помошника в команде
    if (int(variable.voice_period_1) - int(variable.voice_period_2) <= variable.record_time_run):
        # Проверяем наличие тригера помошника
        trg = config.TRIGGER.intersection(set(text.split(' ')))
        if not trg:  # Если тригер отсутствует
            return  # Выход их функции
        # Удаляем триггер из команды
        text.replace(list(trg)[0], '')
        variable.voice_period_1 = time.time()
    # Получаем вектор полученного текста
    text_vector = vectorizer.transform([text]).toarray()[0]
    # Вычисляем косинусное расстояние между векторами
    similarities = cosine_similarity(text_vector.reshape(1, -1),
                                     vectors)
    # Находим максимальное расстояние
    max_similarity = np.max(similarities)
    # Сравниваем с вариантами, получая наиболее подходящий ответ
    answer = clf.predict([text_vector])[0]


    if max_similarity >= 0.75:
        print('комнда распознана ')
        def_name = answer.split()[0]
        if def_name == 'get_wikipedia_info':
            variable.record = False
            exec(def_name + '(text)')
            variable.record = True
        else:
            variable.record = False
            exec(def_name + '()')
            variable.record = True
    else:
        print('комнда не распознана ')
        if variable.response_recognized:
            variable.record = False
            tts.audio_playback(config.response_recognized_tuple[random.randint(0, len(config.response_recognized_tuple) - 1)])
            variable.record = True
