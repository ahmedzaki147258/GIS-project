# 8
import os
import arcpy
arcpy.env.overwriteOutput = True

country = arcpy.GetParameterAsText(0)
road = arcpy.GetParameterAsText(1)
outputFolder = arcpy.GetParameterAsText(2)
pop_number = arcpy.GetParameterAsText(3)

african_countries = {}
african_income = {}
Roads_in_Africa = []
with arcpy.da.SearchCursor(country, ["FID", "ADMIN", "POP_EST", "REGION_UN", "INCOME_GRP", "TYPE"]) as cursor:
    for row in cursor:
        if row[3] == "Africa" and row[2] > int(pop_number) and "country" in row[5]:
            african_countries[row[0]] = row[1]
            african_income[row[0]] = row[4]

arcpy.MakeFeatureLayer_management(road, "roads_layer")
with arcpy.da.SearchCursor("roads_layer", ["FID", "NAME"]) as cursor:
    for row in cursor:
        # Check if the road is within an African country with a population > 25,000,000
        if row[0] in african_countries.keys():
            country_name = african_countries[row[0]]
            country_income = african_income[row[0]]
            arcpy.MakeFeatureLayer_management(country, 'countries_layer', """ "FID" = {} """.format(row[0]))
            arcpy.SelectLayerByLocation_management('roads_layer', 'WITHIN', 'countries_layer')
            Roads_in_Africa.append(arcpy.FeatureClassToFeatureClass_conversion('roads_layer', outputFolder,
                                                        "Roads_in_{0}_{1}".format(country_name,
                                                                                ' '.join(country_income.split()[1:]))))
arcpy.Merge_management(Roads_in_Africa, os.path.join(outputFolder, 'Roads_in_Africa.shp'))
arcpy.AddMessage("finished")
