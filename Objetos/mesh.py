# coding=utf-8

from OpenGL.GL import *
from OpenGL.GLUT import *
import numpy as np

# una malla (mesh) es una estructura de datos que representa
# la geometría de un objeto tridimensional mediante vértices, aristas y caras. 

#  En OpenGL, la representación de una malla generalmente se realiza 
# mediante el uso de buffers de vértices y elementos (índices) que almacenan 
# la información necesaria para renderizar la malla de manera eficiente.

# Definir los vértices de la malla
vertices = np.array([
    [-0.5, -0.5, 0.0],  # Vértice 1
    [0.5, -0.5, 0.0],   # Vértice 2
    [0.0, 0.5, 0.0],    # Vértice 3
])

# Definir los índices de las caras de la malla
indices = np.array([
    [0, 1, 2],  # Cara 1 (triángulo)
])

def render():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    glEnableClientState(GL_VERTEX_ARRAY)
    glVertexPointer(3, GL_FLOAT, 0, vertices)

    glColor3f(1.0, 0.0, 0.0)  # Establecer el color de la malla a rojo

    glDrawElements(GL_TRIANGLES, len(indices.flatten()), GL_UNSIGNED_INT, indices)

    glDisableClientState(GL_VERTEX_ARRAY)

    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
    glutInitWindowSize(800, 600)
    glutCreateWindow("Mesh OpenGL")

    glutDisplayFunc(render)
    glutMainLoop()

if __name__ == '__main__':
    main()


# En este ejemplo, hemos definido una malla simple con tres vértices 
# y una cara triangular. Los vértices se almacenan en un array NumPy 
# llamado vertices, y los índices de las caras se almacenan en un 
# array NumPy llamado indices.

# En la función render, se habilita el uso del puntero de vértices con 
# glEnableClientState(GL_VERTEX_ARRAY) y se especifica el puntero de 
# vértices utilizando glVertexPointer. Luego, se establece el color de 
# la malla con glColor3f. Finalmente, se utiliza glDrawElements para 
# renderizar la malla utilizando los índices de las caras.

