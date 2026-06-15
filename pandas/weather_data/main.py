# with open("weather_data (1).csv") as data:
#     data_list= data.readlines()
#     print(data_list )

# import csv
# with open("weather_data (1).csv") as data_file:
#     data = csv.reader(data_file)
#     temp = []
#     for row in data:
#         if row[1] != "temp":
#             temp.append(row[1])
#
#     print(temp)

#here so much of code to handiling the data for free purpose we are going to use pandas

import pandas as pd
data = pd.read_csv("weather_data (1).csv")
# print(data)
# print(type(data["day"]))
#
# temp_list = data["temp"].to_list()
# avg = 0
# sum = 0
# for temp in temp_list:
#     sum += temp
#
# avg = sum / len(temp_list)
# avg = round(avg,2)
# print(avg)
#
# print(f"Maximum value {data["temp"].max()}")
#
# print(f"Mean value {round(data["temp"].mean(),2)}")


print(data[data.temp == data.temp.max()])
