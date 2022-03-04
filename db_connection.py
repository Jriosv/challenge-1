import sqlalchemy as db
import pandas as pd

class DBController:    
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.engine = None
        self.connection = None
        metadata = None
        
    def connect_db(self):
        """This method creates and returns a SQL-Alchemy engine that we are going to use for database transactions
        """   
        self.engine = db.create_engine(f'sqlite:///.{self.db_name}', echo=False)
        self.connection = self.engine.connect()
        self.metadata = db.MetaData()
        
    def create_table(self,data_frame: pd.DataFrame, table_name: str):
        """This method create a table taking of reference the dataframe, firt verify that the table doesn't exist

        Args:
            data_frame (pd.DataFrame): reference data_frame
            table_name (str): this is the name that the table are going to take
        """
        try:
            table = db.Table(table_name,self.metadata,autoload=True,autoload_with=self.engine)
        except:
            data_frame.to_sql(table_name,con=self.connection,index=False,if_exists='replace')
        
    def get_all(self, table_name: str):
        """This methos is to select all rows of a table 

        Args:
            table_name (str): table name

        Returns:
            LegacyCursorResult type
        """
        all_table = db.Table(table_name,self.metadata,autoload=True,autoload_with=self.engine)
        query = db.select([all_table])
        items = self.connection.execute(query)
        return items
    
    def get_by_country(self, table_name: str, country_name: str, lang: str):
        """Returns the rows where the table have a passed country name

        Args:
            table_name (str): table where we are going to search
            country_name (str): country name
            lang (str): language

        Returns:
            _type_: list of rows of the table
        """
        table = db.Table(table_name,self.metadata,autoload=True,autoload_with=self.engine)
        country_name = country_name.title()
        query = db.select([table]
                ).where(db.and_(table.columns.City_Name == country_name,
                                table.columns.Language == lang))
        items = self.connection.execute(query)
        return items.fetchall()
    
    def save_dataframe_row(self, dataframe: pd.DataFrame, table: str, country_name:str, con: str, lang:str):
        """This method verify that a register doesn't exist and store a new row

        Args:
            dataframe (pd.DataFrame): reference dataframe that is built in main.py
            table (str): table where the row is going to be stored
            country_name (str): country name to searc and verify the register is not already into database
            con (str): database engine or connection
        """
        items = self.get_by_country(table, country_name, lang)
        if len(items) == 0:
            dataframe.to_sql(table,con=con,index=False, if_exists='append')
        else:
            print('This data already exists in the database!\n')
        
        
    
    





