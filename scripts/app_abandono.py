# script para analizar abandono de clientes
todo por desarrollar

df['segmento_valor'] = pd.qcut(df['valor'], 3, labels=['bajo', 'medio', 'alto'])