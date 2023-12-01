import sqlite3 as sq
import pandas as pd

class DataBase:
    # === from db ===
    def from_db_to_pd(self, params, query):
        """ reading data from database into pandas """
        try:
            conn = sq.connect(params.nameDB)
            df = pd.read_sql(con=conn, sql=query)
        except Exception as ex:
            print('error db:', ex)
            df = pd.DataFrame()
        return df

    def from_db_query_to_pd(self, params, query):
        """ reading data from database 'query' into pandas """
        try:
            conn = sq.connect(params.nameDB)
            df = pd.read_sql_query(query, conn)
        except Exception as ex:
            print('error db:', ex)
            df = pd.DataFrame()
        return df

    # ==== to db ===

    def df_to_db(self, params, df):
        """ saving pandas dataframe to database """
        try:
            conn = sq.connect(params.nameDB)
            df.to_sql(params.nameTab, conn, if_exists='replace', index=False)
            conn.close()
        except Exception as ex:
            print('error db:', ex)

    def from_csv_to_db(self, params, splitter):
        """ reading data from csv into database """
        df = pd.read_csv(params.filename, sep=splitter, encoding='utf-8')
        try:
            conn = sq.connect(params.nameDB)
            df.to_sql(params.tab_name, conn, if_exists='replace', index=False)
        except Exception as ex:
            print('error db:', ex)
            
    def from_excel_to_db(self, params):
        """ reading data from excel into database """
        df = pd.read_excel(params.filename, sheet_name=0)
        try:
            conn = sq.connect(params.nameDB)
            df.to_sql(params.tab_name, conn, if_exists='replace', index=False)
        except Exception as ex:
            print('error db:', ex)
            
            

    



   
