import maya.cmds as cmds 

sad_nuggets = cmds.ls(sl=True,long=True) #cmds.ls listing sl(selected DAG objects), long(the full names of the objects)
ascii_encoded = [str(nugget) for nugget in sad_nuggets]
#sadder_nuggets = [sad_nuggets.Replace("u'|", "")] 

print sad_nuggets
print ascii_encoded