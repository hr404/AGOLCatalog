import arcpy
arcpy.env.overwriteOutput = 1
arcpy.env.workspace = "C:\Projects\TEST\TEST_extents.gdb"

toDelete = arcpy.ListRasters()
for delete in toDelete:
    arcpy.Delete_management(delete)
pointpolydelete = arcpy.ListFeatureClasses("*","Point")
for pointdelete in pointpolydelete:
    arcpy.Delete_management(pointdelete)
    arcpy.GetMessages()

listfc = arcpy.ListFeatureClasses("*_*")

for fc in listfc:
    try:
        arcpy.PolygonToRaster_conversion(fc,"ORIG_FID",fc + "poly")
    except:
        print "Could not rasterize " + fc

listrs = arcpy.ListRasters()
for rs in listrs:
    try:
        arcpy.RasterToPoint_conversion(rs,rs + "points")
    except:
        print "Could not pointize " + fc

pointFC = arcpy.ListFeatureClasses("*points","Point")
for pfc in pointFC:
    if pfc != pointFC[0]:
        try:
            arcpy.Append_management(pfc,pointFC[0],"TEST")
            print arcpy.GetMessages()
            arcpy.Delete_management(pfc)
        except:
            print "Could not append " + pfc
    else:
        pass