### Import ###
import pandas
import numpy
import csv
from fcmeans import FCM
from enum import Enum
from matplotlib import pyplot
### Import ###

### Functions ###
def column_to_dicts(data_frame_column):
    dict_num_to_value = dict(enumerate(set(data_frame_column)))
    dict_value_to_num = dict([(value, key) for key, value in dict_num_to_value.items()])
    return dict_num_to_value, dict_value_to_num
    
def process_array(arr, n_clusters, label_x, label_y):
    arr = numpy.array(arr)
    fcm = FCM(n_clusters)
    fcm.fit(arr)
    
    f, axes = pyplot.subplots(1, 2, figsize = (11, 5))
    axes[0].scatter(arr[:, 0], arr[:, 1], alpha = .1)
    axes[1].scatter(arr[:, 0], arr[:, 1], c = fcm.predict(arr), alpha = .1)
    axes[1].scatter(fcm.centers[:, 0], fcm.centers[:, 1], marker = "s", s = 20, c = "r")
    
    axes[0].set_xlabel(label_x)
    axes[0].set_ylabel(label_y)
    
    pyplot.savefig(label_x + " - " + label_y + ".png")
    pyplot.show()
    
def dict_save_to_csv(dictionary, csv_file_name):
    with open(csv_file_name + ".csv", "w", newline = "") as csv_file:
        writer = csv.writer(csv_file)
        for key, value in dictionary.items():
            writer.writerow([key, value])
    csv_file.close()
### Functions ###

### Classes ###
class Field(Enum):
    name = "Name"
    platform = "Platform"
    release_year = "Year_of_Release"
    genre = "Genre"
    publisher = "Publisher"
    sales_na = "NA_Sales"
    sales_eu = "EU_Sales"
    sales_jp = "JP_Sales"
    sales_other = "Other_Sales"
    sales_global = "Global_Sales"
    score_critic = "Critic_Score"
    count_critic = "Critic_Count"
    score_user = "User_Score"
    count_user = "User_Count"
    developer = "Developer"
    rating = "Rating"
### Classes ###

### Main ###
all_data = pandas.read_csv("data.csv")
# Drop rows with null value columns.
all_data.dropna(inplace = True) 

# Prepare dictionaries to be able to process numeric values.
platform_num_to_value, platform_value_to_num = column_to_dicts(all_data[Field.platform.value])
genre_num_to_value, genre_value_to_num = column_to_dicts(all_data[Field.genre.value])
publisher_num_to_value, publisher_value_to_num = column_to_dicts(all_data[Field.publisher.value])
developer_num_to_value, developer_value_to_num = column_to_dicts(all_data[Field.developer.value])
rating_num_to_value, rating_value_to_num = column_to_dicts(all_data[Field.rating.value])

# Save dictionaries into CSV files to be available recognize values from numeric plots.
dict_save_to_csv(platform_num_to_value, "Platforms")
dict_save_to_csv(genre_num_to_value, "Genres")
dict_save_to_csv(publisher_num_to_value, "Publishers")
dict_save_to_csv(developer_num_to_value, "Developers")
dict_save_to_csv(rating_num_to_value, "Ratings")

# Fill up arrays for cluster analysing.
a_1 = [] # platform <-> sales_global
a_2 = [] # developer <-> score_user
a_3 = [] # sales_na <-> platform
a_4 = [] # score_critic <-> sales_global
for index, row in all_data.iterrows():
    platform_num = platform_value_to_num[row[Field.platform.value]]
    sales_global = row[Field.sales_global.value]
    a_1.append([
        platform_num,
        sales_global
    ])
    a_2.append([
        developer_value_to_num[row[Field.developer.value]],
        float(row[Field.score_user.value])
    ])
    a_3.append([
        row[Field.sales_na.value],
        platform_num
    ])
    a_4.append([
        row[Field.score_critic.value],
        sales_global
    ])

# Process arrays.
process_array(a_1, 3, "Platform", "Global sales")
process_array(a_2, 3, "Developer", "User score")
process_array(a_3, 3, "NA sales", "Platform")
process_array(a_4, 3, "Critic score", "Global sales")
### Main ###