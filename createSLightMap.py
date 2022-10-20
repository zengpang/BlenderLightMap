import bpy
bpy.context.scene.render.engine = 'CYCLES'
for object in bpy.data.objects:
    if object.type=="MESH":
      mat =bpy.data.materials.new(name=object.name)
      mat.use_nodes=True
      matnodes = mat.node_tree.nodes
      AO = matnodes.new('ShaderNodeAmbientOcclusion')
      tex = matnodes.new('ShaderNodeTexImage')
      emission=mat.node_tree.nodes["Principled BSDF"].inputs['Emission']
      emissionPower=mat.node_tree.nodes["Principled BSDF"].inputs['Emission Strength']
      baseColor=mat.node_tree.nodes["Principled BSDF"].inputs['Base Color']
      aoDistance=AO.inputs['Distance']
      mat.node_tree.links.new( AO.outputs['Color'],emission)
      mat.node_tree.links.new(AO.outputs['AO'], emissionPower)
      baseColor.default_value=(0.045402,0.045402,0.045402,1)
      aoDistance.default_value=65
      tex.image = bpy.data.images.new(object.name+'LightTex',1024,1024, alpha=True, float_buffer=True)
      tex.image.colorspace_settings.name='Linear'
      object.data.uv_layers[0].name="UV1"
      object.data.uv_layers[1].name="UV2"
      object.data.uv_layers[0].active_render = False
      object.data.uv_layers[1].active_render = True
      if mat.name==object.name:
        object.data.materials[0]=mat