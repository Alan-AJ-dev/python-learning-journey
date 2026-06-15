import pandas as pd
data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260613.csv")
colors = list(data["Primary Fur Color"].unique())
grey_squirels_count= len(data["Primary Fur Color"] == "Gray")
grey_squirels_count = len(data["Primary Fur Color"] == "Cinnamon")
grey_squirels_count = len(data["Primary Fur Color"] == "Black")
data_frame = {
    "colors":["Gray","Cinnamon","Black"],
    "count" : [grey_squirels_count,grey_squirels_count,grey_squirels_count]
}
df= pd.DataFrame(data_frame)
df.to_csv("squirel_count.csv")




print(df["colors"])



