import rhinoscriptsyntax as rs
import random as rnd
import math

 

def PointMatrix(): # function of the matrix

    # Declare the dictionary
    PtMtx = {}
    LP_list = {}

    # Size of the matrix
    imax = rs.GetInteger("Max num of pts in x",10)
    jmax = rs.GetInteger("Max num of pts in y",10)
    kmax = rs.GetInteger("Max num of pts in z",10)

    # Effect range
    rng_max = rs.GetInteger("Max range",15)
    # Move box or not
    move_on = rs.GetInteger("Move switch",0)

    # Select the curve to effect the matrix
    attract_line = rs.GetObject("Select attractor line")

    # Generate the points of the matrix
    for k in range (kmax):
        for i in range (imax):
            for j in range (jmax):
                x = i*5
                y = j*5
                z = k*5
                point = (x,y,z)
                PtMtx[(i,j,k)] = [x,y,z]

                # Generate the boxes
    for i in range (imax) :
        for j in range (jmax) :
            for k in range (kmax) :
                if i > 0 and j > 0 and k >0 :
                    # Generate the box by using 8 points
                    box_list = [PtMtx[i,j,k],PtMtx[i-1,j,k],PtMtx[i-1,j-1,k],PtMtx[i,j-1,k],PtMtx[i,j,k-1],PtMtx[i-1,j,k-1],PtMtx[i-1,j-1,k-1],PtMtx[i,j-1,k-1]] 
                    Box = rs.AddBox(box_list)
    
                    # Analyze the inputed curve
                    LP_list = rs.DivideCurve(attract_line,100,False,True)
                    temp_2 = 0
                    temp = rng_max # The effect range

                # Calculate the shortest distance from each box to the curve
                for m in range (0,len(LP_list)):
                    distance = rs.Distance(PtMtx[i,j,k],LP_list[m])
                    if (temp > distance):
                        temp = distance
                        temp_2 = m
                    else :
                        temp = temp
                        temp_2 = temp_2
                        distance = temp # The shortest distance
    
                        # Scaling the boxes
                        scale_list = ((1/rng_max)*distance,(1/rng_max)*distance,(1/rng_max)*distance)
                        Box_scale = rs.ScaleObject(Box, PtMtx[(i,j,k)], scale_list)

                    # Moving factor
                    if (temp < rng_max):
                        move_distance = temp
                    else:
                        move_distance = 0
    
                        # Moving direction
                        vec = rs.VectorCreate(PtMtx[(i,j,k)],LP_list[temp_2])
    
                        # Moving distance
                    if (move_distance and move_on == 1 > 0):
                        rs.MoveObject(Box_scale,3*vec/move_distance)
                    else:
                        rs.MoveObject(Box_scale,0*vec)

 

PointMatrix() # Call function