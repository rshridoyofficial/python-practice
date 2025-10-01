from random import choice
words = ["SNACK", "WATER", "GUN"]
computerChoice = choice(words)
myChoice = input("choze any of them [SNACK, WATER, GUN]  : ").upper()
dictionary= {
    "SNACK":"Snack",
    "WATER":"Water",
    "GUN":"Gun"
}
print(f"You Selected {dictionary[myChoice]} and computer Was selected {dictionary[computerChoice]} ")


if computerChoice == myChoice:
    print("It's draw")
else:
    if dictionary[computerChoice] == "Water" and dictionary[myChoice] == "Snack" :
        print("So you win!")
    elif dictionary[computerChoice] == "Water" and dictionary[myChoice] == "Gun":
        print("So you lose!")
    elif dictionary[computerChoice] == "Snack" and dictionary[myChoice] == "Water" :
        print("So you lose!")
    elif dictionary[computerChoice] == "Snack" and dictionary[myChoice] == "Gun":
        print("So you Win!")
    elif dictionary[computerChoice] == "Gun" and dictionary[myChoice] == "Snack" :
        print("So you lose!")
    elif dictionary[computerChoice] == "Gun" and dictionary[myChoice] == "Water":
        print("So you Win!")
    else:
        print("Something went wrong!")