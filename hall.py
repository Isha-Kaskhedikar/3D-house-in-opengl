from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
   
WINDOW_WIDTH =1000
WINDOW_HEIGHT =1000

# // angle of rotation for the camera direction
angle = 0.0
yAngle = 0.0
# // actual vector representing the camera's direction
lx = 0.0
ly = 0.0 
lz = -1.0
# // XZ position of the camera
x = -5.0
z = 18.0
roll = 0.0

# //for mouse movements
halfWidth = (float)(WINDOW_WIDTH/2.0)
halfHeight = (float)(WINDOW_HEIGHT/2.0)
mouseX = 0.0
mouseY = 0.0

v_cube = [[0.0, 0.0, 0.0], #0
    [0.0, 0.0, 3.0], #1
    [3.0, 0.0, 3.0], #2
    [3.0, 0.0, 0.0], #3
    [0.0, 3.0, 0.0], #4
    [0.0, 3.0, 3.0], #5
    [3.0, 3.0, 3.0], #6
    [3.0, 3.0, 0.0]  #7
]

quadIndices = [
    [0, 1, 2, 3], #bottom
    [4, 5, 6, 7], #top
    [5, 1, 2, 6], #front
    [0, 4, 7, 3], # back is clockwise
    [2, 3, 7, 6], #right
    [1, 5, 4, 0]  #left is clockwise
]

colors = [
    [0.4, 0.1, 0.0], #bottom
    [0.6, 0.0, 0.7], #top
    [0.0, 1.0, 0.0],
    [0.0, 1.0, 1.0],
    [0.8, 0.0, 0.0],
    [0.3, 0.6, 0.7]
]



def drawCube():

    glBegin(GL_QUADS)
    for i in range(6):    
        glVertex3f(v_cube[quadIndices[i][0]][0],v_cube[quadIndices[i][0]][1],v_cube[quadIndices[i][0]][2])
        glVertex3f(v_cube[quadIndices[i][1]][0],v_cube[quadIndices[i][1]][1],v_cube[quadIndices[i][1]][2])
        glVertex3f(v_cube[quadIndices[i][2]][0],v_cube[quadIndices[i][2]][1],v_cube[quadIndices[i][2]][2])
        glVertex3f(v_cube[quadIndices[i][3]][0],v_cube[quadIndices[i][3]][1],v_cube[quadIndices[i][3]][2])
    
    glEnd()

def sofa1():
    glColor3f(0.40,0.60,1.00)
    glPushMatrix()
    glTranslatef(-4,0,-3)
    glScalef(2, 0.4, 0.8)
    drawCube()
    glPopMatrix()

    glColor3f(0.42,0.30,1.00)
    glPushMatrix()
    glTranslatef(-4,1,-3)
    glScalef(2, 0.4, 0.2)
    drawCube()
    glPopMatrix()

    glColor3f(0.33,0.00,1.00)
    glPushMatrix()
    glTranslatef(-4.3,0,-3)
    glScalef(0.1, 0.6, 0.9)
    drawCube()
    glPopMatrix()

    glColor3f(0.33,0.00,1.00)
    glPushMatrix()
    glTranslatef(1.87,0,-3)
    glScalef(0.1, 0.6, 0.9)
    drawCube()
    glPopMatrix()

def TV():
    glColor3f(0,0,0)
    glPushMatrix()
    glTranslatef(8,1.7,4)
    glScalef(0.03, 0.7, 1.2)
    drawCube()
    glPopMatrix()

# def cirtable():
#     glBegin(GL_CYLINERT)

def tvtable():
    glColor3f(0.10,0.00,0.30)
    glPushMatrix()
    glTranslatef(8,0.5,2.8)
    glScalef(0.8, 0.2, 1.9)
    drawCube()
    glPopMatrix()    

    glPushMatrix()
    glTranslatef(8,4.9,5)
    glScalef(0.2, 0.01, 1)
    drawCube()
    glPopMatrix()    

    glPushMatrix()
    glTranslatef(8,4.3,3)
    glScalef(0.2, 0.01, 1)
    drawCube()
    glPopMatrix()    

def vase():
    glColor3f(0.10,0.00,0.30)
    glPushMatrix()
    glTranslatef(3.4,0,-2)
    glScalef(0.2, 0.4, 0.2)
    drawCube()
    glPopMatrix()  

    glColor3f(0.00,0.90,0.30)
    glPointSize(8)
    glBegin(GL_POINTS)
    glVertex3f(3.6, 3, -1.5) 
    glVertex3f(3.5, 3.1, -1.5) 
    glVertex3f(3.4, 3, -1.5)  
    glVertex3f(3.8, 2, -1.5)
    glVertex3f(3.7, 2.1, -1.5)
    glVertex3f(3.6, 2, -1.5)
    glEnd()

    glColor3f(1,0.5,0)
    glPointSize(8)
    glBegin(GL_POINTS)
    glVertex3f(3.3, 2.4, -1.5)
    glVertex3f(3.2, 2.45, -1.5)
    glVertex3f(3.1, 2.4, -1.5)
    glVertex3f(4, 2.7, -1.5)
    glVertex3f(3.9, 2.8, -1.5)
    glVertex3f(3.8, 2.7, -1.5)
    glEnd()
  
    glColor3f(0.30,0.05,0.00)
    glLineWidth(3.0) 
    glBegin(GL_LINES)
    glVertex3f(3.5, 3, -1.5)
    glVertex3f(3.5, 0, -1.5)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(3.9, 2.7, -1.5)
    glVertex3f(3.5, 0, -1.5)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(3.2, 2.4, -1.5)
    glVertex3f(3.9, 0, -1.5)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(3.7, 2, -1.5)
    glVertex3f(3.6, 1, -1.5)
    glEnd()


def window():        
        #cupboard
    glColor3f(0.00,0.84,1) #0.3,0.1,0.0
    glPushMatrix()
    glTranslatef(-4,2,-10)
        #glRotatef(22, 0,0,1)
    glScalef(2, 1, 0.03)
    drawCube()
    glPopMatrix()

    #----------------HORIZONTAL PART---------------
    glColor3f(0.25,0.28,0.28) #0.3,0.1,0.0
    glLineWidth(7.0)
    glBegin(GL_LINES)
    glVertex3f(-4.0, 3.5, -9.9)
    glVertex3f(2.0, 3.5, -9.9)
    glEnd()


    glColor3f(0.25,0.28,0.28) #0.3,0.1,0.0
    glLineWidth(7.0)
    glBegin(GL_LINES)
    glVertex3f(-4.0, 2, -9.9)
    glVertex3f(2.0, 2, -9.9)
    glEnd()


    glColor3f(0.25,0.28,0.28) #0.3,0.1,0.0
    glLineWidth(7.0)
    glBegin(GL_LINES)
    glVertex3f(-4.0, 5, -9.9)
    glVertex3f(2.0, 5, -9.9)
    glEnd()

    #----------------HVERTICAL PART---------------
    glColor3f(0.25,0.28,0.28) #0.3,0.1,0.0
    glLineWidth(7.0)
    glBegin(GL_LINES)
    glVertex3f(-4, 2, -9.9)
    glVertex3f(-4, 5, -9.9)
    glEnd()


    glColor3f(0.25,0.28,0.28) #0.3,0.1,0.0
    glLineWidth(7.0)
    glBegin(GL_LINES)
    glVertex3f(2, 2, -9.9)
    glVertex3f(2, 5, -9.9)
    glEnd()


    glColor3f(0.25,0.28,0.28) #0.3,0.1,0.0
    glLineWidth(7.0)
    glBegin(GL_LINES)
    glVertex3f(-2.0, 2, -9.9)
    glVertex3f(-2.0, 5, -9.9)
    glEnd()

    glColor3f(0.25,0.28,0.28) #0.3,0.1,0.0
    glLineWidth(7.0)
    glBegin(GL_LINES)
    glVertex3f(0, 2, -9.9)
    glVertex3f(0, 5, -9.9)
    glEnd()

    # glBegin(GL_LINES)
    # glVertex3f(-6.0, 4, 10.01)
    # glVertex3f(-6.0, 4, 10.01)
    # glEnd()

    # glBegin(GL_LINES)
    # glVertex3f(-3.0, 0.0, 10.01)
    # glVertex3f(-3.0, 5.0, 10.01)
    # glEnd()
     


def table():
    #table *****************************************
        
        #table base
        glColor3f(0.10,0.00,0.30)
        glPushMatrix()
        glTranslatef(.6,1.5,4.1)
        glScalef(0.8, 0.08, 0.8)
        drawCube()
        glPopMatrix()
        
        #legs
        glColor3f(0.40,0.27,0.00)
        glPushMatrix()
        glTranslatef(.6,0,4.1)
        glScalef(0.08, 0.5, 0.08)
        drawCube()
        glPopMatrix()
        
        glColor3f(0.40,0.27,0.00)
        glPushMatrix()
        glTranslatef(2.8,0,4.18)
        glScalef(0.08, 0.5, 0.08)
        drawCube()
        glPopMatrix()

        glColor3f(0.40,0.27,0.00)
        glPushMatrix()
        glTranslatef(2.8,0,6.25)
        glScalef(0.08, 0.5, 0.08)
        drawCube()
        glPopMatrix()

        glColor3f(0.40,0.27,0.00)
        glPushMatrix()
        glTranslatef(0.58,0,6.25)
        glScalef(0.08, 0.5, 0.08)
        drawCube()
        glPopMatrix()


def cupboard():
    #Cupboard/Almari ************************************************************
        
        #cupboard
        glColor3f(0.40,0.27,0.00) #0.3,0.1,0.0
        glPushMatrix()
        glTranslatef(4,0,4.4)
        #glRotatef(22, 0,0,1)
        glScalef(0.5, 1, 0.5)
        drawCube()
        glPopMatrix()
        
        #cupboard's 1st vertical stripline
        glColor3f(0.2,0.1,0.1)
        glPushMatrix()
        glTranslatef(4,1,5.9)
        #glRotatef(22, 0,0,1)
        glScalef(0.5, 0.01, 0.0001)
        drawCube()
        glPopMatrix()
        
        #cupboard's 2nd vertical stripline
        glColor3f(0.2,0.1,0.1)
        glPushMatrix()
        glTranslatef(4,0.5,5.9)
        #glRotatef(22, 0,0,1)
        glScalef(0.5, 0.01, 0.0001)
        drawCube()
        glPopMatrix()
        
        #cupboard's last stripline
        glColor3f(0.2,0.1,0.1)
        glPushMatrix()
        glTranslatef(4,0,5.9)
        #glRotatef(22, 0,0,1)
        glScalef(0.5, 0.01, 0.0001)
        drawCube()
        glPopMatrix()
        
        #cupboard's lst horizontal stripline
        glColor3f(0.2,0.1,0.1)
        glPushMatrix()
        glTranslatef(5.5,0,5.9)
        #glRotatef(22, 0,0,1)
        glScalef(0.01, 1, 0.0001)
        drawCube()
        glPopMatrix()
        
        #cupboard's right side horizontal stripline
        glColor3f(0.2,0.1,0.1)
        glPushMatrix()
        glTranslatef(4.75,1,5.9)
        #glRotatef(22, 0,0,1)
        glScalef(0.01, 0.67, 0.0001)
        drawCube()
        glPopMatrix()
        
        #cupboard's left side horizontal stripline
        glColor3f(0.2,0.1,0.1)
        glPushMatrix()
        glTranslatef(4,0,5.9)
        #glRotatef(22, 0,0,1)
        glScalef(0.01, 1, 0.0001)
        drawCube()
        glPopMatrix()
        
        #cupboard's handle right
        glColor3f(0.2,0.1,0.1)
        glPushMatrix()
        glTranslatef(5,1.4,5.9)
        #glRotatef(22, 0,0,1)
        glScalef(0.02, 0.18, 0.0001)
        drawCube()
        glPopMatrix()
        
        #cupboard's handle left
        glColor3f(0.2,0.1,0.1)
        glPushMatrix()
        glTranslatef(4.5,1.4,5.9)
        #glRotatef(22, 0,0,1)
        glScalef(0.02, 0.18, 0.01)
        drawCube()
        glPopMatrix()
        
        #cupboard's drawer's 1st handle
        glColor3f(0.2,0.1,0.1)
        glPushMatrix()
        glTranslatef(4.5,0.7,5.9)
        #glRotatef(22, 0,0,1)
        glScalef(0.16, 0.02, 0.01)
        drawCube()
        glPopMatrix()
        
        #cupboard's drawer's 2nd handle
        glColor3f(0.2,0.1,0.1)
        glPushMatrix()
        glTranslatef(4.5,0.25,5.9)
        #glRotatef(22, 0,0,1)
        glScalef(0.16, 0.02, 0.01)
        drawCube()
        glPopMatrix()



def renderScene():
    global angle,yAngle,lx,ly,lz,mouseX,mouseY
    # // Clear Color and Depth Buffers

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # // Reset transformations
    glLoadIdentity()
    # // Set the camera
    gluLookAt(x, 2.5, z,
        x + lx, 2.5 + ly, z + lz,
        roll + 0.0, 2.5, 0.0)

    # // Draw floor
    glColor3f(0.7, 0.7, 0.7)
    glBegin(GL_QUADS)
    glVertex3f(-10.0, 0.0, -10.0)
    glVertex3f(-10.0, 0.0, 10.0)
    glVertex3f(10.0, 0.0, 10.0)
    glVertex3f(10.0, 0.0, -10.0)
    glEnd()
    
    sofa1()

    glPushMatrix()
    glTranslatef(-6,0,2.9)
    glRotatef(90,0,1,0)
    sofa1()#----------------------------------------------------------------sofa
    glPopMatrix()
    # sofa2()
    TV()#----------------------------------------------------------------TV
    tvtable()

    glPushMatrix()
    glTranslatef(-6,0,-5)
    glScalef(1.8,0.5,1.4)  
    table()#----------------------------------------------------------------main table
    glPopMatrix()


    glPushMatrix()
    glTranslatef(2,0,0)
    glScalef(2,1,1)  
    window()#----------------------------------------------------------------window
    glPopMatrix()

    # -----------------------------------------------------------window wall
    glColor3f(1.00,0.90,0.70)
    glBegin(GL_QUADS)
    glVertex3f(-10.0, 0.0, -10.0)
    glVertex3f(-10.0, 7.0, -10.0)
    glVertex3f(10.0, 7.0, -10.0)
    glVertex3f(10.0, 0.0, -10.0)
    glEnd()

    vase()

    # ---------------------------------------------left wall
    # glColor3f(1.00,0.90,0.70)
    # glBegin(GL_QUADS)
    # glVertex3f(-10.0, 0.0, -10.0)
    # glVertex3f(-10.0, 7.0, -10.0)
    # glVertex3f(-10.0, 7.0, 10.0)
    # glVertex3f(-10.0, 0.0, 10.0)
    # glEnd()

    glColor3f(1.00,0.90,0.70)
    glBegin(GL_QUADS)
    glVertex3f(-10.0, 0.0,-10.0)
    glVertex3f(-10.0, 7.0,-10.0)
    glVertex3f(-10.0, 7.0, -6.0)
    glVertex3f(-10.0, 0.0, -6.0)
    glEnd()

    # glColor3f(1.00,0.90,0.70)
    glBegin(GL_QUADS)
    glVertex3f(-10.0, 7.0,-6.0)
    glVertex3f(-10.0, 5.0,-6.0)
    glVertex3f(-10.0, 5.0,-3.0)
    glVertex3f(-10.0, 7.0, -3.0)
    glEnd()

    # glColor3f(1.00,0.90,0.70)
    glBegin(GL_QUADS)
    glVertex3f(-10.0, 0.0, -3.0)
    glVertex3f(-10.0, 7.0, -3.0)
    glVertex3f(-10.0, 7.0, 10.0)
    glVertex3f(-10.0, 0.0, 10.0)
    glEnd()

    glColor3f(0.4, 0.2, 0.0)
    glLineWidth(30.0)
    glBegin(GL_LINES)
    glVertex3f(-10.01, 5.0, -6)
    glVertex3f(-10.01, 5.0, -3)
    glEnd()

    # --------------------------------------------------------entrance wall
    glColor3f(1.00,0.90,0.70)
    glBegin(GL_QUADS)
    glVertex3f(-10.0, 0.0, 10.0)
    glVertex3f(-10.0, 7.0, 10.0)
    glVertex3f(-6.0, 7.0, 10.0)
    glVertex3f(-6.0, 0.0, 10.0)
    glEnd()

    glColor3f(1.00,0.90,0.70)
    glBegin(GL_QUADS)
    glVertex3f(-3.0, 0.0, 10.0)
    glVertex3f(-3.0, 7.0, 10.0)
    glVertex3f(10.0, 7.0, 10.0)
    glVertex3f(10.0, 0.0, 10.0)
    glEnd()

    glColor3f(1.00,0.90,0.70)
    glBegin(GL_QUADS)
    glVertex3f(-6.0, 7.0, 10.0)
    glVertex3f(-6.0, 5.0, 10.0)
    glVertex3f(-3.0, 5.0, 10.0)
    glVertex3f(-3.0, 7.0, 10.0)
    glEnd()

    glColor3f(0.4, 0.2, 0.0)
    glLineWidth(30.0)
    glBegin(GL_LINES)
    glVertex3f(-6.0, 5.0, 10.01)
    glVertex3f(-3.0, 5.0, 10.01)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(-6.0, 5.0, 10.01)
    glVertex3f(-6.0, 0.0, 10.01)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(-3.0, 0.0, 10.01)
    glVertex3f(-3.0, 5.0, 10.01)
    glEnd()


    # -----------------------------------------------------------right wall
    glColor3f(1.00,0.90,0.70)
    glBegin(GL_QUADS)
    glVertex3f(10.0, 0.0,-10.0)
    glVertex3f(10.0, 7.0,-10.0)
    glVertex3f(10.0, 7.0, -6.0)
    glVertex3f(10.0, 0.0, -6.0)
    glEnd()

    # glColor3f(1.00,0.90,0.70)
    glBegin(GL_QUADS)
    glVertex3f(10.0, 7.0,-6.0)
    glVertex3f(10.0, 5.0,-6.0)
    glVertex3f(10.0, 5.0,-3.0)
    glVertex3f(10.0, 7.0, -3.0)
    glEnd()

    # glColor3f(1.00,0.90,0.70)
    glBegin(GL_QUADS)
    glVertex3f(10.0, 0.0, -3.0)
    glVertex3f(10.0, 7.0, -3.0)
    glVertex3f(10.0, 7.0, 10.0)
    glVertex3f(10.0, 0.0, 10.0)
    glEnd()

    glColor3f(0.4, 0.2, 0.0)
    glLineWidth(30.0)
    glBegin(GL_LINES)
    glVertex3f(10.01, 5.0, -6)
    glVertex3f(10.01, 5.0, -3)
    glEnd()

    # --------------------------------------------------------------ceiling
    glColor3f(0.95, 0.95, 0.95)
    glBegin(GL_QUADS)
    glVertex3f(-10.0, 7.0, -10.0)
    glVertex3f(10.0, 7.0, -10.0)
    glVertex3f(10.0, 7.0, 10.0)
    glVertex3f(-10.0, 7.0, 10.0)
    glEnd()
	
    if(abs(mouseX) > 0.3):
        angle -= (0.004 * mouseX)
        lx = math.math.sin(angle)
        lz = -math.math.cos(angle)

    if(abs(mouseY) > 0.3):
        if(abs(yAngle) < (math.pi/2)):
            yAngle += (0.002 * mouseY)
        ly = math.math.sin(yAngle)


    glutSwapBuffers()


# // Handles the events triggered when one of the arrow keys are pressed.
# // @param key : key pressed
# // @param xx : x coordinate of mouse position
# // @param yy : y coordinate of mouse position
def processSpecialKeys(key,xx,yy):
    global x,z,angle,lx,lz

    fraction = 0.1

    if GLUT_KEY_LEFT:
        x += math.sin(angle - math.pi/2.0) * fraction
        z += -math.cos(angle - math.pi/2.0) * fraction
    if GLUT_KEY_RIGHT:
        x += math.sin(math.pi/2.0 + angle) * fraction
        z += -math.cos(math.pi/2.0 + angle) * fraction
    if GLUT_KEY_UP:
        x += lx * fraction
        z += lz * fraction
    if GLUT_KEY_DOWN:
        x -= lx * fraction
        z -= lz * fraction
		



# // Handles the events triggered when any key on the keyboard is pressed.
# //Specifically, handles w,a,s,d and Esc.
# // moves the camera frward, backward and sideways.
# // @param key : key pressed
# // @param xx : x coordinate of mouse position
# // @param yy : y coordinate of mouse position
def processNormalKeys(key,xx,yy):
    global x,z,roll,lx,ly,lz,angle
    fraction = 0.1
    print('keyss')
    print(key)
    if key == b'w':
        x += lx * fraction
        z += lz * fraction
    elif(key == b'a'):
        x += math.sin(angle - math.pi/2.0) * fraction
        z += -math.cos(angle - math.pi/2.0) * fraction
    elif(key == b's'):
        x -= lx * fraction
        z -= lz * fraction
    elif(key == b'd'):
        x += math.sin(math.pi/2.0 + angle) * fraction
        z += -math.cos(math.pi/2.0 + angle) * fraction
    elif (key == b'x'): 
        roll += 0.5
    elif (key == b'z'):
        roll -= 0.5

    if (key == 27):
        exit(0)


#  // Handles the events triggered when the mouse is moved in the window area. 
# // Handles yaw and pitch of the camera.
# // @param xx : x coordinate of mouse position
# // @param yy : y coordinate of mouse position
def processMouseMovement(xx,yy):

    global angle,yAngle,lx,lz,ly 
    mouseX = (float)(halfWidth - xx)/halfWidth
    mouseY = (float)(halfHeight - yy)/halfHeight
    angle -= (0.005 * mouseX)
    lx = math.sin(angle)
    lz = -math.cos(angle)

    if(abs(yAngle) < (math.pi/2)):
        yAngle += (0.005 * mouseY)
    ly = math.sin(yAngle)


#  // Adjusts the viewport sie when the window size is changed and sets the projection.
#  // @param w : new width of window
#  // @param h : new height of window
def changeSize(w, h) :

	# // Prevent a divide by zero, when window is too short
	# // (you cant make a window of zero width).
	if (h == 0):
		h = 1
	ratio = w * 1.0 / h

	# // Use the Projection Matrix
	glMatrixMode(GL_PROJECTION)

	# // Reset Matrix
	glLoadIdentity()

	# // Set the viewport to be the entire window
	glViewport(0, 0, w, h)
	halfWidth = (float)(w/2.0)
	halfHeight = (float)(h/2.0)

	# // Set the correct perspective.
	gluPerspective(45.0, ratio, 0.1, 100.0)

	# // Get Back to the Modelview
	glMatrixMode(GL_MODELVIEW)


# void animate () {

#     f.rotateFan()

#     /* refresh screen */
#     glutPostRedisplay()
# }



# // init GLUT and create window
glutInit()
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGBA)
glutInitWindowPosition(0, 0)
glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
glutCreateWindow("Bedroom")

# // register callbacks
glutDisplayFunc(renderScene)
glutReshapeFunc(changeSize)
# glutIdleFunc(animate)
glutKeyboardFunc(processNormalKeys)
glutSpecialFunc(processSpecialKeys)
glutIdleFunc(renderScene)
glutPassiveMotionFunc(processMouseMovement)

# // OpenGL init
glEnable(GL_DEPTH_TEST)

# // enter GLUT event procesmath.sing cycle
glutMainLoop()


