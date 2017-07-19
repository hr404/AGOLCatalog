import os, urllib, json, csv

#File parameters
item_details = r".\ItemDetails_counts.csv"
#--------------------------------------Delete File----------------------------------------------------------
try:
    os.remove(item_details)
    print "Deleted " + item_details + ".  Beginning script."
except:
    print item_details + " did not exist.  Beginning script."
#--------------------------------------Get number of web items views----------------------------------------------------------
location = r".\JSON_details\\"
addrow = open(item_details, 'a')
print >> addrow, "id,title,numviews"
addrow.close()
for dirpath, dirname, filename in os.walk(location ,topdown=True, onerror=None, followlinks=True):
    for file in filename:
        #print file
        strfile = file[:-5]

        log = open(item_details,'a')
        with open(location + file) as json_data:
            d = json.load(json_data)
            try:
                numviews = d["numViews"]
                name = d["title"]
                if ',' in name:
                    name1 = name.replace(',',"")
                    print >> log, str(strfile) + ',' + str(name1) + ',' +str(numviews)
                else:
                    print >> log, str(strfile) + ',' + str(name) + ',' +str(numviews)
                #print >> log, str(strfile) + ',' + extent1[1:-1] + "," + extent2[1:-1]
                #print >> log, str(strfile) + '|' + str(d["extent"][0]) + "|" + str(d["extent"][1])
            except:
                pass
                #print "No extents"
        log.close()