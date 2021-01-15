#Script Settings:
filtered = []
#with open ('stations.csv') as stations:
 #   print(file)

# First we open the json file and load it into python, calling it 'rain'
import json
with open ('precipitation.json') as f:
    rain= json.load(f)
with open ('seatle_rain.json', 'w') as file:
# then we only include the measurments for the station we are intersted, calling it by its code
    for measurment in rain:
        if 'US1WAKG0038' in measurment['station']: 
            filtered.append(measurment)
            file.write(f"{measurment['date']},{measurment['value']}\n")
print(file)

    #for line in rain:
     #   monthly = rain.split('-')
    #print(value[''])