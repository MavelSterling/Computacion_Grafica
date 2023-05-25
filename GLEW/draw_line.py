from OpenGL.GL import *
from OpenGL.GLUT import *
import sys

def draw_line():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    glBegin(GL_LINES)
    x = -0.9  # Coordenada inicial en x
    while x <= 0.9:  # Coordenada final en x
        glVertex2f(x, -0.5)  # Punto inicial de la línea
        glVertex2f(x + 0.1, 0.5)  # Punto final de la línea
        x += 0.1  # Incremento en x
    glEnd()

    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"OpenGL Line")


    glutDisplayFunc(draw_line)
    glutMainLoop()

if __name__ == '__main__':
    main()


