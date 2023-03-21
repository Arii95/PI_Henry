# __Proyecto Engineer & Machine Learning__ #

<br/>

![imagen ilustrativa](cartoon.avif)

Para este proyecto se establecieron varias metas con la finalidad de proponer un modelo de Machine Learning en el cual se pudieran observar recomendaciones de películas para cada usuario almacenado en la base de datos. 

<br/>

En primer lugar se realizó un análisis general de las columnas que venían en el data set para evaluar las transformaciones necesarias. 

<br/>

# __Data Engineer__

1) Se generó campo __id__ para darle un código unico a cada película en cada plataforma

2) Se sustituyeron valores nulos en el campo de __rating__ para tomarlo como "General for All Audiences"

3) Se cambió el formato de fecha en la que se agregó a la plataforma para poder localizar en primer lugar Año-Mes-Día 

4) Se transformaron todos los campos con tipo de dato string a minúsculas para homogeneizar la base y no tener problemas al manipular la data. 

5) Se dividió la columna de __duration__ para tener dos campos, uno donde se tendría el número y otra donde se almacenara el tipo de película o serie.

<br/>

Una vez teniendo estas modificaciones, se realizó un join de todas las plataformas con sus respectivas películas y una vez terminada, se exportó como archivo .csv en la carpeta de app como "df_final.csv" para ser consultada por la API en el archivo main.py. Además de sacar una columna extra a partir del promedio que le dieron los usuarios a cada película registrada a partir de las 8 bases de datos sobre el score que se registraron de 11, 5077 usuarios. Adicional a esto, se extrajo en una columna el año de ingreso a la plataforma a la que se le llamo __Year__.

En el archivo main.py se construyeron 4 decoradores para realizar consultas online sobre la base de datos trabajadas con el apoyo del notebook de consultas para testear los códigos necesarios:

<br/>

- Obtener el título de la película con mayor duración, dado año, plataforma y tipo de duración.

- Obtener la cantidad de películas por encima de determinado score, dada la plataforma y el año.

- Obtener la cantidad de peliculas dada la plataforma.

- Obtener el actor que más se repite dada la plataforma y el año.

<br/>

# __Deployment con FastApi y Render__


Concluyendo este paso, las consultas se pasaron al archivo "main.py" para que, al definir variable global, las consultas tomaran la información necesaria del dataframe para esas consultas en específico. Echando a andar la API local, se prosiguió a conectar con la página de render para realizar el deployment de las consultas en una página web. Para esto era necesario crear un archivo dockerfile que permitiera crear el ambiente requerido para realizar el deploy desde un web service, en donde se cargó la imagen de: __tiangolo/uvicorn-gunicorn-fastapi__ y se cargaron las librearias de __fastapi__ y __pandas__. En la siguiente liga se pueden realizar las consultas pertinentes:




    https://proyecto-individual1-qfv1.onrender.com/docs

<br/>

# __EDA__


Habiendo realizado el deployment se procedió a utilizar __pandas_profiling__ para realizar un informe sobre los datos y sus relaciones. Acá se hará una descripción de los hallazgos encontrados: 

- Se verificó que los Id no tuvieran duplicados, en el show_id (identificador de películas)

- No obstante, el nombre de las películas se podían repetir, debido a que podían estar registradas en más de un plataforma. 

- Había dos tipos de items en esta base de datos:

| Item  | Conteo|
| ------ | -------- |
 películas | 16,481  
 programa de televisión | 6,517

 <br/>

- En las columnas en donde se encontraban la mayoría de los datos nulos eran: director, cast, country, date_added, duración y año de agregación

- Las películas y series empezaron a ser agregadas a partir del 2019 y fue incrementando exponencialmente con el paso de los años.

- En cuanto al año de lanzamiento, comienza en 1920 y se tiene registro de las películas lanzadas hasta el 2021.

- Se tienen 28 clasificaciones en la columna de rating con la siguiente distribución:

<br/>
        rating

| Rating  | Conteo|
| ------ | -------- |
| tv-ma   |	3675  
 tv-14 |	3138 
r     |	2154 
 13+	| 2117 
 tv-pg   |	1654
 16+	| 1547
 g	| 1269
 all	| 1268
 18+	| 1243
 pg-13 |	1112
 pg	| 881
 tv-g  |	767
 tv-y7 | 550
 tv-y |	462
 7+	| 385
 nr	| 304
 Sin dato  |	295
tv-nr |	105
unrated	| 33
tv-y7-fv |	19
nc-17 |	6
ages_18_ |	3
ur |	3
not_rate |	3
ages_16_ |	2
16	| 1
not rated |	1
all_ages |	1

<br/>

- En cuanto a la cantidad de películas por plataforma: 

| Plataforma  | Items|
| ------ | -------- |
amazon | 9,668 
netflix  | 8807
hulu | 3073
disney |1450

<br/>

- En cuanto a la distribución de los ratings de los usuarios por las películas tiene un comportamiento normal y el rango que se maneja es de 3.4 a 3.7 de puntaje (que va del 1 al 5)

<br/>


# __Modelo de Machine Learning__

<br/>

Para la creación del modelo de Machine Learning se optó por  concatenar la base de datos de reviews, y sacar un promedio de score por cada clase de rating que puntuaba cada usuario para poder predecir si una pelicula o serie, que cayera en la categoría con alta preferencia o baja preferencia, le gustará o no a ese usuario. 

Con 50 vecinos se obtuvo un accuracy  de 0.63 



![imagen](pelis.jpeg)



