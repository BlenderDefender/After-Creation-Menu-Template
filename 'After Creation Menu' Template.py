#The Standard BL info block
bl_info = {
    "name": "Hello World After Creation",
    "author": "Blender Defender",
    "version": (1, 0, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Add > Lights",
    "description": "Create this 'After Creation Toolbar' that appears after almost every action.",
    "warning": "",
    "tracker_url": "",
    "category": "Lighting",
    "wiki_url": "",
}

import bpy
from bpy.types import Operator


#Class the Operator
class OBJECT_OT_HelloWorld(Operator):
    bl_idname = "object.helloworld"
    bl_label = "Hello World After Creation"
    bl_description = ("Make this 'After Creation Toolbar' appear")
    bl_options = {'REGISTER', 'UNDO'}



 
#Create a bool Property
    my_boolprop = bpy.props.BoolProperty(name="Hide", default=False)

#Create an integer Property
    my_intprop = bpy.props.IntProperty(name="Location X")
    



#Draw the menu
    def draw(self, context):
        layout = self.layout


#Show the label
        col = layout.column()
        col.label(text="Hello World", icon="WORLD")


#Show the bool Prop (as button, not as checkbox)        
        row = col.row()
        row.prop(self, "my_boolprop", toggle=True, icon="HIDE_OFF")


#Show the integer Prop
        row = col.row()
        row.prop(self, "my_intprop")
        

#Two more Labels (optional)
#        layout.label(text="This is a label")
#        layout.label(text="It works, that's awesome!!")


#Execute the Operator
    def execute(self, context):
        

#Defines, what the Bool Prop does.        
        play = self.my_boolprop
        bpy.context.object.hide_viewport = play
        


#Defines, what the Int Prop does.
        xlocation = self.my_intprop        
        bpy.context.object.location[0] = xlocation


        return {'FINISHED'}


#Function to let the Operator appear in the ADD menu
def menu_func(self, context):
    self.layout.operator(OBJECT_OT_HelloWorld.bl_idname, text="Hello World After Creation", icon='WORLD')




# Registers all operators and menus
def register():
    bpy.utils.register_class(OBJECT_OT_HelloWorld)
    bpy.types.VIEW3D_MT_light_add.append(menu_func)


# Unregisters all operators and menus
def unregister():
    bpy.utils.unregister_class(OBJECT_OT_HelloWorld)
    bpy.types.VIEW3D_MT_light_add.remove(menu_func)


if __name__ == "__main__":
    register()
