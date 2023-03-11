num = int(input("Informe um número: "))

fibonacci = [0, 1]
while fibonacci[-1] < num:
    next_fibonacci = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(next_fibonacci)

if num in fibonacci:
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")

# Explicação:

# Primeiro, solicitamos ao usuário que informe um número e o armazenamos na variável num.
# Em seguida, definimos uma lista fibonacci com os dois primeiros números da sequência.
# Em um loop while, continuamos a adicionar o próximo número da sequência até que o último número adicionado seja maior ou igual ao número informado pelo usuário.
# Por fim, verificamos se o número informado está na lista fibonacci e exibimos uma mensagem apropriada.