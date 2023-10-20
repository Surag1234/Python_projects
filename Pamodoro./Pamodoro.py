from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def timer_reset():
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    check_mark.config(text=None)
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    work_min = WORK_MIN * 60
    short_break_min = SHORT_BREAK_MIN * 60
    long_break_min = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_min)
        timer_label.config(text="Break", fg=GREEN)

    elif reps % 2 == 0:
        count_down(short_break_min)
        timer_label.config(text="Break", fg=GREEN)

    else:
        count_down(work_min)
        timer_label.config(text="Work", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_minutes = count // 60
    count_seconds = count % 60

    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text=f"{count_minutes} : {count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = reps // 2
        for _ in range(work_sessions):
            if work_sessions % 2 == 0:
                mark = "✓"
        check_mark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=50, pady=50, bg=YELLOW)
window.title("Pomodoro App")

canvas = Canvas(width=200, height=225, bg=YELLOW, highlightthickness=0)
photo_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font='Helvetica 35 bold')
canvas.grid(row=1, column=1)

timer_label = Label(text="Timer", font='Helvetica 35 bold', fg=GREEN)
timer_label.grid(row=0, column=1)

start_label = Button(text="Start", font='Helvetica 10 bold', highlightthickness=0, command=start_timer)
start_label.grid(row=2, column=0)

restart_label = Button(text="Reset", font='Helvetica 10 bold', highlightthickness=0, command=timer_reset)
restart_label.grid(row=2, column=2)

check_mark = Label(fg=GREEN, bg=YELLOW)
check_mark.grid(row=3, column=1)

window.mainloop()
