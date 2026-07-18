#Modulo de clasificacion de compromiso
def calcular_compromiso(duracion, clic):
    """
    Evalua y clasifica el nivel de compromiso de una sesion.
    R2: Logica de negocio mediante estructuras de control de condicionales.
    """
    #condicion  para compromiso alto (uso de operador AND)
    if duracion >= 180 and clic >= 8:
        return "alto"
    #condicion para compromiso bajo (uso de operador OR)
    elif duracion < 60 or clic < 3:
        return "bajo"
    #caso para compromiso medio
    else:
        return "medio"

def generar_informe(matriz, datos):
    """
    R3: recorre los datos cargados y genera el informe final por el cliente.
    """
    print("\n" + "-"*45)
    print("INFORME DE COMPROMISO DE SESIONES")
    print("-"*45)
    print(f"{'ID Cliente':<15}{'Duracion (s)':<15}{'Clics':<10}{'Clasificacion':<12}")
    print("-"*45)

    for fila in matriz:
        id_cliente = fila[0]
        duracion = fila[1]
        clic = fila[2]
        clasificacion = calcular_compromiso(duracion, clic)
        print(f"{id_cliente:<15}{duracion:<15}{clic:<10}{clasificacion:<12}")
        print("-"*45)


# =============================================================================================================
# R1: Datos iniciales (matriz con al menos 5 filas)
# ===========================================================================================
# Punto de entrada
if __name__=="__main__":
    #Estructura de datos: (ID Cliente, Duracion de la sesion en segundos, Numero de clics)
    datos_Sesiones = [
        ["C001", 200, 10], #alto compromiso (>=180 y >=8)
        ["C002", 45, 2], #bajo compromiso (<60 o <3)    
        ["C003", 120, 5], #Medio entre otros (otros casos )
        ["C004", 300, 12],#alto compromiso (>=180 y >=8)
        ["C005", 75, 2] #bajo compromiso (<60 o <3)
    ]
    while True:
        continuar = input("\n¿Desea ingresar una nueva sesion? (s/n): ").strip().lower()
        if continuar == 's':
            try:
                id_cliente = input("Ingrese el ID del cliente: ")
                duracion = int(input("Ingrese la duración de la sesión en segundos: "))
                clic = int(input("Ingrese el número de clics: "))
                nueva_sesion = [id_cliente, duracion, clic]
                datos_Sesiones.append(nueva_sesion)
                print(f"¡Sesión de {id_cliente} agregada exitosamente!")
            except ValueError:
                print("Error: Por favor, ingrese un número válido para la duración y los clics.")
        elif continuar == 'n':
            break
        else:
            print("Opción no válida. Por favor, ingrese 's' o 'n'.")
    #ejecucion_principal
    generar_informe(datos_Sesiones, None)
