from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

timer = None
reps = 0

def reset_timer():
  global reps
  
  window.after_cancel(timer)
  
  title_label.config(text="Timer", fg=GREEN)
  canvas.itemconfig(timer_text, text="00:00")
  reps = 0

def start_timer():
  global reps
  reps += 1
  
  work_sec = WORK_MIN * 60
  short_break_sec = SHORT_BREAK_MIN * 60
  long_break_sec = LONG_BREAK_MIN * 60
  
  if reps % 8 == 0:
    countdown(long_break_sec)
    title_label.config(text="Break", fg=RED)
  elif reps % 2 == 0:
    countdown(short_break_sec)
    title_label.config(text="Break", fg=PINK)
  else:
    countdown(work_sec)
    title_label.config(text="Work", fg=GREEN)

def countdown(count):
  global timer
  
  count_min = math.floor(count / 60)
  count_sec = count % 60
  
  canvas.itemconfig(timer_text, text=f"{"0" if count_min < 10 else ""}{count_min}:{"0" if count_sec < 10 else ""}{count_sec}")
  if count > 0:
    timer = window.after(1000, countdown, count-1)
  else:
    start_timer()

window = Tk()
window.title("Pomodoro")
window.config(padx=200, pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)

canvas = Canvas(width=204, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white")
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()