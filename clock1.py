import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

windowsize=500
GLOBAL_MANGLE=90
GLOBAL_SANGLE=90
FPS = 60



def clearscreen():
    glClearColor(0,0,0,0)
    gluOrtho2D(-windowsize,windowsize,-windowsize,windowsize)

def circle():
    
    glColor3f(0.6,0.6,0.5)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0,0)
    for i in range(0,361,1):
        glVertex2f(200*math.cos(i*math.pi/180),200*math.sin(i*math.pi/180))
    glEnd()

    x1 = 180 * math.cos(math.pi * GLOBAL_SANGLE / 180.0)
    y1 = 180 * math.sin(math.pi * GLOBAL_SANGLE / 180.0)
    x2 = 150 * math.cos(math.pi * GLOBAL_MANGLE / 180.0)
    y2 = 150 * math.sin(math.pi * GLOBAL_MANGLE / 180.0)
    glColor3f(1.0, 0.0, 0.0)
    glLineWidth(2.0)
    glBegin(GL_LINES)
    glVertex2f(0, 0)
    glVertex2f(x1, y1)
    glEnd()
    glColor3f(1.0, 1.0, 0.0)
    glBegin(GL_LINES)
    glVertex2f(0, 0)
    glVertex2f(x2, y2)
    glEnd()



   
def draw():
    circle()
    glutSwapBuffers() 


def animate(temp):
    global GLOBAL_SANGLE
    global GLOBAL_MANGLE

    glutPostRedisplay()
    glutTimerFunc(int(1000 / FPS), animate, int(0))

    if GLOBAL_SANGLE == 0:
        if GLOBAL_MANGLE == 0:
            GLOBAL_MANGLE = 360
        else:
            GLOBAL_MANGLE -= 5
        GLOBAL_SANGLE = 360
    else:
        GLOBAL_SANGLE -= 5

def main():
    glutInit()
    glutInitDisplayMode(GL_RGB)
    glutInitWindowSize(windowsize,windowsize)
    glutInitWindowPosition(50,50)
    glutCreateWindow("bouncing")
    glutDisplayFunc(draw)
    glutTimerFunc(0,animate,0)
    glutIdleFunc(draw)
    clearscreen()
    glutMainLoop()

main()