"""import pandas as pd

dados = pd.read_csv("Top_Anime_data.csv")
print(dados.head())

dados["Aired"] = dados["Aired"].apply(lambda x: x.split(",")[0] + " " + x.split(",")[1])
dados["Aired"] = pd.to_datetime(dados["Aired"], format="%Y %b %d")"""

import pandas as pd

dados = pd.read_csv("Top_Anime_data.csv")


def extrair_primeira_data(texto):
    if pd.isna(texto) or not isinstance(texto, str):
        return pd.NaT  
    
    
    primeira_data = texto.split(" to ")[0].strip()
    
    try:
        return pd.to_datetime(primeira_data, format="%b %d, %Y", errors="coerce")
    except:
        return pd.NaT  


dados["Aired"] = dados["Aired"].apply(extrair_primeira_data )
dados.to_csv("Top_Anime_data.csv", index=False)


print(dados["Aired"].head(100))



