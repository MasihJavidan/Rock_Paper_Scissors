from tkinter import *
from random import choice

select = ['سنگ', 'کاغذ', 'قیجی']

def stone():
    comp = choice(select)
    label["text"] = "انخاب حریف:" + " " + comp
    if comp == "کاغذ":
        frame_score_computer["text"] = int(frame_score_computer["text"]) + 1
    elif comp == "قیجی":
        frame_score_player["text"] = int(frame_score_player["text"]) + 1
    

def paper():
    comp = choice(select)
    label["text"] = "انخاب حریف:" + " " + comp
    if comp == "قیجی":
        frame_score_computer["text"] = int(frame_score_computer["text"]) + 1
    elif comp == "سنگ":
        frame_score_player["text"] = int(frame_score_player["text"]) + 1


def scissors():
    comp = choice(select)
    label["text"] = "انخاب حریف:" + " " + comp
    if comp == "سنگ":
        frame_score_computer["text"] = int(frame_score_computer["text"]) + 1
    elif comp == "کاغذ":
        frame_score_player["text"] = int(frame_score_player["text"]) + 1


def reset_game():
    frame_score_player["text"] = int(frame_score_player["text"]) - int(frame_score_player["text"])
    frame_score_computer["text"] = int(frame_score_computer["text"]) - int(frame_score_computer["text"])


window = Tk()
window.title("سنگ کاغذ قیچی")
window.minsize(500, 600)
window.rowconfigure([0,1,2,3], weight=1)
window.columnconfigure(0, weight=1)

label = Label(master=window, text='انتخاب کنید', bg="#fff", height=2,
    font=("None",18,"bold"))
label.grid(row=0, column=0, sticky="nwe")


frame_button = Frame(master=window, height=100, bg='red')
frame_button.rowconfigure(0, weight=1)
frame_button.columnconfigure([0,1,2], weight=1)

stone_button = Button(master=frame_button, text="سنگ", height=3, command=stone,
    font=("None", 16, "bold")).grid(row=0, column=0, sticky="nwes", padx=2, pady=3)

paper_button = Button(master=frame_button, text="کاغذ", height=3, command=paper,
    font=("None", 16, "bold")).grid(row=0, column=1, sticky="nwes", padx=2, pady=3)

scissors_button = Button(master=frame_button, text="قیجی", height=3, command=scissors,
    font=("None", 16, "bold")).grid(row=0, column=2, sticky="nwes",  padx=2, pady=3)

frame_button.grid(row=1, column=0, sticky="wen")


frame_result = Frame(master=window, height=200)
frame_result.rowconfigure([0,1], weight=1)
frame_result.columnconfigure([0,1], weight=1)

frame_label_player = Label(master=frame_result, text="امتیاز شما",
     relief="ridge").grid(row=0, column=0, sticky="nswe")
frame_label_computer = Label(master=frame_result, text="امتیاز حریف", 
    relief="ridge").grid(row=0, column=1, sticky="nswe")

frame_score_player = Label(master=frame_result,text="0", height=4, bg="blue",
    font=("None", 40, "bold"))
frame_score_player.grid(row=1, column=0, sticky="nswe")

frame_score_computer = Label(master=frame_result, text="0", height=3, bg="red"
    ,font=("None", 40, "bold"))
frame_score_computer.grid(row=1, column=1, sticky="nswe")

frame_result.grid(row=2, column=0, sticky="nswe")

Button_reset = Button(master=window, text="برو از اول", height=2, bg="#fff", command=reset_game,
    font=("None", 18, "bold"), relief="ridge").grid(row=3, column=0, sticky="nwe")

window.mainloop()
