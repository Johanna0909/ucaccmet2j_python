#Script Settings:
import json

# First we open the json file and load it into python, calling it all measurments
with open ('precipitation.json') as f:
    all_measurements= json.load(f)

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

#And dumping it into a Json file:
with open ('results1.json', 'w') as file:
     json.dump (monthly_rain, file, indent=4)

#Part 2
#to get the yearly total rain for Seattle, we do the same stuff again!
monthly_rain=[0]*12
monthly_relative= []
for measurement in all_measurements:
    if 'US1WAKG0038' in measurement['station']: 
        month= int(measurement['date'].split('-')[1])
        value= measurement['value']
        #now I have the values and months for each measurement in Seatle. Now we got to add them together into a list!
        monthly_rain[month-1]+=value
    #and we get the yearly total rain
    yearly_total_rain= sum(monthly_rain)
    #And now we find the relative rainfall
for total_rain_month in monthly_rain:
    monthly_relative_values=((total_rain_month/yearly_total_rain)*100)
    monthly_relative.append(round(monthly_relative_values,2))
#And we get a list with relative rainfalls, where the position corresponds to the month of 2010!
print(monthly_relative)

#And adding this list into a json file
with open ('results2.json', 'w') as file:
     json.dump (monthly_relative, file, indent=4)