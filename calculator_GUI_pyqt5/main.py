"""Calculator_GUI"""
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import calc_for_main
import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5 import uic  # этот модуль отвечает за присоединение шаблона приложения к данному скрипту, дает возможность
# поднять XML таблицы нашего шаблона и обращаться к ним как к объектам

ROOT_DIR = os.path.dirname(os.path.abspath(__name__))
DIST_DIR = '\\dist\\main'

if DIST_DIR in ROOT_DIR:
    ROOT_DIR = ROOT_DIR.replace(DIST_DIR, '')
UI_PATH = os.path.join(ROOT_DIR, 'SC2.ui')
# UI_PATH = os.path.join(ROOT_DIR, '\\Python projects\\Smart calculator\\calculator_GUI\\SC2.ui')


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi(UI_PATH)  # имя шаблона, создание графического объекта
        self.set()
        self.ui.show()  # показывает шаблон

    def set(self):
        # метод, который связывает все кнопки
        self.ui.btn_0.clicked.connect(lambda: self.click('0'))
        self.ui.btn_1.clicked.connect(lambda: self.click('1'))
        self.ui.btn_2.clicked.connect(lambda: self.click('2'))
        self.ui.btn_3.clicked.connect(lambda: self.click('3'))
        self.ui.btn_4.clicked.connect(lambda: self.click('4'))
        self.ui.btn_5.clicked.connect(lambda: self.click('5'))
        self.ui.btn_6.clicked.connect(lambda: self.click('6'))
        self.ui.btn_7.clicked.connect(lambda: self.click('7'))
        self.ui.btn_8.clicked.connect(lambda: self.click('8'))
        self.ui.btn_9.clicked.connect(lambda: self.click('9'))

        self.ui.btn_left.clicked.connect(lambda: self.click('('))
        self.ui.btn_right.clicked.connect(lambda: self.click(')'))
        self.ui.btn_plus.clicked.connect(lambda: self.click('+'))
        self.ui.btn_minus.clicked.connect(lambda: self.click('-'))
        self.ui.btn_division.clicked.connect(lambda: self.click('/'))
        self.ui.btn_multi.clicked.connect(lambda: self.click('*'))
        self.ui.btn_point.clicked.connect(lambda: self.click('.'))
        self.ui.btn_eq.clicked.connect(self.calculate)
        self.ui.btn_sqrt.clicked.connect(self.sqrt)
        self.ui.btn_power.clicked.connect(self.power)
        self.ui.btn_clear.clicked.connect(self.function_clear)
        self.ui.btn_back.clicked.connect(self.function_delete)
        # self.ui.btn_c.clicked.connect(lambda: self.click())
        # self.ui.btn_d.clicked.connect(lambda: self.click())
        # self.ui.btn_help.clicked.connect(self.help_button)

    def click(self, text):  # метод принимает аргумент (цифру, на которую будем нажимать)
        self.display(text)

    def display(self, text):
        # метод принимает аргумент и выводит на label_display
        text_on_display.append(text)
        if len(all_results) != 0 and all_results[-1] == self.ui.label_display.text() and \
                text_on_display[-1] not in calc_for_main.signs:
            self.ui.label_display.clear()
        symbol = self.ui.label_display.text()
        if symbol in ('0', '0.0'):
            symbol = ''
        elif symbol == '.':
            symbol = '0.'
        all_text = symbol + text
        self.ui.label_display.setText(all_text)
        # if len(all_text) < 18:
        #     self.ui.label_display.setText(all_text)

    def function_clear(self):
        self.ui.label_display.setText('0')
        while len(all_results) != 0:
            del all_results[0]

    def function_delete(self):
        value = self.ui.label_display.text()
        self.ui.label_display.setText(value[:-1])
        if len(value) == 1:
            self.ui.label_display.setText('0')

    def sqrt(self):
        result_sqrt = calc_for_main.sqrt(self.ui.label_display.text())
        all_results.append(result_sqrt)
        self.ui.label_display.clear()
        self.display(result_sqrt)

    def power(self):
        result_power = calc_for_main.power(self.ui.label_display.text())
        all_results.append(result_power)
        self.ui.label_display.clear()
        self.display(result_power)

    def calculate(self):
        result = calc_for_main.expression(self.ui.label_display.text())
        all_results.append(result)
        self.ui.label_display.clear()
        self.display(result)

    @staticmethod
    def help_button():
        window_help = QMessageBox()
        window_help.setWindowTitle('Help')
        window_help.setText('''Just enter what you want to calculate.
The calculator supports standard operations: addition, subtraction, multiplication, division. 
You can also evaluate expressions with parentheses, such as: (1*(2-3)+4)/3 or (2,3 - 3.2) / 0,1. 
Or you can set your variable a=5 and then use 4-a+2 in the expression.''')
        window_help.show()
        window_help.exec_()


all_results = []
text_on_display = []

if __name__ == "__main__":
    app = QApplication(sys.argv)
    example = App()  # экземплаяр класса (графический объект класса), приложение является объектом класса
    sys.exit(app.exec_())  # или так: app.exec_() - завершает приложение, останавливает скрипт
