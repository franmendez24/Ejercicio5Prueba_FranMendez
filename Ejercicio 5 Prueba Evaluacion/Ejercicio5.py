#Fran Mendez Gonzalez
#12/11/2026
#Una máquina expendedora necesita calcular el cambio que debe devolver. Escribe un programa que pida el importe de la
#compra y el dinero entregado por el cliente (ambos en euros, con decimales) y muestre:
#El cambio total que hay que devolver.
#El desglose del cambio con el menor número posible de billetes y monedas, usando billetes de 20 €, 10 € y 5 € y
# monedas de 2 €, 1 €, 50 cént., 20 cént., 10 cént. y 5 cént.
#Puedes suponer que el dinero entregado es siempre mayor o igual que el importe y que todas las cantidades
#son múltiplos de 5 céntimos.


# input() devuelve texto, float() lo convierte a número decimal.
# Se multiplica por 100 para pasar de euros a céntimos
importe = round(float(input("Importe de la compra €: ")) * 100)
entregado = round(float(input("Dinero entregado €: ")) * 100)

# Cambio total en céntimos (lo que entrega el cliente menos lo que cuesta).
cambio_total = entregado - importe
cambio = cambio_total

#   // dice cuántas piezas caben
#   %  dice cuánto cambio queda por repartir

# Billetes de 20 € (2000 céntimos)
billetes20 = cambio // 2000
cambio = cambio % 2000

# Billetes de 10 € (1000 céntimos)
billetes10 = cambio // 1000
cambio = cambio % 1000

# Billetes de 5 € (500 céntimos)
billetes5 = cambio // 500
cambio = cambio % 500

# Monedas de 2 € (200 céntimos)
monedas2 = cambio // 200
cambio = cambio % 200

# Monedas de 1 € (100 céntimos)
monedas1 = cambio // 100
cambio = cambio % 100

# Monedas de 50 céntimos
monedas50 = cambio // 50
cambio = cambio % 50

# Monedas de 20 céntimos
monedas20 = cambio // 20
cambio = cambio % 20

# Monedas de 10 céntimos
monedas10 = cambio // 10
cambio = cambio % 10

# Monedas de 5 céntimos
monedas5 = cambio // 5
cambio = cambio % 5

# Se divide entre 100 para volver a mostrar el cambio en euros.
print("Cambio:", cambio_total / 100, "€")

# Desglose de billetes y monedas
print("Billetes de 20 €:", billetes20)
print("Billetes de 10 €:", billetes10)
print("Billetes de 5 €:", billetes5)
print("Monedas de 2 €:", monedas2)
print("Monedas de 1 €:", monedas1)
print("Monedas de 50 cént.:", monedas50)
print("Monedas de 20 cént.:", monedas20)
print("Monedas de 10 cént.:", monedas10)
print("Monedas de 5 cént.:", monedas5)


