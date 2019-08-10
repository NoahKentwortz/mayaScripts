import maya.cmds as cmds
#config
src_obj = "pCube1"


#paste the string of all the selected things here:
sad_nuggets = cmds.ls(sl=True,long=True) #cmds.ls listing sl(selected DAG objects), long(the full names of the objects)
ascii_encoded = [str(nugget) for nugget in sad_nuggets] #re-encodes to ascii from unicode; don't use non-ascii characters in your object names
ascii_encoded_and_cleaned = [x[1:] for x in ascii_encoded] #removes the first character, regardless of what it is (in this case it should be a | )
#big_boi_obj_list = saddest_nuggets.split(' ')

print(str(len(ascii_encoded_and_cleaned)) + " objects detected. Hold on to your muffins.")

for dest_obj in ascii_encoded_and_cleaned:
    namb = 'tst'

    dest_coords = cmds.objectCenter(dest_obj, gl=True)
    dest_rot = maya.cmds.xform(dest_obj, q=True, ws=True, ro=True)

    dupe_obj = cmds.duplicate(src_obj, name = namb)
    cmds.move(dest_coords[0], dest_coords[1], dest_coords[2], dupe_obj, absolute=True)
    cmds.rotate(dest_rot[0], dest_rot[1], dest_rot[2], dupe_obj)


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