from multiprocessing import connection
import pandas as pd
import sys
import requests
import cx_Oracle
import json
import urllib
from requests.auth import HTTPBasicAuth

cx_Oracle.init_oracle_client(lib_dir=r"C:\instantclient_19_9")


def GetConn():

    try:
        dsnStr = cx_Oracle.makedsn(
        "192.168.70.12", "1521", "ORCL")

        # Connect as user "hr" with password "welcome" to the "orclpdb1" service running on this computer.
        connection = cx_Oracle.connect(user="datamart", password="datamart",
                                    dsn=dsnStr)

        return connection   
    except:
        print(sys.exc_info())     

def insert(d):
    try:

        connection = GetConn()
        cursor = connection.cursor()
        query = f"INSERT INTO CONT_CAMARAS(Interval_start,Interval_stop,Camera_serial_number,Counter_name,Pedestrians_coming_in,Pedestrians_going_out) VALUES {d} "
        #print(query)
        cursor.execute(query)
        connection.commit()

    except:
        print(sys.exc_info())    
    finally:    
        if cursor:
            cursor.close()
        if connection:
            connection.close()   

def delete():
    try:

        connection = GetConn()
        cursor = connection.cursor()
        query = f"delete from cont_camaras"
        #print(query)
        cursor.execute(query)
        connection.commit()

    except:
        print(sys.exc_info())    
    finally:    
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def call_contingencia_Camaras(today):
    connection = GetConn()
    try:
        cursor = connection.cursor()

        cursor.callproc('contingencia_Camaras', [today,today])

    except Exception as e:
        return {"messaje": str(e)}
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()