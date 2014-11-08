# Turtle Game
# By Samuel Leonard
#       
#   
#   This program asks if you would like to play a game.
#   If yes, then it loads the turtle game from the Python turtle Module
#   if no, it continues to ask until you say yes.
#   Then the turtle draws your desired shape with sides n.
#   After turtle runs it will output the resulting shape to an ArcGIS polygon shapefile.


from turtle import *
import random
import arcpy
from arcpy import env
import fileinput, os


def turtle_game():
    print "This program will create a shapefile from a polygon drawn using python turtle.\n" \
          "After drawing a shape you can export the points to a new shapefile\n" \
          "just follow the onscreen instructions and have fun!"
    play = " "
    FileName = " "
    while play != "e" or play != "E":
        play = raw_input('Shall we create some polygons? Type yes to start E to export or quit to exit. ')
        if play == "yes" or play == "Yes" or play == "sure":
            #  Sets the starting values for turtle.
            turtle = Pen()
            turtle.shape("turtle")
            turtle.screen.bgcolor("black")
            turtle.color("blue")
            xpos = random.randint(-300,300)
            ypos = random.randint(-300,300)
            # List for turtle coordinates.
            X = []
            Q1 = int
            while Q1 < 10 or Q1 > 50:
                turtle.penup()
                turtle.goto(xpos,ypos)
                turtle.pendown()
                try:
                    Q1 = int(raw_input('What length do you want the sides of your shape? \n'
                                       'Please choose a number between 10 and 50: '))
                    if Q1 > 10 and Q1 < 50:
                        try:
                            Q2 = int(raw_input("How many sides in your polygon? "))
                            if Q2 > -7 and Q2 < 9:
                                # Runs turtle operation and outputs coordinates to list.
                                for i in range(Q2):
                                    turtle.forward(Q1)
                                    turtle.left(360 / Q2)
                                    X.append(turtle.position())
                        except:
                            print "Choose a number between -8 and 8"
                except ValueError:
                    print "choose a valid number between 10 and 50"
                else:
                    break
        elif play == "no" or play == "No":
            print "It has a really cool turtle in it..."
        elif play == "quit":
            raise SystemExit
        # Calls next function.
        elif play == "E" or play == "e":
            Q3 = raw_input("Type y to output shapefile, or q to quit ")
            if Q3 == "y":
                createShapefile(FileName,X)
            elif Q3 == "q":
                print "Have a nice afternoon! "
                raise SystemExit
            else:
                raw_input(Q3)
        else:
            print "Please type yes or quit. "

# This function sets file path and creates new shapefile.
def createShapefile(FileName,X):
    InPath = raw_input("filepath for your new shapefile example.. C:/Data/folder/subfolder : ")
    env.workspace = InPath
    FileName = raw_input("what would you like to name your new shapefile, example... myfile.shp: ")
    SpatRef = arcpy.SpatialReference('WGS 1984')
    # Checks to see if file already exists.
    while arcpy.Exists(FileName):
        FileName = raw_input("This file already exists. please choose a different name ")
    else:
        arcpy.CreateFeatureclass_management(env.workspace,FileName,"POLYGON","","","",SpatRef)
    addPoints(FileName,X)

# Creates polygon from points created using turtle function. However mine only sorta works. I get multiple instances of polygon shapes but, I should only have one.
def addPoints(FileName,X):
    cursor = arcpy.da.InsertCursor(FileName,["SHAPE@"])
    array = arcpy.Array()
    # I think there is something broken in here, but I can't find it.
    for x,y in X:
        point = arcpy.Point(x,y)
        array.append(point)
        polygon = arcpy.Polygon(array)
        cursor.insertRow([polygon])
    raise SystemExit
turtle_game()

