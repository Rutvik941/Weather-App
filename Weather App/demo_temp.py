from tkinter import *
from tkinter import ttk
import requests

def data_get():
   city = city_name.get()
   data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=a62dce6b36b41e24cb0de8c1e5b8cf53").json()
   temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
   wc_label1.config(text=data["weather"][0]["main"])
   wd_label1.config(text=data["weather"][0]["description"]) 
   pre_label1.config(text=data["main"]["pressure"])


win = Tk()
win.title("World Weather App")
win.config(bg = "sky blue")
win.geometry("500x500")


name_label = Label(win,text="World Weather App",
                font=("Time New Roman",25,"bold"))
name_label.place(x=25,y=50,height=50,width=450)

city_name = StringVar()
list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox(win,text="India Weather App",values=list_name,
                font=("Time New Roman",15,"bold"),textvariable=city_name)
com.place(x=40,y=120,height=40,width=420)


temp_label = Label(win,text="Temperature",
                font=("Time New Roman",15))
temp_label.place(x=35,y=260,height=40,width=190)

temp_label1 = Label(win,text="",
                font=("Time New Roman",15))
temp_label1.place(x=270,y=260,height=40,width=190)


wc_label = Label(win,text="Weather Climate",
                font=("Time New Roman",15))
wc_label.place(x=35,y=320,height=40,width=190)

wc_label1 = Label(win,text="",
                font=("Time New Roman",15))
wc_label1.place(x=270,y=320,height=40,width=190)


wd_label = Label(win,text="Weather Description",
                font=("Time New Roman",15))
wd_label.place(x=35,y=380,height=40,width=190)

wd_label1 = Label(win,text="",
                font=("Time New Roman",15))
wd_label1.place(x=270,y=380,height=40,width=190)


pre_label = Label(win,text="Pressure",
                font=("Time New Roman",16))
pre_label.place(x=35,y=440,height=40,width=190)

pre_label1 = Label(win,text="",
                font=("Time New Roman",16))
pre_label1.place(x=270,y=440,height=40,width=190)


done_button = Button(win,text="Done",
                font=("Time New Roman",15,"bold"), command=data_get)
done_button.place(y=190,height=40,width=100,x=200)


win.mainloop()