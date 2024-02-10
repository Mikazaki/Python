from tkinter import *

window = Tk()
window.title("Unit Converter")
window.minsize(width=225, height=100)
window.config(padx=20, pady=20)

equal = Label(text="is equal to", font=('Arial', 11, "normal"))
equal.grid(column=0, row=2)
output = Label(text="0", font=('Arial', 11, "bold"))
output.grid(column=1, row=2)
output.config(padx=5, pady=5)

menu1 = StringVar()
menu1.set("Select Any Unit")

drop1 = OptionMenu(window, menu1, "Millimeter", "Decimeter", "Centimeter", "Meter", "Kilometer", "Inch", "Feet",
                   "Yard", "Miles", "Light Year")
drop1.config(font=('Arial', 9, "normal"))
drop1.grid(column=3, row=1)

menu2 = StringVar()
menu2.set("Select Any Unit")

drop2 = OptionMenu(window, menu2, "Millimeter", "Decimeter", "Centimeter", "Meter", "Kilometer", "Inch", "Feet",
                   "Yard", "Miles", "Light Year")
drop2.config(font=('Arial', 9, "normal"))
drop2.grid(column=3, row=2)

cat = StringVar()
cat.set("Select Any Category")

drop = OptionMenu(window, cat, "Length")
drop.config(font=('Arial', 9, "normal"))
drop.grid(column=1, row=0)


def calculate():
    category = cat.get()
    unit1 = menu1.get()
    unit2 = menu2.get()
    value = float(input.get())

    conversion_factors = {
        "Millimeter": 0.001,
        "Decimeter": 0.1,
        "Centimeter": 0.01,
        "Meter": 1.0,
        "Kilometer": 1000.0,
        "Inch": 0.0254,
        "Feet": 0.3048,
        "Yard": 0.9144,
        "Miles": 1609.34,
        "Light Year": 9.461e+15,
    }

    if category == "Length":

        if unit1 in conversion_factors and unit2 in conversion_factors:
            factor1 = conversion_factors[unit1]
            factor2 = conversion_factors[unit2]
            result = value * (factor1 / factor2)
            output.config(text=round(result, 9))


button = Button(text='Calculate', command=calculate)

button.grid(column=1, row=3)

input = Entry(width=10)

input.grid(column=1, row=1)

window.mainloop()
