# Data_Engineer_Challenge



Teniendo en cuenta que es un archivo JSON pense inicialmente hacer una lectura del mismo mediante la libreria ujson o la libreria json; debido a que estan enfocadas netamente en la lectura de archivos y por tanto el rendimiento en la lectura deberia ser mejor a usar otras librerias. No obstante, al avanzar e intentar realizar las agrupaciones de los datos según se requeria me parecio más sencillo trabajar con pandas. Considere en usar la libreria pyspark para el procesamiento debido a que en un entorno de procesamiento distribuido es mucho mejor, pero en este caso estoy trabajando sobre mi computador y tuve algunos problemas de compatibilidad con la instalación por tanto obte por usar pandas



La logica implementada en los ejercicios es muy semejante, un aspecto clave en el que enfoque el ejercicio fue la lectura de los archivos, inicialmente implemente dos logicas diferentes pero al realizar varias pruebas de rendimiento opte por realizar la lectura del archivo JSON mediante pandas, pero por bloques con el fin de no generar un consumo de excesivo de memoria y tranversalmente extraer la información requerida para cada ejercicio

Las mejoras que podrian implementarse para este ejercicio podrian ser las siguientes:

- Implementarlo en un entorno distribuido donde se pueda hacer un procesamiento en paralelo de los archivos haciendo uso de spark
- Dependiendo el entorno y sus recursos se podria jugar la variable 'chunksize' con el fin de encontrar un valor que le de un rendimiento optimo al entorno
- En caso de que el objetivo sea almacenar la información y s requiera consumir la información de una base de datos no relacional o de un api, se podria implementar una tarea programada bajo otro lenguaje de programación como .net donde se extraiga la info y se generen las transformaciones

Los resultados de ejecución son los siguientes:


Ejercicio N#1

q1_time:   7.78 Segundos,  800 MB
q1_memory: 8.0 Segundos,  600 MB

Ejercicio N#2

q2_time:   16.6 Segundos,  210 MB Aprox
q2_memory: 17.0 Segundos,  160 MB Aprox


Ejercicio N#3

q3_time:   7.2 Segundos,  920 MB Aprox
q3_memory: 7.3 Segundos,  720 MB Aprox


Aclaraciones

- El ejercicio numero 2, tuvo un tiempo prolongado debido a la manera en que se recorrio la información para encontrar los emojis


