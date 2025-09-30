from stack import Stack
from queue_ds import Queue
from symbol_table import SymbolTable

def run_tests():
    # ----- pruebas de stack (lifo) -----
    s = Stack()               #aqui crea la pila
    s.push("id")              
    s.push("+")               
    s.push("num")             
    assert s.peek() == "num"  #el tope debe ser num
    assert s.pop() == "num"   #al sacar, sale num
    assert s.peek() == "+"    #nuevo tope es +

    # ----- pruebas de queue (fifo) -----
    q = Queue()                          #crea la queue
    q.enqueue("token(id)")               
    q.enqueue("token(+)")                
    assert q.front() == "token(id)"      #frente correcto
    assert q.dequeue() == "token(id)"    #sale token(id)
    assert q.front() == "token(+)"       #ahora el frente es token(+)

    # ----- pruebas de symbol table -----
    st = SymbolTable()                         #crea la tabla
    st.set("x", {"type":"int","addr":0})       #guarda un dict en x
    st.set("y", 3.14)                          #guarda un numero en y
    assert st.get("x")["type"] == "int"        #lee parte del dict
    assert st.delete("x")                       
    assert st.get("x") is None                 

def demo():

    print("== stack ==")
    s = Stack()                       #nueva pila
    for x in ("id", "+", "num"):      #mete tres elementos
        s.push(x)
    print("peek:", s.peek(),          #mira el tope 
          "pop:", s.pop(),            #saca el tope 
          "peek:", s.peek())          #mira nuevo tope 

    print("\n== queue ==")
    q = Queue()                               #nueva queue
    for t in ("token(id)", "token(+)", "token(num)"):
        q.enqueue(t)                          
    print("front:", q.front(),                
          "dequeue:", q.dequeue(),            
          "front:", q.front())                

    print("\n== symbol table ==")
    st = SymbolTable()                        #nueva tabla
    st.set("x", {"type":"int","addr":0})      #guarda dict en x
    st.set("y", {"type":"float","addr":4})    #guarda dict en y
    print("get(x):", st.get("x"))             #imprime valor de x
    #ejemplo de mutabilidad, esto cambia el dict guardado en x
    st.get("x")["type"] = "float"
    print("get(x) modificado:", st.get("x"))  #muestra el cambio
    st.delete("x")                             
    print("after delete x -> get(x):", st.get("x"))  #none

if __name__ == "__main__":
    run_tests()
    print("all basic tests passed.")
    demo()
