from utilities.clear_console import clear

def apply_operator(f_num: int, s_num: int, operator: str) -> int | float | None:
    if operator == "+":
        return f_num + s_num
    elif operator == "-":
        return f_num - s_num
    elif operator == "*":
        return f_num * s_num
    elif operator == "/":
        return f_num / s_num
    else:
        return None

def calculator():
    end = "y"

    while end == "y":
        f_num = int(input("What's the first number?: "))

        continue_calc = "y"
        print("+\n-\n*\n/\n")

        while continue_calc == "y":
            operator = input("Pick an operator: ")
            s_num = int(input("What's the next number?: "))
            result = apply_operator(f_num, s_num, operator)
            print(f"{f_num}{operator}{s_num} = {result}")
            f_num = result

            continue_calc = input(f"Type 'y' to continue calculating with "
                                  f"{f_num} or type 'n' to start a new calculation: ")

        end = input("Type 'y' if you want to end the calculation else 'n': ")
        clear()


calculator()

