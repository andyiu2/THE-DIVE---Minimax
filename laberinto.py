
tablero = []
direcciones = ["w", "s", "a", "d"]

nro_columnas = 6
nro_filas = 6

class Jugador:
    def __init__(self, nombre, simbolo, fila, columna):
        self.nombre = nombre
        self.simbolo = simbolo
        self.fila = fila
        self.columna = columna
    def __str__(self):
        return self.simbolo
    
    def mover(self, direccion):
        if direccion == "w" and self.fila > 0:
            self.fila -= 1
            return True
        elif direccion == "s" and self.fila < nro_filas - 1:
            self.fila += 1
            return True
        elif direccion == "a" and self.columna > 0:
            self.columna -= 1
            return True
        elif direccion == "d" and self.columna < nro_columnas - 1:
            self.columna += 1
            return True
        else:
            print("Movimiento invalido")
            return False
        
    def posicion(self):
        return(self.fila, self.columna)
    


gato = Jugador("Gato", "🐱", 0, 0)
raton = Jugador("Raton","🐭", 5, 5)

def crear_tablero():
    
    tablero = [["🔳"]* nro_columnas for i in range(nro_filas)]

    if gato.fila == raton.fila and gato.columna == raton.columna:
        tablero[gato.fila][gato.columna] = gato
    else:
        tablero[gato.fila][gato.columna] = gato
        tablero[raton.fila][raton.columna] = raton

    for fila in tablero:
        print(" ".join(str(celda) for celda in fila))
    
    return tablero


def mostrar_posicion_inicial():
    print("Posicion inicial del gato y el raton")
    print("\n")
    crear_tablero()


def aplicar_movimiento(estado, jugador, movimiento):
    pos_gato, pos_raton = estado

    if jugador == "Raton":
        return(pos_gato, movimiento)
    else:
        return(movimiento, pos_raton)
    

def movimientos_posibles(jugador):

    movimientos = []

    direcciones = {
        "w" : (-1, 0),
        "s" : (1, 0),
        "a" : (0, -1),
        "d" : (0, 1)
    }

    for df, dc in direcciones.values():
        nueva_fila = jugador.fila + df
        nueva_columna = jugador.columna + dc

        if 0 <= nueva_fila < nro_filas and 0 <= nueva_columna < nro_columnas:
            movimientos.append((nueva_fila, nueva_columna))

    return movimientos

    
def estado_actual(gato, raton):
    return (gato.posicion(), raton.posicion())


def evaluar_estado(estado):
    pos_gato, pos_raton = estado

    fila_g, col_gato = pos_gato
    fila_r, col_raton = pos_raton

    #DISTANCIA MANHATTAN
    return abs(fila_g - fila_r) + abs(col_gato - col_raton)


def es_estado_final(estado, turnos_restantes):
    pos_gato, pos_raton = estado

    if pos_gato == pos_raton:
        return True, "Gato"
    
    if turnos_restantes == 0:
        return True, "Raton"
    
    return False, None

def minimax_raton(estado, turnos_restantes, profundidad, es_turno_raton):

    final, _ = es_estado_final(estado, turnos_restantes)
    if final or profundidad == 0:
        return evaluar_estado(estado), estado[1]
    
    pos_gato, pos_raton = estado
    
    if es_turno_raton:
        mejor_valor = -float('inf')
        mejor_mov = None
        fila_r, col_r = pos_raton
        raton_copia = Jugador("Raton","🐭", fila_r, col_r)

        for mov in movimientos_posibles(raton_copia):
            nuevo_estado = aplicar_movimiento(estado, "Raton", mov)
            valor, _ = minimax_raton(nuevo_estado, turnos_restantes -1, profundidad -1, False)

            if valor > mejor_valor:
                mejor_valor = valor
                mejor_mov = mov

        return mejor_valor, mejor_mov
    
    else:
        mejor_valor = float('inf')
        mejor_mov = None
        fila_g, col_g = pos_gato
        gato_copia = Jugador("Gato", "🐱", fila_g, col_g)

        for mov in movimientos_posibles(gato_copia):
            nuevo_estado = aplicar_movimiento(estado, "Gato", mov)
            valor, _ = minimax_raton(nuevo_estado, turnos_restantes -1, profundidad -1, True)

            if valor < mejor_valor:
                mejor_valor = valor
                mejor_mov = mov

        return mejor_valor, mejor_mov


def juega_gato():
    
    turnos = 12

    profundidad = 2
    
    print("Atrapa al raton🐭!")

    while turnos > 0:

        
        direccion = input("w: arriba | s: abajo | a: izquierda | d: derecha ")
        print("\n")

        if direccion in direcciones:
            
            if gato.mover(direccion):
                turnos -= 1
                print(f"Quedan {turnos} intentos")
                print("\n")
                
                estado = estado_actual(gato, raton)
                final, ganador = es_estado_final(estado, turnos)
                if final:
                    crear_tablero()
                    if ganador == "Gato":
                        print("Juego terminado, ganaste!!")
                        break
                    else:
                        print("Juego terminado, ganó: ", ganador)
                        break


                _, mejor_mov = minimax_raton(estado, turnos, profundidad, True)
                if mejor_mov:
                    raton.fila, raton.columna = mejor_mov
                    print("\n")
                    crear_tablero()
                print("\n")
                estado = estado_actual(gato, raton)
                final, ganador = es_estado_final(estado, turnos)
                if final:
                    if ganador == "Gato":
                        print("Juego terminado, ganaste!!")
                        break
                    else:
                        print("Juego terminado, ganó: ", ganador)
                        break
        else:
            print("Ingrese un caracter valido, (w: arriba | s: abajo | a: izquierda | d: derecha)")


    else:

        print("Se acabaron los intentos :(")
        


def iniciar_juego():
    mostrar_posicion_inicial()

    while True:
        try:
            decision = int(input("Presione 1 para jugar como el Gato o 0 para salir: "))
        except ValueError:
            print("Opcion invalida, intente de nuevo")
            continue

        if decision == 1:
            juega_gato()
            break
        elif decision == 0:
            print("Saliendo del Juego...")
            break

        else:
            continue




print("\n")
iniciar_juego()
print("\n")

