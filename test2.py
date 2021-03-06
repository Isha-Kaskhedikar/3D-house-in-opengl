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

# //Fan
# Fan f

# def interactWithSnowman :
	
# 	char str1[] = "Hello! You seem to be the only student in class today."
# 	int l1 = strlen(str1) // see how many characters are in text string.
# 	glPushMatrix()

# 	glColor3f(0.0, 0.0, 0.0)

# 	glRasterPos3f(-9.6, 2.7, -2.8) // location to start printing text
# 	for( int i=0 i < l1 i++) // loop until i is greater then l
# 	{
# 		glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, str1[i]) // Print a character on the screen
# 	}
# 	glPopMatrix()

def window():        
        #cupboard
    glColor3f(0.00,1,1) #0.3,0.1,0.0
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

    #----------------HORIZONTAL PART---------------
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
    glVertex3f(-1.0, 2, -9.9)
    glVertex3f(-1.0, 5, -9.9)
    glEnd()

    # glBegin(GL_LINES)
    # glVertex3f(-6.0, 4, 10.01)
    # glVertex3f(-6.0, 4, 10.01)
    # glEnd()

    # glBegin(GL_LINES)
    # glVertex3f(-3.0, 0.0, 10.01)
    # glVertex3f(-3.0, 5.0, 10.01)
    # glEnd()
     

def bed():
    #bed headboard
    glColor3f(0.40,0.27,0.00)
    glPushMatrix()
    glScalef(0.1, 0.5, 0.9)
    glTranslatef(-2,-0.5,6)
    drawCube()
    glPopMatrix()
    
    #bed body
    glColor3f(0.824, 0.706, 0.549)
    glPushMatrix()
    glScalef(1, 0.2, 0.9) #1, 0.2, 0.9
    glTranslatef(0,-0.5,6.2)
    drawCube()
    glPopMatrix()
    
    #pillow right far
    glColor3f(0.00,0.50,0.25)
    glPushMatrix()
    glTranslatef(0.5,0.5,6)
    glRotatef(20, 0,0,1)
    glScalef(0.1, 0.15, 0.48)
    drawCube()
    glPopMatrix()
      
    #blanket
    glColor3f(0.67,0.80,0.00)
    glPushMatrix()
    glTranslatef(1.4,0.45,5.5)
    #glRotatef(22, 0,0,1)
    glScalef(0.5, 0.05, 0.95)
    drawCube()
    glPopMatrix()
    
    #blanket side left part
    glColor3f(0.67,0.80,0.00)
    glPushMatrix()
    glTranslatef(1.4,-0.3,8.15)
    #glRotatef(22, 0,0,1)
    glScalef(0.5, 0.25, 0.05)
    drawCube()
    glPopMatrix()

def table():
    #table *****************************************
        
        #table base
        glColor3f(0.17,0.20,0.00)
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
    
    glPushMatrix()
    glTranslatef(0,0,-13)
    glScalef(1,2,1)
    cupboard()#----------------------------------------------------------------cupboard
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(2,0,-13)
    glScalef(1,2,1)
    cupboard()
    glPopMatrix()
    

    window()

    glPushMatrix()
    glTranslatef(3,0,-13)
    glScalef(2,2,2)
    glRotatef(-45,0,1,0)
    bed()#----------------------------------------------------------------bed
    glPopMatrix()

    # //wall
    glColor3f(1.00,0.90,0.70)
    glBegin(GL_QUADS)
    glVertex3f(-10.0, 0.0, -10.0)
    glVertex3f(-10.0, 7.0, -10.0)
    glVertex3f(10.0, 7.0, -10.0)
    glVertex3f(10.0, 0.0, -10.0)
    glEnd()

    glPushMatrix()
    glTranslatef(5,0,-4)
    glScalef(1,0.8,1.5)
    table()#----------------------------------------------------------------table
    glPopMatrix()

    # //wall
    glColor3f(1.00,0.90,0.70)
    glBegin(GL_QUADS)
    glVertex3f(-10.0, 0.0, -10.0)
    glVertex3f(-10.0, 7.0, -10.0)
    glVertex3f(-10.0, 7.0, 10.0)
    glVertex3f(-10.0, 0.0, 10.0)
    glEnd()

    # //wall with door
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


    # //wall
    glColor3f(1.00,0.90,0.70)
    glBegin(GL_QUADS)
    glVertex3f(10.0, 0.0, -10.0)
    glVertex3f(10.0, 7.0, -10.0)
    glVertex3f(10.0, 7.0, 10.0)
    glVertex3f(10.0, 0.0, 10.0)
    glEnd()


    glColor3f(0.4, 0.2, 0.0)
    glLineWidth(30.0)
    glBegin(GL_LINES)
    glVertex3f(10.01, 5.2, -6)
    glVertex3f(10.01, 5.2, -3)
    glEnd()

    glBegin(GL_QUADS)
    glVertex3f(9.91, 0.0,-6.0)
    glVertex3f(9.91, 5.0,-6.0)
    glVertex3f(9.91, 5.0,-3.0)
    glVertex3f(9.91, 0.0, -3.0)
    glEnd()

    glColor3f(1,1,0)
    glPointSize(8)
    glBegin(GL_POINTS)
    glVertex3f(9.87, 2.0,-5.5)
    glEnd()

    # //ceiling
    glColor3f(0.95, 0.95, 0.95)
    glBegin(GL_QUADS)
    glVertex3f(-10.0, 7.0, -10.0)
    glVertex3f(10.0, 7.0, -10.0)
    glVertex3f(10.0, 7.0, 10.0)
    glVertex3f(-10.0, 7.0, 10.0)
    glEnd()

    # # // Draw prof's chair
    # Chair profChair
    # glPushMatrix()
    # glTranslatef( 6.0, 1.0, -9.0)
    # glScalef(0.32, 0.32, 0.32)
    # glRotatef(-30.0, 0.0, 1.0, 0.0)
    # profChair.drawChair()
    # glPopMatrix()

    # # // Draw prof's table
    # Table profTable
    # glPushMatrix()
    # glTranslatef( 6.0, 1.4, -7.6)
    # glScalef(0.5, 0.5, 0.5)
    # glRotatef(-30.0, 0.0, 1.0, 0.0)
    # profTable.drawTable()
    # glPopMatrix()

    # # // Draw student chairs
    # Chair studentChair[4][4]
    # for (int i = -3 i <= 3 i+=2){
    #     for (int j = -3 j <= 3 j+=2) {
    #         glPushMatrix()
    #         glTranslatef(i*2.0, 0.8, j * 2.0 + 2.2)
    #         glScalef(0.25, 0.25, 0.25)
    #         glRotatef(180.0, 0.0, 1.0, 0.0)
    #         studentChair[i][j].drawChair()
    #         glPopMatrix()
    #     }

	# # // Draw student tables
	# Table studentTable[4][4]
	# for (int i = -3 i <= 3 i+=2){
	# 	for (int j = -3 j <= 3 j+=2) {
	# 		glPushMatrix()
	# 		glTranslatef(i*2.0 + 0.3, 1.2, j * 2.0 + 1.2)
	# 		glScalef(0.4, 0.4, 0.4)
	# 		// glRotatef(180.0, 0.0, 1.0, 0.0)
	# 		studentTable[i][j].drawTable()
	# 		glPopMatrix()
	# 	}
	# }

	# // Draw cupboard
	# Cupboard cupboard
	# glPushMatrix()
	# glTranslatef( 8.49, 0.0, -3.5)
	# glRotatef(-90.0, 0.0, 1.0, 0.0)
	# cupboard.drawCupboard()
	# glPopMatrix()

    # #table *****************************************
        
    #     #table base
    # glColor3f(0,0,1)
    # glPushMatrix()
    # glTranslatef(.6,0.5,9.1)
    # glScalef(0.07, 0.02, 0.07)
    # drawCube()
    # glPopMatrix()
       
    #     #table stand
    # glColor3f(1,0,0)
    # glPushMatrix()
    # glTranslatef(.7,0.35,9.2)
    # glScalef(0.01, 0.2, 0.01)
    # drawCube()
    # glPopMatrix()
        
    #     #table shade
    # glColor3f(0.000, 0.000, 0.545)
    # glPushMatrix()
    # glTranslatef(.7,0.9,9.2)
    # glScalef(0.08, 0.09, 0.08)
    # drawCube()
    # glPopMatrix()

	# //Floor pattern
	# glColor3f(0.149, 0.149, 0.149)
	# glLineWidth(3.0)
	# for(int i = 0 i < 20 i += 2)
	# {
	# 	glBegin(GL_LINES)
	# 	glVertex3f(-10.0 + i, 0.001, -10.01)
	# 	glVertex3f(-10.0 + i, 0.001, 10.01)
	# 	glEnd()
	# }
	# for(int i = 0 i < 20 i += 2)
	# {
	# 	glBegin(GL_LINES)
	# 	glVertex3f(-10.0, 0.001, -10.01 + i)
	# 	glVertex3f(10.0, 0.001, -10.01 + i)
	# 	glEnd()
	# }

	# //windows
	# Window w
	# w.drawWindow1()
	# w.drawWindow2()
	# w.drawWindowSill()
	# glPushMatrix()
	# glTranslatef( 0.0, 0.0, 8.0)
	# w.drawWindowSill()
	# glPopMatrix()

	# //Draw Snowmen
	# Snowman s
	# glPushMatrix()
	# glTranslatef(-9.7, 2.0, -3.0)
	# glScalef(0.3, 0.3, 0.3)
	# s.drawSnowMan()
	# glPopMatrix()
	
	# if ( x < -8.0 && x > -9.0 && z < -1.0 && z > -2.0) {
	# 	interactWithSnowman()
	# }

	
	# glPushMatrix()
	# glTranslatef(0.0, 6.0, 0.0)
	# glScalef(0.3, 0.3, 0.3)
	# f.drawFan()
	# glPopMatrix()

	# Shelf sh
	# glPushMatrix()
	# glTranslatef(8.99, 3.5, 4.0)
	# glScalef(0.25, 0.25, 0.25)
	# glRotatef(-90, 0.0, 1.0, 0.0)
	# sh.drawShelf()
	# glPopMatrix()
	
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


