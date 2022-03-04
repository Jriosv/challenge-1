from db_connection import DBController
from controller import Controller
import requests
import pandas as pd
import json

#create table(data frame) with pandas
COLUMNS = ['Region','City_Name','Language','Time(ms)']
data_frame = pd.DataFrame(columns=COLUMNS)

#database connection
database = DBController('test.db')
database.connect_db()
database.create_table(data_frame,'Languages')

controller = Controller()

#Ask for countries until user want to leave
while True:
    
    
    country_name = input("Please enter country name or enter 'exit' to finish the program: ")

    if not country_name == "exit":
        
        # make the request to the API  
        url = f"https://restcountries.com/v3.1/name/{country_name}"
        payload={}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)

        #handling response
        if response.status_code == 200:
            formated_response = response.json()[0]
            country_data = controller.take_data_from_json(formated_response)
            
            #There are several countries that have more than 1 language so we need this loop
            for lang in country_data['languages'].keys():
                spent_time = controller.build_row(country_data,data_frame,lang)
                data_frame.loc[data_frame.index[-1],'Time(ms)'] = spent_time
                new_lang = data_frame.loc[data_frame.index[-1],'Language']
                database.save_dataframe_row(data_frame,'Languages',country_name,database.engine, new_lang)
                data_frame = pd.DataFrame(columns=COLUMNS)                    
        else:
            print("[ERROR] Bad country name, try again.\n")
    else:
        break

#Calculate time after the loop and store the result into the database
times = controller.calculate_times(data_frame)
database.create_table(times,'Time(ms)')

#Build json
items = database.get_all('Languages')
with open('data.json','w') as file:
    json.dump([dict(r) for r in items], file, indent=4)