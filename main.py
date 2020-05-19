import PySimpleGUI as sg
from translate_code import translate

sg.theme("Dark Green 5")

layout_main = [[sg.Text('Welcome to ALP', justification='r', size=(30, 1))],
          [sg.Text('       Choose text file with your Algorithm to translate in Python')],
          [sg.In(disabled=True), sg.FileBrowse()],
          [sg.Button('Translate')],
          [sg.Multiline(default_text='Here will be Python code', key='result', size=(70, 10))],
          [sg.Exit()]
          ]

layout_rules = [[sg.Text('Внимание! Перед использованием программы ознакомтесь с правилами!', justification='c')],
                [sg.Text('1. Перед запуском переводчика проверьте алгоритм на синтаксические ошибки', justification='l')],
                [sg.Text('2. В данной версии программы не используются служебные слова "то" и слова, описывающие предназначение кода', justification='l')],
                [sg.Text('3. Соблюдайте логическую табуляцию (не надо писать длинные инструкции в одной строке)', justification='l')],
                [sg.Text('4. Также в данной версии не поддерживаются условия с более чем одним "И", "ИЛИ", "НЕ"')],
                [sg.Button('OK')]]

window = sg.Window("ALP by Leo", layout_rules)

while True:
    event, values = window.read()
    if event == 'OK':
        break
window.close()
window = sg.Window("ALP by Leo", layout_main)

while True:
    event, values = window.read()
    if event == 'Exit':
        break
    if event == 'Translate':
        with open(values[0], 'r', encoding='utf-8') as file:
            buffer = [i for i in file]
        result_buffer = translate(buffer)
        print(result_buffer)
        st = ''
        for i in result_buffer:
            st += i
        window['result'](st)

window.close()