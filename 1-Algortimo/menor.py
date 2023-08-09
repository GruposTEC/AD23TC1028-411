'''
recibo moneda1;
recibo moneda2;
recibo moneda3;
if moneda1 es menor a moneda2
{
  menor es moneda1;
}
else
{
  menor es moneda2;
}
if moneda3 es menor a la menor
{
  menor es moneda3:
}
fin;
imprimir menor
'''

mon1=10
mon2=5
mon3=20

if mon1 < mon2:
    menor = mon1
else:
    menor = mon2
if mon3 < menor:
    menor = mon3

print(menor)