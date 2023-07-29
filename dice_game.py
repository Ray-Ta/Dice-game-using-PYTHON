import random
#print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
#● ┌ ─ ┐ │ └ ┘

dice_pattern= {             #dictionarie of dice
    1:("┌───────────┐",
       "│           │",     #tupel of number
       "│     ●     │",
       "│           │",
       "└───────────┘"),
    2: ("┌───────────┐",
        "│  ●        │",
        "│           │",
        "│        ●  │",
        "└───────────┘"),
    3: ("┌───────────┐",
        "│  ●        │",
        "│     ●     │",
        "│        ●  │",
        "└───────────┘"),
    4: ("┌───────────┐",
        "│  ●     ●  │",
        "│           │",
        "│  ●     ●  │",
        "└───────────┘"),
    5: ("┌───────────┐",
        "│  ●     ●  │",
        "│     ●     │",
        "│  ●     ●  │",
        "└───────────┘"),
    6: ("┌───────────┐",
        "│  ●     ●  │",
        "│  ●     ●  │",
        "│  ●     ●  │",
        "└───────────┘")
}
while True:
    dice=[]
    total =0

    num= 2 #int(input("number of dice:")) #customizing dice number
    for d in range(num):
        dice.append(random.randint(1,6))
    for l in range(5):
        for d in dice:
            print(dice_pattern.get(d)[l], end="")
        print()
    #for d in range(num):
    #   for l in dice_pattern.get(dice[d]):
    #       print(l)
    for d in dice:
        total+=d
    print("total:", str(total))
    toss = int(input("press any number if you wanna toss else press 0 to end:"))
    if toss==0:
        break
    else:
        continue

