from rich.console import Console

console = Console()
while True:
    print("1: start new game")
    print("2: Exit")
    choice: str = input ("Enter your choice: ").strip()

    if choice == "2":
        break
    if choice != "1":
        continue
    soal=[
        ("your faverit color?",["A : red","B : greeen","C : yeloow","D : blue"],"A"),
        ("your faverit food?",["A : ric","B : cebab","C : saled","D : whater"],"C" ),
        ("your faverit car?",["A : bmw","B : benz","C : porshe","D : pars"],"D")
        ]

    score = 0
    index = 1
    NORMAL_SCORE = 10
    HIGH_score = 20
    PENALTY = 3
    correct_answer = 0
    for soal , ansewer, correct in soal:
        console.print(soal, style="blue")
        for ansewer in ansewer:
            console.print(ansewer,style= "red")
        user_answer= input(" your ansewer (A/B/C/D): ").strip().upper()
        if user_answer == correct:
            correct_answer += 1
            if index == len(soal):
                score+= HIGH_score
            else:
                score += NORMAL_SCORE
            console.print("correct!\n")
            
        else:
            score -= PENALTY
            console.print(f"wrong! The correct answer is {correct}.\n")
            
        index+= 1

    print(f"yor ansewed {correct_answer} out of {len(soal)} soal correctly.")
    print(f"your final percentage is: {correct_answer} / len(soal) * 100% ")
    print(f"your final score is: {score}")

