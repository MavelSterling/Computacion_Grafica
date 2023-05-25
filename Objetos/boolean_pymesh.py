# coding=utf-8

import pymesh

# Cargar las mallas desde archivos
mesh1 = pymesh.load_mesh("mesh1.obj")
mesh2 = pymesh.load_mesh("mesh2.obj")

# Realizar la operación booleana de unión
union_mesh = pymesh.boolean(mesh1, mesh2, operation="union")

# Realizar la operación booleana de intersección
intersection_mesh = pymesh.boolean(mesh1, mesh2, operation="intersection")

# Realizar la operación booleana de diferencia
difference_mesh = pymesh.boolean(mesh1, mesh2, operation="difference")

# Guardar las mallas resultantes en archivos
pymesh.save_mesh("union.obj", union_mesh)
pymesh.save_mesh("intersection.obj", intersection_mesh)
pymesh.save_mesh("difference.obj", difference_mesh)


# PyMesh: Es una biblioteca de Python que proporciona una amplia 
# gama de operaciones geométricas, incluidas operaciones booleanas.
# PyMesh permite realizar uniones, intersecciones y diferencias entre mallas poligonales 3D. 
# Proporciona una interfaz fácil de usar para cargar, manipular y guardar mallas. 
# Puedes encontrar más información y ejemplos en el sitio web oficial de PyMesh.