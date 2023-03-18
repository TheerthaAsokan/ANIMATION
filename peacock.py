from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

windowsize=500
fps=60
angle=69
mode=0
count=0

def init():
    glClearColor(0,0,0,0)
    gluOrtho2D(-windowsize,windowsize,-windowsize,windowsize)

def draw():
    global angle
    glClear(GL_COLOR_BUFFER_BIT)

    for i in range(0,180,1):
        glBegin(GL_LINES)
        if i%2==0:
            glColor3f(0,1,0)
        else:
            glColor3f(0,0,1)
        glVertex2f(0,0)
        glVertex2f(300*math.cos(i*math.pi/180),300*math.sin(i*math.pi/180))
        glEnd()



    global count
    count=0

    for i in range (30,170,20):
        if count==0:
            glBegin(GL_TRIANGLE_FAN)
            glColor3f(0,0,1)
            glVertex2f(150*math.cos(i*math.pi/180),150*math.sin(i*math.pi/180))

            for j in range(0,361,1):
                glVertex2f(150*math.cos(i*math.pi/180)+20*math.cos(j*math.pi/180),150*math.sin(i*math.pi/180)+20*math.sin(j*math.pi/180))

            count=1
            glEnd()

            glBegin(GL_TRIANGLE_FAN)
            glColor3f(1,0.5,0)
            glVertex2f(150*math.cos(i*math.pi/180),150*math.sin(i*math.pi/180))

            for j in range(0,361,1):
                glVertex2f(150*math.cos(i*math.pi/180)+10*math.cos(j*math.pi/180),150*math.sin(i*math.pi/180)+10*math.sin(j*math.pi/180))

            count=1
            glEnd()
        else:
            count=0
            glBegin(GL_TRIANGLE_FAN)
            glColor3f(0,0,1)
            glVertex2f(75*math.cos(i*math.pi/180),75*math.sin(i*math.pi/180))

            for j in range(0,361,1):
                glVertex2f(75*math.cos(i*math.pi/180)+20*math.cos(j*math.pi/180),75*math.sin(i*math.pi/180)+20*math.sin(j*math.pi/180))
            glEnd()

            glBegin(GL_TRIANGLE_FAN)
            glColor3f(1,0.5,0)
            glVertex2f(75*math.cos(i*math.pi/180),75*math.sin(i*math.pi/180))

            for j in range(0,361,1):
                glVertex2f(75*math.cos(i*math.pi/180)+10*math.cos(j*math.pi/180),75*math.sin(i*math.pi/180)+10*math.sin(j*math.pi/180))
            glEnd()

            glBegin(GL_TRIANGLE_FAN)
            glColor3f(0,0,1)
            glVertex2f(225*math.cos(i*math.pi/180),225*math.sin(i*math.pi/180))

            for j in range(0,361,1):
                glVertex2f(225*math.cos(i*math.pi/180)+20*math.cos(j*math.pi/180),225*math.sin(i*math.pi/180)+20*math.sin(j*math.pi/180))
            glEnd()

            glBegin(GL_TRIANGLE_FAN)
            glColor3f(1,0.5,0)
            glVertex2f(225*math.cos(i*math.pi/180),225*math.sin(i*math.pi/180))

            for j in range(0,361,1):
                glVertex2f(225*math.cos(i*math.pi/180)+10*math.cos(j*math.pi/180),225*math.sin(i*math.pi/180)+10*math.sin(j*math.pi/180))
            glEnd()
        


    glBegin(GL_TRIANGLE_FAN)
    print("RIGHT")
    glColor3f(0,0,0)
    glVertex2f(0,0)
    for i in range (0,angle,1):
        glVertex2f(300*math.cos(i*math.pi/180),300*math.sin(i*math.pi/180))
    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    print("LEFT")
    glColor3f(0,0,0)
    glVertex2f(0,0)
    for i in range (0,angle,1):
        glVertex2f(300*math.cos((180-i)*math.pi/180),300*math.sin((180-i)*math.pi/180))
    glEnd()



    glBegin(GL_TRIANGLE_FAN)
    glColor3f(0,0,1)
    glVertex2f(0,0)
    glVertex2f(50,50)
    glVertex2f(5,100)
    glVertex2f(-5,100)
    glVertex2f(-50,50)
    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    glColor3f(0,0,1)
    glVertex2f(4,100)
    glVertex2f(20,120)
    glVertex2f(5,150)
    glVertex2f(0,153)
    glVertex2f(-5,150)
    glVertex2f(-20,120)
    glVertex2f(-4,100)
    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1,0,0)
    glVertex2f(-20,127)
    glVertex2f(-40,120)
    glVertex2f(-20,113)
    glEnd()

    
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1,1,1)
    glVertex2f(0,130)
    for j in range(0,361,1):
            glVertex2f(5*math.cos(j*math.pi/180),130+5*math.sin(j*math.pi/180))
    

    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    glColor3f(0,0,0)
    glVertex2f(0,130)
    for j in range(0,361,1):
            glVertex2f(2*math.cos(j*math.pi/180),130+2*math.sin(j*math.pi/180))
    

    glEnd()

    glutSwapBuffers()

def animate(temp):
    global mode,angle
    if(mode==0):
        angle+=1
        if(angle==70):
            mode=1
    if (mode==1):
        angle-=1
        if(angle==0):
            mode=0

    glutPostRedisplay()
    glutTimerFunc(int(1500/fps),animate,0)

def main():
    glutInit()
    glutInitWindowSize(windowsize,windowsize)
    glutInitWindowPosition(50,50)
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("Peakoack")
    glutDisplayFunc(draw)
    glutTimerFunc(0,animate,0)
    glutIdleFunc(draw)
    init()
    glutMainLoop()

main()