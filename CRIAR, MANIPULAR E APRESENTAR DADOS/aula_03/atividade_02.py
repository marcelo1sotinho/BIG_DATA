import numpy as np 

casas = [150000, 180000, 200000, 220000, 250000, 280000, 300000, 320000, 400000, 1500000 ]

media = np.mean(casas)

mediana = np.median(casas) 

print(f"Média: {media:,.2f}")
print(f"Mediana: {mediana:,.2f}")

print(f'O valor Típico das casas é dados pela mediana pois é o que mais se aproxima do valor da maioria das casas {mediana:,.2f}')