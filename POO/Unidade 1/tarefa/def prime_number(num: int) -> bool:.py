def perfect_number(num: int) -> bool:
    div = list([])
    for i in range(1, num):
        if (num % i) == 0:
            div.append(i)
    sum_div = sum(div)
    return (num == sum_div)


def list_perfect_numbers(x: int):
    number_int = isinstance(x, int)
    if x >= 2 and number_int:
        numbers_list = list([])
        for i in range(2, x):
            perfect_number(i)
            if perfect_number(i):
                numbers_list.append(i)
        if len(numbers_list) == 0:
            print('Não há números perfeitos menores que 6')
        else:
            print(f'Os números perfeitos menores que {x} são: {numbers_list}')
    else:
        print(f'O número {x} é inválido')


def input_insertion_perfect_number_for_list(value: int):
    list_perfect_numbers(value)


# Caso prefira adicionar seus valores manualmente, comente a linha 78 e descomente a linha 77

def test_list_perfect_number():
    #inputs = []
    inputs = [2, 3, 5, 7, 11, 13, 9.8, 0.3, -98, 4, 6, 8, 10, 496, 8128]
    int_list = list(map(int, inputs))
    if len(int_list) > 0:
        for i in inputs:
            print(f'Digite um número: {i}')
            list_perfect_numbers(i)
        print("Fim do teste")
    else:
        number = int(input("Digite um número:"))
        if number >= 5000:
            print("Isso pode demorar um pouco :/")
            print("-----------------------------")
        input_insertion_perfect_number_for_list(number)


test_list_perfect_number()
