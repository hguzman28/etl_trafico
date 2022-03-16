import sys
import cx_Oracle

cx_Oracle.init_oracle_client(lib_dir=r"C:\instantclient_19_9")

def GetConn():
    dsnStr = cx_Oracle.makedsn(
    "192.168.70.12", "1521", "ORCL")

    # Connect as user "hr" with password "welcome" to the "orclpdb1" service running on this computer.
    connection = cx_Oracle.connect(user="datamart", password="datamart",
                                dsn=dsnStr)

    return connection    

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


def read_files():
    
    list_all_cam = []

    for file in range(18):
        
        try:    
            print(str(file)+".txt")

            f = open(str(file)+".txt","r")

            f = f.read().split("\n")
                        

            lista_data = [ eval("'"+line.replace(",","','")+"'") for line in f    ]

            lista_data.pop(0)
            #print(lista_data)
            list_all_cam.extend(lista_data)
                


        except:
            print(str(sys.exc_info()))

    return list_all_cam  
 


datos = read_files()

for line in datos:
    print(line)
    insert(line)


 



