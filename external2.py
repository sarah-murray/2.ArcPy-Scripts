import arcpy

arcpy.env.workspace = "M:/All_GIS_work/Programming2"

try:
	try:
		arcpy.ImportToolbox("M:/All_GIS_work/Programming2/Week1/Models.tbx", "models")
	except arcpy.ExecuteError as e:
		print("Import toolbox error", e)
	try:
		if arcpy.Exists("/Week2/Explosion_script.shp"):
			arcpy.Delete_management("/Week2/Explosion_script.shp")
		arcpy.Explosion_models("/Week1/albertsurface/explosion/point","100 Meters","/Week1/albertsurface/build/polygon","/Week2/Explosion_script.shp")
	except arcpy.ExecuteError as e:
		print ("Model run error", e)
except Exception as e:
	print(e)
