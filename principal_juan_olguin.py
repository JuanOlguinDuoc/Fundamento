import funciones_juan_olguin as fn
registros = []

opciones = {
    1: fn.registro,
    2: fn.listar,
    3: fn.despacho
}



while True:
    print("""
1. Registrar Cobro
2. Listar Cobros Registrados
3. Definir Sector de Despacho
4. Salir
""")
    try:

        opc = int(input("Ingrese una opción: "))
            
        if opc == 4:
            print("Saliendo...")
            break

        if opc in opciones:
            opciones[opc](registros)
        else:
            print("Opcion ingresada no válida")

    except ValueError:
        print("Debe ingresar una opción válida")
