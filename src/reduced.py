from dataclasses import dataclass

@dataclass
class Empleado:
    nombre: str
    puesto: str
    salario: int
    
@dataclass
class Gerente:
    nombre: str
    responsability: str

e = Empleado("Ana", "Ingeniera", 50000)
print(e) # Imprime automáticamente: Empleado(nombre='Ana', puesto='Ingeniera', salario=50000)