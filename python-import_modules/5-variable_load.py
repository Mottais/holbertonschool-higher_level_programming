#!/usr/bin/python3

if __name__ == "__main__":
    import variable_load_5
    for value in dir(variable_load_5):
        if value == "a":
            from variable_load_5 import a
            print(a)
