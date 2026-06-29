# Dicconario de medidas en aceros incolloy

incolloy = {
    "1/2": 0.84,
    "3/4": 0.84,
    "1": 0.84,
    "1 1/4": 0.84,
    "1 1/2": 0.84
}

#

class Three:
    
    """
        Class developed exclusively for github
    """

    def clousure(self, **kwargs: str) -> None:
        """
            test data base of snickers
        """
        import time
        try:
            if "under armour" in kwargs.values():
                print('next fase ->')
                for i in range(0, 16):
                    time.sleep(2)
                    print('process...')
                    if i == 15:
                        print('sucessful')
            elif 'undefined' not in kwargs.values():
                count: int = 0
                while True:
                    count += 1
                    time.sleep(2)
                    print(f'{count*25}') # 25, 50, 75 and 100
                    if count == 4:
                        print('listo')
                        break
            else:
                raise TypeError('Error de interprete')
        except ValueError as e:
            print(f'Error: {e}')
        # return none
        

if __name__ == "__main__":
    first_three = Three()
    print(first_three)
    
    # dict
    snickers: dict[str, str] = {
    "basketball": "under armour",
    "running": "nike",
    "casual": "adidas",
    }
    
    first_three.clousure(**snickers) # desempaquetado

