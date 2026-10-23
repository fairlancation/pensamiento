# Importamos la librería pandas y le asignamos el alias 'pd' para el manejo y análisis de datos en tablas
import pandas as pd
# Importamos numpy con el alias 'np' para realizar operaciones matemáticas complejas y manejo de matrices
import numpy as np
# Importamos el módulo pyplot de matplotlib con el alias 'plt' para la creación de gráficos
import matplotlib.pyplot as plt
# Importamos datetime con el alias 'dt' para manipular y calcular fechas
import datetime as dt
# Importamos yfinance con el alias 'yf' para descargar datos financieros históricos de Yahoo Finance
import yfinance as yf

# Definimos una función para configurar y obtener los datos del mercado en un rango de fechas
def obtener_datos(acciones, inicio, fin):
    # Descargamos los datos de yfinance pasándole la lista de acciones, la fecha de inicio y la fecha de fin
    datos_acciones = yf.download(acciones, start=inicio, end=fin)
    # De todos los datos descargados, filtramos para conservar únicamente los precios de cierre diarios ('Close')
    datos_acciones = datos_acciones['Close']
    # Calculamos el rendimiento porcentual diario (cuánto subió o bajó respecto al día anterior)
    rendimientos = datos_acciones.pct_change()
    # Calculamos el promedio de estos rendimientos diarios para cada una de las acciones
    rendimientos_medios = rendimientos.mean()
    # Calculamos la matriz de covarianza, que nos dice cómo se mueven los rendimientos de las acciones entre sí
    matriz_covarianza = rendimientos.cov()
    # La función devuelve el cálculo de los rendimientos promedio y la matriz de covarianza
    return rendimientos_medios, matriz_covarianza

# Creamos una lista con los símbolos bursátiles de las empresas que queremos analizar
lista_acciones = ['CBA', 'BHP', 'TLS', 'NAB', 'WBC', 'STO']
# Añadimos el sufijo '.AX' a cada símbolo bursátil porque estas acciones cotizan en la bolsa de Australia (ASX)
acciones = [accion + '.AX' for accion in lista_acciones]
# Obtenemos la fecha actual del sistema para usarla como fecha de finalización
fecha_fin = dt.datetime.now()
# Calculamos la fecha de inicio restándole 300 días a la fecha actual
fecha_inicio = fecha_fin - dt.timedelta(days=300)

# Ejecutamos nuestra función 'obtener_datos' y guardamos los resultados en dos variables
rendimientos_medios, matriz_covarianza = obtener_datos(acciones, fecha_inicio, fecha_fin)

# Generamos valores aleatorios para decidir qué porcentaje de dinero (peso) invertiremos en cada acción
pesos = np.random.random(len(rendimientos_medios))
# Dividimos cada peso entre la suma total de los pesos para que el total de nuestra inversión sume exactamente 1 (o 100%)
pesos /= np.sum(pesos)

# Definimos la cantidad de simulaciones de Montecarlo que queremos correr
simulaciones_mc = 100
# Definimos el horizonte de tiempo (en días) que queremos proyectar hacia el futuro
periodo_dias = 100

# Creamos una matriz llena con los rendimientos medios de tamaño (días de proyección, cantidad de acciones)
matriz_medias = np.full(shape=(periodo_dias, len(pesos)), fill_value=rendimientos_medios)
# Transponemos (invertimos filas por columnas) la matriz para poder multiplicarla correctamente después
matriz_medias = matriz_medias.T

# Preparamos una matriz vacía (llena de ceros) donde guardaremos los resultados de la simulación. Su tamaño es días x simulaciones
simulaciones_portafolio = np.full(shape=(periodo_dias, simulaciones_mc), fill_value=0.0)
# Definimos el capital de dinero con el que empezaremos nuestra inversión
portafolio_inicial = 10000

# Iniciamos un bucle que se va a repetir tantas veces como simulaciones de Montecarlo definimos (100 veces)
for m in range(0, simulaciones_mc):
    # Generamos números aleatorios distribuidos de forma normal (campana de Gauss) para simular la volatilidad diaria
    Z = np.random.normal(size=(periodo_dias, len(pesos)))
    # Aplicamos la descomposición de Cholesky a la covarianza para que nuestra aleatoriedad respete la correlación entre las acciones
    L = np.linalg.cholesky(matriz_covarianza)
    # Calculamos los rendimientos diarios simulados sumando nuestro promedio a la volatilidad correlacionada generada (L * Z)
    rendimientos_diarios = matriz_medias + np.inner(L, Z)
    
    # Calculamos el rendimiento acumulado del portafolio sumando el 100% (+1) diario, multiplicándolo por la inversión inicial y lo guardamos en la matriz. (Se agregó el '*' faltante).
    simulaciones_portafolio[:, m] = np.cumprod(np.inner(pesos, rendimientos_diarios.T) + 1) * portafolio_inicial

# Usamos matplotlib para trazar todas las líneas de simulación de nuestro portafolio generadas en el bucle
plt.plot(simulaciones_portafolio)
# Le asignamos una etiqueta de texto al eje Y (vertical) de la gráfica
plt.ylabel('Valor del Portafolio ($)')
# Le asignamos una etiqueta de texto al eje X (horizontal) de la gráfica
plt.xlabel('Días')
# Le ponemos un título principal a la ventana del gráfico
plt.title('Simulación de Montecarlo')
# Finalmente, renderizamos y mostramos la gráfica en una ventana emergente en pantalla
plt.show()
