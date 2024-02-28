import PySimpleGUI as sg

sg.theme('DarkBrown4')

layout = [
    [sg.Text('Primo numero:'), sg.Input(key='num1')],
    [sg.Text('Secondo numero:'), sg.Input(key='num2')],
    [sg.Button('Pari'), sg.Button('Esci')],
    [sg.Text('Risultato:'), sg.Text(key='risultato')]
]

window = sg.Window('Trova numeri pari', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Esci':
        break

    if event == 'Pari':
        num1 = int(values['num1'])
        num2 = int(values['num2'])
        risultato = ''

        if num1 % 2 == 0:
            risultato += f'{num1} è pari\n'
        else:
            risultato += f'{num1} è dispari\n'

        if num2 % 2 == 0:
            risultato += f'{num2} è pari'
        else:
            risultato += f'{num2} è dispari'

        window['risultato'].update(risultato)

window.close()