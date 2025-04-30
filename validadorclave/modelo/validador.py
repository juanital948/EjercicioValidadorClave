from validadorclave.modelo.errores import NoCumpleLongitudMinimaError, NoTieneLetraMayusculaError, \
    NoTieneLetraMinusculaError, NoTieneNumeroError, NoTieneCaracterEspecialError


class ReglaValidacion:
    pass

class ReglaValidacionGanimedes:
    def validar(self, clave):
        if len(clave) <= 8:
            raise NoCumpleLongitudMinimaError("Debe tener más de 8 caracteres")
        if not any(c.isupper() for c in clave):
            raise NoTieneLetraMayusculaError("Debe tener al menos una letra mayúscula")
        if not any(c.islower() for c in clave):
            raise NoTieneLetraMinusculaError("Debe tener al menos una letra minúscula")
        if not any(c.isdigit() for c in clave):
            raise NoTieneNumeroError("Debe tener al menos un número")
        if not any(c in "@_#$%" for c in clave):
            raise NoTieneCaracterEspecialError("Debe tener al menos un carácter especial (@ _ # $ %)")
        return True
class ReglaValidacionCalisto:
    pass

class Validador:
    pass