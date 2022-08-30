# import pandas

# start = open("./2.1 weather_data.csv")

# with open("2.1 weather_data.csv") as data_file:
#     data = data_file.readlines() ;     print(data)

################### OR #####################

# with open("2.1 weather_data.csv") as data_file:
#      data = data_file.readlines()
#      print(data)

###############################################
# import csv
#
# with open("2.1 weather_data.csv") as data_file:
#      data = csv.reader(data_file)
#      temprature = []
#      print(data)
#      for list in data: ## list or row or you name it anything####
#           # print(list[0]) ### for the first line
#           ### or ##
#           ############# for mondey temperature and it label ###########
#           # print(list[1])  ### for the second line
#           ## or ###
#           # print(list[2]) ### for the third line
#
#           ################## to remove label or tempeature#############
#           if list[1] != "temp":
#                # temprature.append(list[1])
#              ######### to only number without this '
#                temprature.append(int(list[1]))
#      print(temprature)

# ######################  with pandas ################################################################################
# import pandas
#
# data = pandas.read_csv("2.1 weather_data.csv")
# ################# for all data #########
# print(data)
# ################ for a specific data ##############
# print(data["temp"])


######################  with pandas ################################################################################
import pandas

data = pandas.read_csv("2.1 weather_data.csv")
################# for data type #########
# print(type(data))
################ for series or colum #########
# print(type(data["temp"]))
################### converting data to python dictionary
dic = data.to_dict()
print(dic)
############## date to list ##
list = data['temp'].to_list()
print(list)
############ how many number of temp are there ###
temp_list = data['temp']
print(len(temp_list))

################## Adding each temp together######
add_each = data['temp']
final = add_each + add_each
print(final)
############### adding all temp together #######
temp_lis = data['temp']
average = sum(temp_lis) / len(temp_lis)
print(average)
################### OR ###############
mean_add = data['temp'].mean()
print(mean_add)

############### The Maximum value ##
max_v = max(data['temp'])
############ Or ###########
# max_v = data['temp'].max()
print(max_v)

###### Get Data In Colum ###########
print(data["condition"])
colum_data = data.condition
print(colum_data)

################## Get Data in Row #########
Row_data = data[data.day == "Monday"]
print(Row_data)

################## get row with highest temp ########
highest_data = data[data.temp == data.temp.max()]
print(highest_data)

################################
monday = data[data.day == "Monday"]
print(monday.condition)
################################# coverting temp from celcius to farenheit #######

monday_temp = data[data.day == "Monday"]
monday_2 = int(monday_temp.temp)
monday_3 = monday_2 * 9/5 + 32
print(monday_3)

################### Create a dataframe from scratch ####
data_dic = {
    "student": ["Abdul", "Faridah", "Opeyemi"],
    "scores": [76, 56, 65]
}
data_frame = pandas.DataFrame(data_dic)
print(data_frame)

################## dictionary to csv file ########
data_dic = {
    "student": ["Kabir", "Barakah", "Aish"],
    "scores": [76, 56, 65]
}
data_frame = pandas.DataFrame(data_dic)
data_frame.to_csv("New_data.csv")
