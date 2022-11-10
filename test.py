import bpy

bpy.ops.mesh.primitive_cube_add()

#My first Blender script
#Mover cubo a la derecha
# Path: test.py
import bpy

bpy.ops.mesh.primitive_cube_add()
bpy.ops.transform.translate(value=(4, 0, 0))