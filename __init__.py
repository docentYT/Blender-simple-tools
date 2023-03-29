import bpy
from .JoinByNames import JoinByNames
from .JoinByLinkedMaterials import JoinByLinkedMaterials

bl_info = {
    "name": "Blender simple tools",
    "description": "Simple functions that will make your life easier.",
    "version": (0,2),
    "blender": (3, 1, 0),
    "category": "Object",
    "author": "Christopher Kwiatkowski (kwiatek_123)"
}

def menu_func(self, context):
    self.layout.operator(JoinByLinkedMaterials.bl_idname)
    self.layout.operator(JoinByNames.bl_idname)

def register():
    bpy.utils.register_class(JoinByLinkedMaterials)
    bpy.utils.register_class(JoinByNames)
    bpy.types.VIEW3D_MT_object.append(menu_func)

def unregister():
    bpy.utils.unregister_class(JoinByLinkedMaterials)
    bpy.utils.unregister_class(JoinByNames)
    bpy.types.VIEW3D_MT_object.remove(menu_func)