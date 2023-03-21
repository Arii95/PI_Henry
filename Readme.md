## Proyecto Engineer & Machine Learning ##

![imagen ilustrativa](cartoon.avif)

Para este proyecto se establecieron varias metas con la finalidad de proponer un modelo de Machine Learning en el cual se pudieran observar recomendaciones de películas para cada usuario almacenado en la base de datos. 


En primer lugar se realizó un análisis general de las columnas que venían en el data set para evaluar las transformaciones necesarias. 



1) Se generó campo __id__ para darle un código unico a cada película en cada plataforma

2) Se sustituyeron valores nulos en el campo de __rating__ para tomarlo como "General for All Audiences"

3) Se cambió el formato de fecha en la que se agregó a la plataforma para poder localizar en primer lugar Año-Mes-Día 

4) Se transformaron todos los campos con tipo de dato string a minúsculas para homogeneizar la base y no tener problemas al manipular la data. 

5) Se dividió la columna de __duration__ para tener dos campos, uno donde se tendría el número y otra donde se almacenara el tipo de película o serie.




Una vez teniendo estas modificaciones, se realizó un join de todas las plataformas con sus respectivas películas y una vez terminada, se exportó como archivo .csv en la carpeta de app como "df_final.csv" para ser consultada por la API en el archivo main.py. En ese archivo se construyeron 4 decoradores para realizar consultas online sobre la base de datos trabajadas con el apoyo del notebook de consultas para testear los códigos necesarios:

- Obtener el título de la película con mayor duración, dado año, plataforma y tipo de duración.

- Obtener la cantidad de películas por encima de determinado score, dada la plataforma y el año.

- Obtener la cantidad de peliculas dada la plataforma.

- Obtener el actor que más se repite dada la plataforma y el año.


Concluyendo este paso, las consultas se les pasó al .py para que, definida una variable global en la que se llamaba una sola vez al dataframe necesario para esas consultas en específico.








https://proyecto-individual1-qfv1.onrender.com/docs