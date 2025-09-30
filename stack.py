

class Stack:
    #se definio la clase stack
    def __init__(self):
        #se crrea la estructura interna como lista vacia
        self._data = []

    def push(self, x):
        #mete x al final de la lista  
        self._data.append(x)

    def pop(self):
        #si la lista esta vacia, no hay que sacar, se lanza error claro
        if not self._data:
            raise IndexError("pop empty stack")
        #saca y regresa el ultimo elemento
        return self._data.pop()

    def peek(self):
        #si laa lista esta vacia, no hay tope que mirar
        if not self._data:
            # se lanza error claro
            raise IndexError("peek empty stack")
        #se regresa el ultimo elemento sin quitarlo
        return self._data[-1]

    # notas 
    # - el tope es siempre self._data[-1]
    # - se puede guardar cualquier tipo: str, int, dict, etc
    # - si se cambia self._data por algo que no sea list, los metodos pueden fallar
