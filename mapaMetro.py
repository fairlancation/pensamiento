!pip install networkx matplotlib numpy scipy
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

%matplotlib inline
print('Versión de Networkx:', nx.__version__)
print('Versión de numpy:', np.__version__)

G=nx.Graph()
#1
G.add_node('Observatorio')
# G.add_node('Tacubaya') #1, 7 y 9
G.add_node('Juanacatlán')
G.add_node('Chapultepec')
G.add_node('Sevilla')
G.add_node('Insurgentes')
G.add_node('Cuauhtémoc')
G.add_node('Balderas') #1 y 3
G.add_node('Salto del Agua') #1 y 8
G.add_node('Isabel la Católica')
# G.add_node('Pino Suárez') #1 y 2
G.add_node('Merced')
G.add_node('Candelaria') #1 y 4
G.add_node('San Lázaro') #1 y B
G.add_node('Moctezuma')
G.add_node('Balbuena')
G.add_node('Boulevard Puerto Aéreo')
G.add_node('Gómez Farías')
G.add_node('Zaragoza')
G.add_node('Pantitlán') #1, 5, 9 y A
#2
G.add_node('Cuatro Caminos')
G.add_node('Panteones')
# G.add_node('Tacuba') #2 y 7
G.add_node('Cuitláhuac')
G.add_node('Popotla')
G.add_node('Colegio Militar')
G.add_node('Normal')
G.add_node('San Cosme')
G.add_node('Revolución')
G.add_node('Hidalgo') #2 y 3
G.add_node('Bellas Artes') #2 y 8
G.add_node('Allende')
G.add_node('Zócalo')
G.add_node('Pino Suárez') #1 y 2
G.add_node('San Antonio Abad')
G.add_node('Chabacano') #2 y 9
G.add_node('Viaducto')
G.add_node('Xola')
G.add_node('Villa de Cortés')
G.add_node('Nativitas')
G.add_node('Portales')
G.add_node('Ermita') #2 y 12
G.add_node('General Anaya')
G.add_node('Tasqueña')
#3
G.add_node('Indios Verdes')
G.add_node('Deportivo 18 de Marzo')
G.add_node('Potrero')
G.add_node('La Raza') #3 y 5
G.add_node('Tlatelolco')
G.add_node('Guerrero') #3 y B
# G.add_node('Hidalgo') #2 y 3
G.add_node('Juárez')
# G.add_node('Balderas') #1 y 3
G.add_node('Niños Héroes')
G.add_node('Hospital General')
G.add_node('Centro Médico') #3 y 9
G.add_node('Etiopía y Plaza de la Transparencia')
G.add_node('Eugenia')
G.add_node('División del Norte')
# G.add_node('Zapata')
G.add_node('Coyoacán')
G.add_node('Viveros y Derechos Humanos')
G.add_node('Miguel Ángel de Quevedo')
G.add_node('Copilco')
G.add_node('Universidad')
#4
G.add_node('Martín Carrera')
G.add_node('Talismán')
G.add_node('Bondojito')
G.add_node('Consulado') #4 y 5
G.add_node('Canal del Norte')
G.add_node('Morelos') #4 y B
# G.add_node('Candelaria') #1 y 4
G.add_node('Fray Servando')
G.add_node('Jamaica') #4 y 9
G.add_node('Santa Anita') #4 y 8
#5
G.add_node('Politécnico')
G.add_node('Instituto del Petróleo') #5 y 6
G.add_node('Autobuses del Norte')
# G.add_node('La Raza') #3 y 5
G.add_node('Misterios')
G.add_node('Valle Gómez')
G.add_node('Consulado')
G.add_node('Eduardo Molina')
G.add_node('Aragón')
G.add_node('Oceanía') #5 y B
G.add_node('Terminal Aérea')
G.add_node('Hangares')
# G.add_node('Pantitlán') #1, 5, 9 y A
#6
# G.add_node('El Rosario') #6 y 7
G.add_node('Tezozómoc')
G.add_node('Azcapotzalco')
G.add_node('Ferrería')
G.add_node('Norte 45')
G.add_node('Vallejo')
# G.add_node('Instituto del Petróleo') #5 y 6
G.add_node('Lindavista')
# G.add_node('Deportivo 18 de Marzo') #3 y 6
G.add_node('La Villa Basílica')
G.add_node('Martín Carrera')
#7
G.add_node('El Rosario')
G.add_node('Aquiles Serdán')
G.add_node('Camarones')
G.add_node('Refinería')
G.add_node('Tacuba')
G.add_node('San Joaquín')
G.add_node('Polanco')
G.add_node('Auditorio')
G.add_node('Constituyentes')
G.add_node('Tacubaya') #1, 7 y 9
G.add_node('San Pedro de los Pinos')
G.add_node('San Antonio')
G.add_node('Mixcoac') #7 y 12
G.add_node('Barranca del Muerto')
#8
G.add_node('Garibaldi')
# G.add_node('Bellas Artes') #2 y 8
G.add_node('San Juan de Letrán')
# G.add_node('Salto del Agua') #1 y 8
G.add_node('Doctores')
G.add_node('Obrera')
# G.add_node('Chabacano') #2, 8 y 9
G.add_node('La Viga')
# G.add_node('Santa Anita') #4 y 8
G.add_node('Coyuya')
G.add_node('Iztacalco')
G.add_node('Apatlaco')
G.add_node('Aculco')
G.add_node('Escuadrón 201')
G.add_node('Atlalilco') #8 y 12
G.add_node('Iztapalapa')
G.add_node('Cerro de la Estrella')
G.add_node('UAM-l')
G.add_node('Constitución de 1917')
#9
# G.add_node('Tacubaya') #1, 7 y 9
G.add_node('Patriotismo')
G.add_node('Chilpancingo')
# G.add_node('Centro Médico') #3 y 9
G.add_node('Lázaro Cárdenas')
# G.add_node('Chabacano') #2, 8 y 9
# G.add_node('Jamaica') #4 y 9
G.add_node('Mixiuhca')
G.add_node('Velódromo')
G.add_node('Ciudad Deportiva')
G.add_node('Puebla')
# G.add_node('Pantitlán') #1, 5, 9 y A
#A
# G.add_node('Pantitlán') #1, 5, 9 y A
G.add_node('Agrícola Oriental')
G.add_node('Canal de San Juan')
G.add_node('Tepalcates')
G.add_node('Guelatao')
G.add_node('Peñón Viejo')
G.add_node('Acatitla')
G.add_node('Santa María')
G.add_node('Los Reyes')
G.add_node('La Paz')
#B
G.add_node('Buenavista')
# G.add_node('Guerrero') #3 y B
# G.add_node('Garibaldi') #8 y B
G.add_node('Lagunilla')
G.add_node('Tepito')
G.add_node('Morelos')
# G.add_node('San Lázaro') #1 y B
G.add_node('Ricardo Flores Magón')
G.add_node('Romero Rubio')
# G.add_node('Oceanía')  #5 y B
G.add_node('Deportivo Oceanía')
G.add_node('Bosque de Aragón')
G.add_node('Villa de Aragón')
G.add_node('Nezahualcóyotl')
G.add_node('Río de los Remedios')
G.add_node('Impulsora')
G.add_node('Múzquiz')
G.add_node('Ecatepec')
G.add_node('Olímpica')
G.add_node('Plaza Aragón')
G.add_node('Ciudad Azteca')
#12
# G.add_node('Mixcoac') #7 y 12
G.add_node('Insurgentes Sur')
G.add_node('Hospital 20 de Noviembre')
G.add_node('Zapata') #3 y 12
G.add_node('Parque de los Venados')
G.add_node('Eje Central')
# G.add_node('Ermita') #2 y 12
G.add_node('Mexicaltzingo')
# G.add_node('Atlalilco') #8 y 12
G.add_node('Culhuacán')
G.add_node('San Andres Tomatlán')
G.add_node('Lomas Estrella')
G.add_node('Calle 11')
G.add_node('Periférico Oriente')
G.add_node('Tezonco')
G.add_node('Olivos')
G.add_node('Nopalera')
G.add_node('Zapotitlán')
G.add_node('Tlaltenco')
G.add_node('Tláhuac')


# Línea 1 (Rosa)
G.add_edges_from([('Observatorio', 'Tacubaya'), ('Tacubaya', 'Juanacatlán'), ('Juanacatlán', 'Chapultepec'), ('Chapultepec', 'Sevilla'), ('Sevilla', 'Insurgentes'), ('Insurgentes', 'Cuauhtémoc'), ('Cuauhtémoc', 'Balderas'), ('Balderas', 'Salto del Agua'), ('Salto del Agua', 'Isabel la Católica'), ('Isabel la Católica', 'Pino Suárez'), ('Pino Suárez', 'Merced'), ('Merced', 'Candelaria'), ('Candelaria', 'San Lázaro'), ('San Lázaro', 'Moctezuma'), ('Moctezuma', 'Balbuena'), ('Balbuena', 'Boulevard Puerto Aéreo'), ('Boulevard Puerto Aéreo', 'Gómez Farías'), ('Gómez Farías', 'Zaragoza'), ('Zaragoza', 'Pantitlán')])
# Línea 2 (Azul)
G.add_edges_from([('Cuatro Caminos', 'Panteones'), ('Panteones', 'Tacuba'), ('Tacuba', 'Cuitláhuac'), ('Cuitláhuac', 'Popotla'), ('Popotla', 'Colegio Militar'), ('Colegio Militar', 'Normal'), ('Normal', 'San Cosme'), ('San Cosme', 'Revolución'), ('Revolución', 'Hidalgo'), ('Hidalgo', 'Bellas Artes'), ('Bellas Artes', 'Allende'), ('Allende', 'Zócalo'), ('Zócalo', 'Pino Suárez'), ('Pino Suárez', 'San Antonio Abad'), ('San Antonio Abad', 'Chabacano'), ('Chabacano', 'Viaducto'), ('Viaducto', 'Xola'), ('Xola', 'Villa de Cortés'), ('Villa de Cortés', 'Nativitas'), ('Nativitas', 'Portales'), ('Portales', 'Ermita'), ('Ermita', 'General Anaya'), ('General Anaya', 'Tasqueña')])
# Línea 3 (Verde olivo)
G.add_edges_from([('Indios Verdes', 'Deportivo 18 de Marzo'), ('Deportivo 18 de Marzo', 'Potrero'), ('Potrero', 'La Raza'), ('La Raza', 'Tlatelolco'), ('Tlatelolco', 'Guerrero'), ('Guerrero', 'Hidalgo'), ('Hidalgo', 'Juárez'), ('Juárez', 'Balderas'), ('Balderas', 'Niños Héroes'), ('Niños Héroes', 'Hospital General'), ('Hospital General', 'Centro Médico'), ('Centro Médico', 'Etiopía y Plaza de la Transparencia'), ('Etiopía y Plaza de la Transparencia', 'Eugenia'), ('Eugenia', 'División del Norte'), ('División del Norte', 'Zapata'), ('Zapata', 'Coyoacán'), ('Coyoacán', 'Viveros y Derechos Humanos'), ('Viveros y Derechos Humanos', 'Miguel Ángel de Quevedo'), ('Miguel Ángel de Quevedo', 'Copilco'), ('Copilco', 'Universidad')])
# Línea 4 (Cian)
G.add_edges_from([('Martín Carrera', 'Talismán'), ('Talismán', 'Bondojito'), ('Bondojito', 'Consulado'), ('Consulado', 'Canal del Norte'), ('Canal del Norte', 'Morelos'), ('Morelos', 'Candelaria'), ('Candelaria', 'Fray Servando'), ('Fray Servando', 'Jamaica'), ('Jamaica', 'Santa Anita')])
# Línea 5 (Amarilla)
G.add_edges_from([('Politécnico', 'Instituto del Petróleo'), ('Instituto del Petróleo', 'Autobuses del Norte'), ('Autobuses del Norte', 'La Raza'), ('La Raza', 'Misterios'), ('Misterios', 'Valle Gómez'), ('Valle Gómez', 'Consulado'), ('Consulado', 'Eduardo Molina'), ('Eduardo Molina', 'Aragón'), ('Aragón', 'Oceanía'), ('Oceanía', 'Terminal Aérea'), ('Terminal Aérea', 'Hangares'), ('Hangares', 'Pantitlán')])
# Línea 6 (Roja)
G.add_edges_from([('El Rosario', 'Tezozómoc'), ('Tezozómoc', 'Azcapotzalco'), ('Azcapotzalco', 'Ferrería'), ('Ferrería', 'Norte 45'), ('Norte 45', 'Vallejo'), ('Vallejo', 'Instituto del Petróleo'), ('Instituto del Petróleo', 'Lindavista'), ('Lindavista', 'Deportivo 18 de Marzo'), ('Deportivo 18 de Marzo', 'La Villa Basílica'), ('La Villa Basílica', 'Martín Carrera')])
# Línea 7 (Naranja)
G.add_edges_from([('El Rosario', 'Aquiles Serdán'), ('Aquiles Serdán', 'Camarones'), ('Camarones', 'Refinería'), ('Refinería', 'Tacuba'), ('Tacuba', 'San Joaquín'), ('San Joaquín', 'Polanco'), ('Polanco', 'Auditorio'), ('Auditorio', 'Constituyentes'), ('Constituyentes', 'Tacubaya'), ('Tacubaya', 'San Pedro de los Pinos'), ('San Pedro de los Pinos', 'San Antonio'), ('San Antonio', 'Mixcoac'), ('Mixcoac', 'Barranca del Muerto')])
# Línea 8 (Verde)
G.add_edges_from([('Garibaldi', 'Bellas Artes'), ('Bellas Artes', 'San Juan de Letrán'), ('San Juan de Letrán', 'Salto del Agua'), ('Salto del Agua', 'Doctores'), ('Doctores', 'Obrera'), ('Obrera', 'Chabacano'), ('Chabacano', 'La Viga'), ('La Viga', 'Santa Anita'), ('Santa Anita', 'Coyuya'), ('Coyuya', 'Iztacalco'), ('Iztacalco', 'Apatlaco'), ('Apatlaco', 'Aculco'), ('Aculco', 'Escuadrón 201'), ('Escuadrón 201', 'Atlalilco'), ('Atlalilco', 'Iztapalapa'), ('Iztapalapa', 'Cerro de la Estrella'), ('Cerro de la Estrella', 'UAM-l'), ('UAM-l', 'Constitución de 1917')])
# Línea 9 (Café)
G.add_edges_from([('Tacubaya', 'Patriotismo'), ('Patriotismo', 'Chilpancingo'), ('Chilpancingo', 'Centro Médico'), ('Centro Médico', 'Lázaro Cárdenas'), ('Lázaro Cárdenas', 'Chabacano'), ('Chabacano', 'Jamaica'), ('Jamaica', 'Mixiuhca'), ('Mixiuhca', 'Velódromo'), ('Velódromo', 'Ciudad Deportiva'), ('Ciudad Deportiva', 'Puebla'), ('Puebla', 'Pantitlán')])
# Línea A (Morada)
G.add_edges_from([('Pantitlán', 'Agrícola Oriental'), ('Agrícola Oriental', 'Canal de San Juan'), ('Canal de San Juan', 'Tepalcates'), ('Tepalcates', 'Guelatao'), ('Guelatao', 'Peñón Viejo'), ('Peñón Viejo', 'Acatitla'), ('Acatitla', 'Santa María'), ('Santa María', 'Los Reyes'), ('Los Reyes', 'La Paz')])
# Línea B (Verde y Gris)
G.add_edges_from([('Buenavista', 'Guerrero'), ('Guerrero', 'Garibaldi'), ('Garibaldi', 'Lagunilla'), ('Lagunilla', 'Tepito'), ('Tepito', 'Morelos'), ('Morelos', 'San Lázaro'), ('San Lázaro', 'Ricardo Flores Magón'), ('Ricardo Flores Magón', 'Romero Rubio'), ('Romero Rubio', 'Oceanía'), ('Oceanía', 'Deportivo Oceanía'), ('Deportivo Oceanía', 'Bosque de Aragón'), ('Bosque de Aragón', 'Villa de Aragón'), ('Villa de Aragón', 'Nezahualcóyotl'), ('Nezahualcóyotl', 'Río de los Remedios'), ('Río de los Remedios', 'Impulsora'), ('Impulsora', 'Múzquiz'), ('Múzquiz', 'Ecatepec'), ('Ecatepec', 'Olímpica'), ('Olímpica', 'Plaza Aragón'), ('Plaza Aragón', 'Ciudad Azteca')])
# Línea 12 (Dorada)
G.add_edges_from([('Mixcoac', 'Insurgentes Sur'), ('Insurgentes Sur', 'Hospital 20 de Noviembre'), ('Hospital 20 de Noviembre', 'Zapata'), ('Zapata', 'Parque de los Venados'), ('Parque de los Venados', 'Eje Central'), ('Eje Central', 'Ermita'), ('Ermita', 'Mexicaltzingo'), ('Mexicaltzingo', 'Atlalilco'), ('Atlalilco', 'Culhuacán'), ('Culhuacán', 'San Andres Tomatlán'), ('San Andres Tomatlán', 'Lomas Estrella'), ('Lomas Estrella', 'Calle 11'), ('Calle 11', 'Periférico Oriente'), ('Periférico Oriente', 'Tezonco'), ('Tezonco', 'Olivos'), ('Olivos', 'Nopalera'), ('Nopalera', 'Zapotitlán'), ('Zapotitlán', 'Tlaltenco'), ('Tlaltenco', 'Tláhuac')])


# Ampliar significativamente el lienzo para evitar superposiciones
plt.figure(figsize=(25, 25))

# kamada_kawai_layout suele funcionar mejor para distribuir redes de transporte sin coordenadas
pos = nx.kamada_kawai_layout(G)

# Aquí puse otro método de impresión para que no se vea superpuesto, puesto que se veía mal de tal modo
# Dibujar ajustando proporciones geométricas
nx.draw(G, pos,
        with_labels=True,
        font_size=9,
        font_weight='bold',
        node_size=180,
        node_color='lightblue',
        edge_color='gray')
plt.show()
