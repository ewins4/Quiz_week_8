#Can you please write some code in climate_q1.py to connect to the database,
#fetch the values from the database, and populate some Python lists with the
#corresponding values? I've already written the code to generate the graphs.

import matplotlib.pyplot as plt
import sqlite3
years = []
co2 = []
temp = []
conn = sqlite3.connect('climate.db')
cursor = conn.cursor()
cursor.execute('''SELECT Year, Temperature, CO2 from climatedata''')


for i in cursor.fetchall():
    years.append(i[0])
    co2.append(i[1])
    temp.append(i[2])


plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_1.png") 
