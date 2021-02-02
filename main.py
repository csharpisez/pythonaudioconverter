import PySimpleGUI as sg
from os import path
from pydub import AudioSegment

sg.theme('Reddit')  

layout = [
    [sg.InputText('Source File', size=(37,1), key='input_value')],
    [sg.InputText('Output Name', size=(37,1), key='input_value1')],
    [sg.InputOptionMenu(('MP3 to WAV', 'WAV to MP3'), size=(32,1), key='-OPTION-')],
    [sg.Submit(size=(32,1))],]

window = sg.Window('Audioconverter', layout)
event, values = window.read()

def mpthreetowav():
    sound = AudioSegment.from_mp3(value)
    sound.export(value1, format="wav")

def wavtompthree():
    sound = AudioSegment.from_wav(value)
    sound.export(value1, format="mp3")

if event == 'Submit':
    value = values['input_value']
    value1 = values['input_value1']
    option = values['-OPTION-']

if option == 'MP3 to WAV' :
    mpthreetowav();

if option == 'WAV to MP3' :
    wavtompthree();

window.close()
