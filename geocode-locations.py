from geopy import geocoders
import csv
g_api_key = 'your_Google_API'
g = geocoders.GoogleV3(g_api_key)

filename = "costcos-geocoded.csv"
f = open(filename, "w")
headers = "geo-codes\n"
f.write(headers)

costcos = csv.reader(open('costcos-limited.csv'), delimiter=',')
next(costcos) # Skip header
for row in costcos:
	full_addy = row[1] + "," + row[2] + "," + row[3] + "," + row[4]
	try:
		place, (lat, lng) = list(g.geocode(full_addy, exactly_one=False))[0]
		print(full_addy + "," + str(lat) + "," + str(lng))
	except:
		print(full_addy + ",NULL,NULL")
	# print(row)
	print(row)
# Done getting data! Close file.
f.close()


import os
cwd = os.getcwd()
print(cwd)
