# ==============================================================================
# EJERCICIOS DE FUNCIONES EN PYTHON (1 al 60)
# Referencias:
# - El Pythonista: https://elpythonista.com/funciones-en-python-guia-completa-2025-sintaxis-parametros-y-ejemplos
# - Pythones: https://pythones.net/funciones-en-python-3-tipos-y-sintaxis/
# ==============================================================================

# ------------------------------------------------------------------------------
# BLOQUE 1: LISTA DEL 1 AL 30 (HOMBRES Y MUJERES)
# Incluye 6 ejemplos adaptados de la guía de El Pythonista
# ------------------------------------------------------------------------------

#Matias Lopez NC 0117
# Lista de personas del 1 al 30 (15 hombres, 15 mujeres)
personas_1_30 = [
    {"id": 1, "nombre": "Carlos", "genero": "hombre"},
    {"id": 2, "nombre": "Ana", "genero": "mujer"},
    {"id": 3, "nombre": "Luis", "genero": "hombre"},
    {"id": 4, "nombre": "María", "genero": "mujer"},
    {"id": 5, "nombre": "Jorge", "genero": "hombre"},
    {"id": 6, "nombre": "Laura", "genero": "mujer"},
    {"id": 7, "nombre": "Fernando", "genero": "hombre"},
    {"id": 8, "nombre": "Sofía", "genero": "mujer"},
    {"id": 9, "nombre": "Diego", "genero": "hombre"},
    {"id": 10, "nombre": "Carmen", "genero": "mujer"},
    {"id": 11, "nombre": "Gabriel", "genero": "hombre"},
    {"id": 12, "nombre": "Lucía", "genero": "mujer"},
    {"id": 13, "nombre": "Alejandro", "genero": "hombre"},
    {"id": 14, "nombre": "Elena", "genero": "mujer"},
    {"id": 15, "nombre": "Javier", "genero": "hombre"},
    {"id": 16, "nombre": "Patricia", "genero": "mujer"},
    {"id": 17, "nombre": "Manuel", "genero": "hombre"},
    {"id": 18, "nombre": "Isabel", "genero": "mujer"},
    {"id": 19, "nombre": "Ricardo", "genero": "hombre"},
    {"id": 20, "nombre": "Marta", "genero": "mujer"},
    {"id": 21, "nombre": "Roberto", "genero": "hombre"},
    {"id": 22, "nombre": "Paula", "genero": "mujer"},
    {"id": 23, "nombre": "Andrés", "genero": "hombre"},
    {"id": 24, "nombre": "Valeria", "genero": "mujer"},
    {"id": 25, "nombre": "Daniel", "genero": "hombre"},
    {"id": 26, "nombre": "Claudia", "genero": "mujer"},
    {"id": 27, "nombre": "Marcos", "genero": "hombre"},
    {"id": 28, "nombre": "Beatriz", "genero": "mujer"},
    {"id": 29, "nombre": "Gonzalo", "genero": "hombre"},
    {"id": 30, "nombre": "Rocío", "genero": "mujer"}
]

# --- Ejemplos basados en "El Pythonista" ---

# Ejemplo 1: Sintaxis básica y definición de función (Saludo personalizado)
def saludar_persona(nombre, genero):
    tratamiento = "Bienvenido" if genero == "hombre" else "Bienvenida"
    print(f"Hola, {nombre}. ¡{tratamiento} al sistema!")

# Ejemplo 2: Parámetros posicionales y retorno de valores
def obtener_etiqueta_id(id_persona, nombre):
    return f"ID #{id_persona:02d} -> {nombre}"

# Ejemplo 3: Parámetros con valores por defecto (Default arguments)
def registrar_asistencia(nombre, estado="Presente"):
    return f"Usuario {nombre}: {estado}"

# Ejemplo 4: Uso de *args (Argumentos variables posicionales)
def listar_hombres(*nombres):
    print("Lista de hombres registrados en la selección:")
    for nombre in nombres:
        print(f"- {nombre}")

# Ejemplo 5: Uso de **kwargs (Argumentos variables por clave)
def mostrar_ficha_tecnica(**datos):
    print("--- Ficha de Registro ---")
    for clave, valor in datos.items():
        print(f"{clave.capitalize()}: {valor}")

# Ejemplo 6: Expresiones Lambda e iteración sobre listas
filtrar_hombres = lambda lista: [p["nombre"] for p in lista if p["genero"] == "hombre"]


# ------------------------------------------------------------------------------
# BLOQUE 2: LISTA DEL 31 AL 60 (HOMBRES Y MUJERES)
# Incluye 5 ejemplos adaptados de la guía de Pythones
# ------------------------------------------------------------------------------

# Lista de personas del 31 al 60 (15 hombres, 15 mujeres)
personas_31_60 = [
    {"id": 31, "nombre": "Raúl", "genero": "hombre"},
    {"id": 32, "nombre": "Alicia", "genero": "mujer"},
    {"id": 33, "nombre": "Enrique", "genero": "hombre"},
    {"id": 34, "nombre": "Lorena", "genero": "mujer"},
    {"id": 35, "nombre": "Hugo", "genero": "hombre"},
    {"id": 36, "nombre": "Silvia", "genero": "mujer"},
    {"id": 37, "nombre": "Víctor", "genero": "hombre"},
    {"id": 38, "nombre": "Natalia", "genero": "mujer"},
    {"id": 39, "nombre": "Adrián", "genero": "hombre"},
    {"id": 40, "nombre": "Irene", "genero": "mujer"},
    {"id": 41, "nombre": "Óscar", "genero": "hombre"},
    {"id": 42, "nombre": "Monica", "genero": "mujer"},
    {"id": 43, "nombre": "Rubén", "genero": "hombre"},
    {"id": 44, "nombre": "Camila", "genero": "mujer"},
    {"id": 45, "nombre": "Alfonso", "genero": "hombre"},
    {"id": 46, "nombre": "Julia", "genero": "mujer"},
    {"id": 47, "nombre": "Pablo", "genero": "hombre"},
    {"id": 48, "nombre": "Sara", "genero": "mujer"},
    {"id": 49, "nombre": "Ignacio", "genero": "hombre"},
    {"id": 50, "nombre": "Miriam", "genero": "mujer"},
    {"id": 51, "nombre": "Guillermo", "genero": "hombre"},
    {"id": 52, "nombre": "Esther", "genero": "mujer"},
    {"id": 53, "nombre": "César", "genero": "hombre"},
    {"id": 54, "nombre": "Daniela", "genero": "mujer"},
    {"id": 55, "nombre": "Mario", "genero": "hombre"},
    {"id": 56, "nombre": "Rosa", "genero": "mujer"},
    {"id": 57, "nombre": "Tomás", "genero": "hombre"},
    {"id": 58, "nombre": "Cristina", "genero": "mujer"},
    {"id": 59, "nombre": "Jaime", "genero": "hombre"},
    {"id": 60, "nombre": "Noelia", "genero": "mujer"}
]

# --- Ejemplos basados en "Pythones" ---

# Ejemplo 7 (Pythones 1): Función Nula (Void function / sin return explícito)
def imprimir_separador():
    print("=" * 50)

# Ejemplo 8 (Pythones 2): Función con Retorno Fraccionado / Múltiples Valores (Tupla)
def separar_por_genero(lista_personas):
    hombres = [p["nombre"] for p in lista_personas if p["genero"] == "hombre"]
    mujeres = [p["nombre"] for p in lista_personas if p["genero"] == "mujer"]
    return hombres, mujeres

# Ejemplo 9 (Pythones 3): Tipado de Parámetros y Scope / Ámbito de Variables
def contar_registros_por_rango(inicio: int, fin: int) -> int:
    # 'total' es una variable de ámbito local
    total = (fin - inicio) + 1
    return total

# Ejemplo 10 (Pythones 4): Funciones compuestas o anidadas (Closure simple)
def creador_de_saludo_por_rol(rol):
    def saludar(nombre):
        return f"[{rol.upper()}] Estimado {nombre}, acceso concedido."
    return saludar

# Ejemplo 11 (Pythones 5): Pasar funciones como argumentos (First-class functions)
def procesar_lista(lista, funcion_callback):
    for elemento in lista:
        funcion_callback(elemento)


# ------------------------------------------------------------------------------
# EJECUCIÓN Y PRUEBAS
# ------------------------------------------------------------------------------

if __name__ == "__main__":
    imprimir_separador()
    print("EJECUCIÓN DE EJEMPLOS: BLOQUE 1 (EL PYTHONISTA - IDs 1 a 30)")
    imprimir_separador()

    # Probando Ejemplos 1 y 2 con el usuario 1 (Carlos)
    p1 = personas_1_30[0]
    saludar_persona(p1["nombre"], p1["genero"])
    print(obtener_etiqueta_id(p1["id"], p1["nombre"]))

    # Probando Ejemplo 3
    print(registrar_asistencia(personas_1_30[1]["nombre"]))

    # Probando Ejemplo 4 y 6 (Filtrar y listar hombres de la lista 1-30)
    hombres_bloque1 = filtrar_hombres(personas_1_30)
    listar_hombres(*hombres_bloque1[:3])  # Primeros 3 hombres

    # Probando Ejemplo 5
    mostrar_ficha_tecnica(id=p1["id"], nombre=p1["nombre"], perfil="Usuario Activo")

    print("\n")
    imprimir_separador()
    print("EJECUCIÓN DE EJEMPLOS: BLOQUE 2 (PYTHONES - IDs 31 a 60)")
    imprimir_separador()

    # Probando Ejemplo 8 (Retorno múltiple)
    hombres_b2, mujeres_b2 = separar_por_genero(personas_31_60)
    print(f"Total hombres (31-60): {len(hombres_b2)}")
    print(f"Total mujeres (31-60): {len(mujeres_b2)}")

    # Probando Ejemplo 9
    print(f"Registros procesados en el bloque: {contar_registros_por_rango(31, 60)}")

    # Probando Ejemplo 10
    saludo_admin = creador_de_saludo_por_rol("Administrador")
    print(saludo_admin(personas_31_60[0]["nombre"]))  # Raúl

    # Probando Ejemplo 11
    print("\nProcesando los primeros 3 registros de la lista 31-60:")
    procesar_lista(personas_31_60[:3], lambda p: print(f"ID {p['id']}: {p['nombre']} ({p['genero']})"))
    print("Matias Lopez NC 0117")