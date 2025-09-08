

seleccionArgentina = {
    10 : {'Nombre': 'Lionel Mesi', 'Edad': 35, 'Altura': 1.70, 'Precio': ' 50 millones', 'Posicion': 'Extremo Derecho'},
    11 : {'Nombre': 'Angel Di Maria', 'Edad': 34, 'Altura': 1.83, 'Precio': '12 millones', 'Posicion': 'Extremo Derecho'},
    24 : {'Nombre': 'Paulo Dvbala', 'Edad': 28, 'Altura': 1.77, 'Precio': '35 millones', 'Posicion': 'Media Punta'},
    19 :{'Nombre': 'Nicolas Otamendi', 'Edad': 34, 'Altura': 1.83, 'Precio': '3.5 millones', 'Posicion': 'Defensa Central'},
     1 :{'Nombre': 'Franco Armani', 'Edad': 35, 'Altura': 1.89, 'Precio': '3.5 millones', 'Posicion': 'Portero'},
}
del seleccionArgentina[11] # Elimino a Agel Di Maria
del seleccionArgentina[24] # Elimino a Paulo Dvbala
del seleccionArgentina[1]  # Elimina a Franco Armani


seleccionArgentina[24] = {'Nombre': 'Nahuel Molina', "Edad": 27, "Altura": 1.75, "Precio": "20 Millones", "Posicion": "Lateral Derecho"}
seleccionArgentina[22] = {"Nombre": "Lautaro Martinez", "Edad": 27, "Altura": 1.74, "Precio": "95 Millones", "Posicion": "Delantero"}
seleccionArgentina[23] = {"Nombre": "Lisandro Martinez", "Edad": 26, "Altura": 1.75, "Precio": "50 Millones", "Posicion": "Defensa Central"}
seleccionArgentina[20] = {"Nombre": "Alexis Mac Allister", "Edad": 25, "Altura": 1.76, "Precio": "100 Millones", "Posicion": "Mediocampista"}
seleccionArgentina[9] =  {"Nombre": "Julian Alvarez", "Edad": 24, "Altura": 1.70, "Precio": "100 Millones", "Posicion": "Delantero"}
seleccionArgentina[8] =  {"Nombre": "Marcos Javier Acuña", "Edad": 33, "Altura": 1.72, "Precio": "2 Millones", "Posicion": "Lateral izquierdo"}
seleccionArgentina[5] =  {"Nombre": "Leandro Paredes", "Edad": 31, "Altura": 1.80, "Precio": "5 Millones", "Posicion": "Pivote"}

print("Jugadores de la Selección Argentina ")
# Imprime los encabezados de las columnas
print(f"{'Número':<8}{'Nombre':<25}{'Edad':<8}{'Altura':<10}{'Precio':<20}{'Posición':<25}")
print("-----------------------------------------------------------------------------------------------------")

# CICLO para imprimir cada jugador con formato
for numero, info in seleccionArgentina.items():
    print(f"{numero:<8}{info['Nombre']:<25}{info['Edad']:<8}{info['Altura']:<10}{info['Precio']:<20}{info['Posicion']:<25}")

print("\n")
print(f"Total de jugadores cargados: {len(seleccionArgentina)}")




