from tkinter import *
import requests

root = Tk()
root.resizable(width=False, height=False)
root.geometry('300x250')

def get_weather():
    city = cityField.get()
    key = 'cae8088163a070950b77b056372c3bd5'

    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': key, 'q': city, 'units': 'metric'}

    result = requests.get(url, params=params)
    weather = result.json()
    info['text'] = f'{str(weather["name"])}: {weather["main"]["temp"]}'

frame_top = Frame(root, bg='#ffb700', bd=5)
frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.25)

frame_bottom = Frame(root, bg='#ffb700', bd=5)
frame_bottom.place(relx=0.15, rely=0.45, relwidth=0.7, relheight=0.1)

cityField = Entry(frame_top, bg='white', font=30)
cityField.pack()

info = Label(frame_bottom, text='Information about weather', bg='#ffb700', font=40)
info.pack()

btn = Button(frame_top, text='Watch the weather', command=get_weather)
btn.pack()


root.mainloop()