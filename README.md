# EloCalculator
Este Script sirve para realizar los calculos de ranking interno de un club usando archivos de texto que se obtienen como output de los torneos hechos con el *Swiss Manager*, genera un reporte con las variaciones de elo de los jugadores, el ranking obtenido despues del torneo y para los jugadores que no tienen ranking un pequeño reporte de su actuación.

### Ingresar los jugadores
Es importante que a la hora de ingresar los jugadores al torneo dentro del Swiss Manager el ranking a ser computado esté en la pestaña "Elo.nat"

### Terminado el torneo
Para obtener el archivo de output del Swiss Manager que vamos a utilizar tenemos que:
1) Ir a la pestaña *Listados -> cuadro cruzado por clasificación*
2) En esta ventana vamos al botón inferior *Menu*
3) Pestaña *Archivos de texto*
4) Botón Generar listado en: *Archivo de texto*

Este archivo debe ser guardado en el mismo directorio (o carpeta) en el que se encuentra el script (ranking.py)

### Ejecutar
Al ejecutar ranking.py el primer menu nos da la opción de computar un torneo suizo o un torneo americano (Round Robin), es importante elegir el correcto.

Luego nos pide el nombre del archivo del input (el que generamos al terminar el torneo)

A continuación nos pide el nombre que le queremos dar al archivo que contendrá el reporte del torneo

Y por último tenemos que ingresar el factor K de cada jugador

Al terminar vamos a tener un archivo con un reporte para cada jugador/a
