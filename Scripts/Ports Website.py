# 9
import arcpy
import random
arcpy.env.overwriteOutput = True
port = arcpy.GetParameterAsText(0)
website_list = []

with arcpy.da.SearchCursor(port, ['website']) as website_cursor:
    for x in website_cursor:
        if x[0].replace(" ", "") and x[0] not in website_list:
            website_list.append(x[0])

with arcpy.da.UpdateCursor(port, ['website']) as website_cursor:
    for x in website_cursor:
        if not x[0].replace(" ", ""):
            x[0] = random.choice(website_list)
            website_cursor.updateRow(x)
arcpy.AddMessage("finished fill")
