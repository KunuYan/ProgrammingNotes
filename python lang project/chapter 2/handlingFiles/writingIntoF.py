# working with csv files
'''
import csv

# reading CSV files
with open('toolhire.csv')as th:
    toolreader = csv.reader(th)
    print(list(toolreader))

# writting  to a CSV file
items = [ 
['1','Lawnmower', 'Small Hover mower', 'Fred','$150','Excellent','2012-01-05'],
['2','Lawnmower','Ride-on mower','Mike','$370','Fair','2012-04-01'],
['3','Bike','BMX bike','Joe','$200','Good','2013-03-22'],
['4','Drill','Heavy duty hammer','Rob','$100','Good','2013-10-28'],
['5','Scarifier','Quality, stainless steel','Anne','$200','2013-09-14'],
['6','Sprinkler','Cheap but effective','Fred','$80','2014-01-06']
]

with open('tooldesc.csv', 'w', newline='') as tooldata:
    toolwritter = csv.writer(tooldata)
    for item in items:
        toolwritter.writerow(item)
'''
