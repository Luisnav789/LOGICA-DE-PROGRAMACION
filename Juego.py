from Clase import Opcion
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