import sounddevice as sd
import queue
import json
import time

import vosk

import variable
import text_to_speech as tts
import recognizer

q = queue.Queue()


def callback(indata, frames, time, status) -> None:
    if variable.record:
        q.put(bytes(indata))


def stt(samplerate, blocksize, device, dtype, model) -> None:
    if variable.stt_record:
        variable.run_micro_up_say = False
        with sd.RawInputStream(samplerate=samplerate, blocksize=blocksize, device=device, dtype=dtype,
                               channels=1, callback=callback):
            rec = vosk.KaldiRecognizer(model, samplerate)
            variable.record = False
            tts.audio_playback('я вас слушаю')
            variable.record = True

            variable.cycle_record = True
            while variable.cycle_record:
                if variable.run_micro_up_say:
                    return
                data = q.get()
                if rec.AcceptWaveform(data):
                    variable.text = (json.loads(rec.Result())['text'])
                    if variable.text != '' and variable.text != ' ':
                        recognizer.recognize(variable.text, variable.vectorizer, variable.clf, variable.vectors)
def stt_restart() -> None:
    stt(variable.samplerate, variable.blocksize, variable.micro_device, variable.dtype, variable.model)

def start() -> None:
    while variable.cycle_record:
        stt_restart()
        time.sleep(1)