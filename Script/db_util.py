import numpy as np
import pandas as pd

from sqlalchemy import create_engine
import pymysql
import traceback

# MySQL Connector using pymysql
pymysql.install_as_MySQLdb()
import MySQLdb


def save_db(df, table):
    try:
        engine = create_engine("mysql+mysqldb://root:"+'kdpark81'+"@localhost/beer", encoding='utf-8')
        conn = engine.connect()

        # Save dataframe to database
        df.to_sql(name=table, con=engine, if_exists='append')
        print("Saved successfully!!")
        
    except:
        traceback.print_exc()
        
    finally:
        conn.close()
        