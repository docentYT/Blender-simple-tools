bl_info = {
    "name": "Blender simple tools",
    "description": "Simple functions that will make your life easier.",
    "version": (0,2),
    "blender": (3, 1, 0),
    "category": "Object",
    "author": "Christopher Kwiatkowski (kwiatek_123)"
}

import bpy
import os

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
    
class JoinByNames(bpy.types.Operator):
    """Joining selected objects by the same name with blender's .001, .002 etc."""
    bl_idname = "object.join_by_names"
    bl_label = "Join objects by the same names"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        object_names = [ob.name for ob in bpy.context.selected_objects]
        
        if not object_names:
            self.report({'ERROR_INVALID_INPUT'}, "Please select objects to join.")
            return {'FINISHED'}
        
        objs = sorted([x for x in bpy.context.selected_editable_objects if x.type == 'MESH'], 
            key = lambda x: x.name)

        obj_names_stripped = [os.path.splitext(x.name)[0] for x in objs]

        bpy.ops.object.select_all(action='DESELECT')
        for i, obj_name in enumerate(obj_names_stripped):
        # check for i=0 to skip the very first item     
            if i != 0:
                # check if the current item has the same name when stripped
                # than the previous item
                if obj_name == obj_names_stripped[i-1]:
                    objs[i].select_set(True)
                else:
                    bpy.ops.object.join()
                    bpy.ops.object.select_all(action='DESELECT')
                    objs[i].select_set(True)
                    context.view_layer.objects.active = bpy.data.objects.get(objs[i].name)
            else:
                objs[i].select_set(True)
                context.view_layer.objects.active = bpy.data.objects.get(objs[i].name)
        
        bpy.ops.object.join()      
        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator(JoinLinkedMaterials.bl_idname)
    self.layout.operator(JoinByNames.bl_idname)

def register():
    bpy.utils.register_class(JoinLinkedMaterials)
    bpy.utils.register_class(JoinByNames)
    bpy.types.VIEW3D_MT_object.append(menu_func)

def unregister():
    bpy.utils.unregister_class(JoinLinkedMaterials)
    bpy.utils.unregister_class(JoinByNames)
    bpy.types.VIEW3D_MT_object.remove(menu_func)
    
#if __name__ == "__main__":
#    register()
