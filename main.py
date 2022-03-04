from db_controller import DBController
from controller import Controller
import requests
import pandas as pd
import json

#create table(data frame) with pandas
COLUMNS = ['Region','City_Name','Language','Time(ms)']
data_frame = pd.DataFrame(columns=COLUMNS)
aux_dataframe = pd.DataFrame(columns=COLUMNS) #to add rows to the database

#database connection
database = DBController('challenge.db')
database.connect_db()
database.create_table(aux_dataframe,'Languages')

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
                #build row calculating time
                spent_time = controller.build_row(country_data,aux_dataframe,lang)
                aux_dataframe.loc[aux_dataframe.index[-1],'Time(ms)'] = spent_time
                
                #save that row into database
                new_lang = aux_dataframe.loc[aux_dataframe.index[-1],'Language']
                was_stored = database.save_dataframe_row(aux_dataframe,'Languages',country_name,database.engine, new_lang)
                
                #add that row to the main data frame and clean the auxiliar dataframe
                if was_stored:
                    data_frame = pd.concat([data_frame,aux_dataframe], ignore_index=True, axis=0)
                    
                aux_dataframe = pd.DataFrame(columns=COLUMNS)                    
        else:
            print("[ERROR] Bad country name, try again.\n")
    else:
        break

#Calculate time after the loop and store the result into the database
times = controller.calculate_times(data_frame)
database.create_table(times,'Time(ms)')

#Build jsons
items = database.get_all('Languages')
with open('data.json','w') as file:
    json.dump([dict(r) for r in items], file, indent=4)
   
time_items = database.get_all('Time(ms)')
with open('times.json','w') as file:
    json.dump([dict(r) for r in time_items], file, indent=4)