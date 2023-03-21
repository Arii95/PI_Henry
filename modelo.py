## Importación de librerias 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import sklearn


## Se llama a la base de datos y se le hacen las transformaciones necesarias


df_ = pd.read_csv('app/df_final.csv')
list_column = df_['rating'].str.split(", ").dropna().to_numpy()
list_column = np.unique(sum(list_column, []))
list_column = np.array(sorted(list_column, key=len, reverse=True))
np.set_printoptions(threshold=sys.maxsize)

df_.loc[df_['rating'].str.contains('min'), 'rating'] = "Sin dato"
df_.loc[df_['rating'].str.contains('season'), 'rating'] = "Sin dato"


## Label encoder en la columna de rating para agrupar 

from sklearn import preprocessing

le = preprocessing.LabelEncoder()
labels_rating= le.fit_transform(df_.rating)
le.classes_

# se guarda la etiqueta y la categoría a la que se ajusta

etiquetas= pd.DataFrame({
    "original": df_.rating,
    "codificada": labels_rating
})

df_.rating = le.fit_transform(df_.rating)

#Definición de una base 

df = df_.rename(columns={'id':'movieId'})


#se llama a los archivos con los ratings


rev1= pd.read_parquet('Reviews/rev1.gzip')
rev2= pd.read_parquet('Reviews/rev2.gzip')
rev3= pd.read_parquet('Reviews/rev3.gzip')
rev4= pd.read_parquet('Reviews/rev4.gzip')
rev5= pd.read_parquet('Reviews/rev5.gzip')
rev6= pd.read_parquet('Reviews/rev6.gzip')
rev7= pd.read_parquet('Reviews/rev7.gzip')
rev8= pd.read_parquet('Reviews/rev8.gzip')

##Se concatenan
reviews= pd.concat([rev1, rev2, rev3, rev4, rev5, rev6, rev7, rev8])

reviews.rename(columns={'rating':'score_usuario'}, inplace=True)

extract= df[['movieId','title', 'rating']]

#Se combinan las dos bases de datos con el movieId, score por usuario 

base= reviews.merge(extract, on='movieId')

##Se agrega una columna que determina alta y baja preferencia para cada clasificación de  rating 


condicion = [(base['score_usuario'] <3.0),
            (base['score_usuario']>3.0)]
valores=['Alta Preferencia','Baja preferencia']

base['preferencia']= np.select(condicion, valores)

## Modelo de K-vecinos

from sklearn.neighbors import KNeighborsClassifier

clf = KNeighborsClassifier(n_neighbors=50)

X = base[['rating', 'userId']]  # Denotamos X con mayúscula ya que 
                                                     # incluye más de un atributo
y = base.preferencia 

clf.fit(X.values,y.values)

y_pred = clf.predict(X.values)

from sklearn.metrics import accuracy_score

print(accuracy_score(y,y_pred))