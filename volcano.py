import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

windowsize=500
FPS = 60
count=1


def clearscreen():
    glClearColor(0,0,.4,0)
    gluOrtho2D(-windowsize,windowsize,-windowsize,windowsize)

def volcano():
    er=0
    glClear(GL_COLOR_BUFFER_BIT)
   
   
    glColor3f(.9,0.4,.2) 
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(-300,0)
    glVertex2f(300,0)
    glVertex2f(0,300)
    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    glColor3f(0,0,.4)
    glVertex2f(0,300)
    for i in range(0,361,1):
        glVertex2f(100*math.cos(i*math.pi/180),300+100*math.sin(i*math.pi/180))
    glEnd()

    glPointSize(6)
    glBegin(GL_POINTS)
    glColor3f(1,.2,0)
    for j in range(0,count):
        for i in range(225,316,1):
            glVertex2f((100+er)*math.cos(i*math.pi/180),300+(100+er)*math.sin(i*math.pi/180))
        er+=1
    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    glColor3f(0,1,0)
    glVertex2f(-windowsize,0)
    glVertex2f(windowsize,0)
    glVertex2f(windowsize,-windowsize)
    glVertex2f(-windowsize,-windowsize)
    

    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    glColor3f(.5,.4,.5)
    glVertex2f(300,300)
    for i in range(0,361,1):
        glVertex2f(300+100*math.cos(i*math.pi/180),300+100*math.sin(i*math.pi/180))
    glEnd()

    glutSwapBuffers()


def animate(temp):

    global count
    count+= 1
    
    glutPostRedisplay()
    glutTimerFunc(int(1000/FPS),animate,int(0))


def main():
    glutInit()
    glutInitDisplayMode(GL_RGB)
    glutInitWindowSize(windowsize,windowsize)
    glutInitWindowPosition(50,50)
    glutCreateWindow("window")
    glutDisplayFunc(volcano)
    glutIdleFunc(volcano)
    glutTimerFunc(0,animate,0)
    clearscreen()
    glutMainLoop()

main()