# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '106061131.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))
for item in data:
    if item['HUMD'] == '-99.000' or item['HUMD'] == '-999.000':
        item['HUMD'] = 'None'

output = []
station = ['C0A880', 'C0F9A0', 'C0G640', 'C0R190', 'C0X260']
for station_id in station:
    target_data = list(filter(lambda item: item['station_id'] == station_id, data))
    target_data = list(filter(lambda item: item['HUMD'] != 'None', target_data))
    HUMD = [float(item['HUMD']) for item in target_data]
    summa = sum(HUMD)
    if summa == 0:
        summa = 'None'
    output.append([station_id, summa])

# Retrive ten data points from the beginning.
#target_data = data[:10]

#=======================================

# Part. 4
#=======================================
# Print result
print(output)
#========================================
