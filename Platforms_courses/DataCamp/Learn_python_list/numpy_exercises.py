'''
    Numpy Arrays
    Los arrays Numpy son una excelente alternativa a las listas de Python. Algunas de las ventajas clave de los arrays Numpy es que son rápidos, faciles de trabajar con ellos, y ofrece a los usuarios la oportunidad de realizar cálculos a través de arrays completos.

    En el siguiente ejemplo, primero crearás dos listas Python. Luego, importarás el paquete numpy y crearás un array numpy de cada lista recien creada.
'''
def print_border_name(title, mark="=", quantity=30):
    print(f'{mark*quantity} {title} {mark*quantity}')


from datetime import datetime
d = datetime.now()   

print_border_name(title="Initializing...")
print(f'Fecha cuando se ejecuta el script sin formato = {d}')
print(f'Fecha cuando se ejecuta el script con formato = {d:%d/%m/%Y}')
print_border_name(title="START CODE")

# Crear dos nuevas listas, height and weight
height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# Importar el paquete numpy como np
import numpy as np

# Crear 2 array numpy desde height y weight
np_height = np.array(height)
np_weight = np.array(weight)
print_border_name(title="Numpy", mark="*", quantity=5)
print(f'{"np_height"!r} is type: {type(np_height)}')


'''
    El !r imprine el texto (unicamente texto) entre comillas simples

    Imprimir el tipo de np_altura
    print(type(np_altura))

    Cálculos de elementos
    Ahora podemos hacer cálculos de elementos en height y weight. Por ejemplo, podrías coger las seis observaciones de altura y peso anteriores, y calcular el BMI para cada observación con una única ecuación. Estás operaciones son muy rápidas y computacionalmente eficientes. Son particularmente útiles cuando tienes 1000s de observaciones en tus datos.
'''
# Calculate bmi
bmi = np_weight / np_height ** 2

# Print the result
print(f'All Body mass Index {bmi}')


'''
    Subconjunto
    Otra gran característica de los arrays Numby es la habilidad de crear subconjuntos. Por ejemplo, si quieres saber que observaciones de nuestro array BMI están por encima de 23, podemos hacer un subconjunto rapidamente para buscarlos.
'''
# For a boolean response
print(f'Print the boolean response of BMI(Body Mass Index) when this be >= 25: { bmi > 25}')

# Print only those observations above 23
print(f'Print the BMI(Body Mass Index) when this be >= 25: { bmi[bmi > 25]}')

print_border_name(title="EXERCISE")

# Create a numpy array np_weight_kg from weight that is kilogram list
np_weight_kg = np.array(weight)

# Create np_weight_lbs from np_weight_kg
np_weight_lbs = np_weight_kg*1000*2.2
# Print out np_weight_lbs
print(np_weight_lbs)