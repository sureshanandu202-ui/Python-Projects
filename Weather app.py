# import required modules
from configparser import ConfigParser
import requests
from tkinter import *
from tkinter import messagebox

# extract key from the
# configuration file

config_file = "config.ini" 
config = ConfigParser()
config.read(config_file)
api_key =config['gfg']['api']
url = 'http://api.openweathermap.org/data/2.5/weather?q=%7B%7D%appid=%7B%7D'

# explicit function to get 
# weather details 
def getweather(city):
    result =requests.get(url.format(city,api_key))
    if result:
        json = result.json()
        city = json['name'] 
        country = json['sys']
        temp_kelvin = json['main']
['temp']
temp_celcius = 'temp_kelvin' - 273.15
weather1 = 'json'('weather'[0])
()

['main']
final = ['city,country,temp_kelvin,temp_celcius,weather1']
 
#< --- ERROR: Not in a function block
'return':final # type: ignore   
print("NO Content Found") 

#explicit function to 
# search city
def search():
    city = city_text.get()
    weather = getweather(city) 
    if weather:
        location_1b1['text'] = '{} {}'.format(weather[0], weather[1])
        temperature_label['text'] = str(weather[3]) + " Degree Celcius"
        weather_1['text'] = weather[4]
    else:
        messagebox.showerror('Error', "Cannot find {}".format(city))


# Driver Code
# create object
app = Tk()
# add title
app.title("Weather App")
# adjust window size
app.geometry("300x300")

# add labels, buttons and text
city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack()
search_btn = Button(app, text="Search Weather", width=12, command=search)
search_btn.pack()
location_1b1 = Label(app, text="Location", font=('bold', 20))
location_1b1.pack()
temperature_label = Label(app, text="")
temperature_label.pack()
weather_1 = Label(app, text="")
weather_1.pack()
app.mainloop()
