# coding=utf-8

import bpy

# Cargar los objetos desde archivos
bpy.ops.import_scene.obj(filepath="object1.obj")
bpy.ops.import_scene.obj(filepath="object2.obj")

# Seleccionar los objetos
obj1 = bpy.context.selected_objects[0]
obj2 = bpy.context.selected_objects[1]

# Realizar la operación booleana de unión
bpy.context.view_layer.objects.active = obj1
bpy.ops.object.modifier_add(type='BOOLEAN')
obj1.modifiers["Boolean"].operation = 'UNION'
obj1.modifiers["Boolean"].object = obj2
bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

# Realizar la operación booleana de intersección
bpy.context.view_layer.objects.active = obj1
bpy.ops.object.modifier_add(type='BOOLEAN')
obj1.modifiers["Boolean"].operation = 'INTERSECT'
obj1.modifiers["Boolean"].object = obj2
bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

# Realizar la operación booleana de diferencia
bpy.context.view_layer.objects.active = obj1
bpy.ops.object.modifier_add(type='BOOLEAN')
obj1.modifiers["Boolean"].operation = 'DIFFERENCE'
obj1.modifiers["Boolean"].object = obj2
bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

# Guardar el resultado en un nuevo archivo
bpy.ops.export_scene.obj(filepath="result.obj")


# Blender: Blender es un software de modelado y renderizado 3D de 
# código abierto que también puede ser utilizado como una biblioteca de Python. 
# Blender ofrece una amplia gama de operaciones booleanas para manipular objetos y mallas 3D. 
# Puedes escribir scripts en Python dentro de Blender para realizar operaciones booleanas y 
# manipulaciones geométricas más avanzadas. La documentación oficial de Blender proporciona 
# información detallada sobre cómo utilizar las operaciones booleanas en Blender.