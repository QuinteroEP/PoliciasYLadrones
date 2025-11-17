# Policias y Ladrones

## Herramientas
<ol>
    <li>Python</li>
    <li>Tkinter</li>
</ol>

## Explicacion del algoritmo
Cada policia tiene almacenado un valor que representa la distancia euclidiana desde su posicion hasta el ladron. En cada turno de los policias se recalcula su distancia, se toma el policia más cercano y se vuelve a calcular la distancia para el caso donde se mueve hacia la derecha y a la izquierda, el movimiento realizado es el que minimize la distancia del policia al ladron. En caso de que un policia este en la misma fila que el ladron, osea, ya no le es posible capturarlo, se le asigna un valor maximo a su distancia para que no sea tomado en cuenta.

## Universidad Javeriana - Análisis de Algoritmos 2025
<i>Pablo Quintero</i>
