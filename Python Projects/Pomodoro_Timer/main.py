from tkinter import *
import math
import pygame

# CONSTANTS

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
count_time = ""
pygame.mixer.init()
alert = pygame.mixer.Sound('alarm.wav')


# TIMER RESET

def reset():
    window.after_cancel(count_time)
    canvas.itemconfig(time, text="00:00")
    timer.config(text="Timer", fg=GREEN)
    check_mark.config(text="")
    global REPS
    REPS = 0


# TIMER MECHANISM

def start():
    global REPS
    REPS += 1
    work = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        count_down(long_break)
        timer.config(text="Break", fg=RED)
        alert.play()

    elif REPS % 2 == 0:
        count_down(short_break)
        timer.config(text="Break", fg=PINK)
        alert.play()

    else:
        count_down(work)
        timer.config(text="Work", fg=GREEN)


# COUNTDOWN MECHANISM

def count_down(count):
    global REPS
    min = math.floor(count / 60)
    sec = count % 60
    if sec < 10:
        sec = f"0{sec}"

    canvas.itemconfig(time, text=f"{min}:{sec}")
    if count > 0:
        global count_time
        count_time = window.after(1000, count_down, count - 1)

    else:
        start()
        check = ""
        for rep in range(math.floor(REPS / 2)):
            check += "✅"
        check_mark.config(text=check)


# UI

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato)
time = canvas.create_text(100, 132, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 45, "bold"), bg=YELLOW)
timer.grid(column=1, row=0)

start_button = Button(text="Start", font=(FONT_NAME, 8, "bold"), highlightthickness=0, command=start)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=(FONT_NAME, 8, "bold"), highlightthickness=0, command=reset)
reset_button.grid(column=2, row=2)

check_mark = Label(fg="#037d50", bg=YELLOW, font=(FONT_NAME, 10, "bold"))
check_mark.grid(column=1, row=3)

copy = Label(text="© Copyright Mikazaki™", fg="#000000", font=(FONT_NAME, 10, "bold"), bg=YELLOW)
copy.grid(column=1, row=4)

window.mainloop()
