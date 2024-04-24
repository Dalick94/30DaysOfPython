### Modules ###

# Exercises: Level 1
#1.
def random_user_id():
    import random
    letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    unir = letras + numeros
    lista = []
    x = 0
    for i in range(6):
        x = random.choice(unir)
        lista.append(str(x))
    print(lista)

random_user_id()

#2.
def user_id_gen_by_user():
    largo_id = int(input("Introduzca el largo de su ID: "))
    cantidad_id = int(input("Indique el número de ID que quiere crear: "))
    import random
    letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    unir = letras + numeros
    lista = []
    x = 0
    for i in range(largo_id):
        x = random.choice(unir)
        lista.append(str(x))
    print(lista)

user_id_gen_by_user()

#3.
def rgb_color_gen():
    import random
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"

print(rgb_color_gen())


#Exercises: Level 2
#1. 
import random

def list_of_hexa_colors(num_colors):
    colors = []
    hex_chars = "0123456789ABCDEF"
    
    for _ in range(num_colors):
        color = "#"
        for _ in range(6):
            color += random.choice(hex_chars)
        colors.append(color)
    
    return colors

#2.
def list_of_rgb_colors(num_colors):
    colors = []
    for _ in range(num_colors):
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        colors.append((red, green, blue))
    return colors

#3.
def generate_colors(num_colors, format='hexa'):
    colors = []
    for _ in range(num_colors):
        if format == 'hexa':
            color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        elif format == 'rgb':
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        else:
            return "Invalid format. Please choose 'hexa' or 'rgb'."
        colors.append(color)
    return colors


#Exercises: Level 3
#1.
def shuffle_list():
    import random
    lista = ["Micho", "Jorge", "Guido", "Andrés", "Fran"]
    random.shuffle(lista)
    print(lista)

shuffle_list()

#2.
def unique_liste():
    import random
    lista_unica = []
    i = 0
    while len(lista_unica) < 7:
        x = random.randrange(0, 9, 1)
        if x in lista_unica:
            pass
        else:
            lista_unica.append(x)
            i += 1
    print(lista_unica)

unique_liste()