print("LOVE CALCULATOR")

name1=input("What is your name?\n")
name2=input("what is the name of your partner\n")

t=name1.count("t")
r=name1.count("r")
u=name1.count("u")
e=name1.count("e")

true=t+r+u+e

l=name2.count("l")
o=name2.count("o")
v=name2.count("v")
e=name2.count("e")

love=l+o+v+e
yourlovecore=str(love)+str(true)
print(yourlovecore)

if yourlovecore<10 or yourlovecore>90:
    print(f"Your score is {yourlovecore} and you go like coke and mentos")
elif yourlovecore>=40 or yourlovecore<=50:
    print(f"Your score is {yourlovecore} ,youralright together")
else:
    print(f"your score is{yourlovecore}")

