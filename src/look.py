import re
import math

def __init__():
    pass

def large_pipe(text):
    # Encontrar el largo de la tubería
    ptt = r"\d\.\d"
    pipe = re.search(ptt, text)
    large = pipe.group()
    large = float(large)
    return large

def tan(grados):
    new_grade: float = grados/2
    tangente: float = math.tan(math.radians(new_grade))
    return tangente

def advanced_elbow(inch, tangente_30, tangente_60):
    """
    Docstring  funcion
    @author: luis
    """
    advanced_90 = inch*1.5
    advanced_90 = advanced_90*25.4 # codo de 90 grade

    advanced_45 = inch*0.625
    advanced_45 = advanced_45*25.4 # codo de 45 grade

    advanced_30: float = inch*38.1*tangente_30 # codo degradado especial 30 grade

    advanced_60: float = inch*38.1*tangente_60 # codo degradado especial 30 grade

    print("Avances de tuberia R.L. en milimetros: ")
    print(f"El avance de un codo de 90 grados radio largo de {inch} pulgas es: {advanced_90} mm")
    print(f"El avance de un codo de 45 grados radio largo de {inch} pulgadas es: {advanced_45} mm")
    print(f"El avance de un codo de 30 grados radio largo de {inch} pulgadas es: {advanced_30} mm")
    print(f"El avance de un codo de 60 grados radio largo de {inch} pulgadas es: {advanced_60} mm")

def peso(od: float, t: float, c: float = 0.02491):
    calculo: float = (od-t)*t*c
    return calculo

# Main
if __name__ == "__main__":
    text = "10 Pipes, EFW + 100% RT, ASME C3ZCF0T2 6.6 M B36.19/B36.10, ASTM A358 Gr.304/304L Cl.1, BE, -, Imp Tested -196°C, Cryo Serv., S-10S"

    print("Con los datos obtenidos se calculo lo siguiente:")

    # Buscamos el primer grupo de números en el texto
    pattern = re.search(r'\d+', text)

    if pattern:
        # Si encuentra un número, lo extraemos y lo convertimos a int
        pipe_inches = int(pattern.group()) # Salida: El número es: 10
    else:
        print("No se encontro las pulgadas diametrales de la tubería.")

    tg_30 = tan(30)
    tg_60 = tan(60)

    advanced_elbow(pipe_inches, tg_30, tg_60)

    # Obtenemos del metodo large_pipe el largo de la tuberia en una variable float
    large = large_pipe(text)

    inox_304 = re.search("304/304L", text)
    inox_316 = re.search("316/316L", text)
    carbon_steel = re.search("A36", text)

    # atributo del material
    material = None

    # Elejimos el material
    if inox_304: material = "inox 304"
    elif inox_316: material = "inox 316"
    elif carbon_steel: material = "carbon steel"
    else: material = "No tiene un material definido"

    print(f"El mateial es {material}")

    # Convertir la cedula en mm
    # <= == === !=
    cedula_mm= 0.0

    pulgada: float = pipe_inches

    cedula = re.search("S-10S", text)
    if (cedula):
        if pulgada == 0.5:
            cedula_mm = 1.65
        elif pulgada == 1 or pulgada == 2:
            cedula_mm = 2.77
        elif pulgada == 4:
            cedula_mm = 3.05
        elif pulgada >= 6:
            cedula_mm = 3.40

    # print(f"datos obtenidos: {pipe_inches}, {material}, {large}, {cedula.group()} y {cedula_mm} mm")

    # od: float = 273.1
    # adquirir diametro exterior
    od: float = 0.0
    if pulgada == 8:
        od: float = 219.1
    elif pulgada == 10:
        od: float = 273.1

    print(f"El diametro exterior es: {od} mm")

    # Espesor de pared
    t: float = 4.19

    peso_d: float = peso(od, t)
    print(f"El peso es: {peso_d} por kg/m y el peso total es: {peso_d * large} kg/m")