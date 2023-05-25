from OpenGL.GL import *
from OpenGL.GLUT import *

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

def draw_loop():
    glClear(GL_COLOR_BUFFER_BIT)

    lineVertices = [
        200, 100, 0,
        100, 300, 0,
        500, 50, 0,
        320, 100, 0,
        10, 10, 0
    ]

    print("Vertices:")
    for i in range(0, len(lineVertices), 3):
        vertex = lineVertices[i:i+3]
        print(vertex)

    # Dibujar los vértices como puntos
    glColor3f(1.0, 0.0, 0.0)  # Color rojo para los vértices
    glPointSize(5.0)  # Tamaño de los puntos
    glBegin(GL_POINTS)
    for i in range(0, len(lineVertices), 3):
        vertex = lineVertices[i:i+3]
        glVertex3fv(vertex)
    glEnd()

    glEnableClientState(GL_VERTEX_ARRAY)
    glVertexPointer(3, GL_FLOAT, 0, lineVertices)
    glDrawArrays(GL_LINE_LOOP, 0, 5)
    glDisableClientState(GL_VERTEX_ARRAY)

    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(SCREEN_WIDTH, SCREEN_HEIGHT)
    glutCreateWindow(b"OpenGL Loop")

    glViewport(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT, 0, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glutDisplayFunc(draw_loop)
    glutMainLoop()

if __name__ == '__main__':
    main()
