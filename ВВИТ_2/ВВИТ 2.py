#1
def greet(name:str) -> str:
    return f'Hello, {name}'


def square(number: int | float) -> int | float:
    return number * number


def max_of_two(x: int | float, y: int | float) -> int | float:
    return max(x,y)


#2
def describe_person(name: str, age: int = 30) -> str:
    return f'Я {name}, мне {age}'


#3
def is_prime(number: int) -> bool:
    a = []
    for i in range(1, number + 1):
        if number % i == 0:
            a.append(i)
    return len(a) == 2


print(describe_person('Fdu', 15))
print(is_prime(10))