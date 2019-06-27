# CNN-vs-SincNet
DISEÑO DE UN SISTEMA DE ETIQUETADO DE AUDIO BASADO EN REDES CONVOLUCIONALES


Este Trabajo de Fin de Máster tiene como objetivo principal el diseño de un modelo de etiquetado de archivos de audio, basado en redes neuronales convolucionales, como sistema de referencia, para su posterior comparación con un modelo novedoso llamado SincNet.

# CNN
Se expone el desarrollo y el estudio de un algoritmo CNN como sistema de referencia, explicando las diferentes capas existentes y sus funciones. 

# SincNet
Es un modelo creado por Mirco Ravanelli y Yoshua Bengio, que supone un método novedoso y eficiente respecto a los modelos CNN tradicionales. 
Además, se presentan los resultados obtenidos tanto con la base de datos proporcionada por el estudio del algoritmo SincNet, como con la base de datos proporcionada por Freesound.

# Comparación
Finalmente, se realiza una comparación entre la precisión proporcionada por ambos modelos, con el objetivo de comprobar y tratar de llegar a la conclusión de si el modelo SincNet presenta ventajas respectos a los algoritmos CNN tradicionales. Además, con el fin de realizar mejoras en ambos modelos, se realiza un ajuste de los principales parámetros empleados en un algoritmo de aprendizaje automático. Se presentan dos métodos de mejora, que se aplican a ambos modelos, obteniéndose representaciones de la precisión conseguida tras aplicar las distintas aproximaciones propuestas.


## ¿Como ejecutar el código?

1. Para crear la red CNN es necesario trabajar con el archivo CNN.py. En este archivo en primer lugar se descargan los datos de entrada con los que se va a trabajar. Posteriormente se presentan unas serie de gráficas, que permiten conocer dicha base de datos.

El siguiente paso es, mediante el método prepare_data, seleccionar el freagmento de cada archivo con el que va a trabajar la red, creando el conjunto de entrenamiento y el de validación.

A continuación, se ejecuta la arquitectura perteneciente al sistema de referencia de CNN. En esta arquitectura se definen distintos tipos de optimizadores, eligiendo aquel que mejor resultados proporciona. Por último se ejecuta el modelo, seleccionando el número de epochs deseados, y se obtienen tantos las gráficas pertenecientes a los filtros, como los resultados del modelo.

2. A la hora de realizar las mejoras, es necesario realizar el cambio de parámetros en la clase Config, tanto para el learning rate como el audio_duration.

Además, se plantean dos métodos con el objetivo de mejorar los resultados: Divide_data y divide_data2.
Es necesario ejecutar cada modelo y el método prepare_data asociado.

3. Para ejecutar la red SincNet, en primer lugar es necesario seguir los pasos que aparecen en https://github.com/mravanelli/SincNet/blob/master/README.md

Es necesario usar la plataforma Google Cloud Engine, u otra plataforma que permita una larga ejecución. Hay que crear uns instancia e inicar el Google Engine.

En primer lugar es necesario obtener la base de datos TIMIT, con el objetivo de obtener los resultados de la red para dicha base de datos, y compararlos con los proporcionados en el estudio. En segundo lugar es necesario, realizar los cambios necesarios para aplicar la base de datos de Freesound. Se proporcionan diferentes archivos de tipo .cfg con los cambios aplicados, aunque es necesario cambiar los directorios. Además, se proporcionan nuevas listas de validación y entrenamiento, con los archivos empleados en Freesound.

python speaker_id.py --cfg=cfg/SincNet_TIMIT_nuevo.cfg

Para aplicar el método de mejora es necesario ejecutar en primer lugar el método prepare_data modificando los directorios, y posteriormente ejecutar el comando de SincNet.

python prepare_data.py $TIMIT_FOLDER $OUTPUT_FOLDER data_lists/TIMIT_all.scp
python speaker_id.py --cfg=cfg/SincNet_TIMIT_nuevo_recortado.cfg

