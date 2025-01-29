from threading import Thread
import speech_to_text as stt
import main_gui as gi


def main():
    Thread(target=gi.gui_activation).start()
    Thread(target=stt.start, daemon=True).start()


if __name__ == '__main__':
    main()
