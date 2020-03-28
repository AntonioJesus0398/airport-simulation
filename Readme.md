# Aereopuerto de Barajas

Este documento contiene las instrucciones para ejecutar el simulador y los tests. El informe donde se explica la solución desarrollada se encuentra en la carpeta **doc**.

## Pre-requisitos 📋

python 3.6 o superior

## Ejecutar el simulador

Para llevar a cabo la simulación ejecutar en el directorio raíz:
**python3 main.py [--arg1] [value1] [--arg2] [value2] ...**

### Argumentos adicionales

Usted puede decidir los parámetros de la simulación. A continuación se muestra una lista con los parámetros que se pueden especificar.

| Parámetro | Flag | Tipo | Default |
| :-------- | :------- | :------: | :------: |
| No. de simulaciones | \--nosim | int | 10000 |
| Tiempo | \--time | string | "w" |
| Arribos | \--arrival | float | 0.05 |
| Aterrizaje | \--landing | int int | 10 5 |
| Despegue | \--takeoff | int int | 10 5 |
| Cargar&descargar | \--load | float | 0.033 |
| Recargar combustible | \--refuel | float | 0.033 |
| Reparación | \--repair | float | 0.066 |
| Prob (rotura) | \--repairprob | float | 0.1 |

Para decidir cuanto tiempo se va a simular, pasar el flag --time con uno de los siguientes valores (el valor por defecto es una semana):

"h": Una hora

"d": Un día

"m": Un mes

"y": Un año

El tiempo que demora el aterrizaje y/o el despegue, al distribuir Normal, lleva como primer valor la media y como segundo la varianza.

## Ejecutando los tests ⚙️

Los tests chequean la correcta generación de las variables aleatorias. Para correr los tests, ejecutar en el directorio raíz:
**python3 test.py**

## Autor

Antonio Jesús Otaño Barrera.
4to año, Ciencias de la Computación, Universidad de La Habana
