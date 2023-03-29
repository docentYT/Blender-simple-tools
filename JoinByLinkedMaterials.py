import bpy

class JoinByLinkedMaterials(bpy.types.Operator):
    """Joining selected objects by the same material on scene."""
    bl_idname = "object.join_linked_materials"
    bl_label = "Join objects by linked materials"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        object_names = [ob.name for ob in bpy.context.selected_objects]
        
        if not object_names:
            self.report({'ERROR_INVALID_INPUT'}, "Please select objects to join with linked objects.")
            return {'FINISHED'}
        
        for object_name in object_names:
            obj = bpy.data.objects.get(object_name)
            if not obj or obj.type != 'MESH':
                continue
            bpy.ops.object.select_all(action='DESELECT')
            obj.select_set(True)
            context.view_layer.objects.active = obj
            bpy.ops.object.select_linked(type='MATERIAL')
            bpy.ops.object.join()

        return {'FINISHED'}