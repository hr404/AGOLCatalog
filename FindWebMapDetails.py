import os, urllib, json, csv

#File parameters
location = r".\JSON_details"
csv_file_input = r".\AGOLCat.csv"
csv_file_output = r".\ItemTitles_details.csv"
item_details = r".\ItemDetails_details.csv"


#AGOL User parameters
# replace <<PLACEHOLDERS>> in next three lines with your information
# e.g., portal = 'https://www.arcgis.com', username = 'jdoe1234', password = 'mypassword'
portal = raw_input("Insert portal here")
username = raw_input("Insert username here")
password = raw_input("Insert password here")

#--------------------------------------Delete File----------------------------------------------------------
try:
    os.remove(item_details)
    print "Deleted " + item_details + ".  Beginning script."
except:
    print item_details + " did not exist.  Beginning script."

#--------------------------------------list of items in AGOL----------------------------------------------------------
data = [] #Buffer list
with open(csv_file_input, "rb") as the_file:
	reader = csv.reader(the_file, delimiter=",")
	for row in reader:

		try:
			new_row = row[0], row[5]
			#Basically ´write the rows to a list
			data.append(new_row)
		except IndexError as e:
			print e
			pass

	with open(csv_file_output, "wb") as to_file:
		writer = csv.writer(to_file, delimiter=",")
		for new_row in data:
			writer.writerow(new_row)

##for stuff in data:
##    print stuff[0]
#--------------------------------------CSV Row to Dictionary----------------------------------------------------------
with open(csv_file_input) as f:
    a1 = [row["id"] for row in csv.DictReader(f)]
###print a1

#-----------------------------------------------Generate Table of Items with URLS-----------------------------------------------------
for item in a1:
    print item
    # Generate token to get item info
    # Generate Token Example
    parameters = urllib.urlencode({'username':username,'password':password,'client':'requestip','f':'json'})
    request = portal + '/sharing/rest/generateToken?'
    response = json.loads(urllib.urlopen(request, parameters).read())
    #print response
    token = response['token']
    #return parameters
    parameters2 = urllib.urlencode({'title' : 'PYTHON', 'token': token, 'f': 'json'})
    request2 = portal + '/sharing/content/items/' + item + '/details?' + parameters2
    itemDataReq = urllib.urlopen(request2).read()
    itemString = str(itemDataReq)
    jsonFile = open(location + "\\" + item + ".json", 'w')
    print >> jsonFile, itemString
    jsonFile.close()

location = "C:\\Projects\\AGOLData\\JSON_details\\"
addrow = open(item_details, 'a')
print >> addrow, "id,x1,y1,x2,y2"
addrow.close()
for dirpath, dirname, filename in os.walk(location ,topdown=True, onerror=None, followlinks=True):
    #print filename

    for file in filename:
        #print file
        strfile = file[:-5]

        log = open(item_details,'a')
        with open(location + file) as json_data:
            d = json.load(json_data)
            try:
                extent1 = str(d["extent"][0])
                extent2 = str(d["extent"][1])
                print >> log, str(strfile) + ',' + extent1[1:-1] + "," + extent2[1:-1]
                #print >> log, str(strfile) + '|' + str(d["extent"][0]) + "|" + str(d["extent"][1])
            except:
                pass
                #print "No extents"
        log.close()






