from funcionesValidacion import validarSocio, validarInstructor, validarClase, validarFecha

def test_validar_socio():
    socios = [
        {"IdSocio": 1, "Activo": "Activo"},
        {"IdSocio": 2, "Activo": "Inactivo"}
    ]

    assert validarSocio(socios, 1) == True
    assert validarSocio(socios, 2) == False
    assert validarSocio(socios, 99) == False

def test_validar_instructor():
    instructores = [
        {"IdInstructor": 1, "Activo": "Activo"},
        {"IdInstructor": 2, "Activo": "Inactivo"},
        {"IdInstructor": 3, "Activo": "Activo"}
    ]

    assert validarInstructor(instructores, 1) == True    
    assert validarInstructor(instructores, 2) == False   
    assert validarInstructor(instructores, 50) == False  

def test_validar_clase():
    clases = [
        {"IdClase": 1, "Activo": "Activo"},
        {"IdClase": 2, "Activo": "Inactivo"},
        {"IdClase": 3, "Activo": "Activo"}
    ]

    assert validarClase(clases, 1) == True
    assert validarClase(clases, 2) == False
    assert validarClase(clases, 99) == False

def test_validar_fecha():
    fechas_validas = [
        "01/01/2025",
        "31/12/2024",
        "29/02/2024",
        "15/06/2020"
    ]
    
    fechas_invalidas = [
        "29/02/2023",
        "31/04/2025",
        "32/01/2025",
        "01/13/2025",
        "01-01-2025",
        ""
    ]
    
    for fecha in fechas_validas:
        assert validarFecha(fecha) == True

    for fecha in fechas_invalidas:
        assert validarFecha(fecha) == False