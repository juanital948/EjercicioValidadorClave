from validadorclave.modelo.errores import NoCumpleLongitudMinimaError, NoTieneLetraMayusculaError, \
    NoTieneLetraMinusculaError, NoTieneNumeroError, NoTieneCaracterEspecialError, NoTienePalabraSecretaError, \
    ValidadorError


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
    def validar(self, clave):
        if len(clave) <= 6:
            raise NoCumpleLongitudMinimaError("Debe tener más de 6 caracteres")
        if not any(c.isdigit() for c in clave):
            raise NoTieneNumeroError("Debe tener al menos un número")
        if "calisto" not in clave.lower():
            raise NoTienePalabraSecretaError("Debe contener la palabra 'calisto'")
        for i in range(len(clave) - 6):
            parte = clave[i:i + 7]
            if parte.lower() == "calisto":
                mayus = sum(1 for c in parte if c.isupper())
                if 2 <= mayus < 7:
                    return True
        raise NoTienePalabraSecretaError(
            "La palabra 'calisto' debe tener al menos 2 letras en mayúscula, pero no todas")



 class Validador:
        def _init_(self, regla):
            self.regla = regla

        def es_valida(self, clave):
            try:
                return self.regla.es_valida(clave)
            except ValidadorError as e:
                raise e
