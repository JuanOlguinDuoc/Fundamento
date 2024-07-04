def registro (registros):
    nombre          = ""
    apellido        = ""
    direccion       = ""
    totalHosp       = 0
    totalInsumos    = 0
    totalBono       = 0
    total           = 0
    dias            = 0
    
    while True:
        if len(nombre) <= 0:
            nombre      = input("Ingrese un nombre: ").upper()
        elif len(apellido) <= 0:
            apellido    = input("Ingrese un apellido: ").upper()
        elif len(direccion) <= 0:
            direccion   = input("Ingrese una dirección: ").upper()
        elif totalHosp == 0:
            while True:
                try:
                    dias = int(input("Ingrese el total de días hospitalizado: "))
                    break
                except ValueError:
                    print("Debe ingresar un numero")
            totalHosp += dias * 90000
        elif totalInsumos == 0:
            while True:
                try:
                    totalInsumos = int(input("Ingrese el total por concepto de insumos médicos: "))
                    break
                except ValueError:
                    print("Debe ingresar un número") 
        else:
            break
        totalBono = round((totalHosp + totalInsumos) * 0.7)   
        total += totalHosp + totalInsumos - totalBono
    registros.append({
        "Paciente"              : nombre + " " + apellido,
        "Direccion"             : direccion,
        "Hospitalizacion"       : totalHosp,
        "Insumos"               : totalInsumos,
        "Bonificacion"          : totalBono,
        "Total"                 :total
    })
    
    print(f"""
    REGISTRO EXITOSO
          
    Paciente:           {nombre} {apellido}
    Dirección:          {direccion}
    Hospitalización:    ${totalHosp}
    Insumos:            ${totalInsumos}
    Bonos:              ${totalBono}
    TOTAL:              ${total}

""")


def listar(registros):
    for registro in range(len(registros)):
        paciente = registros[registro]
        print(f"""
    Paciente:           {paciente["Paciente"]}
    Dirección:          {paciente["Direccion"]}
    Hospitalización:    ${paciente["Hospitalizacion"]}
    Insumos:            ${paciente["Insumos"]}
    Bonos:              ${paciente["Bonificacion"]}
    TOTAL:              ${paciente["Total"]}
""")
        

        
def despacho(registros):
    sector = ["C", "N", "S"]
    opc = ""
    while True:
        if len(opc) == 0:
            opc = input("¿A que sector desea enviar el despacho? (C/N/S): ").upper()

        elif opc in sector:
            print("Si esta")
            
            break
        else:
            print("No esta")
            opc = input("¿A que sector desea enviar el despacho? (C/N/S): ").upper()
            