"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""

""" Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv" """

def pregunta_01():
    import pandas as pd
    import os

    def convertir_fecha(fecha):
        try:
            return pd.to_datetime(fecha, format='%Y/%m/%d', errors="raise").strftime('%Y-%m-%d')
        except Exception:
            try:
                return pd.to_datetime(fecha, format='%d/%m/%Y', errors="raise").strftime('%Y-%m-%d')
            except Exception:
                return pd.NaT  
    path="files/input/solicitudes_de_credito.csv"
    df = pd.read_csv(path, sep=';')

    df = df.dropna(subset=['tipo_de_emprendimiento'])
    df = df.dropna(subset=['barrio'])

    df['barrio'] = df['barrio'].astype(str)
    df['barrio'] = df['barrio'].apply(lambda x: x.replace('_', ' '))
    df['barrio'] = df['barrio'].apply(lambda x: x.replace('-', ' '))
    df['barrio'] = df['barrio'].apply(lambda x: x.lower() if isinstance(x, str) else x)
    # df['barrio'] = df['barrio'].str.replace('bel¿n', 'belen', regex=False)
    # df['barrio'] = df['barrio'].str.replace('antonio nari¿o', 'antonio nariño', regex=False)  
    df = df = df.apply(lambda col: col.map(lambda x: x.lower() if isinstance(x, str) else x))
    df = df.drop(df.columns[0], axis=1)
    
    print(df['línea_credito'].value_counts())

    df['idea_negocio'] = df['idea_negocio'].apply(lambda x: x.replace('-', ' ').replace('_', ' ').strip())
    df['fecha_de_beneficio'] = df['fecha_de_beneficio'].apply(convertir_fecha)

    df['línea_credito'] = df['línea_credito'].apply(lambda x: x.replace('-', ' ').replace('_', ' ').replace('.', '').strip())
    # df['línea_credito'] = df['línea_credito'].str.replace('soli diaria', 'solidaria', regex=False)

    

    df['monto_del_credito'] = df['monto_del_credito'].replace({'\\$': '', ',': '', '\\.00': ''}, regex=True)
    df['monto_del_credito'] = pd.to_numeric(df['monto_del_credito'], errors='coerce')
    df = df.drop_duplicates()
    
    
    print(df.shape)
    print(df['línea_credito'].value_counts())

    output_folder = 'files/output/'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"La carpeta '{output_folder}' fue creada.")

    path = "files/output/solicitudes_de_credito.csv"
    df.to_csv(path, sep=";", index=False) 
    

if __name__ == '__main__':
    print(pregunta_01())
