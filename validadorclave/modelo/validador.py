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

class ReglaValidacionCalisto:
    pass

class Validador:
    pass