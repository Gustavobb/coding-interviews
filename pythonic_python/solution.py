def print_indices_and_elements(elements) -> None:
    for count, value in enumerate(elements):
        print(count, value)

def get_even_numbers_between(start: int, end: int) -> list[int]:
    return [n for n in range(start, end + 1) if n % 2 == 0]

def get_char_set_from(s: str) -> set[str]:
    return {c for c in s}

def get_perfect_squares_between(start: int, end: int) -> dict[int,int]:
    return {n : n ** (0.5) for n in range(start, end + 1) if int(n ** (0.5) + 0.5) ** 2 == n}

def filter_even_from(numbers: list[int]) -> list[int]:
    return [n for n in numbers if n % 2 == 0]

def get_number_or_minus_one(n: int) -> int:
    return n if n % 2 == 0 else -1

def transform_multiples_of_5(numbers: list[int]) -> list[int]:
    return [n if n % 2 == 0 else -1 for n in numbers if n % 5 == 0]

def str_lengths(strings: list[str]) -> list[int]:
    return [len(s) for s in strings]

def get_fibonacci_type(version: int) -> str:
    return "<class 'generator'>" if version == 1 else "<class 'list'>"

def difference_between_fibonacci1_and_fibonacci2() -> str:
    return """O generator produz um item por vez, e apenas de acordo com a demanda, caso não 
    houver ele não gera os números. Ja em uma list comprehension, é alocada uma quantidade de 
    memória para aquele return da função poi ele retorna de uma só vez. Portanto podemos dizer 
    que o generator é mais eficiente em questões de memória. Um ponto negativo pode ser o fato
    de as vezes ser necessário reservar um espaço na memória para uso. Além de generators serem 
    menos legíveis que list comprehension"""

class SkipIterator:
    def __init__(self, elements):
        self.elements = elements
        self.index = 0
    
    def __next__(self):
        if self.index >= len(self.elements):
            raise StopIteration
            
        self.index += 2
        return self.elements[self.index - 2]
    
    def __iter__(self):
        return self

def my_avg(e1: float, e2: float, *others: tuple[float]) -> float:
    mean = e1 + e2

    for n in others:
        mean += n
    
    return mean / (len(others) + 2)


def keys_with_different_value() -> list[int]:
    a = dict(zip(range(10), range(10)))
    b = dict(zip(range(5, 15), range(15, 25)))
    c = {**a, **b}
    d = {**b, **a}

    return sorted([n for n in c if c[n] != d[n]])

def print_out_in(*numbers) -> None:
    while len(numbers) > 1:
        n1, n2 = numbers[0], numbers[-1]
        numbers = numbers[1:-1]
        print(n1, n2)

    if numbers:
        print(numbers[0])

def append_range(start: int, end: int, step: int=1, to: list[int]=None):
    if to is None:
        to = []

    for i in range(start, end, step):
        to.append(i)
    return to

global_var = 10

def global_var_func1(n: int):
    for i in range(n):
        print(global_var)

def global_var_func2(n: int):
    global global_var
    for i in range(n):
        global_var += i
        print(global_var)

def value_is_None(value):
    return value is None