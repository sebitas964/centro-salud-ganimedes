def validar_dni(dni):
    if not dni.isdigit() or len(dni) != 8:
        raise ValueError("El DNI debe contener exactamente 8 dígitos")
    return True