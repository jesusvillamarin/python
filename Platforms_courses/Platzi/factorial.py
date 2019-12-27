
def calculate_factorial(number): 
    if number == 1: 
        return 1;
    
    return number * calculate_factorial(number-1)


if __name__ == '__main__':
    number = int(input("Escribe un número a multiplicar: "))
    result = calculate_factorial(number)
    print(f'El resultado del factorial para el número {number} es: {result}')