def main():
    #escribe tu código abajo de esta línea
    import os
    os.system("clear")
    a = float(input("Valor para 'a'"))
    b = float(input("Valor para 'b'"))
    c = float(input("Valor para 'c'"))
    d = float(input("Valor para 'd'"))
    e = float(input("Valor para 'e'"))
    f = float(input("Valor para 'f'"))

    if (a * e - b * d) != 0 :
        x = (c * e - b * f) / (a * e - b * d)
        y = (a * f - c * d) / (a * e - b * d)
        print (f"La solucion al sistema es x= {x} e y= {y}")
        #print ("La solucion al sistema es x= %d e y= %d" %(x, y)) #sin decimales
    else :
        if (d / a) * c == f :
            print ("El sistema tiene infinitas soluciones")
        else:
            print ("El sistema no tiene solución")

if __name__=='__main__':
    main()
