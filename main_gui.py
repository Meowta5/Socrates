import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from new_gui import Ui_MainWindow
import game
import skill
import variable




class start_socrat(QtWidgets.QMainWindow):
    def __init__(self):
        super(start_socrat, self).__init__()
        self.new_gui = Ui_MainWindow()
        self.new_gui.setupUi(self)



        self.new_gui.pushButton_18.clicked.connect(game.start_game)


        #при нажатие на кнопку вызов функции переключателей main
        self.new_gui.Button_main.clicked.connect(self.show_page_main)
        self.new_gui.Button_settings.clicked.connect(self.show_page_settings)
        # при нажатие на кнопку вызов функции трех переключателей settings
        self.new_gui.Button_page1_main.clicked.connect(self.show_page_setting_one)
        self.new_gui.Button_page2_programms.clicked.connect(self.show_page_setting_two)
        self.new_gui.Button_page3_web.clicked.connect(self.show_page_setting_three)
        # при нажатие на кнопку вызов функции переключателей программ
        self.new_gui.pushButton_2.clicked.connect(self.show_page_programms_one)
        self.new_gui.pushButton_3.clicked.connect(self.show_page_programms_two)
        self.new_gui.pushButton_4.clicked.connect(self.show_page_programms_three)
        self.new_gui.pushButton_5.clicked.connect(self.show_page_programms_four)
        # при нажатие на кнопку вызов функции переключателей сайтов
        self.new_gui.pushButton_11.clicked.connect(self.show_page_web_one)
        self.new_gui.pushButton_13.clicked.connect(self.show_page_web_two)
        self.new_gui.pushButton_12.clicked.connect(self.show_page_web_three)
        self.new_gui.pushButton_14.clicked.connect(self.show_page_web_four)

        self.new_gui.pushButton_19.clicked.connect(skill.response_not_recognized_true)
        self.new_gui.pushButton_20.clicked.connect(skill.response_not_recognized_false)


        #готово (программы)
        self.new_gui.pushButton_6.clicked.connect(self.line_show_programms_one)
        self.new_gui.pushButton_7.clicked.connect(self.line_show_programms_two)
        self.new_gui.pushButton_8.clicked.connect(self.line_show_programms_three)
        self.new_gui.pushButton_9.clicked.connect(self.line_show_programms_four)
        #готово (сайты)
        self.new_gui.pushButton_10.clicked.connect(self.line_show_web_one)
        self.new_gui.pushButton_15.clicked.connect(self.line_show_web_two)
        self.new_gui.pushButton_16.clicked.connect(self.line_show_web_three)
        self.new_gui.pushButton_17.clicked.connect(self.line_show_web_four)


        list2 = skill.search_micro()
        self.new_gui.comboBox.activated[str].connect(self.start_divece)
        for i in list2:
            self.new_gui.comboBox.addItem(i)


    #смена дивайсов
    def start_divece(self, text):

        list2 = skill.search_micro()
        num_list = []
        dict_micro = {}

        for i in range(len(list2)):
            num_list.append(i + 1)

        for key, meaning in zip(list2, num_list):
            dict_micro[key] = meaning
        skill.change_micro_device(dict_micro[text])
        variable.run_micro_up_say = True

    #основные переключатели
    def show_page_main(self):
        self.new_gui.stackedWidget.setCurrentWidget(self.new_gui.page)  # Переключатель на страницу main
    def show_page_settings(self):
        self.new_gui.stackedWidget.setCurrentWidget(self.new_gui.page_2)  # Переключатель на страницу settings


    #настройки
    def show_page_setting_one(self):
        self.new_gui.stackedWidget_2.setCurrentWidget(self.new_gui.page_perekl1)
    def show_page_setting_two(self):
        self.new_gui.stackedWidget_2.setCurrentWidget(self.new_gui.page_perekl2)
    def show_page_setting_three(self):
        self.new_gui.stackedWidget_2.setCurrentWidget(self.new_gui.page_perekl3)


    #программы
    def show_page_programms_one(self):
        self.new_gui.stackedWidget_3.setCurrentWidget(self.new_gui.page_4)
    def show_page_programms_two(self):
        self.new_gui.stackedWidget_3.setCurrentWidget(self.new_gui.page_3)
    def show_page_programms_three(self):
        self.new_gui.stackedWidget_3.setCurrentWidget(self.new_gui.page_5)
    def show_page_programms_four(self):
        self.new_gui.stackedWidget_3.setCurrentWidget(self.new_gui.page_6)


    #сайты
    def show_page_web_one(self):
        self.new_gui.stackedWidget_4.setCurrentWidget(self.new_gui.page_7)
    def show_page_web_two(self):
        self.new_gui.stackedWidget_4.setCurrentWidget(self.new_gui.page_9)
    def show_page_web_three(self):
        self.new_gui.stackedWidget_4.setCurrentWidget(self.new_gui.page_10)
    def show_page_web_four(self):
        self.new_gui.stackedWidget_4.setCurrentWidget(self.new_gui.page_8)


    def line_show_programms_one(self):
        skill.def_program_add_one(name=self.new_gui.lineEdit_3.text(), path=self.new_gui.lineEdit_2.text())
    def line_show_programms_two(self):
        skill.def_program_add_two(name=self.new_gui.lineEdit_5.text(), path=self.new_gui.lineEdit_4.text())
    def line_show_programms_three(self):
        skill.def_program_add_three(name=self.new_gui.lineEdit_7.text(), path=self.new_gui.lineEdit_6.text())
    def line_show_programms_four(self):
        skill.def_program_add_four(name=self.new_gui.lineEdit_9.text(), path=self.new_gui.lineEdit_8.text())


    def line_show_web_one(self):
        skill.def_site_add_one(name=self.new_gui.lineEdit_11.text(), link=self.new_gui.lineEdit_10.text())
    def line_show_web_two(self):
        skill.def_site_add_two(name=self.new_gui.lineEdit_13.text(), link=self.new_gui.lineEdit_12.text())
    def line_show_web_three(self):
        skill.def_site_add_three(name=self.new_gui.lineEdit_15.text(), link=self.new_gui.lineEdit_14.text())
    def line_show_web_four(self):
        skill.def_site_add_four(name=self.new_gui.lineEdit_17.text(), link=self.new_gui.lineEdit_16.text())



def gui_activation() -> None:
    global app
    global application
    app = QtWidgets.QApplication([])
    application = start_socrat()
    application.show()

    sys.exit(app.exec())