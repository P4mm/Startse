num = int(input("Digite n:"))
rep = 1
factorial = num
while rep < num :
    factorial = factorial * (num - rep)
    rep = rep + 1
print("O fatorial de", num, "é:", factorial)
