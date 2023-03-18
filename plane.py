import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random

windowsize=500
FPS=60
dx=0
mode=0


def clearscreen():
    glClearColor(0,0,.2,1)
    gluOrtho2D(-windowsize,windowsize,-windowsize,windowsize)


def plane():
    global dx
    glClear(GL_COLOR_BUFFER_BIT)

    #BODY
    glColor3f(.5,.5,.5)
    glBegin(GL_POLYGON)
    glVertex2f((dx-300),100)
    glVertex2f((dx-80),100)
    glVertex2f((dx-80),50)
    glVertex2f((dx-300),50)
    glEnd()

    #FRONT
    glColor3f(.9,.3,0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f((dx-80),100)
    glVertex2f((dx-45),75) 
    glVertex2f((dx-80),49)
    glEnd()

    #BACK
    glColor3f(.9,0.3,0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f((dx-300),100)
    glVertex2f((dx-350),50)
    glVertex2f((dx-300),50)
    glEnd()

    #WING1
    glColor3f(.9,0.3,0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f((dx-190),100)
    glVertex2f((dx-250),150)
    glVertex2f((dx-80),100) #Ok
    glEnd()

    #WING2
    glColor3f(.9,0.3,0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f((dx-190),50)
    glVertex2f((dx-250),5)
    glVertex2f((dx-80),50) #OK
    glEnd()

    #moon
    glColor3f( 0.858824,0.858824,0.439216)
    glBegin(GL_TRIANGLE_FAN)
    glVertex(300,300)
    for i in range(0,361):
        glVertex2f(300+70*math.cos(i*math.pi/180),300+70*math.sin(i*math.pi/180))
    glEnd()

    #parachute
    glColor3f(0,0,0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex(0,-100)
    for i in range(35,135):
        glVertex2f(75*math.cos(i*math.pi/180),-100+75*math.sin(i*math.pi/180))
    glEnd()

    glutSwapBuffers()
def animate(temp):
    global dx,mode
    if (mode==0):
        dx+=1
        if (dx==200):
            mode =1
      


    glutPostRedisplay()
    glutTimerFunc(int(1000/FPS),animate,int(0))


def main():
    glutInit() 
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(windowsize,windowsize)
    glutInitWindowPosition(50,50)
    glutCreateWindow("areoplane")
    glutDisplayFunc(plane)
    glutTimerFunc(0,animate,0)
    glutIdleFunc(plane)
    clearscreen()
    glutMainLoop()

main()