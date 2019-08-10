import maya.cmds as cmds 

sad_nuggets = cmds.ls(sl=True,long=True) #cmds.ls listing sl(selected DAG objects), long(the full names of the objects)
ascii_encoded = [str(nugget) for nugget in sad_nuggets] #re-encodes to ascii from unicode; don't use non-ascii characters in your object names
ascii_encoded_and_cleaned = [x[1:] for x in ascii_encoded] #removes the first character, regardless of what it is (in this case it should be a | )

print ascii_encoded
print ascii_encoded_and_cleaned