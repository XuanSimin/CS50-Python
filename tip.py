def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dollar = d.replace("$", "")
    new_dollar = float(dollar)
    return new_dollar


def percent_to_float(p):
    percentage = p.replace("%", "")
    new_percentage = float(percentage)/100
    return new_percentage


main()
