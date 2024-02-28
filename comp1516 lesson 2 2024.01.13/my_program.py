# author: jason wilder

import functions
import mathematics


def main():
    functions.greet_user()
    # print(functions.greet_user())  # None
    functions.say_hi_to_user("tiger woods")
    functions.say_hi_to_user("jason")
    print(1 + mathematics.multiply(5.67, 6))
    print(mathematics.add(1, 2, 3))
    print(mathematics.add(100, 2000, 3))


if __name__ == '__main__':
    print('welcome to my program')
    main()
