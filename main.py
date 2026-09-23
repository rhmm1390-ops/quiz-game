import tkinter as tk
from tkinter import messagebox

questions = [
    (
        "YOUR FAVORITE COLOR?",
        ["A : RED", "B : GREEN", "C : YELLOW", "D : BLUE"],
        "A"
    ),
    (
        "YOUR FAVORITE FOOD?",
        ["A : RICE", "B : KEBAB", "C : SALAD", "D : WATER"],
        "C"
    ),
    (
        "YOUR FAVORITE CAR?",
        ["A : BMW", "B : BENZ", "C : PORSCHE", "D : PARS"],
        "D"
    )
]

score = 0
correct_answers = 0
index = 0

NORMAL_SCORE = 10
HIGH_SCORE = 20
PENALTY = 3

BG = "#090A16"
PANEL = "#111329"
PURPLE = "#8A2BE2"
BLUE = "#00BFFF"
WHITE = "#FFFFFF"
GREEN = "#00FF99"

window = tk.Tk()
window.title("QUIZ BATTLE")
window.geometry("800x600")
window.resizable(False, False)
window.configure(bg=BG)

title = tk.Label(
    window, text="⚡ QUIZ BATTLE ⚡",
    font=("Arial", 30, "bold"),
    bg=BG, fg=PURPLE
)
title.pack(pady=(25, 5))

subtitle = tk.Label(
    window, text="TEST YOUR KNOWLEDGE",
    font=("Arial", 11, "bold"),
    bg=BG, fg=BLUE
)
subtitle.pack()

score_frame = tk.Frame(
    window, bg=PANEL,
    highlightbackground=PURPLE,
    highlightthickness=2
)
score_frame.pack(pady=20, padx=50, fill="x")

score_label = tk.Label(
    score_frame, text="SCORE: 0",
    font=("Arial", 16, "bold"),
    bg=PANEL, fg=GREEN
)
score_label.pack(side="left", padx=25, pady=12)

question_number = tk.Label(
    score_frame, text="QUESTION: 1 / 3",
    font=("Arial", 16, "bold"),
    bg=PANEL, fg=WHITE
)
question_number.pack(side="right", padx=25, pady=12)

question_frame = tk.Frame(
    window, bg=PANEL,
    highlightbackground=BLUE,
    highlightthickness=2
)
question_frame.pack(padx=70, pady=10, fill="x")

question_label = tk.Label(
    question_frame, text="",
    font=("Arial", 22, "bold"),
    bg=PANEL, fg=WHITE, pady=25
)
question_label.pack()

answers_frame = tk.Frame(window, bg=BG)
answers_frame.pack(pady=20)

answer_buttons = []

button_colors = [
    "#7B2CBF",
    "#0077B6",
    "#D00070",
    "#00695C"
]

def check_answer(answer):
    global score, correct_answers, index

    correct = questions[index][2]

    if answer == correct:
        correct_answers += 1

        if index == len(questions) - 1:
            score += HIGH_SCORE
        else:
            score += NORMAL_SCORE

        messagebox.showinfo(
            "CORRECT!",
            "🔥 GREAT JOB!\n\nYour answer is correct!"
        )
    else:
        score -= PENALTY

        messagebox.showerror(
            "WRONG!",
            f"❌ WRONG ANSWER!\n\nCorrect answer: {correct}"
        )

    index += 1

    if index < len(questions):
        show_question()
    else:
        finish_game()

def show_question():
    question = questions[index]

    question_label.config(text=question[0])
    score_label.config(text=f"SCORE: {score}")
    question_number.config(
        text=f"QUESTION: {index + 1} / {len(questions)}"
    )

    for i in range(4):
        answer_buttons[i].config(
            text=question[1][i],
            command=lambda x=chr(65 + i): check_answer(x)
        )

def finish_game():
    percentage = (correct_answers / len(questions)) * 100

    question_label.config(text="🏆 GAME COMPLETE 🏆")
    score_label.config(text=f"SCORE: {score}")
    question_number.config(text="FINISHED!")

    for button in answer_buttons:
        button.config(state="disabled")

    messagebox.showinfo(
        "GAME OVER",
        f"🎮 QUIZ COMPLETE!\n\n"
        f"Correct Answers: {correct_answers} / {len(questions)}\n\n"
        f"Percentage: {percentage:.0f}%\n\n"
        f"Final Score: {score}"
    )

for i in range(4):
    button = tk.Button(
        answers_frame,
        text="",
        font=("Arial", 15, "bold"),
        width=24,
        height=2,
        bg=button_colors[i],
        fg=WHITE,
        activebackground=PURPLE,
        activeforeground=WHITE,
        relief="flat",
        bd=0,
        cursor="hand2"
    )

    button.grid(
        row=i // 2,
        column=i % 2,
        padx=12,
        pady=10
    )

    answer_buttons.append(button)

show_question()
window.mainloop()