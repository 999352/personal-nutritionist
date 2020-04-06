from fatsecret import Fatsecret
from tkinter import *
import tkinter as tk
from tkinter import messagebox

consumer_key = "2721ecada6154bffa1aafab612348b13"
consumer_secret = "5f93269b0fc34b57a29b1ceff6af1d52"
fs = Fatsecret(consumer_key, consumer_secret)




def display():
    item = fooditem.get()
    foods = fs.foods_search(item)
    print(foods)
    text = ''
    sb = Scrollbar(top)
    food_list = Listbox(top,width = 100,height = 30,yscrollcommand=sb.set, bg='pink', fg='blue')
    food_list.place(x=550, y=250)
    for i in foods:
        text += 'Food Description : '
        text =text + i['food_description']
        food_list.insert(END, text)
        text = ''
        text += 'Food Id : '
        text = text + i['food_id']
        food_list.insert(END, text)
        text = ''
        text += 'Food Name : '
        text = text + i['food_name']
        food_list.insert(END, text)
        text = ''
        text += 'Food Type : '
        text = text + i['food_type']
        food_list.insert(END, text)
        text = ''
        text += 'Food Id : '
        text = text + i['food_id']
        food_list.insert(END, text)
        text = ''
        text += 'Food URL : '
        text = text + i['food_url']
        food_list.insert(END, text)
        text = '-----------------------------------------------------------'
        food_list.insert(END,text)
        text = ''


def display_list():
    clear = Label(top, bg='#00ffec', height=500, width=200)
    clear.place(x=100, y=250)
    food_label = Label(top,text = "Food Item : ",bg = 'pink',fg = 'blue',font = 'Times 10 bold italic',bd = 5)
    food_label.place(x = 100,y = 250)
    food = Entry(top, textvariable=fooditem,width = 30, bd=5)
    food.place(x = 200,y = 250)
    search = Button(top,bd = 5,text = "search",command = display,bg = 'pink',font = 'Times 10 bold italic')
    search.place(x = 250,y = 300)

def close_home():
    top.destroy()

def result():

    intake_male = (66.5 + (13.8 * weight.get()) + (5 * height.get()))/(6.8*age.get())
    intake_female = (655.1 + (9.6 * weight.get()) + (1.9 * height.get())) / (4.7 * age.get())
    text = "Male : " + str(intake_male) + "Kcal" +"\n"+ "female : " +str(intake_female) + "Kcal."
    messagebox.showinfo("CALORIE REQUIREMENT",text)

def calculate():
    claorie = 0;
    clear = Label(top,bg = '#00ffec',height = 500,width = 200)
    clear.place(x = 100,y = 250)
    age_label = Label(top, text="Age(in years) : ", bg='pink', fg='blue', font='Times 10 bold italic', bd=5)
    age_label.place(x=100, y=250)
    age_entry = Entry(top, textvariable=age, width=30, bd=5)
    age_entry.place(x=200, y=250)

    weight_label = Label(top, text="Weight(in Kg) : ", bg='pink', fg='blue', font='Times 10 bold italic', bd=5)
    weight_label.place(x=100, y=350)
    weight_entry = Entry(top, textvariable=weight, width=30, bd=5)
    weight_entry.place(x=200, y=350)

    height_label = Label(top, text="height(in cm) : ", bg='pink', fg='blue', font='Times 10 bold italic', bd=5)
    height_label.place(x=100, y=450)
    height_entry = Entry(top, textvariable=height, width=30, bd=5)
    height_entry.place(x=200, y=450)

    dis = Button(top, bd=5, text="Result", command=result, bg='pink', font='Times 10 bold italic')
    dis.place(x=300, y=550)

top = Tk()


top.configure(background = '#00ffec')
heading = Label(top,text = "RAVI PERSONAL NUTRITIONIST",bg = 'pink',fg = 'blue',font = 'Times 50 bold italic',bd = 10,relief = 'raised')
heading.place(x = 250,y = 50)

search = Button(top,bd = 5,text = "List Food Items",command = display_list,bg = 'pink',font = 'Times 10 bold italic')
search.place(x = 300,y = 160)

cal = Button(top,bd = 5,text = "Calculate Calorie",command = calculate,bg = 'pink',font = 'Times 10 bold italic')
cal.place(x = 650,y = 160)

exit = Button(top,bd = 5,text = "Exit",command = close_home,bg = 'pink',font = 'Times 10 bold italic')
exit.place(x = 1150,y = 160)

fooditem = StringVar()
foodlist = StringVar()

age = IntVar()
weight = IntVar()
height = IntVar()

top.mainloop()

