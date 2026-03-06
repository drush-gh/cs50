grocery = {}

while True:
    try:
        item = input().upper()
        if item in grocery:
            grocery[item] += 1
        else:
            # list and sorted from
            # https://docs.python.org/3/tutorial/datastructures.html#dictionaries
            list(grocery).append(item)
            grocery[item] = 1
    except KeyError:
        pass
    except EOFError:
        print(end = "\n")
        for item in sorted(grocery):
            print(f"{grocery[item]} {item}")
        break
