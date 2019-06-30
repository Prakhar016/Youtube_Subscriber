import PySimpleGUI as sg
import urllib.request
import json
layout = [
              [sg.Text('Please enter youtuber Name')],
              [sg.Text('Name', size=(15, 1)), sg.InputText()],
              [sg.Submit(bind_return_key=True)],[sg.Text('subscriber are:', size=(15, 1))],[sg.Text('', size=(15, 1), key='out')]]
window = sg.Window('youtuber subscriber count', layout)

key = "Enter your API"#enter your API key

while True:
    event, values = window.Read()
    data = urllib.request.urlopen( "https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=" + values[0] + "&key=" + key).read()
    subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
    print(subs)
    window.Element('out').Update(subs)
window.Close()