from turtle import *
from random import *
from math import *

def create_string(axiom, generator, order):
    newFractal = axiom 
    for j in range(order):
        tempFractal = ""
        for i in range(len(newFractal)):
            found = False
            for rule in generator:
                if newFractal[i] == rule[0]:
                    contextL = rule[1][1]
                    contextR = rule[1][2]
                    if (contextL == context_search(newFractal, i, contextL, contextR)[0] or contextL == "*"):
                        if (contextR == context_search(newFractal, i, contextL, contextR)[1] or contextR == "*"):
                            found = True
                            tempFractal += rule[1][0]
                            
            if found == False:
                tempFractal += newFractal[i]
        newFractal = tempFractal
    return newFractal

def context_search(tempString, pos, searchL, searchR):
    realContextL, realContextR = "", ""
    ignore = ["F", "+", "-", "[", "]"]
    r, l = pos, pos
    branchCounter = 0
    
    while len(realContextR) < len(searchR) and r < len(tempString) - 1:
        r += 1
        if tempString[r] == "]":
            if r == pos+1:
                realContextL += " "                    
        if tempString[r] == "[":
            branchCounter += 1
        if tempString[r] == "]" and branchCounter > 0:          
            branchCounter -= 1
        if branchCounter == 0 and (tempString[r] not in ignore):
            realContextR += tempString[r]
            
    branchCounter = 0
    while len(realContextL) < len(searchL) and l > 0:
        l -= 1
        if tempString[l] == "]":
            branchCounter += 1
        if tempString[l] == "[" and branchCounter > 0:
            branchCounter -= 1        
        if branchCounter == 0 and (tempString[l] not in ignore):
            realContextL += tempString[l]
        
    return [realContextL, realContextR]

def draw_fractal(fractal, D, angle):
    positions = []
    for i in range(len(fractal)):
        if fractal[i] == 'F':
            fd(D)
        elif fractal[i] == 'f':
            pu()
            fd(D)
            pd() 
        elif fractal[i] == '+':
            right(angle)
        elif fractal[i] == '-':
            left(angle)
        elif fractal[i] == '[':
            positions.append([pos(), heading(), D])
        elif fractal[i] == ']':
            turtleState = positions.pop()
            pu()
            setpos(turtleState[0][0], turtleState[0][1])
            seth(turtleState[1])
            D = turtleState[2]
            pd()
            
def random_fractals(axiom, generator, maxOrder, D, angle, amount):
    for z in range(amount):
        new_fractal = create_string(axiom, generator, round(random() * maxOrder))
        pu()
        sety(random() * 700 - 350)
        setx(random() * 900 - 450)
        seth(90)
        pd()    
        draw_fractal(new_fractal, D, angle)