# 10
import arcpy
import random
arcpy.env.overwriteOutput = True

country = arcpy.GetParameterAsText(0)
country_list = []
pop_list = []

with arcpy.da.SearchCursor(country, ['POP_EST']) as country_cursor:
    for x in country_cursor:
        pop_list.append(x[0])

pop_list = sorted(pop_list)
with arcpy.da.UpdateCursor(country, ['SOVEREIGNT', 'POP_EST', 'POP_YEAR']) as country_cursor:
    for x in country_cursor:
        if x[2] < 2019:
            country_list.append(x[0])
            x[1] = random.randint(pop_list[10], pop_list[-5])
            country_cursor.updateRow(x)
arcpy.AddMessage(country_list)
