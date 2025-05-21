while True:
    
    num1 = input("Número 1: ")
    num2 = input("Número 2: ")
    op = input("Operador (+ - / *): ")
   
    r=0

    num1f = 0
    num2f = 0

    try:
        num1f = float(num1)
        num2f = float(num2)
        numerov = True
    except:
        numerov = None 
    
    if numerov is None:
        print("Um ou mais números digitados são inválidos")
        continue
    
    opv = '+-/*'

    if op not in opv:
        print("Operador inválido")
    
    if len(op) > 1:
        print("Apenas um operador")
        continue

    if op == "+":
        r=num1f+num2f
        print(r)
    
    elif op == "-":
        r=num1f-num2f
        print(r)

    elif op == "/":
        r=num1f/num2f
        print(r)
    
    elif op == "*":
        r=num1f*num2f
        print(r)

    sair = input("quer sair? [s]im [n]ão ").lower().startswith('s')

    if sair is True:
        break