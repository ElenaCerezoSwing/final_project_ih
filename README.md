# Vidrio, papel, papelera, pila, Spok

El presente proyecto es el correspondiente a la entrega final del curso de Data del Bootcamp de Part-Time de IronHack.


Consiste en un modelo sencillo de entrenamiento una red neuronal convolucional aplicada al reconocimiento de imágenes.

Esta red neuronal artificial emula la respuesta de las neuronas en la corteza visual primaria de un cerebro biológico.

Es una variación de un perceptrón multicapa.  Y es muy efectiva para las tareas de visión artificial porque se aplica sobre matrices bidimensionales. Esto permite que sea óptima para la clasificación y para la segmentación entre otras aplicaciones.


## Objetivo

![](https://assets.change.org/photos/0/gb/gf/ZnGbgfehIOGsYDm-800x450-noPad.jpg?1487898640)

Generar una red neuronal que permita la clasificación de imágenes de residuos para facilitar la identificación de los mismos y poder aprender a reciclar mientras se reduzca la generación de ellos.

## Pasos
- Estudio de métodos de generación de redes de neuronas convolucionales
- Intentos:
	1. 	~~Generación de nuestro propio dataset~~ &rarr; fallos en:
		- instalación de librerías
		- entornos virtuales
		- docker

	1. 	~~Utilización de otros datasets~~ &rarr; 
		- falta de adaptación al objetivo (no encontramos lo que buscábamos)

- Vuelta a la primera idea.  No estamos solos, hay más gente que quiere hacer lo mismo y tiene un [dataset disponible](http://https://towardsdatascience.com/how-to-build-an-image-classifier-for-waste-sorting-6d11d3c9c478 "dataset disponible")

- Generación de la topología de la red neuronal.

## Conclusiones

A lo largo de este proyecto hemos observado la repercusión de los siguientes factores y parámetros:

- La importancia del procesamiento de las imágenes:
	- 		 redimensionado
	- 		escala de grises (importa más la textura que el color)
	- 		 normalización
	- 		importancia del casteo de los tipos de datos
	
- La topología de la red neuronal convolucional:
	- 		 elección de los métodos
	- 		elección de los parámetros
			(no es tan importante en nuestro caso el número de capas como el uso correcto de los parámetros)
			
- La importancia de evaluar el modelo tanto en los datos de entrenamiento como de evaluación:
	- 		 permite detectar problemas de sobreentrenamiento 
	- 		permite enfocar el estudio a la modificación de la topología o al tratamiento de los datos
			

## Tecnología aplicada
 Para la consecución de este proyecto se ha utilizado:

- **OpenCV**  para el procesamiento de imágenes
- **Keras (Tensorflow)** para la creación del modelo de la CNN



## Siguientes pasos
 Porque  queremos seguir con este proyecto.
 Los siguientes objetivos son los siguientes:
-  Densificar el dataset de imágenes mediante captura.
-  Mejor procesamiento de las imágenes.
-  Mayor definición en las clases centrándonos en texturas.
-  Continuo estudio y mejora de la topología de la red neuronal.
-  Generación de una interfaz gráfica que permita la accesibilidad al producto.
-  Generación de un equipo de trabajo (en proceso) sólido e interesado en el cambio del paradigma del consumo, generación y reciclaje de residuos.
