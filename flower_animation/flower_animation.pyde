import math
import time

TOTAL_DEGREES = 360
radius = 0

def setup():
    #time.sleep(10)
    global displayWidth, displayHeight, radius
    size(displayWidth, displayHeight)
    background(0) #black background
    noFill()
    stroke(255, 0,0,10)
    radius = height / 2
    draw_down = [0,1,2]

def draw():
    counter=0
    #translate(cos(frameCount), radius/2)
    center_x = displayWidth /2 
    center_y = displayHeight/2 

    beginShape()
    draw_down = [0,1,2]
    j=0 
    '''
    for i in range(TOTAL_DEGREES):
        if j==3:
            j=0
        noiseFactor = noise(i*0.001, float(frameCount)/10) # Framecount keeps track how many frames has passed
        
        x = center_x+ radius * cos(radians(i)) * noiseFactor
        y = (center_y+ radius * sin(radians(i)) * noiseFactor-draw_down[j]*10)
            
        curveVertex(x, y) #its a circular shape
        j+=1
    endShape(CLOSE)
    '''
    
    beginShape()
    #noiseFactor = noise(i*0.05, float(frameCount)/10) # Framecount keeps track how many frames has passed
    for i in range(TOTAL_DEGREES):
        noiseFactor = noise(i*0.1, float(frameCount)/10) # Framecount keeps track how many frames has passed
        #noiseFactor = noise(i*0.05, float(frameCount)/10) # Framecount keeps track how many frames has passed
        x = center_x+ (radius/3 * cos(radians(i)) * noiseFactor)
        y = center_y+ radius/3 * sin(radians(i)) * noiseFactor
        curveVertex(x, y) #its a circular shape
    endShape(CLOSE)
    
    beginShape()
    #noiseFactor = noise(i*0.05, float(frameCount)/10) # Framecount keeps track how many frames has passed
    for i in range(TOTAL_DEGREES):
        noiseFactor = noise(i*0.1, float(frameCount)/40) # Framecount keeps track how many frames has passed
        #noiseFactor = noise(i*0.05, float(frameCount)/10) # Framecount keeps track how many frames has passed
        x = center_x+ (radius*1.5 * cos(radians(i)) * noiseFactor)
        y = center_y+ radius*1.5 * sin(radians(i)) * noiseFactor
        curveVertex(x, y) #its a circular shape
    endShape(CLOSE)
    
