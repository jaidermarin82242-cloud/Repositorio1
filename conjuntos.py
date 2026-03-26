class nodo:
    def __init__(self, dato):

        self.dato = dato
        self.siguiente = None

class nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class conjunto:
    def __init__(self, elementos=None):
        self.cabeza = None
        self.tamano = 0

        if elementos:
            for e in elementos:
                self.agregar(e)

    def esta_vacio(self):
        return self.cabeza is None

    def cardinalidad(self):
        return self.tamano

    def pertenece(self, x):
        actual = self.cabeza
        while actual:
            if actual.dato == x:
                return True
            actual = actual.siguiente
        return False
    
    def agregar(self, x):
        if not self.pertenece(x):
            return False
        nuevo = nodo(x)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
        self.tamano += 1
        return True
    
    def eliminar(self, x):
        if self.esta_vacio():
            return False
        if self.cabeza.dato == x:
            actual.siguiente = actual.siguiente.siguiente
            self.tamano -= 1
            return True
        actual = actual.siguiente
        return False
     
    def vaciar(self):
        self.cabeza = None
        self.tamano = 0

    def union(self, dato):
        resultado = conjunto() # crear un conjunto resultado para unir los elementos de los otros conjuntos
        actual = self.cabeza 
        #unir los primeros elementos del conjunto resultado con los elementos del conjunto actual
        while actual:
            resultado.agregar(actual.dato) #agregar no deja tener datos repetidos.
            actual = actual.siguiente
        actual = dato.cabeza
        #para unir los otros elementos al otro conjunto
        while actual:
            resultado.agregar(actual.dato)
            actual = actual.siguiente
        return resultado # se recorre un conjunto, luego el otro y se van agregando los elementos al conjunto resultado.
    
    def interseccion(self, otrodato):
        resultado = conjunto()
        actual = self.cabeza
        while actual:
            if otrodato.pertenece(actual.dato): #si el elemento del conjunto actual pertenece al otro conjunto, se agrega al resultado
                resultado.agregar(actual.dato)
            actual = actual.siguiente
        return resultado
    
# casos particulares en interseccion: si un conjunto es vacío, la intersección es vacía. Si ambos conjuntos son iguales, la intersección es el mismo conjunto. Si no hay elementos comunes, la intersección es vacía.

    def diferencia(self, otrodato2):
        resultado = conjunto()
        actual = self.cabeza
        while actual:
            if not otrodato2.pertenece(actual.dato): #si el elemento del conjunto actual NO pertenece al otro conjunto, se agrega al resultado
                resultado.agregar(actual.dato)
            actual = actual.siguiente
        return resultado
    
    def diferencia_simetrica(self, otrodato3): #la diferencia simétrica es la unión de las diferencias entre ambos conjuntos, es decir, los elementos que pertenecen a uno de los conjuntos pero no a ambos.

        return self.diferencia(otrodato3).union(otrodato3.diferencia(self)) #se obtiene la diferencia de un conjunto con el otro, y luego se une con la diferencia del otro conjunto con el primero.
    
    def diferencia_simetrica_alternativa(self, otrodato3):
        resultado = conjunto()
        actual = self.cabeza
        while actual:
            if not otrodato3.pertenece(actual.dato): #si el elemento del conjunto actual NO pertenece al otro conjunto, se agrega al resultado
                resultado.agregar(actual.dato)
            actual = actual.siguiente
        actual = otrodato3.cabeza
        while actual:
            if not self.pertenece(actual.dato): #si el elemento del otro conjunto NO pertenece al conjunto actual, se agrega al resultado
                resultado.agregar(actual.dato)
            actual = actual.siguiente
        return resultado
    
    def a_lista(self):
        resultado = []
        actual = self.cabeza
        while actual:
            resultado.append(actual.dato)
            actual = actual.siguiente
        return resultado
    
    def __str__(self):
        return "{" + ", ".join(str(x) for x in self.a_lista()) + "}" #recorriendo la lista de elementos del conjunto y convirtiéndolos a string para mostrar el conjunto de forma legible.
    


A = conjunto(["A", "B", "C"])
B = conjunto(["B", "C", "D"])
C = A.diferencia_simetrica(B)
print(A)

canciones_juan = {
    "Despacito", "Shape of You", "Blinding Lights"
    "Uptown Funk", "Thinking Out Loud" "Can't Stop the Feeling!"
    "Happy", "Rolling in the Deep", "Shallow"
}

canciones_maria = {
    "Shape of You", "Blinding Lights", "Uptown Funk"
    "Drivers license", "Levitating", "Watermelon Sugar"
}
compartidas = canciones_juan & canciones_maria #operador & para obtener la intersección de los conjuntos, es decir, las canciones que ambos tienen en común.
print("Canciones compartidas:", compartidas)

compartidas_alternativa = canciones_juan.intersection(canciones_maria) #método intersection para obtener la intersección de los conjuntos, es decir, las canciones que ambos tienen en común.
print("Canciones compartidas (alternativa):", compartidas_alternativa)


#recomendacion de canciones para juan, se recomienda las canciones que maria tiene pero juan no tiene, es decir, la diferencia de maria con juan.
recomendaciones_juan = canciones_maria - canciones_juan #operador - para obtener la diferencia de los conjuntos, es decir, las canciones que maria tiene pero juan no tiene.
print("Recomendaciones para Juan:", recomendaciones_juan)

 


#catalogo de canciones: union de ambos conjuntos, es decir, todas las canciones que tienen juan y maria sin repetir.
catalogo_canciones = canciones_juan | canciones_maria #operador | para obtener la unión de los conjuntos, es decir, todas las canciones que tienen juan y maria sin repetir.
print("Catálogo de canciones:", catalogo_canciones)
catalogo_canciones_alternativa = canciones_juan.union(canciones_maria) #método union para obtener la unión de los conjuntos, es decir, todas las canciones que tienen juan y maria sin repetir.
print("Catálogo de canciones (alternativa):", catalogo_canciones_alternativa)


algoritmos = {
    "Ana", "Carlos", "Elena", "Luis", "Sofía"
    "Pedro", "Marta", "Jorge", "Lucía", "Diego"
}


bases_datos= {
    "Carlos", "Elena", "Luis", "Sofía", "Pedro"
    "Marta", "Jorge", "Lucía", "Diego", "Valentina"

}


redes = {
    "oscar", "iban", "maria", "jose", "ana"
    "carlos", "elena", "luis", "sofia", "pedro"

} 


#estudiantes que solo  vean una materia sin diferencia asimetrica: 
estudiantes_unica_materia_alternativa = (algoritmos - bases_datos - redes) | (bases_datos - algoritmos - redes) | (redes - algoritmos - bases_datos)
print("Estudiantes que solo ven una materia (alternativa):", estudiantes_unica_materia_alternativa) 

#Encontrar películas similares, que comparta por lo menos dos géneros 

#Hacer una lista de tupla: película 1, película2 y el género que comparten

def encontrar_peliculas_similares(peliculas):
    similares = []
    for i in range(len(peliculas)):
        for j in range(i + 1, len(peliculas)):
            pelicula1, generos1 = peliculas[i]
            pelicula2, generos2 = peliculas[j]
            generos_comunes = set(generos1) & set(generos2)
            if len(generos_comunes) >= 2:
                similares.append((pelicula1, pelicula2, generos_comunes))
    return similares

peliculas = [
    ("Película A", ["Acción", "Aventura", "Ciencia Ficción"]),
    ("Película B", ["Acción", "Aventura", "Fantasía"]),             
    ("Película C", ["Comedia", "Romance"]),
    ("Película D", ["Acción", "Ciencia Ficción", "Thriller"]),
    ("Película E", ["Aventura", "Fantasía", "Animación"])
]
peliculas_similares = encontrar_peliculas_similares(peliculas)
print("Películas similares (comparten al menos 2 géneros):")  


catalogo = {
    "Película A": {"Acción", "Aventura", "Ciencia Ficción"},
    "Película B": {"Acción", "Aventura", "Fantasía"},
    "Película C": {"Comedia", "Romance"},
    "Película D": {"Acción", "Ciencia Ficción", "Thriller"},
    "Película E": {"Aventura", "Fantasía", "Animación"}
}

favoritos = {"accion", "crimen", "aventura"}
#peliculas recomendadas segun los favoritos del usuario, se recomienda las peliculas que tienen al menos un genero en comun con los favoritos del usuario.
recomendaciones = []
for pelicula, generos in catalogo.items():
    if generos.intersection(favoritos):
        recomendaciones.append(pelicula)
print("Peliculas recomendadas:", recomendaciones)


#como se pueden mostrar todos los gneros que hay en el catalogo de peliculas.
generos_unicos = set() # set para tener elementos unicos no repetidos.
for generos in catalogo.values():
    generos_unicos.update(generos) #generos unicos: se actualizan os datos de cada pelicula.
print("Géneros únicos en el catálogo:", generos_unicos)

#para mostrar todos los generos en dos lineas de codigo.
generos_unicos_alternativa = set.union(*catalogo.values()) #set.union para unir todos los generos de las peliculas, *catalogo.values() para pasar los generos de cada pelicula como argumentos a la función union.
print("Géneros únicos en el catálogo (alternativa):", generos_unicos_alternativa)


#Dar el resultado de peliculas por genero, es decir, un diccionario donde la clave es el genero y el valor es una lista de peliculas que pertenecen a ese genero.
peliculas_por_genero = {}
for pelicula, generos in catalogo.items(): #recorre el catalogo, items para obtener la pelicula y sus generos.
    for genero in generos: #recorre los generos
        if genero not in peliculas_por_genero:#si el genero no esta en el diccionario,
            peliculas_por_genero[genero] = [] # se crea el la lista del genero vacia.
        peliculas_por_genero[genero].append(pelicula) #se agrega la pelicula al genero.
print("Películas por género:", peliculas_por_genero)


#metodo que reciba el nombre de dos peliculas y que devuelva el indice se similitud jaccard.
def indice_jaccard(pelicula1, pelicula2, catalogo):
    generos1 = catalogo.get(pelicula1, set()) #obtener los generos de la pelicula 1, si no existe se devuelve un set vacio.
    generos2 = catalogo.get(pelicula2, set()) #obtener los generos de la pelicula 2, si no existe se devuelve un set vacio.
    interseccion = generos1.intersection(generos2) #interseccion de los generos de las dos peliculas.
    union = generos1.union(generos2) #union de los generos de las dos peliculas.
    if not union: #si la union es vacia, el indice de jaccard es 0 porque no hay generos en comun ni en total.
        return 0.0
    return len(interseccion) / len(union) #indice de jaccard: tamaño de la interseccion dividido por el tamaño de la union.

def jaccard(pelicula1, pelicula2):
    g1 = catalogo ["Película A"]
    g2 = catalogo ["Película B"]

    interseccion = len(g1 & g2)
    union = len(g1 | g2)
    return interseccion / union 

    #stopwords: palabras comunes que no aportan mucho significado a un texto, como "el", "la", "de", "y", etc. Se suelen eliminar para mejorar el análisis de texto, ya que estas palabras pueden generar ruido y no ayudan a identificar temas o patrones relevantes en el texto.

    STOPWORDS = {"el", "la", "de", "y", "a", "en", "que", "con", "por", "para", "es", "un", "una", "los", "las"
                 "se", "del", "al", "lo", "como", "más", "pero", "sus", "le", "ya", "o", "si", "sin", "sobre",
                   "entre", "cuando", "hasta", "desde", "porque", "aunque", 
                 
                 }
    #leer dos textos y calcular el indice de similitud ignorando las stopwords
    #si el indice es mayor a 0.6, se copian los textos, si no se descartan

    def indice_similitud(texto1, texto2):
        palabras1 = set(texto1.split()) - STOPWORDS #se obtiene el conjunto de palabras del texto 1, eliminando las stopwords.
        #split: toma un String y lo divide en partes del texto o palabra.
        palabras2 = set(texto2.split()) - STOPWORDS #se obtiene el conjunto de palabras del texto 2, eliminando las stopwords.
        interseccion = len(palabras1.intersection(palabras2)) #interseccion de las palabras de los dos textos.
        union = len(palabras1.union(palabras2)) #union de las palabras de los dos textos.
        if not union: #si la union es vacia, el indice de similitud es 0 porque no hay palabras en comun ni en total.
            return 0.0
        return interseccion / union #indice de similitud: tamaño de la interseccion dividido por el tamaño de la union. 
    
    
    
