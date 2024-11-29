import turtle

# Calcular a sequência de Fibonacci
x = 1
y = 1
sequ_fibonacci = [x, y]  # Iniciando com os dois primeiros valores

quant = 15
for _ in range(quant - 2):  # Já temos 2 valores, então subtrai 2
    z = x + y
    sequ_fibonacci.append(z)
    x, y = y, z

qant= len(sequ_fibonacci)

print(qant)
print("Sequência de Fibonacci:", sequ_fibonacci)

# Configurar o Turtle
turtle.speed(80)
turtle.penup()  # Levanta a caneta para reposicionar no início
turtle.goto(0, 0)  # Centraliza um pouco mais no início
turtle.pendown()

# Desenhar os quadrados
for tamanho in sequ_fibonacci:
    for _ in range(5):
        turtle.forward(tamanho)  # Ajuste de escala para visualização
        turtle.right(90)
    turtle.forward(tamanho)  # Mover para o próximo quadrado

turtle.right(84)

    
rep = (0)

turtle.penup()
turtle.goto(0,0)
turtle.pendown()

for i in range (qant):
    for i in range(15):
        contador =0
        
        turtle.forward(0.1007*(sequ_fibonacci[rep]))
        turtle.right(6)
    rep +=1

turtle.right(1)
turtle.forward(59)
turtle.right(0.5)
turtle.forward(59)
turtle.done()
