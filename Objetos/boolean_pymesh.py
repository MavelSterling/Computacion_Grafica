# coding=utf-8

import pymesh
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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

# Mostrar gráficamente las mallas resultantes
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# Función auxiliar para visualizar una malla
def plot_mesh(mesh, color):
    vertices = mesh.vertices
    faces = mesh.faces
    ax.plot_trisurf(vertices[:, 0], vertices[:, 1], vertices[:, 2], triangles=faces, color=color)

# Visualizar las mallas resultantes
plot_mesh(mesh1, "blue")
plot_mesh(mesh2, "red")
plot_mesh(union_mesh, "green")
plot_mesh(intersection_mesh, "orange")
plot_mesh(difference_mesh, "purple")

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.show()



# PyMesh: Es una biblioteca de Python que proporciona una amplia 
# gama de operaciones geométricas, incluidas operaciones booleanas.
# PyMesh permite realizar uniones, intersecciones y diferencias entre mallas poligonales 3D. 
# Proporciona una interfaz fácil de usar para cargar, manipular y guardar mallas. 
# Puedes encontrar más información y ejemplos en el sitio web oficial de PyMesh.