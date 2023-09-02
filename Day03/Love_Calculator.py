Her = input("Enter her name : ")
Him = input("Enter his name : ")
Together = Her + Him
t = Together.lower().count("t")
r = Together.lower().count("r")
u = Together.lower().count("u")
e = Together.lower().count("e")
true = t + r + u + e
l = Together.lower().count("l")
o = Together.lower().count("o")
v = Together.lower().count("v")
e = Together.lower().count("e")
love = l + o + v + e
love_score = int(str(true) + str(love))
if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score},you go together like oke and mentos.")
elif 40 < love_score < 50:
    print(f"your score is{love_score},you are alright together.")
else:
    print(f"your score is {love_score}")
