
#  Copyright (C) 2018 Craig McIntyre


import click
from textwrap import wrap
from num2words import num2words

@click.command()
@click.argument('component')
@click.argument('code')
def main(component, code):
    if component.upper() == 'R':
        parse_resistor(code)
    elif component.upper() == 'C':
        parse_capacitor(code)
    else:
        print("Select (R)esistor or (C)apacitor.")


def parse_resistor(code):
    colors = {'bla': 0,
              'bro': 1,
              'red': 2,
              'ora': 3,
              'yel': 4,
              'gre': 5,
              'blu': 6,
              'vio': 7,
              'gra': 8,
              'whi': 9}
    if len(code) % 12 != 0:
        print("use four three letter codes")
        return
    code_list = wrap(code, 3)

    num1, num2, num3, num4 = code_list
    num1 = colors[num1]
    num2 = colors[num2]
    num3 = colors[num3]
    num4 = colors[num4]

    base = str(num1) + str(num2)
    value = int(base) * (10**num3)
    clean_value = format(value, ',')
    length = len(str(value))
    if length > 3 and length < 7:
        val = value / 1000
        strung = str(val)
        if strung.endswith(".0"):
            val = strung[:-2]
        print("{}K".format(val))
    elif length > 6:
        val = value / 1000000
        strung = str(val)
        if strung.endswith(".0"):
            val = strung[:-2]
            
        print("{}M".format(val))
    else:
        print("{}".format(value, ','))
    worded_value = num2words(value)
    print("{} ({}) ohms".format(worded_value, clean_value))


def parse_capacitor(code):
    return


if __name__ == "__main__":
    main()
