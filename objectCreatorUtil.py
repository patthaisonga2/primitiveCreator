import maya.cmds as cmds

def CreatePoly(item):
    if item == "cone":
        cmds.polyCone()
    elif item == "cube":
        cmds.polyCube()
    elif item == "sphere":
        cmds.polySphere()
    elif item == "torus":
        cmds.polyTorus()

    else :
        return 