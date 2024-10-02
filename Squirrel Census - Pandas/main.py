import pandas




# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))
#
#
#
# temp_list = data["temp"].to_list()

# print(data["temp"].mean())
# x = data["temp"].max()
#
# Get data in columns
# print(data["condition"])
# print(data.condition)

# Get data in row
#print(data[data.temp == x])

# monday = data[data.day == "Monday"]
#
# m_temp = monday.temp
#
#
# fahrenheit = m_temp * 1.8 + 32
# print(fahrenheit)


# Create a dataframe from scratch
# data_dict = {
#     "students": ["Bomba", "David", "Ben"],
#     "scores":  [46, 85, 23]
#
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")









data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240720.csv")



grey_squirrels = data[data["Primary Fur Color"] == "Gray"]
red_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
black_squirrels = data[data["Primary Fur Color"] == "Black"]
count_grey_squirrels = len(grey_squirrels)
count_red_squirrels = len(red_squirrels)
count_black_squirrels = len(black_squirrels)




print(count_grey_squirrels)
print(count_red_squirrels)
print(count_black_squirrels)


data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [count_grey_squirrels, count_red_squirrels, count_black_squirrels]

}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")