import arcpy, csv
arcpy.env.overwriteOutput = 1
arcpy.env.workspace = r"C:\Projects\TEST\TEST_extents.gdb"
item_details = "C:\\Projects\\AGOLData\\ItemDetails_details.csv"
sr = arcpy.SpatialReference("WGS 1984")
arcpy.DeleteFeatures_management("Extents")


with open(item_details, 'r') as csvfile:

    csvreader = csv.reader(csvfile)

    # This skips the first row of the CSV file.
    # csvreader.next() also works in Python 2.
    next(csvreader)

    for row in csvreader:
        array = arcpy.Array([arcpy.Point(row[1], row[2]),arcpy.Point(row[3], row[4])])
        polyline = arcpy.Polyline(array,sr)
        fc = "Extents_" + row[0]
        to_append = arcpy.FeatureEnvelopeToPolygon_management(polyline,fc,"SINGLEPART")
        arcpy.AddField_management(fc,"ID","TEXT","","",50)
        with arcpy.da.UpdateCursor(fc,"ID") as cursor:
            for update in cursor:
                update[0] = fc[8:]
                cursor.updateRow(update)

        arcpy.Append_management(to_append,"Extents","NO_TEST")



#print data