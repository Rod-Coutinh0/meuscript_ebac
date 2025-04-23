print("Calculadora simples, operações disponiveis adição (+), subtração (-), multiplicação (*) e divisão (/)")

first_num = int(input("digite o primerio número: "))

oper = input("Digite uma operação (+, -, /, *): ")
while oper not in ("+", "-", "/", "*"):
    print("Escolha inválida! Tente novamente.")
    oper = input("Digite uma operação (+, -, /, *): ")
    
second_num = int(input("digite o segundo número: "))

if oper == "+":
  result = first_num + second_num
  print("O resultado é:", result)
elif oper == "-":
  result = first_num - second_num
  print("O resultado é:", result)
elif oper == "*":
  result = first_num * second_num
  print("O resultado é:", result)
elif oper == "/":
  result = first_num / second_num
  print("O resultado é:", result)
