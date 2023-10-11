print (__name__)
""" 
function menor()
{
  if n1 < n2
  {
    menor = n1;
  }
  else
  {
    menor = n2;
  }
  if n3 < menor
  {
    menor = n3;
  }
  return  menor;
}
inicio;
call menor(n1,n2,n3);
fin;
"""
def menor_a_tres(num1,num2,num3):
    """Encuentra el menor de tres valores

    Args:
        num1 (int): Priemr valor
        num2 (int): Segundo valor
        num3 (int): Tercer valor

    Returns:
        int: el emnor de tres
    """
    if num1 < num2:
        menor = num1
    else:
        menor = num2
    if num3 < menor :
        menor = num3 
    
    return menor

def main():
    res = menor_a_tres(10,1,5)
    print(res)
    print(menor_a_tres(4,12,78))

if __name__ == "__main__":
    print(main())