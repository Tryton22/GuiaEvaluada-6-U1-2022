from garden import Garden

def menu():

    # Pasos antes de que todo se muestre en pantalla.
    # Plantas correspondientes a cada niño.
    Alicia = Garden()._alicia
    Andres = Garden()._andres
    Belen = Garden()._belen
    David = Garden()._david
    Eva = Garden()._eva
    Jose = Garden()._jose
    Larry = Garden()._larry
    Lucia = Garden()._lucia
    Marit = Garden()._marit
    Pepito = Garden()._pepito
    Rocio = Garden()._rocio
    Sergio = Garden()._sergio
    
    # Listas que sirven de almacenamiento para vasos y mostrarlos en pantalla.
    lista_A = [Alicia[1][0][0], Alicia[1][1][0], Andres[1][0][0], Andres[1][1][0], Belen[1][0][0], Belen[1][1][0],
               David[1][0][0], David[1][1][0], Eva[1][0][0][0], Eva[1][1][0], Jose[1][0][0], Jose[1][1][0],
               Larry[1][0][0], Larry[1][1][0], Lucia[1][0][0], Lucia[1][1][0], Marit[1][0][0], Marit[1][1][0],
               Pepito[1][0][0],Pepito[1][1][0], Rocio[1][0][0], Rocio[1][1][0], Sergio[1][0][0], Sergio[1][1][0]]

    lista_B = [Alicia[1][2][0], Alicia[1][3][0], Andres[1][2][0], Andres[1][3][0], Belen[1][2][0], Belen[1][3][0],
               David[1][2][0], David[1][3][0], Eva[1][2][0], Eva[1][3][0], Jose[1][2][0], Jose[1][3][0],
               Larry[1][2][0], Larry[1][3][0], Lucia[1][2][0], Lucia[1][3][0], Marit[1][2][0], Marit[1][3][0],
               Pepito[1][2][0],Pepito[1][3][0], Rocio[1][2][0], Rocio[1][3][0], Sergio[1][2][0], Sergio[1][3][0]]

    
    # Lo que se va a imprimir en pantalla.
    print("\n[ventana][ventana][ventana]")
    print(*lista_A)
    print(*lista_B)
    print(" ")

    choice = -1
    print("Alumnos del Curso\n",
            "1. Alicia         ",
            "2. Andrés\n",
            "3. Belen          ",
            "4. David\n",
            "5. Eva            ",
            "6. José\n",
            "7. Larry          ",
            "8. Lucia\n",
            "9. Marit          ",
            "10. Pepito\n",
            "11. Rocio         ",
            "12. Sergio\n")
    print("Pulse 0 para salir del programa\n")

    try:
        choice = int(input("Ingrese el número correspondiente al alumno del cual quiere saber sus plantas: "))

    except ValueError:
        print("Ingrese un número por favor")
    
    if choice == 0:
        exit()

    if choice == 1:
        print("\nLas plantas de Alicia son:", *Alicia[1])
        menu()

    if choice == 2:
        print("\nLas plantas de Andrés son:", *Andres[1])
        menu()
    
    if choice == 3:
        print("\nLas plantas de Belen son:", *Belen[1])
        menu()

    if choice == 4:
        print("\nLas plantas de David son:", *David[1])
        menu()

    if choice == 5:
        print("\nLas plantas de Eva son:", *Eva[1])
        menu()

    if choice == 6:
        print("\nLas plantas de José son:", *Jose[1])
        menu()

    if choice == 7:
        print("\nLas plantas de Larry son:", *Larry[1])
        menu()

    if choice == 8:
        print("\nLas plantas de Lucia son:", *Lucia[1])
        menu()
        
    if choice == 9:
        print("\nLas plantas de Marit son:", *Marit[1])
        menu()

    if choice == 10:
        print("\nLas plantas de Pepito son:", *Pepito[1])
        menu()

    if choice == 11:
        print("\nLas plantas de Rocío son:", *Rocio[1])
        menu()

    if choice == 12:
        print("\nLas plantas de Sergio son:", *Sergio[1])
        menu()

    else:
        print("\nIngrese un número válido")
        menu()

if __name__ == "__main__":

   menu()