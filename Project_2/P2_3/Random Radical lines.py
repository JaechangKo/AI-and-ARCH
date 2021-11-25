#Generate point matrix grid from u v surface
import rhinoscriptsyntax as rs
import random as rnd

def main():
    
    intU = 15
    intV = 10
    Pt = {}
    
    #select surface
    srfGUID = rs.GetObject('Select surface', rs.filter.surface)
    attractPts = rs.GetObjects('Select attractor points', rs.filter.point)
    
    #find surface domain
    UDomain = rs.SurfaceDomain(srfGUID, 0)
    VDomain = rs.SurfaceDomain(srfGUID, 1)
    
    #print UDomain, VDomain
    
    #find step value
    Ustep = (UDomain[1]-UDomain[0])/intU
    Vstep = (VDomain[1]-VDomain[0])/intV
    
    
    #rs.EnableRedraw(False)
    
    #loop to plot points
    for i in range(intU + 1):
        for j in range(intV + 1):
            if  i > 0 and j > 0:
                
                #set u and v values in relation to step and i and j
                u = UDomain[0] + Ustep * i
                v = VDomain[0] + Vstep * j
                
                uPeak = UDomain[0] + Ustep * (i+0.5)
                vPeak = VDomain[0] + Vstep * (j+0.5)
                
                #Assign points to dictionary
                Pt[(i,j)] = rs.EvaluateSurface(srfGUID, u, v)
                point = rs.AddPoint(Pt[(i,j)])
                GridCrv = rs.AddCurve((Pt[(i,j)], Pt[(i-1,j)], Pt[(i-1,j-1)], Pt[(i,j-1)], Pt[(i,j)]),1)
                
                disList = rs.Distance(Pt[(i,j)], attractPts)
                disList.sort()
                distance = disList[0]
                
                #Pt[(i,j)] = rs.MoveObject(point, (rnd.uniform(-1,1)*distance*0.08,rnd.uniform(-1,1)*distance*0.08,0))
                
                #PeakPt0 = rs.AddPoint((Pt[(i,j)][0]+Pt[(i-1,j-1)][0])/2,(Pt[(i,j)][1]+Pt[(i-1,j-1)][1])/2,(Pt[(i,j)][2]+Pt[(i-1,j-1)][2])/2)

                


main()