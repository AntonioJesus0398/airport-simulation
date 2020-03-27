
# Simulación de eventos discretos. Informe escrito

**Nombre y apellidos:** Antonio Jesús Otaño Barrera

**Grupo:** C411

## Orden del problema asignado

En el Aeropuerto de Barajas, se desea conocer cuánto tiempo se encuentran
vacı́as las pistas de aterrizaje. Se conoce que el aeropuerto cuenta con un máximo
de 5 pistas de aterrizaje dedicadas a aviones de carga y que se considera que
una pista está ocupada cuando hay un avión aterrizando, despegando o cuando
se encuentra cargando o descargando mercancı́a o el abordaje o aterrizaje de
cada pasajero. Se conoce que el tiempo cada avión que arriba al aeropuerto distribuye,
mediante una función de distribución exponencial con λ = 20 minutos.
Si un avión arriba al aeropuerto y no existen pistas vacı́as, se mantiene
esperando hasta que se vacı́e una de ellas (en caso de que existan varios aviones
en esta situación, pues se establece una suerte de cola para su aterrizaje.
Se conoce además que el tiempo de carga y descarga de un avión distribu-
ye mediante una función de distribución exponencial con λ = 30 minutos. Se
considera además que el tiempo de aterrizaje y despegue de un avión distribuye
normal (N(10,5)) y la probabilidad de que un avión cargue y/o descargue en
cada viaje corresponde a una distribución uniforme.
Además de esto se conoce que los aviones tiene una probabilidad de tener
una rotura de 0.1. Ası́, cuando un avión posee alguna rotura debe ser reparado
en un tiempo que distribuye exponencial con λ = 15 minutos. Las roturas se
identifican justo antes del despegue de cada avión.
Igualmente cada avión, durante el tiempo que está en la pista debe recargar
combustible y se conoce que el tiempo de recarga de combustible distribuye
expoencial λ = 30 minutos y se comienza justamente cuando el avión aterriza.
Se asume además que los aviones pueden aterrizar en cada pista sin ninguna
preferencia o requerimiento.
Simule el comportamiento del aeropuerto por una semana para estimar el
tiempo total en que se encuentran vacı́a cada una de las pistas del aeropuerto.

## Principales Ideas seguidas para la solución del problema

Para simular el comportamiento del aereopuerto se utilizó el modelo de simulación de eventos discretos basado en servidores en paralelo. Específicamente los aviones constituyen los clientes y las pistas de aterrizaje, los servidores.
El tiempo que demora en atender un servidor a un cliente es la suma de los tiempos que demora el avión en realizar todas las operaciones: aterrizaje, carga y descarga de mercancías, recarga de combustible, reparación y despegue, teniendo en cuenta que la reparación y la carga y descarga de mercancías son opcionales(están sujetos a cierta probabilidad). Para estimar el tiempo de demora de cada una de estas actividades se implementaron las variables aleatorias correspondientes. Para calcular el tiempo que permanece la pista i-ésima vacía se lleva una variable, llamémosle Ti, en la cual se almacena el total de minutos que la pista ha permanecido vacía hasta el instante de tiempo que se está analizando y además se lleva otra, sea Li,  que indica el instante de tiempo desde el cual la pista esta vacía. Cada vez que un avión abandona la pista i-ésima, se actualiza Li y cuando llegue un nuevo avión a la misma en un tiempo t, se incrementa Ti en el tiempo que pasó desde Li hasta el momento t. El tiempo total que permanecen las pistas del aereopuerto vacías es la suma de los Ti.

## Consideraciones obtenidas a partir de la ejecución de las simulaciones del problema

Con respecto a los parametros lambda de las exponenciales, sus valores originales causaban que el tiempo de los procesos de llegada de nuevos aviones, carga y descaraga, reparación y recargar combustible fuera demasiado pequeño. Por ejemplo el tiempo de arribo entre aviones, asumiendo que distribuye Exp(20), posee una media de 1/20 min = 3s, lo cual no es un valor realista. Por ende se sustituyeron los lambda de las exponenciales: 20, 30, 15, 30 por 1/20, 1/30, 1/15, 1/30, que hace que estos procesos duren una media de 20, 30, 15, 30 min respectivamente, lo cual se acerca mucho más a la realidad. Con el objetivo de calcular cuanto tiempo permanece vacía una pista del aereopuerto durante una semana, asumiendo que este funciona las 24 horas durante los 7 días, se realizaron 10000 simulaciones y se obtuvo que en promedio una pista permanece vacía 2 días, 8 horas y 55 minutos.
