import os
import time

import torch
import sounddevice as sd

curdir = os.path.dirname(__file__)

model_ru = os.path.join(curdir, 'files/silero_models/silero_ru.pt')
local_file = model_ru
language = 'ru'
model_id = 'ru_v3'
sample_rate = 48000
speaker = 'eugene' # Другие спикеры: aidar, baya, kseniya, xenia, eugene
put_accent = True
put_yo = True
device = torch.device('cpu')
model = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")
model.to(device)


def audio_playback(text: str) -> None:
    print('делаю голос')
    num = time.time()
    audio = model.apply_tts(text=text,
                                speaker=speaker,
                                sample_rate=sample_rate,
                            put_accent=put_accent,
                            put_yo=put_yo)
    print(abs(num - time.time()))
    time_wait = len(text) * 0.018

    sd.play(audio)
    time.sleep(len(audio) / sample_rate + time_wait)
    sd.stop()
