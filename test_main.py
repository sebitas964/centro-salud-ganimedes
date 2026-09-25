from main import validar_dni

def test_validar_dni_correcto():
    assert validar_dni("12345678") is True

def test_validar_dni_incorrecto():
    try:
        validar_dni("1234")
        assert False
    except ValueError:
        assert True

def test_validar_dni_no_numerico():
    try:
        validar_dni("12AB5678")
        assert False
    except ValueError:
        assert True