# %% [markdown]
# # Déjame escuchar la música

# %% [markdown]
# # Contenido <a id='back'></a>
# 
# * [Introducción](#intro)
# * [Etapa 1. Descripción de los datos](#data_review)
#     * [Conclusiones](#data_review_conclusions)
# * [Etapa 2. Preprocesamiento de datos](#data_preprocessing)
#     * [2.1 Estilo del encabezado](#header_style)
#     * [2.2 Valores ausentes](#missing_values)
#     * [2.3 Duplicados](#duplicates)
#     * [2.4 Conclusiones](#data_preprocessing_conclusions)
# * [Etapa 3. Prueba de hipótesis](#hypotheses)
#     * [3.1 Hipótesis 1: actividad de los usuarios y las usuarias en las dos ciudades](#activity)
#     * [3.2 Hipótesis 2: preferencias musicales los lunes y los viernes](#week)
#     * [3.3 Hipótesis 3: preferencias de género en Springfield y Shelbyville](#genre)
# * [Conclusiones](#end)

# %% [markdown]
# ## Descripción del proyecto
# 
# En el contexto de este proyecto, probaremos hipótesis relacionadas con las preferencias musicales de dos ciudades.     
# Esto se hará mediante el análisis de datos reales de transmisión de música online para probar las hipótesis a continuación y comparar el comportamiento de los usuarios y las usuarias de estas dos ciudades.  
# Esto implicará analizar los datos reales de transmisión de música online para comparar el comportamiento de los usuarios y las usuarias en Springfield y Shelbyville. El proyecto se divide en tres etapas,   cada una con objetivos específicos.  
# En la etapa 1, proporcionaremos una descripción general de los datos y anotarás tus observaciones.   
# En la etapa 2, preprocesaremos los datos al limpiarlos.   
# Finalmente, en la etapa 3, pondremos a prueba las hipótesis siguiendo los pasos de programación necesarios para probar cada declaración y comentando tus resultados en los bloques apropiados.  
# Al completar estas etapas, podrás extraer información valiosa de los datos y tomar decisiones basadas en datos.  
#  

# %%
# Comparar los objetos datetime

dt1 = "12:00:00"
dt2 = "06:00:00"

if dt1 < dt2:
    print("La marca temporal 2 es posterior")
else:
    print("La marca temporal 1 es posterior")

# %% [markdown]
# [Volver a Contenidos](#back)

# %% [markdown]
# ## Etapa 1. Descripción de los datos <a id='data_review'></a>

# %%
# importar pandas
import pandas as pd

# %%
# Leer el archivo y almacenarlo en df
df=pd.read_csv('music_project_en.csv')

# %%
# Obtener las 10 primeras filas de la tabla df
df.head(10)

# %%
# Obtener información general sobre los datos en df
df.info()

# %% [markdown]
# Estas son nuestras observaciones sobre la tabla. Contiene siete columnas. Todas almacenan el mismo tipo de datos: `object` (objeto).
# 
# Según la documentación:
# - `' userID'` — identificador del usuario o la usuaria;
# - `'Track'` — título de la canción;
# - `'artist'` — nombre del artista;
# - `'genre'` — género musical;
# - `'City'` — ciudad del usuario o la usuaria;
# - `'time'` — hora exacta en la que se reprodujo la canción;
# - `'Day'` — día de la semana.
# 
# Podemos ver tres problemas con el estilo en los encabezados de la tabla:
# 1. Algunos encabezados están en mayúsculas; otros, en minúsculas.
# 2. Hay espacios en algunos encabezados.
# 3. No se sigue la modalidad snake_case en el caso de la columna 'userID' que puede ser reemplazada por user_id.
# 
# 
# 

# %% [markdown]
# ### Tus observaciones <a id='data_review_conclusions'></a>
# 
# `1.   ¿Qué tipo de datos tenemos a nuestra disposición en las filas? ¿Y cómo podemos entender lo que almacenan las columnas?`
#     El tipo de dato de nuestras columnas es object, que distingue strings y marcas temporales. Para entender lo que almacenan las columnas debemos tener el contexto y ver algunas filas con datos para entender de que va nuestro DataFrame, con el método info() de pandas podemos obtener más información acerca del dataset.
# 
# `2.   ¿Hay suficientes datos para proporcionar respuestas a nuestras tres hipótesis o necesitamos más información?`
#       Si, debido a que tenemos información de las canciones que escuchan los usuarios, la hora y el día en que se escuchan, el lugar y el genero de cada canción, por lo tanto con análisis exploratorio de datos se pueden probar las hipotesis.
# 
# `3.   ¿Notaste algún problema en los datos, como valores ausentes, duplicados o tipos de datos incorrectos?`
#        Podemos ver datos nulos al aplicar la función info, debido a que no todos los atributos tienen el mismo número de valores no nulos y a simple vista en la primera visual de la tabla podemos ver un valor nulo en la fila 9 columna 'artist', sin embargo, esto lo podemos ver a fondo más adelante.

# %% [markdown]
# [Volver a Contenidos](#back)

# %% [markdown]
# ## Etapa 2. Preprocesamiento de datos <a id='data_preprocessing'></a>
# 

# %% [markdown]
# ### Estilo del encabezado <a id='header_style'></a>

# %%
# La lista de encabezados para la tabla df
columnas=df.columns
print(columnas)

# %% [markdown]
# Ponemos todos los caracteres en minúsculas.

# %%
# Bucle en los encabezados poniendo todo en minúsculas
no_uppers=[]
for column in columnas:#Iteramos en la lista de encabezados de columnas
    #Quitamos las mayusculas al encabezado
    no_uppers.append(column.lower())
    
    
print(no_uppers)

# %% [markdown]
# Ahora eliminamos los espacios al principio y al final de los encabezados:

# %%
# Bucle en los encabezados eliminando los espacios
no_spaces=[]
for column in no_uppers:
    #Quitamos los espacios
    no_spaces.append(column.strip())
print(no_spaces)

# %% [markdown]
# Aplicamos snake_case al encabezado userID:

# %%
#Reemplazamos el valor de userID por user_id
#Primero borramos el valor de la lista
no_spaces.pop(0)
#Luego lo insertamos en la lista de nuevo
no_spaces.insert(0,'user_id')
print(no_spaces)


# %%
#Reemplazamos las columnas por la lista con los valores correctos
df.columns=no_spaces
print(df.columns)

# %% [markdown]
# [Volver a Contenidos](#back)

# %% [markdown]
# ### MissValores ausentes <a id='missing_values'></a>

# %%
#Utilizamos el metodo isna() y sum() para identificar cuantos faltantes hay por cada columna
print(df.isna().sum())

# %% [markdown]
# No todos los valores ausentes afectan a la investigación. Por ejemplo, los valores ausentes en `track` y `artist` no son cruciales. Simplemente puedes reemplazarlos con valores predeterminados como el string `'unknown'` (desconocido).
# 
# Pero los valores ausentes en `'genre'` pueden afectar la comparación entre las preferencias musicales de Springfield y Shelbyville. 

# %% [markdown]
# Reemplazamos los valores ausentes en `'track'`, `'artist'` y `'genre'` con el string `'unknown'`. Para hacer esto, creamos la lista `columns_to_replace`, recórriendola con un bucle `for` y reemplazando los valores ausentes en cada columna:

# %%
# Bucle en los encabezados reemplazando los valores ausentes con 'unknown'
columns_to_replace=['track','artist','genre']
for column in columns_to_replace:
    #Llenamos los ausentes por 'unknown' con al argumento inplace=True para que se reasigne automaticamente
    df[column].fillna('unknown',inplace=True)


# %%
# Contando valores ausentes
print(df.isna().sum())

# %% [markdown]
# **Podemos ver que nuestro dataset quedo sin ausentes.**

# %% [markdown]
# [Volver a Contenidos](#back)

# %% [markdown]
# ### Duplicados <a id='duplicates'></a>

# %%
# Contar duplicados explícitos
print(df.duplicated().sum())

# %%
# Eliminar duplicados explícitos
df.drop_duplicates(inplace=True)
df.reset_index(drop=True)

# %%
# Comprobación de duplicados
print(df.duplicated().sum())

# %% [markdown]
# Ahora queremos deshacernos de los duplicados implícitos en la columna `genre`. Por ejemplo, el nombre de un género se puede escribir de varias formas. Dichos errores también pueden afectar al resultado.

# %% [markdown]
# Para hacerlo, primero mostremos una lista de nombres de género únicos, ordenados en orden alfabético.
# 

# %%
# Inspeccionando los nombres de géneros únicos
genre=df['genre'].unique()
genre.sort()
print(genre)

# %% [markdown]
# Busca en la lista para encontrar duplicados implícitos del género `hiphop`. Estos pueden ser nombres escritos incorrectamente o nombres alternativos para el mismo género.
# 
# Duplicados implícitos:
# * `hip`
# * `hop`
# * `hip-hop`
# 
# Declaramos la función `replace_wrong_genres()` con dos parámetros:
# * `wrong_genres=` — la lista de duplicados;
# * `correct_genre=` — el string con el valor correcto.
# 
# La función debería corregir los nombres en la columna `'genre'` de la tabla `df`, es decir, remplaza cada valor de la lista `wrong_genres` con el valor en `correct_genre`. Utilizamos un bucle `'for'` para iterar sobre la lista de géneros incorrectos y reemplazarlos con el género correcto en la lista principal.

# %%
# Función para reemplazar duplicados implícitos
def replace_wrong_genres(wrong_genres,correct_genre):
    #Bucle que itera en cada valor erroneo
    for value in wrong_genres:
        #Reemplazamos los valores
        df['genre']=df['genre'].replace(value,correct_genre)
    #Devolvemos el dataframe corregido
    return df

# %%
#Asignamos variables y llamamos la función creada para reemplazar los valores erroneos
wrong=['hip','hop','hip-hop']
correct='hiphop'
replace_wrong_genres(wrong,correct)

# %%
# Comprobación de duplicados implícitos
genre=df['genre'].unique()
genre.sort()
print(genre)

# %% [markdown]
# [Volver a Contenidos](#back)

# %% [markdown]
# ### Observaciones <a id='data_preprocessing_conclusions'></a>
# 
# Al análizar los duplicados, podemos ver que la mayoría son genericos, en cambio los duplicados explicitos son menos, debido a que los generos se pueden escribir de varias maneras, es una tarea dificil encontrar generos similares a menos que sepas mucho de musica, sin embargo, esta es una tarea que debemos hacer como analístas.

# %% [markdown]
# [Volver a Contenidos](#back)

# %% [markdown]
# ## Etapa 3. Prueba de hipótesis <a id='hypotheses'></a>

# %% [markdown]
# ### Hipótesis 1: comparar el comportamiento del usuario o la usuaria en las dos ciudades <a id='activity'></a>

# %% [markdown]
# La primera hipótesis afirma que existen diferencias en la forma en que los usuarios y las usuarias de Springfield y Shelbyville consumen música. Para comprobar esto, usaremos los datos de tres días de la semana: lunes, miércoles y viernes.

# %%
# Contando las canciones reproducidas en cada ciudad
df.groupby('city')['genre'].count()

# %% [markdown]
# **Podemos evidenciar que la ciudad de Springfield escucha más canciones que la ciudad de Shelbyville según nuestros datos.**

# %% [markdown]
# Ahora agrupamos los datos por día de la semana y encontramos el número de canciones reproducidas el lunes, miércoles y viernes.
# 

# %%
df.groupby('day')['city'].count()


# %% [markdown]
# **En general por ciudad podemos ver que el día de la semana que más se escuchan canciones es el viernes, seguido del lunes y despues el miercoles.**

# %%
# <creando la función number_tracks()>
# Declararemos la función con dos parámetros: day=, city=.
# Deja que la variable track_list almacene las filas df en las que
# el valor del nombre de la columna ‘day’ sea igual al parámetro day= y, al mismo tiempo,
# el valor del nombre de la columna ‘city’ sea igual al parámetro city= (aplica el filtrado consecutivo
# con la indexación lógica).
# deja que la variable track_list_count almacene el número de valores de la columna 'user_id' en track_list
# (igual al número de filas en track_list después de filtrar dos veces).
# permite que la función devuelva un número: el valor de track_list_count.

# La función cuenta las pistas reproducidas en un cierto día y ciudad.
# Primero recupera las filas del día deseado de la tabla,
# después filtra las filas de la ciudad deseada del resultado,
# luego encuentra el número de canciones en la tabla filtrada,
# y devuelve ese número.
# Para ver lo que devuelve, envuelve la llamada de la función en print().


# comienza a escribir tu código aquí
def number_tracks(day,city):
    track_list=df[(df['day']==day) & (df['city']==city)]
    track_list_count=track_list['user_id'].count()
    return track_list_count

# %%
# El número de canciones reproducidas en Springfield el lunes
list_springfield=['springfield']
list_springfield.append(number_tracks('Monday','Springfield'))
number_tracks('Monday','Springfield')

# %%
# El número de canciones reproducidas en Springfield el miércoles
list_springfield.append(number_tracks('Wednesday','Springfield'))
number_tracks('Wednesday','Springfield')

# %%
# El número de canciones reproducidas en Springfield el viernes
list_springfield.append(number_tracks('Friday','Springfield'))
number_tracks('Friday','Springfield')

# %%
# El número de canciones reproducidas en Shelbyville el lunes
list_shelbyville=['shelbyville']
list_shelbyville.append(number_tracks('Monday','Shelbyville'))
number_tracks('Monday','Shelbyville')

# %%
# El número de canciones reproducidas en Shelbyville el miercoles
list_shelbyville.append(number_tracks('Wednesday','Shelbyville'))
number_tracks('Wednesday','Shelbyville')

# %%
# El número de canciones reproducidas en Shelbyville el viernes
list_shelbyville.append(number_tracks('Friday','Shelbyville'))
number_tracks('Friday','Shelbyville')

# %%
# Tabla con los resultados
#Creamos una lista para almacenar los datos de la tabla
lista_ciudad=[]
lista_ciudad.extend([list_springfield,list_shelbyville])
#Creamos una lista con los encabezados de las columnas
colum=['city', 'monday', 'wednesday', 'friday']
#Aplicamos DataFrame() para crear la tabla
Tabla=pd.DataFrame(data=lista_ciudad,columns=colum)
print(Tabla)

# %% [markdown]
# **Conclusiones**
# 
# **Según los resultados de la exploración de datos, podemos aprobar la hipotesis, ya que podemos ver que el comportamiento de cada ciudad es diferente, teniendo en cuenta que en springfield se escucha mucho más musica que en la ciudad de shelbyville. Podemos ver que la ciudad de springfield dobla la cantidad de canciones que se reproducen al día aproximadamente, por otro lado el día de la semana también influye en la cantidad de canciones que se reproducen al día, al inicio de la semana el numero es alto, para la mitad de la semana baja y para el fin de la semana aumenta el numero siendo el maximo de canciones escuchadas durante la semana.**

# %% [markdown]
# [Volver a Contenidos](#back)

# %% [markdown]
# ### Hipótesis 2: música al principio y al final de la semana <a id='week'></a>

# %% [markdown]
# Según la segunda hipótesis, el lunes por la mañana y el viernes por la noche, los ciudadanos de Springfield escuchan géneros diferentes a los que disfrutan los usuarios de Shelbyville.

# %%
# cree la tabla spr_general a partir de las filas df
# donde el valor en la columna 'city' es 'Springfield'
spr_general=df[df['city']=='Springfield']

# %%
# crea shel_general a partir de las filas df
# donde el valor en la columna 'city' es 'Shelbyville'
shel_general=df[df['city']=='Shelbyville']

# %%
# 1) Deja que la variable genre_df almacene las filas que cumplen varias condiciones:
#    - el valor de la columna 'day' es igual al valor del argumento day=
#    - el valor de la columna 'time' es mayor que el valor del argumento time1=
#    - el valor en la columna 'time' es menor que el valor del argumento time2=
#    Utiliza un filtrado consecutivo con indexación lógica.

# 2) Agrupa genre_df por la columna 'genre', toma una de sus columnas,
#    y use el método size() para encontrar el número de entradas para cada una de
#    los géneros representados; almacena los Series resultantes en
#    la variable genre_df_count

# 3) Ordena genre_df_count en orden descendente de frecuencia y guarda el resultado
#    en la variable genre_df_sorted

# 4) Devuelve un objeto Series con los primeros 15 valores de genre_df_sorted - los 15
#    géneros más populares (en un determinado día, en un determinado periodo de tiempo)

# Escribe tu función aquí
def genre_weekday(df,day,time1,time2):
    # Filtrado consecutivo
    # Cree la variable genre_df que almacenará los filtros
    genre_df = df[(df['day']==day)&(df['time']>=time1)&(df['time']<=time2)]
    
    # Agrupe el DataFrame filtrado por la columna con los nombres de los géneros, seleccione la columna 'genre',
    # y encuentre el número de filas para cada género con el método count()
    genre_df_count = genre_df.groupby('genre')['user_id'].count()

    # Ordene el objeto Serie resultante en orden descendente (para que los géneros más populares aparezcan primero en el objeto Series)
    genre_df_sorted = genre_df_count.sort_values(ascending=False)

    # Devuelve un objeto Series con los primeros 15 valores de genre_df_sorted los 15 géneros más populares (en un día determinado, dentro de un período de timeframe)
    return genre_df_sorted[:15]

# %%
# llamando a la función para el lunes por la mañana en Springfield (utilizando spr_general en vez de la tabla df)
genre_weekday(spr_general,'Monday','07:00:00','11:00:00')

# %%
# llamando a la función para el lunes por la mañana en Shelbyville (utilizando shel_general en vez de la tabla df)
genre_weekday(shel_general,'Monday','07:00:00','11:00:00')

# %%
# llamando a la función para el viernes por la tarde en Springfield
genre_weekday(spr_general,'Friday','17:00:00','23:00:00')

# %%
# llamando a la función para el viernes por la tarde en Shelbyville
genre_weekday(shel_general,'Friday','17:00:00','23:00:00')

# %% [markdown]
# **Conclusión**
# 
# **Según el análisis que se realizó con los datos de cada ciudad, se puede aprobar la hipótesis parcialmente, debido a que los 6 primeros generos en la mañana se mantienen iguales en las 2 ciudades, sin embargo, es cierto que a partír de estos difieren los generos, por ejemplo springfield en las mañanas escucha folk, lo cual no se escucha en shelbyville, y en shelbyville se escucha rnb, lo cual en springfield no es significativo. Por el lado de la noche pasa lo mismo.**

# %% [markdown]
# [Volver a Contenidos](#back)

# %% [markdown]
# ### Hipótesis 3: preferencias de género en Springfield y Shelbyville <a id='genre'></a>
# 
# Hipótesis: Shelbyville ama la música rap. A los residentes de Springfield les gusta más el pop.

# %%
# Escribe una línea de código que:
# 1. agrupe la tabla spr_general por la columna 'genre';
# 2. cuente los valores 'genre' con count() en la agrupación;
# 3. ordene el Series resultante en orden descendente y lo guarde en spr_genres.
spr_gnr=spr_general.groupby('genre')['user_id'].count()
spr_gnr=spr_gnr.sort_values(ascending=False)

# %%
# mostrar las 10 primeras filas de spr_genres
spr_gnr.head(10)

# %%
# Escribe una línea de código que:
# 1. agrupe la tabla shel_general por la columna 'genre';
# 2. cuente los valores 'genre' en el agrupamiento con count();
# 3. ordene el Series resultante en orden descendente y lo guarde en shel_genres.
shel_gnr=shel_general.groupby('genre')['user_id'].count()
shel_gnr=shel_gnr.sort_values(ascending=False)

# %%
# Muestra las 10 primeras filas de shel_genres
shel_gnr.head(10)

# %%
#Realicé un análisis adicional para tener un poco más de claridad respecto al genero rap
rap_spr=spr_general['genre']
rap_shel=shel_general['genre']
rap_spr=rap_spr[rap_spr=='rap'].count()/rap_spr.count()
rap_shel=rap_shel[rap_shel=='rap'].count()/rap_shel.count()
print('Oyentes de rap en springfield: ',rap_spr,'\n','Oyentes de rap en shelbyville: ',rap_shel)
#Analizamos la proporción que tiene el genero rap en cada ciudad.

# %% [markdown]
# **Conclusión**
# 
# **Al realizar el análisis, podemos ver que es verdad que en springfield se escucha más pop que en shelbyville, sin embargo, en cuanto al genero 'rap' en ninguno de las dos ciudades se escucha mucho, ya que en springfield solo el 1,2% escuchan rap y en shelbyville solo el 1,6% lo cual no es significativo. En conclusión esta hipotesis se puede rechazar parcialmente, debido a que el hecho de que shelbyville escuche más rap que pop es erroneo y las ciudades tienen gustos parecidos entre si.**

# %% [markdown]
# [Volver a Contenidos](#back)

# %% [markdown]
# # Conclusiones <a id='end'></a>

# %% [markdown]
# 1. Podemos aprobar esta hipotesis, debido a que es verdad que la ciudad y el día de la semana influyen en la actividad de los usuarios en numeros de reproducción, springfield supera a shelbyville y se escucha más musica los viernes, seguido por los lunes y los miercoles.
# 
# 2. Podemos aprobar parcialmente la hipotesis, debido a que los gustos musicales en cuanto a genero de cada ciudad son parecidos a excepción de unos cuantos, como el folk y el rnb que difiere en ambas ciudades, sin embargo, la hora del día y el día no infiere cambio en cuanto a la musica que se escucha en distintas ciudades.
# 
# 3. Se rechaza parcialmente la hipotesis debido a que solamente se cumple el hecho de que en springfield se escucha más pop que en shelbyville, sin embargo, el genero rap no se escucha más en shelbyville y la cantidad de personas que escuchan este genero es muy baja en ambas ciudades.

# %% [markdown]
# [Volver a Contenidos](#back)


