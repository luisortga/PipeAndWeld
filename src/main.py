# import re
# import nmap

# Tuberia y soldadura
# Pipe and weld

def include(point_x: int, point_y: int):
    if point_y < 16:
        altura = "Recuerda que la altura maxima es 16"
        return  print(len(point_x), altura) # type: ignore
    else:
        return print(f"dejamos los datos siguiente: {point_x} and {point_y}")


class advancelbow:

    # Create the 90 degree long radius elbow class
    def elbow90(self, milimeter: float,inch: float):            
            # Converter milimeter in inches
            result_inch = milimeter/25.4
            radio = result_inch/2
            diametro = result_inch

            # Result
            advance = diametro + radio
            return advance
    

example = advancelbow()
example.elbow90(milimeter=203.2,inch=8)
print(example)
print("Primer cambio en git")

# otro comentari pare git