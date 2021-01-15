import json
#Script Settings:
seattle_measurements = []

#read in the csv and find the code from there later
#with open ('stations.csv') as file:

# First we open the json file and load it into python, calling it 'rain'
with open ('precipitation.json') as f:
    all_measurements= json.load(f)

#with open ('seatle_rain.csv', 'w') as seatle:
# then we only include the measurments for the station we are interested in, calling it by its code

monthly_rain=[0]*12
for measurement in all_measurements:
    if 'US1WAKG0038' in measurement['station']: 
        month= int(measurement['date'].split('-')[1])
        value= measurement['value']
        #now I have the values and months for each measurement in Seatle. Now we got to add them together into a list!
        monthly_rain[month-1]+=value
#And we have a list of monthly rainfall, where the position corresponds to the month!      
print(monthly_rain)
#print(f'{monthly_rain.index()+1}:{monthly_rain}')


# with open ('results1.json', 'w') as file:
#     json.dump (monthly_rain, file, indent=4)


#to get the yearly total rain for Seattle, we do the same stuff again!
yearly_total_rain= 0
monthly_rain=[0]*12
for measurement in all_measurements:
    if 'US1WAKG0038' in measurement['station']: 
        month= int(measurement['date'].split('-')[1])
        value= measurement['value']
        #now I have the values and months for each measurement in Seatle. Now we got to add them together into a list!
        monthly_rain[month-1]+=value
        #and we get the yearly total rain
    yearly_total_rain= sum(monthly_rain)
    #And now
for total_rain_month in monthly_rain:
    print((total_rain_month/yearly_total_rain)*100)


