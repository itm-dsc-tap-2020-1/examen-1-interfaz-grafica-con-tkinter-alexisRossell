import tkinter as tk
from tkinter import ttk, scrolledtext, Menu
from tkinter import messagebox as mBox

window = tk.Tk()
window.title('Examen 01')
window.resizable(0, 0)

labels = {}
entries = {}
comboBoxes = {}
buttons = {}
checkButtons = {}
radioButtons = {}
scrollText = {}
indexes = {
    'window': {
        'row': 0,
        'column': 0
    }
}
respuestas = ('10', 'bien', 'cosa1', 'cosa2', 'check1', 'check2')

def funcionSalir():
    window.quit()
    window.destroy()
    exit()

def makeLabel(window, fieldName, texto, noRow, noColumn, noRowSpan = 1, noColumnSpan = 1, ipady = 5):
    labels[fieldName] = ttk.Label(window, text = texto)
    labels[fieldName].grid(column = noColumn, row = noRow, columnspan = noColumnSpan, rowspan = noRowSpan, ipady = ipady)

def makeEntry(window, fieldName, noRow, noColumn, noRowSpan = 1, noColumnSpan = 1):
    entries[fieldName] = (ttk.Entry(window), tk.StringVar())
    entries[fieldName][0].configure(textvariable = entries[fieldName][1])
    entries[fieldName][0].grid(row = noRow, column = noColumn, rowspan = noRowSpan, columnspan = noColumnSpan)

def makeComboBox(window, fieldName, options, noRow, noColumn, noRowSpan = 1, noColumnSpan = 1, State = 'readonly'):
    comboBoxes[fieldName] = (ttk.Combobox(window), tk.StringVar())
    comboBoxes[fieldName][0].configure(textvariable = comboBoxes[fieldName][1], state = State)
    comboBoxes[fieldName][0]['values'] = options
    comboBoxes[fieldName][0].current(0)
    comboBoxes[fieldName][0].grid(row = noRow, column = noColumn, rowspan = noRowSpan, columnspan = noColumnSpan)

def makeCheckButton(window, fieldName, texto, noRow, noColumn, ipady = 5, ipadx = 5):
    checkButtons[fieldName] = (tk.Checkbutton(window), tk.StringVar())
    checkButtons[fieldName][0].configure(text = texto, var = checkButtons[fieldName][1], onvalue = fieldName.capitalize(), offvalue = '')
    checkButtons[fieldName][0].grid(row = noRow, column = noColumn, ipady = ipady, ipadx = ipadx)

def makeRadioButtons(window, fieldName, variable,value, texto, noRow, noColumn, ipady = 5, ipadx = 5):
    radioButtons[fieldName] = tk.Radiobutton(window)
    radioButtons[fieldName].configure(text = texto, variable = variable, value = value)
    radioButtons[fieldName].grid(row = noRow, column = noColumn, ipady = ipady, ipadx = ipadx)

def makeScrolledText(window, fieldName, row, column, width, height, wrap):
    scrollText[fieldName] = scrolledtext.ScrolledText(window)
    scrollText[fieldName].configure(width = width, height = height, wrap = wrap)
    scrollText[fieldName].grid(column = column, row = row, columnspan = 2)

def makeButton(window, fieldName, texto, function, noRow, noColumn, noRowSpan = 1, noColumnSpan = 1):
    buttons[fieldName] = ttk.Button(window, text = texto, command = function)
    buttons[fieldName].grid(row = noRow, column = noColumn, rowspan = noRowSpan, columnspan = noColumnSpan, ipadx = 5, ipady = 5)

def nextRow(field):
    indexes[field]['row'] += 1

def nextColumn(field):
    indexes[field]['column'] += 1

def wrap(field):
    nextRow(field)
    indexes[field]['column'] = 0

def calificar():
    resultado = 0
    for k, v in entries.items():
        if v[1].get() and v[1].get() in respuestas:
            resultado += 20
        
    for k, v in checkButtons.items():
        if v[1].get() and v[1].get() in respuestas:
            resultado += 20
            break

    seleccionPregunta3 = variablePregunta3.get()
    seleccionPregunta4 = variablePregunta4.get()
    opcion = 1
    for k, v in radioButtons.items():
        if k in respuestas:
            if opcion == seleccionPregunta3 or opcion == seleccionPregunta4:
                resultado += 20
        opcion += 1
    
    mBox.showinfo('Resultados', 'Usted ha obtenido: ' + str(resultado))


makeLabel(window, 'pregunta1', '¿Cuanto esperas sacar en el examen?', indexes['window']['row'], indexes['window']['column'])
nextColumn('window')
makeEntry(window, 'pregunta1', indexes['window']['row'], indexes['window']['column'])
wrap('window')

makeLabel(window, 'pregunta2', '¿Como te sientes?', indexes['window']['row'], indexes['window']['column'])
nextColumn('window')
makeEntry(window, 'pregunta2', indexes['window']['row'], indexes['window']['column'])
wrap('window')

makeLabel(window, 'pregunta3', 'Pregunta 3', indexes['window']['row'], indexes['window']['column'])
variablePregunta3 = tk.IntVar()
nextRow('window')
makeRadioButtons(window, 'cosa1', variablePregunta3, 1, 'cosa1', indexes['window']['row'], indexes['window']['column'])
nextColumn('window')
makeRadioButtons(window, 'cosa2', variablePregunta3, 2, 'cosa2', indexes['window']['row'], indexes['window']['column'])
nextColumn('window')
makeRadioButtons(window, 'cosa3', variablePregunta3, 3, 'cosa3', indexes['window']['row'], indexes['window']['column'])
wrap('window')

makeLabel(window, 'pregunta4', 'Pregunta 4', indexes['window']['row'], indexes['window']['column'])
nextRow('window')
variablePregunta4 = tk.IntVar()
makeRadioButtons(window, 'cosa1', variablePregunta4, 1, 'cosa1', indexes['window']['row'], indexes['window']['column'])
nextColumn('window')
makeRadioButtons(window, 'cosa2', variablePregunta4, 2, 'cosa2', indexes['window']['row'], indexes['window']['column'])
nextColumn('window')
makeRadioButtons(window, 'cosa3', variablePregunta4, 3, 'cosa3', indexes['window']['row'], indexes['window']['column'])
wrap('window')

makeLabel(window, 'pregunta5', 'Pregunta 5', indexes['window']['row'], indexes['window']['column'])
nextRow('window')
makeCheckButton(window, 'check1', 'Leer', indexes['window']['row'], indexes['window']['column'])
nextColumn('window')
makeCheckButton(window, 'check2', 'Peliculas', indexes['window']['row'], indexes['window']['column'])
nextColumn('window')
makeCheckButton(window, 'check3', 'Redes Sociales', indexes['window']['row'], indexes['window']['column'])
nextColumn('window')
makeCheckButton(window, 'check4', 'cosa', indexes['window']['row'], indexes['window']['column'])
nextColumn('window')
makeCheckButton(window, 'check5', 'otracosa', indexes['window']['row'], indexes['window']['column'])
wrap('window')

makeButton(window, 'calificar', 'Calificar', calificar, indexes['window']['row'], indexes['window']['column'])

window.mainloop()