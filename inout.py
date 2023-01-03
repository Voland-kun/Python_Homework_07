from fractions import Fraction
import sys

def get_number():
    user_number = input('Введите число: ')
    try:
        user_number = Fraction(user_number)
        return user_number

    except ValueError:
        try: 
            isinstance(complex(user_number), complex)
            return complex(user_number)
        except ValueError:
            print('Неверные данные, завершение работы')
            sys.exit(0)


def get_operator():
    oper = input('Введите оператор: ')
    return oper