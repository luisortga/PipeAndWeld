# Diccionario de medidas en aceros alloy

alloy = {
    "1/2": 0.84,
    "3/4": 0.84,
    "1": 0.84,
    "1 1/4": 0.84,
    "1 1/2": 0.84
}

incolloy = {
    '1/2': 0.84,
    '1.0' : 0.94,
    '1.5': 1.2
}

inox = {
    'rust': 16,
    'ruby': 18
}

# manipular datos

class Meta:
    
    def __init__(self) -> None:
        pass
    
    def empaquetado(self, biblioteca: dict[str, str | int]):
        """
            datos empaquetados.
        """
        
        total: int = sum(valor for valor in biblioteca.values() if isinstance(valor, int))
        print(total)
        for valor in biblioteca.values():
            if isinstance(valor, str):
                print(f'mark {valor}')
            else:
                print(f"num {valor}")
    
    def desempaquetado(self, **kwargs: str):
        total: int = 0
        for k, v in kwargs.items():
            if isinstance(v, int):
                print(k)
                total += v
                print(f'El total va {total}')
            else:
                print(f'key: {k} and value {v}')
    
    def tensores_test(self, tensores: dict[str, dict[str, str | int] | tuple[str, ...]]):
        pass
    
class Data:
    
    def __init__(self,) -> None:
        pass
    
    def bibliotecas(self) -> dict[str, str | int]:
        return {
            'basketball': 'nike air',
            'running': 'under armour',
            'casual': 'adidas',
            'extreme': 'caterpiller',
            'court': 16,
            'tennis': 28
        }
        
    def tensor(self) -> dict[str, dict[str, str | int]]:
        return {
            
        }
        
if __name__ == "__main__":
    
    datos: Data = Data()
    logic = Meta()
    
    database: dict[str, str | int] = datos.bibliotecas()
    
    logic.empaquetado(database)
    
    # desempaquetado