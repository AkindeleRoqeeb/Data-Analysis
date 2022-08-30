import pandas

# data_1 = open("4.2 2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# data_2 = pandas.read_csv(data_1)
# print(data_2)

###############################################
# data = pandas.read_csv("4.2 2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# data_q = data[data["Primary Fur Color"] == "Gray"]
# print(data_q)

################################################\
data = pandas.read_csv("4.2 2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dictionary = {
    "fur color": ["Gray", "Cinnamon", "black"],
    "count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}
# print(data_dictionary)
differ = pandas.DataFrame(data_dictionary)
differ.to_csv("primary_count.csv")