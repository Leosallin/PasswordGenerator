import random
import string
import PySimpleGUI as sg

# GUI #

layout = [[sg.Output(size=(15,1), key='SenhaGerada')],
          [sg.Button('Gerar Senha', size=(15,1)),sg.Button('Sair'), sg.Text('Version: 1.0')]]

window = sg.Window('Password Generator', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Sair':
        break
    # Output a message to the window
    if event == 'Gerar Senha':
        # Definição de caracteres #

        letras = string.ascii_letters
        numeros = string.digits
        especiais = string.punctuation

        # Definição de tamanho #

        tam = random.randrange(7,13)

        # Construção da senha #

        Pass = letras + numeros + especiais

        PassRandom = "".join(random.sample(Pass,tam))

        print(PassRandom)
        window['SenhaGerada'].update(PassRandom)

# Finish up by removing from the screen
window.close()

