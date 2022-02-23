def check_if_it_is_armstrong_number(val: int) -> bool:
    digits = [int(_) for _ in str(val)]
    number_of_digits = len(str(val))
    counter = 0
    for _ in digits:
        counter += _**number_of_digits
    return (counter == val)

def list_armstrong_numbers(number_input: int):
    number_int = isinstance(number_input, int)
    if number_input > 0 and number_int:
        numbers_list_armstrong = list([])
        for i in range(1, number_input):
            check_if_it_is_armstrong_number(i)
            if check_if_it_is_armstrong_number(i):
                numbers_list_armstrong.append(i)
        if len(numbers_list_armstrong) == 0:
            print('Não há números de Armstrong nesse intervalo')
        else:
            print(f'Os números de Armstrong menores que {number_input} são: {numbers_list_armstrong}')
    else:
        print(f'O número {number_input} é inválido')


def input_insertion_prime_number_for_list(value: int):
    list_armstrong_numbers(value)


# Caso prefira adicionar seus valores manualmente, comente a linha 78 e descomente a linha 77

def test_list_armstrong_number():
    inputs = []
    #inputs = [2, 3, 5, 7, 11, 13, 9.8, 0.3, -98, 4, 6, 8, 10, 999, 99999]
    int_list = list(map(int, inputs))
    if len(int_list) > 0:
        for i in inputs:
            list_armstrong_numbers(i)
        print("Fim do teste")
    else:
        number = int(input("Digite um número:"))
        input_insertion_prime_number_for_list(number)


test_list_armstrong_number()
