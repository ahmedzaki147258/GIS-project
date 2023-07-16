import os
import arcpy
from PIL import Image, ExifTags

arcpy.env.overwriteOutput = True
arcpy.env.workspace = r'D:\4rd\GIS\project\Data'
countries = r'D:\4rd\GIS\project\Data\ne_10m_admin_0_countries.shp'
populated_places = r'D:\4rd\GIS\project\Data\ne_10m_populated_places.shp'
roads = r'D:\4rd\GIS\project\Data\ne_10m_roads.shp'
airports = r'D:\4rd\GIS\project\Data\ne_10m_airports.shp'
ports = r'D:\4rd\GIS\project\Data\ne_10m_ports.shp'
output_path = r'D:\4rd\GIS\project\Output'


## 1
# print arcpy.ListFeatureClasses()


## 2
# arcpy.MakeFeatureLayer_management(airports, 'airports_layer', """ "type" LIKE '%military%' """)
# arcpy.MakeFeatureLayer_management(countries, 'countries_layer')
# arcpy.SelectLayerByLocation_management('countries_layer', 'INTERSECT', 'airports_layer')
# arcpy.FeatureClassToFeatureClass_conversion('countries_layer', output_path, 'military airports')
# with arcpy.da.SearchCursor(os.path.join(output_path, 'military airports.shp'), ['SOVEREIGNT']) as cursor:
#     for row in cursor:
#         print row[0]


## 3
# arcpy.MakeFeatureLayer_management(roads, 'roads_layer', """ "CONTINENT" = 'Asia' """)
# arcpy.MakeFeatureLayer_management(countries, 'countries_layer')
# arcpy.SelectLayerByLocation_management("roads_layer", "WITHIN", "countries_layer")
# arcpy.FeatureClassToFeatureClass_conversion('roads_layer', output_path, 'Roads in Asia')
# selected_roads = os.path.join(output_path, 'Roads in Asia.shp')
# print('Number of roads in Asia within country boundaries: {}'.format(arcpy.GetCount_management(selected_roads)))


## 4
# all_countries = []
# countries_files = ['Italy', 'Spain', 'France']
# arcpy.MakeFeatureLayer_management(ports, 'ports_layer')
# for x in countries_files:
#     print (x)
#     arcpy.MakeFeatureLayer_management(countries, 'countries_layer', """ "NAME" = '{}' """.format(x))
#     arcpy.SelectLayerByLocation_management('ports_layer', 'WITHIN', 'countries_layer')
#     all_countries.append(arcpy.FeatureClassToFeatureClass_conversion('ports_layer', output_path, 'ports in {}'.format(x)))
# arcpy.Merge_management(all_countries, os.path.join(output_path, 'countries ports.shp'))


## 5
#
# countries_files = ['Egypt', 'Saudi Arabia', 'Tunisia', 'Somaliland', 'Algeria', 'Morocco', 'Iraq', 'Syria',
#                    'Yemen', 'Libya', 'Jordan', 'United Arab Emirates', 'Lebanon', 'Mauritania', 'Kuwait',
#                    'Oman', 'Qatar', 'Djibouti', 'Bahrain', 'Comoros', 'Palestine', 'Sudan']
# arcpy.MakeFeatureLayer_management(populated_places, 'points_layer')

########################################## Using Multiple Selections ###########################################
# all_cities = []
# for x in countries_files:
#     arcpy.MakeFeatureLayer_management(countries, 'countries_layer', """ "NAME" = '{}' """.format(x))
#     arcpy.SelectLayerByLocation_management("points_layer", "WITHIN", "countries_layer")
#     all_cities.append(arcpy.FeatureClassToFeatureClass_conversion("points_layer", output_path, 'cities_in_ms_{}'.format(x)))
# arcpy.Merge_management(all_cities, os.path.join(output_path, 'Arabic cities ms.shp'))

############################################## Using If Condition ##############################################
# all_cities = []
# for x in countries_files:
#     arcpy.MakeFeatureLayer_management(countries, 'countries_layer', """ "NAME" = '{}' """.format(x))
#     arcpy.SelectLayerByLocation_management('points_layer', 'WITHIN', 'countries_layer')
#     if int(arcpy.GetCount_management('points_layer')[0]) > 0:
#         all_cities.append(arcpy.FeatureClassToFeatureClass_conversion('points_layer', output_path, 'cities_in_if_{}'.format(x)))
# arcpy.Merge_management(all_cities, os.path.join(output_path, 'Arabic cities if.shp'))


## 6
# with arcpy.da.SearchCursor(airports, ['NAME', 'location', 'wikipedia']) as airports_cursor:
#     for x in airports_cursor:
#         print x[0]
#         print x[1]
#         print x[2] + '\n'


## 7
# african_countries = {}
# african_income = {}
# Roads_in_Africa = []
# with arcpy.da.SearchCursor(countries, ["FID", "ADMIN", "POP_EST", "REGION_UN", "INCOME_GRP", "TYPE"]) as cursor:
#     for row in cursor:
#         if row[3] == "Africa" and row[2] > 25000000 and "country" in row[5]:
#             african_countries[row[0]] = row[1]
#             african_income[row[0]] = row[4]
# print african_countries
# arcpy.MakeFeatureLayer_management(roads, "roads_layer")
# arcpy.SelectLayerByAttribute_management("roads_layer", "NEW_SELECTION", '"FID" in ({})'.format(','.join(map(str, african_countries.keys()))))
#
# with arcpy.da.SearchCursor("roads_layer", ["FID", "NAME"]) as cursor:
#     for row in cursor:
#         country_name = african_countries[row[0]]
#         country_income = african_income[row[0]]
#         print country_name
#         arcpy.MakeFeatureLayer_management(countries, 'countries_layer', """ "FID" = {} """.format(row[0]))
#         arcpy.SelectLayerByLocation_management('roads_layer', 'WITHIN', 'countries_layer')
#         Roads_in_Africa.append(arcpy.FeatureClassToFeatureClass_conversion('roads_layer', output_path, "Roads_in_{0}_{1}".format(country_name, ' '.join(country_income.split()[1:]))))
# arcpy.Merge_management(Roads_in_Africa, os.path.join(output_path, 'Roads_in_Africa.shp'))


## 11
# for field in arcpy.ListFields(populated_places):
#     print("Field name: {0}, Type: {1}".format(field.name, field.type))


## 12
# filtered_fields = []
# for field in arcpy.ListFields(populated_places):
#     if field.type != 'String':
#         filtered_fields.append(field.name)
#
# for field in filtered_fields:
#     with arcpy.da.UpdateCursor(populated_places, [field]) as cities_cursor:
#         for x in cities_cursor:
#             if x[0] is None or x[0] == 0:
#                 x[0] = 6
#                 cities_cursor.updateRow(x)


## 13 to 16
# img_folder = r'D:\4rd\GIS\project\Images'
# img_content = os.listdir(img_folder)  # all img in folder
#
# # print full path to each image
# for i, img in enumerate(img_content):
#     fullpath = os.path.join(img_folder, img)
#     print ("full path of image{}: ".format(i + 1), fullpath)  # F:\arcpython\images\1.jpeg)
#
# for img in img_content:
#     fullpath = os.path.join(img_folder, img)
#     pillow_img = Image.open(fullpath)
#     print(ExifTags.TAGS)  # in general
#
#     exif = {ExifTags.TAGS[k]: v for k, v in pillow_img.getexif().items() if k in ExifTags.TAGS}
#     print ("exif tag for this image", exif)  # has info only and replace id with name
#     gps_all = {}
#     # print gps info dictionary
#     try:
#         for key in exif['GPSInfo'].keys():
#             print "this is code value {}".format(key)  # code 0,1,2
#             print "this is value {}".format(exif['GPSInfo'][key])  # value of code
#             decoded_val = ExifTags.GPSTAGS.get(key)
#             print "this is associated label {}".format(decoded_val)  # code what's describe (label)
#             gps_all[decoded_val] = exif['GPSInfo'][key]
#
#         long_ref = gps_all.get('GPSLongitudeRef')
#         long = gps_all.get('GPSLongitude')
#         lat_ref = gps_all.get('GPSLatitudeRef')
#         lat = gps_all.get('GPSLatitude')
#         print long_ref, " : ", long  # degree
#         print lat_ref, " : ", lat
#
#     except:
#         print "this image has no Gps info in it {}".format(fullpath)
#         pass
#     print ("#######################################################")
