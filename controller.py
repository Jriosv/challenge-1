from utils.encrypt import encrypt_language
from utils.time_decorator import take_time
import pandas as pd

class Controller:
    def __init__(self):
        pass
    
    def take_data_from_json(self,data_json: dict):
        """This method take the json that we get about a country from the API and take the neccesary data

        Args:
            data_json (dict): http response

        Returns:
            _type_: dict
        """
        country_data = {
        'region': data_json['region'],
        'city_name': data_json['name']['common'],
        'languages':data_json['languages']
        }
        return country_data
    
    def calculate_times(self,dataframe: pd.DataFrame):
        """This method calculate required times

        Args:
            dataframe (pd.DataFrame): dataframe we use to take the times

        Returns:
            _type_: dict with all times.
        """
        time_column = dataframe['Time(ms)']
    
        min_time = time_column.min()
        max_time = time_column.max()
        mean_time = time_column.mean()
        total_time = time_column.sum()
    
        times = pd.DataFrame(data=[{
            'Min': min_time,
            'Max': max_time,
            'Mean': mean_time,
            'Total':total_time,   
        }])
    
        return times
    
    @take_time
    def build_row(self, country_data: dict, dataframe: pd.DataFrame, lang: str):
        """This method is in charge to build the row, for that reason we take the time that is required in the challenge in this step

        Args:
            country_data (dict): data about de country to be built
            dataframe (pd.DataFrame): dataframe where we are going to store the values
            lang (str): language of the country
        """
        hashed_language = encrypt_language(lang)
        new_language = [country_data['region'], country_data['city_name'],hashed_language,'']
        df_size = len(dataframe)
        dataframe.loc[df_size] = new_language