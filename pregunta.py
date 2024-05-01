"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd
from datetime import datetime
import re

def clean_data():

    df0 = pd.read_csv("solicitudes_credito.csv", sep=";", index_col=0)

    df = df0.copy()
    
    df = df.dropna()
    
    df["sexo"] = df["sexo"].str.lower()

    df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].str.lower()

    df["idea_negocio"] = df["idea_negocio"].str.lower().str.replace("-"," ").str.replace("_"," ")

    df["barrio"] = df["barrio"].str.lower().str.replace("-"," ").str.replace("_"," ")

    df["estrato"] = df["estrato"].astype(int)

    df["comuna_ciudadano"] = df["comuna_ciudadano"].astype(int)

    df["fecha_de_beneficio"] = [
        (
            datetime.strptime(date, "%d/%m/%Y")
            if bool(re.search(r"\d{1,2}/\d{2}/\d{4}", date))
            else datetime.strptime(date, "%Y/%m/%d")
        )

        for date in df["fecha_de_beneficio"]
        ]
    
    df["monto_del_credito"] = df["monto_del_credito"].str.strip("$").str.replace(r"\.00", "", regex=True).str.replace(",","").astype(int)
    
    df["línea_credito"] = df["línea_credito"].str.strip().str.lower().str.replace("-", " ").str.replace("_", " ").str.replace(". ", ".")
    
    df = df.drop_duplicates()

    return df