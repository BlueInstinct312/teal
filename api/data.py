import mysql
from mysql import connector
from mysql.connector import Error
import pandas as pd
from typing import List
from pydantic import BaseModel, Field, ValidationError
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Boolean, Column, Integer, String, Double, select
from database import URL_DATABASE, engine, SessionLocal, Base
import models as models

DATABASE = "TealDB"
PROJECT_DATA_SAMPLE = "../data/project_data.csv"

class CreateDataTable():

    def __init__(self):
        pass

    def __create_database__(self, db_name: str) -> None:
        try:
            connection = connector.connect(
                host="localhost",
                user="root",
                password="password1234!",
                port=3333
            )
            if connection.is_connected():
                cursor = connection.cursor()
                cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
                print(f"Database '{db_name}' created successfully!")
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
        finally:
            if 'connection' in locals() and connection.is_connected():
                cursor.close()
                connection.close()

    def __create_datatables__(self) -> None:
        models.Base.metadata.create_all(bind=engine)
        print("Datatables have been created successfully.")

    def read_data_from_csv(self) -> pd.DataFrame:
        return pd.read_csv(PROJECT_DATA_SAMPLE)

    def retrieve_food_df(self, df:pd.DataFrame) -> pd.DataFrame:
        food_df = df[["photo_id", "business_id", "caption", "food"]]
        return food_df

    def retrieve_business_df(self, df:pd.DataFrame) -> pd.DataFrame:
        business_df = df.drop(columns=["photo_id", "caption", "food", "is_open", "attributes", "hours"])
        return business_df
    
    def seed_datatable(self, df:pd.DataFrame, table_name:str, insert_mode:str="fail") -> None:
        try:
            df.to_sql(
                name=table_name,
                con=engine,
                if_exists=insert_mode
            )
        except ValueError:
            print("Data in TealDB already exists")

    def run_pipeline(self) -> None:
        self.__create_database__(db_name=DATABASE)
        self.__create_datatables__()
        df = self.read_data_from_csv()
        food_df = self.retrieve_food_df(df=df)
        business_df = self.retrieve_business_df(df=df)
        self.seed_datatable(df=food_df, table_name="food")
        self.seed_datatable(df=business_df, table_name="business")


