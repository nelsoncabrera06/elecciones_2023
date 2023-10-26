import pandas as pd

# Especifica el separador correcto (punto y coma en tu caso)
separador = ';'

# Cargar el archivo CSV con el separador especificado
df = pd.read_csv('test_mis_resultados.csv', sep=separador)
#df = pd.read_csv('ResultadosElectorales_2023.csv', sep=separador)
# Ver el índice
print("Índice del DataFrame:")
print(df.index)

# Ver el número total de filas y columnas
num_filas, num_columnas = df.shape
print(f"El DataFrame tiene {num_filas} filas y {num_columnas} columnas.")
print()


# Crear una nueva columna y asignarle valores
nueva_columna = [None] * num_filas
df['total_votos_en_mesa'] = nueva_columna
df['porcentaje'] = nueva_columna


def print_headers():
    # Obtener la lista de encabezados
    encabezados = df.columns
    
    print("Encabezados en el archivo CSV:")
    for encabezado in encabezados:
        print(encabezado)
    print()
    
def mesas_unicas():
    # Contar valores únicos en la columna "mesa_id"
    valores_unicos = df['mesa_id'].nunique()
    print("Número de valores únicos en la columna 'mesa_id':", valores_unicos)
    #print(type(valores_unicos))
    print("Mesas unicas ", valores_unicos)
    print()

    valores_unicos = df['mesa_id'].drop_duplicates()
    #print(type(valores_unicos))
    for valor in valores_unicos:
        print(valor)
    print()

def mostrar_valores_unicos(columna):
    #valores_unicos = df['agrupacion_id'].drop_duplicates()
    cantidad = df[columna].nunique()
    valores_unicos = df[columna].drop_duplicates()
    
    print(columna + " - cantidad : ", cantidad )
    for valor in valores_unicos:
        print(valor)
    print()

def unicos(columna):
    #valores_unicos = df['agrupacion_id'].drop_duplicates()
    cantidad = df[columna].nunique()
    valores_unicos = df[columna].drop_duplicates()
    
    print(columna + " - cantidad : ", cantidad )
    print()

    return valores_unicos

encabezados = ['mesa', 'agrupacion_nombre', 'votos_cantidad', 'total_votos_en_mesa', 'porcentaje']
# Puedes crear un DataFrame con estos encabezados
tabla = pd.DataFrame(columns=encabezados)


def total_votos_enMesa(mesa):
    global tabla

    #filtro = df['mesa_id'] == mesa
    filtro = df['mesa_id'] == mesa
    filas_filtradas = df[filtro]

    print(filas_filtradas)
    print()
    
    total_votos_en_mesa = filas_filtradas['votos_cantidad'].sum()
    print("Mesa id: ", mesa)
    print("total_votos_en_mesa: ", total_votos_en_mesa)
    print()

    """
    filtro_partido = filas_filtradas['agrupacion_nombre'] == "LA LIBERTAD AVANZA"
    partido_f = filas_filtradas[filtro_partido]
    votos_partido = partido_f['votos_cantidad'].sum()
    print(partido_f)
    print(votos_partido)
    print()

    partido_porcentaje = votos_partido / total_votos_en_mesa * 100
    print(f'{partido_porcentaje:.2f}%')
    """

    # Obtén la lista de todas las agrupaciones_nombre únicas en el DataFrame
    #agrupaciones_unicas = filas_filtradas['agrupacion_nombre'].unique()
    agrupaciones_unicas = ['UNION POR LA PATRIA','LA LIBERTAD AVANZA','JUNTOS POR EL CAMBIO','HACEMOS POR NUESTRO PAIS','FRENTE DE IZQUIERDA Y DE TRABAJADORES - UNIDAD']
    
    
    for agrupacion in agrupaciones_unicas:
        filtro_partido = filas_filtradas['agrupacion_nombre'] == agrupacion
        partido_f = filas_filtradas[filtro_partido]
        votos_partido = partido_f['votos_cantidad'].sum()
        
        partido_porcentaje = (votos_partido / total_votos_en_mesa) * 100
        #partido_porcentaje_formateado = f'{partido_porcentaje:.2f}%'
        partido_porcentaje_formateado = f'{partido_porcentaje:.2f}'.replace('.', ',') 
        

        """
        print(f'Agrupación: {agrupacion}')
        print(f'Votos: {votos_partido}')
        print(f'Porcentaje: {partido_porcentaje_formateado}')
        print()
        """

        #fila = [mesa, total_votos_en_mesa, agrupacion, votos_partido, partido_porcentaje_formateado]
        fila = [mesa, agrupacion, votos_partido, total_votos_en_mesa, partido_porcentaje_formateado]
        tabla = tabla.append(pd.Series(fila, index=tabla.columns), ignore_index=True)
        tabla.append(fila)


        doble_filtro = (df['mesa_id'] == mesa) & (df['agrupacion_nombre'] == agrupacion)
        #df.loc[(df['mesa_id'] == mesa) & (df['agrupacion_nombre'] == agrupacion),'porcentaje'] = partido_porcentaje_formateado
        df.loc[doble_filtro,'porcentaje'] = partido_porcentaje_formateado
        #print(df[doble_filtro]) # esto funciona bien parece
        
        

        
    #print("aca testeando como un campeon")
    df.loc[(df['mesa_id'] == mesa),'total_votos_en_mesa'] = total_votos_en_mesa
    #nueva_tabla = df[filtro]
    #print(nueva_tabla)
    #print(df)
    #print("termino el testeando como un campeon")
    #print()

    # Imprimir el DataFrame
    print(tabla)

    """
    # Guardar el DataFrame en un archivo CSV
    tabla.to_csv('output.csv', sep=';', index=False)
    print("Tabla guardada en archivo output.csv")

    # Guardar el DataFrame en un archivo CSV
    print()
    df.to_csv('output_largo.csv', sep=';', index=False)
    print("Tabla guardada en archivo output_largo.csv")
    
    """
        

def guardar_tabla_en_archivo():
    global tabla

    # Guardar el DataFrame en un archivo CSV
    tabla.to_csv('output.csv', sep=';', index=False)
    print("Tabla guardada en archivo output.csv")

    # Guardar el DataFrame en un archivo CSV
    print()
    df.to_csv('output_largo.csv', sep=';', index=False)
    print("Tabla guardada en archivo output_largo.csv")

    


#print_headers() # lista cuales son los headers
#mesas_unicas()

#mostrar_valores_unicos('agrupacion_id')
#mostrar_valores_unicos('agrupacion_nombre')

#mostrar_valores_unicos('mesa_id')
mesas = unicos('mesa_id')

for mesa in mesas:
    total_votos_enMesa(mesa)
    

# voy a tomar el ejemplo de la mesa 482
# mesa_id = 482


guardar_tabla_en_archivo()


"""
agrupacion_nombre - cantidad :  5
nan
UNION POR LA PATRIA
LA LIBERTAD AVANZA
JUNTOS POR EL CAMBIO
HACEMOS POR NUESTRO PAIS
FRENTE DE IZQUIERDA Y DE TRABAJADORES - UNIDAD
"""