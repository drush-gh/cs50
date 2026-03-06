
order = 0
menu ={
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
        }

while True:
    try:
        item = input("Item: ").title()
        if item in menu:
            order += menu[item]
            # docs.python.org/3/tutorial/floatingpoint.html#tut-fp-issues
            # format(float, '.2f') will give 2 digits after the point
            # otherwise the output will only give one 0 after . even with round(output, 2)
            output = format(order, '.2f')
            print(f"Total: ${output}")
        continue
    except EOFError:
        print(end = "\n")
        break
    except KeyError:
        pass
    except ValueError:
        pass



