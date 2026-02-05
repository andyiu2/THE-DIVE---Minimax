
<img width="560" height="25" alt="image" src="https://user-images.githubusercontent.com/74038190/212744287-14f66c13-5458-40dc-9244-8ff533fc8f4a.gif" />

# Gato vs Ratón 🐱🐭

Juego interactivo en Python donde controlas al **gato** y el **ratón** se mueve usando **inteligencia artificial** con el algoritmo **Minimax**. El objetivo del juego es atrapar al ratón antes de que se acaben tus turnos.  

---

## Contenido del Proyecto

- `main.py` – Código principal del juego.
- Clases para los jugadores (**Gato** y **Ratón**).  
- Funciones de creación y actualización del tablero.  
- Lógica de movimientos y validación de posiciones.  
- Minimax para que el ratón tome decisiones estratégicas.  

---

## Cómo jugar

1. Ejecuta el juego:  
   ```bash
   python main.py

1.  Selecciona una opción:

    -   `1` → Jugar como el Gato.

    -   `0` → Salir del juego.

2.  Mueve al gato usando las teclas:

    -   `w` → Arriba

    -   `s` → Abajo

    -   `a` → Izquierda

    -   `d` → Derecha

3.  Cada movimiento reduce los **turnos** restantes.

4.  El juego termina si:

    -   El gato atrapa al ratón → **gana el gato**.

    -   Se acaban los turnos → **gana el ratón**.

* * * * *

Características
---------------

-   **Tablero dinámico**: Se actualiza después de cada movimiento.

-   **Validación de movimientos**: No se puede mover fuera del tablero.

-   **Minimax para el ratón**: El ratón toma decisiones inteligentes para escapar del gato.

-   **Configuración de dificultad**: Ajustable mediante la variable `profundidad` del algoritmo Minimax.

-   **Interfaz de consola simple**: Fácil de jugar y entender.

* * * * *

Dependencias
------------

-   Python 3.x (no requiere librerías externas).

* * * * *

Posibles mejoras
----------------

-   Añadir más niveles de dificultad.

-   Permitir que el usuario juegue como ratón.

-   Implementar gráficos con `pygame` para un tablero visual.

-   Añadir sonidos o animaciones al movimiento de los jugadores.

-   Registrar estadísticas de partidas jugadas, ganadas y perdidas.
