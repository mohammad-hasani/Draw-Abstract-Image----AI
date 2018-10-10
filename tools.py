import numpy as np
import sympy
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2


def lineFromPoints(p, q):
    a = q.y - p.y
    b = p.x - q.x
    c = a*(p.x) + b*(p.y)

    x, y = sympy.symbols(('x', 'y'))
 
    if b<0:
     result = sympy.Eq(a*x+b*y,c)
    else:
     result = sympy.Eq(a*x+b*y,c)
    return result


def onSegment(p, q, r):
    if (q.x <= max(p.x, r.x) and q.x >= min(p.x, r.x) and 
        q.y <= max(p.y, r.y) and q.y >= min(p.y, r.y)): 
       return True 
  
    return False 

  
def orientation(p, q, r):
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
  
    if (val == 0): return 0   
  
    return 1 if val > 0 else 2 

  
def doIntersect(p1, q1, p2, q2): 
    o1 = orientation(p1, q1, p2) 
    o2 = orientation(p1, q1, q2) 
    o3 = orientation(p2, q2, p1) 
    o4 = orientation(p2, q2, q1) 
  
   
    if (o1 != o2 and o3 != o4):
        return True 
  
    if (o1 == 0 and onSegment(p1, p2, q1)): return True 
    if (o2 == 0 and onSegment(p1, q2, q1)): return True 
    if (o3 == 0 and onSegment(p2, p1, q2)): return True
    if (o4 == 0 and onSegment(p2, q1, q2)): return True 
  
    return False 


def show_lines(lines, x_lim=1024, y_lim=1024):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    x = []
    y = []
    for ind_line in lines:
        x = [ind_line.p1.x, ind_line.p2.x]
        y = [ind_line.p1.y, ind_line.p2.y]
        line = Line2D(x, y)
        ax.add_line(line)
    ax.set_xlim(0, x_lim)
    ax.set_ylim(0, y_lim)
    plt.show()