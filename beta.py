import maya.cmds as cmds

#paste the string of all the selected things here:
sad_nuggets = cmds.ls(sl=True,long=True) #cmds.ls listing sl(selected DAG objects), long(the full names of the objects)
ascii_encoded = [str(nugget) for nugget in sad_nuggets] #re-encodes to ascii from unicode; don't use non-ascii characters in your object names
partsList = [x[1:] for x in ascii_encoded] #removes the first character, regardless of what it is (in this case it should be a | )


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

swapParts('pCube1', 'tst') #running the method with any parameters you want should let you swap multiple objects in one pass!
                                                  #also not sure how to set material of the duplicated object that gets moved, we should look into that


#the bounding box thing:
#import maya.cmds as cmds
#
#bbox = cmds.exactWorldBoundingBox('pCube1')
#
#lengths = [bbox[3] - bbox[0], bbox[4] - bbox[1], bbox[5] - bbox[2]]
#
#print(lengths)
#
#max_dimension = max(lengths)
#print(max_dimension)