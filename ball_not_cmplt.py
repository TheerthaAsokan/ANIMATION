import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLu import *
import math

windowsize=500
radius=20
Radius=100


def init():
    glClearColor(0,0,0,0)
    gluOrtho2D(-windowsize,windowsize,-windowsize,windowsize)



def point():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_POINTS)
    glColor3f(0,1,0)
    glPintSize(3)
    glVertex2f()
    glutSwapBuffers()

def animate():


def main()
    glutInit()
    glutInitDisplayMode(GL_RGB)
    glutInitWindowSize(windowsize,windowsize)
    glutInitWindowPosition(50,50)

