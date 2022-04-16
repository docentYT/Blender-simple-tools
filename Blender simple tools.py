bl_info = {
    "name": "Blender simple tools",
    "description": "Simple functions that will make your life easier.",
    "version": (0,1),
    "blender": (3, 1, 0),
    "category": "Object",
    "author": "Christopher Kwiatkowski (kwiatek_123)"
}

import bpy

class JoinLinkedMaterials(bpy.types.Operator):
    """Joining selected objects by the same material on scene."""
    bl_idname = "object.join_linked_materials"
    bl_label = "Join objects by linked materials"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        object_names = [ob.name for ob in bpy.context.selected_objects]
        
        if not object_names:
            self.report({'ERROR_INVALID_INPUT'}, "Please select objects to join with linked objects.")
            return {'FINISHED'}
        
        print(object_names)
        for object_name in object_names:
            obj = bpy.data.objects.get(object_name)
            if not obj or obj.type != 'MESH':
                continue
            bpy.ops.object.select_all(action='DESELECT')
            print(f"==MESH==\n{obj.name=}")
            obj.select_set(True)
            context.view_layer.objects.active = obj
            bpy.ops.object.select_linked(type='MATERIAL')
            bpy.ops.object.join()

        return {'FINISHED'}
    

def menu_func(self, context):
    self.layout.operator(JoinLinkedMaterials.bl_idname)

def register():
    bpy.utils.register_class(JoinLinkedMaterials)
    bpy.types.VIEW3D_MT_object.append(menu_func)

def unregister():
    bpy.utils.unregister_class(JoinLinkedMaterials)
    bpy.types.VIEW3D_MT_object.remove(menu_func)