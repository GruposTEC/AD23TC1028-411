print (__name__)

def mayor_a_tres(num1,num2,num3):
    if num1 > num2:
        menor = num1
    else:
        menor = num2
    if num3 > menor :
        menor = num3 
    
    return menor

def main():
    res = mayor_a_tres(10,1,5)
    print(res)
    print(mayor_a_tres(4,12,78))

if __name__ == "__main__":
    print(main())