import maya.cmds as cmds

def swapParts(templatePart, outputNamePrefix):
    rawSelectionDump = cmds.ls(sl=True,long=True) #cmds.ls listing sl(selected DAG objects), long(the full names of the objects)
    ascii_encoded = [str(selected) for selected in rawSelectionDump] #re-encodes to ascii from unicode; don't use non-ascii characters in your object names

    #generate a list of parts to duplicate and transform. removes the first character from the string if it's a pipe.
    partsList = []
    for part in ascii_encoded:
        if part[0] == '|':
            partsList.append(part[1:])

        else:
            partsList.append(part)

    print(str(len(partsList)) + " objects detected. Hold on to your muffins")
    
    for part in partsList:
        dest_coords = cmds.objectCenter(part, gl=True) #grab XYZ coordinates as a list from the destination object 
        dest_rot = cmds.xform(part, q=True, ws=True, ro=True) #also grab euler angle rotations from the destination object
    
        dupe_obj = cmds.duplicate(templatePart, name = outputNamePrefix) #duplicate object with specified prefix
        cmds.move(dest_coords[0], dest_coords[1], dest_coords[2], dupe_obj, absolute=True) #move into position
        cmds.rotate(dest_rot[0], dest_rot[1], dest_rot[2], dupe_obj) #rotate into position

    print("All objects swaps attempted")

#swapParts('pCube1', 'tst') #running the method with any parameters you want should let you swap multiple objects in one pass!
                                                  #also not sure how to set material of the duplicated object that gets moved, we should look into that



# this function should take the currently selected wall "brick", create a new box of the same size (without the stud) and move the duplicate into the same position

def swapWallBrick(outputNamePrefix, studHeight):
    rawSelectionDump = cmds.ls(sl=True,long=True) #cmds.ls listing sl(selected DAG objects), long(the full names of the objects)
    ascii_encoded = [str(selected) for selected in rawSelectionDump] #re-encodes to ascii from unicode; don't use non-ascii characters in your object names

    #generate a list of parts to duplicate and transform. removes the first character from the string if it's a pipe.
    partsList = []
    for part in ascii_encoded:
        if part[0] == '|':
            partsList.append(part[1:])

        else:
            partsList.append(part)

    for part in partsList:
        #get spacial coordinates and rotation of the object we're replacing
        dest_coords = cmds.objectCenter(part, gl=True) #grab XYZ coordinates as a list from the destination object 
        dest_rot = cmds.xform(part, q=True, ws=True, ro=True) #also grab euler angle rotations from the destination object

        #get size of the object we're replacing
        boundingBox = cmds.exactWorldBoundingBox(part)
        dimensions = [bbox[3] - bbox[0], bbox[4] - bbox[1], bbox[5] - bbox[2]] #in the format X, Y, Z

        #this is where the spoopyness happens, if the z coordinate be borked, look here!
        dimensions[2] = dimensions[2] - studHeight #make the new box shorter in the Z axis by studHeight
        dest_coords[2] = dest_coords[2] - (studHeight/2) #the center points of the proxy box and the destination box are no longer the same, so we move it down by half of the stud height
        #most of the spoopiness should be done by here

        #make new cube with the specified dimensions, and move and rotate into position
        proxyCube = cmds.polyCube(w = dimensions[0], d = dimensions[1], h = dimensions[2])
        cmds.move(dest_coords[0], dest_coords[1], dest_coords[2], proxyCube, absolute=True) #move into position
        cmds.rotate(dest_rot[0], dest_rot[1], dest_rot[2], proxyCube) #rotate into position

    print("All proxy swaps attempted!")
    print(str(len(partsList)) + " part swaps attempted.")

swapWallBrick("wall", 0.182)