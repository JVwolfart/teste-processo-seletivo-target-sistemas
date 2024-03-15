"""
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
"""
while True:
    n = input("Digite um número (ou ZZZ para sair): ")
    if n.upper() == "ZZZ":
        print("Saída do programa")
        break
    try:
        n = int(n)
        fib1 = 0
        fib2 = 1
    except ValueError:
        print("ERRO! Valor informado precisa ser um número (ou ZZZ para sair)")
    else: 
        if n == 0 or n == 1:
            print(f"O número {n} pertence a sequência de Fibonacci")
        else:
            while True:
                fib3 = fib1 + fib2
                fib1 = fib2
                fib2 = fib3
                if fib3 == n:
                    print(f"O número {n} pertence a sequência de Fibonacci")
                    break
                
                if fib3 > n:
                    print(f"O número {n} NÃO pertence a sequência de Fibonacci")
                    break
    