import re
import nmap

# Tuberia y soldadura
# Pipe and weld

def include(point_x, point_y):
    if point_y < 16:
        altura = "Recuerda que la altura maxima es 16"
        return  print(len(point_x))
    else:
        return print(f"dejamos los datos siguiente: {point_x} and {point_y}")
    

class advancelbow:

    # Create the 90 degree long radius elbow class
    def elbow90(milimeter,inch):            
            # Converter milimeter in inches
            result_inch = milimeter/25.4
            radio = result_inch/2
            diametro = result_inch

            # Result
            advance = diametro + radio
            return advance
    

example = advancelbow.elbow90(milimeter=203.2,inch=8)
print(example)
print("Primer cambio en git")


    
