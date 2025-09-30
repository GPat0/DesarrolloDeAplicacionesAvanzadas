class Queue:
    def __init__(self):
        #pila de entrada aqui se mete con enqueue
        self._in = []
        #pila de salida de aqui se saca con dequeue
        self._out = []

    def _rebalance(self):
        #si _out esta vacia, movemos todos los elementos desde _in
        if not self._out:
            #mientras _in tenga elementos
            while self._in:
                #se pasa el ultimo de _in al final de _out
                self._out.append(self._in.pop())

    def enqueue(self, x):
        #se agrega x a la queue metiendolo en _in
        self._in.append(x)

    def dequeue(self):
        #aseguramos que _out tenga el frente listo
        self._rebalance()
        #si aun asi _out esta vacia, no hay elementos en toda la queue
        if not self._out:
            # se lanza error claro por intento de sacar de cola vacia
            raise IndexError("dequeue empty queue")
        #saca y regresa el tope de _out (
        return self._out.pop()

    def front(self):
        #aseguramos que _out tenga el frente listo
        self._rebalance()
        #si _out esta vacia, la queue esta vacia y no hay frente que ver
        if not self._out:
            # error claro
            raise IndexError("front empty queue")
        #se regresa el elemento en el tope de _out sin quitarlo
        return self._out[-1]

    # notas
    # - fifo significa que sale primero lo que entro primero
    # - se puede meter cualquier tipo de dato sin validacion adicional
