'''
Elaborar un proyecto Python 01Triangulos donde se lea el tamaño de
  un ángulo en grados y se despliegue :
    • Agudo si es menor a 90°
    • Recto si es igual a 90°
    • Obtuso si es mayor que 90° pero menor que 180°
    • Llano si es igual a 180°
    • Cóncavo si es mayor que 180° pero menor que 360°
'''

def main():
    import os
    os.system("clear")
    angulo = int(input("Tamaño del Ángulo en °: "))
    if angulo < 90:
        print("El angulo es Agudo")
    elif angulo == 90:
        print("El angulo es Recto")
    elif angulo > 90 and angulo < 180:
        print("El angulo es Obtuso")
    elif angulo == 180:
        print("El angulo es Llano")
    elif angulo>180 and angulo<360:
        print("El angulo es Cóncavo")

    
    
if __name__=='__main__':
    main()
