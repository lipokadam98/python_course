import calculator_art

print(calculator_art.logo)


class CalculatedNum:
    num1: float
    num2: float
    result: float
    operator: str

    def __init__(self, num1: float, num2: float, calculated_num: float, operator: str):
        self.num1 = num1
        self.num2 = num2
        self.result = calculated_num
        self.operator = operator


def calculate(starting_num: float, is_new_calc: bool) -> CalculatedNum:
    if is_new_calc:
        num1 = float(input("What is the first number? "))
    else:
        num1 = starting_num
        starting_num = 0
    print('+ \n'
          '- \n'
          '* \n'
          '/')
    operation = input("Pick an operation: ")
    num2 = float(input("What is the second number? "))

    match operation:
        case '+':
            starting_num += (num1 + num2)
        case '-':
            starting_num += (num1 - num2)
        case '*':
            starting_num += (num1 * num2)
        case '/':
            starting_num += (num1 / num2)

    return CalculatedNum(num1=num1, num2=num2, calculated_num=starting_num, operator=operation)


def calculate_menu(calculated_num: CalculatedNum):
    print(f'{calculated_num.num1} {calculated_num.operator} {calculated_num.num2} = {calculated_num.result}')
    decision = input(
        f"Type 'y' to continue calculation with {calculated_num.result}, or type 'n' to start a new calculation.")

    if decision == 'y':
        calculate_menu(calculate(calculated_num.result, False))
    else:
        calculate_menu(calculate(0, True))


calculate_menu(calculate(0, True))
