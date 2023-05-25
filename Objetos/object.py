from OpenGL.GL import *
from OpenGL.GLUT import *

def render():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Establecer la posición de la cámara
    gluLookAt(3, 3, 3, 0, 0, 0, 0, 1, 0)

    # Dibujar el cubo
    glBegin(GL_QUADS)

    # Cara frontal
    glColor3f(1.0, 0.0, 0.0)  # Color rojo
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)

    # Otras caras
    # ...

    glEnd()

    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow("Objeto sólido OpenGL")

    glEnable(GL_DEPTH_TEST)  # Habilitar el uso del búfer de profundidad

    glutDisplayFunc(render)
    glutMainLoop()

if __name__ == '__main__':
    main()
