#Importación de libretias necesarias para API y datos
from fastapi import FastAPI

import pandas as pd


app= FastAPI()

@app.on_event('startup')
async def startup():
    global df_pr
    df_pr= pd.read_csv('df_final.csv')
    

#Decoradores para consultas

#Obtener el título de la película con mayor duración, dado año, plataforma y tipo de duración
@app.get("/get_max_duration/{year}/{plataforma}/{duration}")
async def get_max_duration(year:int, plataforma:str,duration:str):
    rslt_df = df_pr.loc[(df_pr['Year'] == year) &
              (df_pr['plataforma']==plataforma)&(df_pr['duration_type']==duration)]
    max_value=int(rslt_df['duration_int'].max())
    fila_max_valor = rslt_df.loc[rslt_df['duration_int'].eq(max_value)]
    a= fila_max_valor['title'].values
    return f'resultado: {a}'


#Obtener la cantidad de películas por encima de determinado score, dada la plataforma y el año 
@app.get("/get_score_count/{plataforma}/{scored}/{year}")
async def get_score_count(plataforma:str, scored:int, year:int):
    rslt_df = df_pr.loc[(df_pr['Year'] == year) &
              (df_pr['plataforma']==plataforma) & (df_pr['rating_y']> scored)]
    b= rslt_df['id'].count()
    return f'resultado: {b}'

#Obtener la cantidad de peliculas dada la plataforma, 
@app.get("/get_count_platform/{plataforma}")
async def get_count_plataform(plataforma:str):
    rslt_df = df_pr.loc[(df_pr['plataforma']==plataforma)]
    return f'resultado: {rslt_df[0]}'


#Obtener el actor que más se repite dada la plataforma y el año 
@app.get("/get_actor/{plataforma}/{year}")
async def get_actor(plataforma:str,year:int):
    df_pr['cast'].fillna(' ',inplace= True)
    rslt_df = df_pr.loc[(df_pr['Year'] == year) & (df_pr['plataforma']==plataforma)]
    tolist= list(rslt_df['cast'].str.split(', '))
    lista_completa = []
    for listas in tolist:
        for elemento in listas:
            lista_completa.append(elemento)
    elemento_mas_comun = max(set(lista_completa), key = lista_completa.count)
    lista_sinNaN = [elem for elem in lista_completa if elem != elemento_mas_comun]
    d = max(set(lista_sinNaN), key=lista_sinNaN.count)
    return f'resultado: {d}'

