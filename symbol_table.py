class SymbolTable:
    def __init__(self):
        self._d = {}

    def set(self, k, v):
        #se vuarda o se actualiza la clave k con el valor v
        #si k ya existia, el valor anterior se reemplaza
        self._d[k] = v

    def get(self, k, default=None):
        #regresa el valor de la clave k
        #si no existe, regresa default 
        #se regresa la misma referencia que se guardo
        return self._d.get(k, default)

    def delete(self, k):
        #elimina la clave k si existe
        #regresa true si se borro, false si no existia
        return self._d.pop(k, None) is not None

    # notas
    # - mutabilidad, si se hace get("x") y se modifica el dict, se cambia lo almacenado
    #   ejemplo: get("x")["type"] = "float" modifica el valor guardado
