#Write your code below this line 👇
print("Welcome to the Tip Calculator")
m = input("What was the Total Bill?\n$")
t = input("What percentage of tip would you like to give? 10, 12, or 15\n")
s = input("How many people to split the bill?\n")
x = float(m)
y = (int(t)/100) + 1
z = (x*y)/int(s)
f = "{:.2f}".format(z)
print(f"Each person should pay: ${f}")