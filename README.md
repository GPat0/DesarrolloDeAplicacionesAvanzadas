# tarea #1 – estructuras basicas (stack, queue, symbol table)
lenguaje: python

## objetivo
implementar 3 estructuras simples sin librerias externas y demostrar su uso:
- stack (lifo) con list
- queue (fifo) con dos pilas internas (listas)
- symbol table (hash) con dict nativo

incluye:
- un programa pequeno que las manipula (`demo()`)
- pruebas basicas con `assert` (`run_tests()`)

## por que asi y como funciona
- **stack (stack.py)**
  - usa una lista interna `_data`.
  - `push(x)` agrega al final (tope).
  - `pop()` saca el ultimo. si esta vacia lanza `indexerror`.
  - `peek()` mira el ultimo sin sacarlo. si esta vacia lanza `indexerror`.
  - costo aproximado: push/pop/peek o(1).
- **queue (queue_ds.py)**
  - usa dos listas: `_in` y `_out`.
  - `enqueue(x)` mete en `_in`.
  - `dequeue()` y `front()` primero llaman `_rebalance()`:
    - si `_out` esta vacia, mueve todo desde `_in` a `_out` (invertido).
    - el frente queda en el tope de `_out`.
  - costo amortizado o(1) para enqueue/dequeue/front.
- **symbol table (symbol_table.py)**
  - usa `dict` nativo `_d`.
  - `set(k, v)` inserta o actualiza la clave.
  - `get(k, default)` regresa el valor o `default` si no existe.
  - `delete(k)` borra la clave si existe y regresa `true`/`false`.
  - costo promedio o(1).


## casos de exito
- **stack**
  - push de "id", "+", "num" -> peek devuelve "num"; pop devuelve "num"; peek queda en "+".
- **queue**
  - enqueue de "token(id)", "token(+)" -> front devuelve "token(id)"; dequeue devuelve "token(id)"; nuevo front "token(+)".
- **symbol table**
  - set("x", {"type":"int","addr":0}) -> get("x") regresa ese dict.
  - delete("x") -> true; luego get("x") -> none.

## que pasa si se modifican parte del codigo
- **stack**
  - pop/peek con pila vacia -> `indexerror` (intencional, ayuda a detectar errores).
  - cambiar `self._data` por algo que no sea list -> los metodos pueden fallar.
  - mezclar tipos (str, int, dict) -> permitido, la pila solo almacena.
- **queue**
  - dequeue/front con cola vacia -> `indexerror`.
  - cambiar `self._in` o `self._out` por otros tipos o reasignarlos raro -> se rompe la logica fifo.
  - encolar `none` o cadenas vacias -> permitido, la cola solo almacena.
- **symbol table**
  - set en clave existente -> reemplaza el valor anterior (ultimo valor gana).
  - get de clave inexistente -> regresa `default` .
  - **mutabilidad**: get("x") regresa la **misma referencia**. si haces `get("x")["type"] = "float"`, cambias lo guardado.
    - si en dado caso no se requiera eso, se puede usar lo siguiente: `info = dict(get("x"))` y se modifica `info`.
  - delete de clave inexistente -> regresa false, no lanza error.

## pruebas incluidas
- valida orden lifo en stack.
- valida orden fifo en queue.
- valida set/get/delete en symbol table y que una clave borrada ya no se lea.
