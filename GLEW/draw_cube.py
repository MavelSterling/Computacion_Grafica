from OpenGL.GL import *
from OpenGL.GLUT import *
import glfw

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

rotationX = 0.0
rotationY = 0.0

def keyCallback(window, key, scancode, action, mods):
    global rotationX, rotationY

    rotationSpeed = 10.0

    if action == GLFW_PRESS or action == GLFW_REPEAT:
        if key == GLFW_KEY_UP:
            rotationX -= rotationSpeed
        elif key == GLFW_KEY_DOWN:
            rotationX += rotationSpeed
        elif key == GLFW_KEY_RIGHT:
            rotationY += rotationSpeed
        elif key == GLFW_KEY_LEFT:
            rotationY -= rotationSpeed

def drawCube(centerPosX, centerPosY, centerPosZ, edgeLength):
    halfSideLength = edgeLength * 0.5

    vertices = [
        # front face
        centerPosX - halfSideLength, centerPosY + halfSideLength, centerPosZ + halfSideLength,
        centerPosX + halfSideLength, centerPosY + halfSideLength, centerPosZ + halfSideLength,
        centerPosX + halfSideLength, centerPosY - halfSideLength, centerPosZ + halfSideLength,
        centerPosX - halfSideLength, centerPosY - halfSideLength, centerPosZ + halfSideLength,

        # back face
        centerPosX - halfSideLength, centerPosY + halfSideLength, centerPosZ - halfSideLength,
        centerPosX + halfSideLength, centerPosY + halfSideLength, centerPosZ - halfSideLength,
        centerPosX + halfSideLength, centerPosY - halfSideLength, centerPosZ - halfSideLength,
        centerPosX - halfSideLength, centerPosY - halfSideLength, centerPosZ - halfSideLength,

        # left face
        centerPosX - halfSideLength, centerPosY + halfSideLength, centerPosZ + halfSideLength,
        centerPosX - halfSideLength, centerPosY + halfSideLength, centerPosZ - halfSideLength,
        centerPosX - halfSideLength, centerPosY - halfSideLength, centerPosZ - halfSideLength,
        centerPosX - halfSideLength, centerPosY - halfSideLength, centerPosZ + halfSideLength,

        # right face
        centerPosX + halfSideLength, centerPosY + halfSideLength, centerPosZ + halfSideLength,
        centerPosX + halfSideLength, centerPosY + halfSideLength, centerPosZ - halfSideLength,
        centerPosX + halfSideLength, centerPosY - halfSideLength, centerPosZ - halfSideLength,
        centerPosX + halfSideLength, centerPosY - halfSideLength, centerPosZ + halfSideLength,

        # top face
        centerPosX - halfSideLength, centerPosY + halfSideLength, centerPosZ + halfSideLength,
        centerPosX - halfSideLength, centerPosY + halfSideLength, centerPosZ - halfSideLength,
        centerPosX + halfSideLength, centerPosY + halfSideLength, centerPosZ - halfSideLength,
        centerPosX + halfSideLength, centerPosY + halfSideLength, centerPosZ + halfSideLength,

        # bottom face
        centerPosX - halfSideLength, centerPosY - halfSideLength, centerPosZ + halfSideLength,
        centerPosX - halfSideLength, centerPosY - halfSideLength, centerPosZ - halfSideLength,
        centerPosX + halfSideLength, centerPosY - halfSideLength, centerPosZ - halfSideLength,
        centerPosX + halfSideLength, centerPosY - halfSideLength, centerPosZ + halfSideLength
    ]

    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glEnableClientState(GL_VERTEX_ARRAY)
    glVertexPointer(3, GL_FLOAT, 0, vertices)

    glDrawArrays(GL_QUADS, 0, 24)

    glDisableClientState(GL_VERTEX_ARRAY)


def main():
    if not glfw.init():
        return -1

    window = glfw.create_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Hello World", None, None)
    if not window:
        glfw.terminate()
        return -1

    glfw.set_key_callback(window, keyCallback)
    glfw.set_input_mode(window, GLFW_STICKY_KEYS, 1)

    glfw.make_context_current(window)
    glViewport(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT, 0, 1000)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    halfScreenWidth = SCREEN_WIDTH / 2
    halfScreenHeight = SCREEN_HEIGHT / 2

    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)

        glPushMatrix()
        glTranslatef(halfScreenWidth, halfScreenHeight, -500)
        glRotatef(rotationX, 1, 0, 0)
        glRotatef(rotationY, 0, 1, 0)
        glTranslatef(-halfScreenWidth, -halfScreenHeight, 500)

        drawCube(halfScreenWidth, halfScreenHeight, -500, 200)

        glPopMatrix()

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()
    return 0


if __name__ == "__main__":
    main()

