from Clase import Opcion
import random
a="Piedra"
b="Papel"
c="Tijera"
d="Lagarto"
e="Spock"

spock = Opcion(e, [c, a], [b,d])
piedra = Opcion(a, [d, c], [e,b])
papel = Opcion(b, [a, e], [d,c])
tijera = Opcion(c, [b, d], [e,a])
lagarto = Opcion(d, [e, b], [a,c])

print("Como desea jugar\n")
print("1.- Contra Persona\n")
print("2.- Contra la Maquina\n")
modoJuego = input('Escoja una opcion: ')
while True:
    if modoJuego == '1':
        print("Escoja la opción:\n")
        print("a. Piedra\n")
        print("b. Papel\n")
        print("c. Tijera\n")
        print("d. Lagarto\n")
        print("e. Spock\n")
        while True:
            turno_uno=input('¿Qué eliges, jugador 1?\n')
            if turno_uno=="a":
                jugador1=piedra
                break
            elif turno_uno=="b":
                jugador1=papel
                break
            elif turno_uno=="c":
                jugador1=tijera
                break
            elif turno_uno=="d":
                jugador1=lagarto
                break
            elif turno_uno=="e":
                jugador1=spock
                break
            else:
                print ("Escoge bien")
        while True:
            turno_dos=input('¿Qué eliges, jugador 2?\n')
            if turno_dos=="a":
                print("Jugador1: "+jugador1.comprobar_Gana(a))
                break
            elif turno_dos=="b":
                print("Jugador1: "+jugador1.comprobar_Gana(b))
                break
            elif turno_dos=="c":
                print("Jugador1: "+jugador1.comprobar_Gana(c))
                break
            elif turno_dos=="d":
                print("Jugador1: "+jugador1.comprobar_Gana(d))
                break
            elif turno_dos=="e":
                print("Jugador1: "+jugador1.comprobar_Gana(e))
                break
            else:
                print ("Escoge bien")
        break
    elif modoJuego == '2':
        print("Escoja la opción:\n")
        print("a. Piedra\n")
        print("b. Papel\n")
        print("c. Tijera\n")
        print("d. Lagarto\n")
        print("e. Spock\n")
        while True:
            turno_uno=input('¿Qué eliges, jugador 1?\n')
            if turno_uno=="a":
                jugador1=piedra
                break
            elif turno_uno=="b":
                jugador1=papel
                break
            elif turno_uno=="c":
                jugador1=tijera
                break
            elif turno_uno=="d":
                jugador1=lagarto
                break
            elif turno_uno=="e":
                jugador1=spock
                break
            else:
                print ("Escoge bien")
        turno_maquina = random.randint(1,5)
        if turno_maquina==1:
            jugadormaquina=piedra
        elif turno_maquina==2:
            jugadormaquina=papel
        elif turno_maquina==3:
            jugadormaquina=tijera
        elif turno_maquina==4:
            jugadormaquina=lagarto
        elif turno_maquina==5:
            jugadormaquina=spock
        print("Jugador: " + jugador1.atributo)
        print("Maquina: " + jugadormaquina.atributo)
        print("Jugador1: "+jugador1.comprobar_Gana(jugadormaquina.atributo))
        break
    else:
        print("No")
        modoJuego = input('\nEscoja una opcion valida: ')
        