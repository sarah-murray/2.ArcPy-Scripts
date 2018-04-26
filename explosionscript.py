import arcpy
import pythonaddins

arcpy.env.workspace = "M:/All_GIS_work/Programming2"

Input_features = arcpy.GetParameterAsText(0)
Distance = arcpy.GetParameterAsText(1)
Layer = arcpy.GetParameterAsText(2)
Output_Feature_Class = arcpy.GetParameterAsText(3)
Output_Feature_Class2 = arcpy.GetParameterAsText(4)

pythonaddins.MessageBox("1","1")
arcpy.ImportToolbox("M:/All_GIS_work/Programming2/Prac1/Models.tbx", "models")
pythonaddins.MessageBox("2","2")
arcpy.Explosion_models(Input_features,Distance,Layer,Output_Feature_Class, Output_Feature_Class2)
pythonaddins.MessageBox("3","3")
"""
try:
	try:
		
	except arcpy.ExecuteError as e:
		print("Import toolbox error", e)
	try:
		if arcpy.Exists(Output_Feature_Class):
			arcpy.Delete_management(Output_Feature_Class)

	except arcpy.ExecuteError as e:
		print ("Model run error", e)
except Exception as e:
	print(e)
"""