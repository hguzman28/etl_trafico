from multiprocessing import connection
import pandas as pd
import sys
import requests
import cx_Oracle
import json
import db
import datetime

  
def leer_csv(lista_camaras,list_fecha):



    tiendas_hechas=[]
    tiendas_no_hechas=[]

    num = 1

    for camara in lista_camaras:

        for dia in list_fecha:

            try:

                url= "http://"+camara+"/local/people-counter/.api?export-csv&date="+dia+"&res=1h"
                #url = "http://10.4.0.35/local/people-counter/.api?export-csv&date=20220228&res=1h"
                #url="http://"+camara+"/local/people-counter/.api?export-csv&date=all&res=1h"
                datos = pd.read_csv(url)

                datos.to_csv(str(num)+".csv")
                print(num)
                datos.to_csv(camara+".csv")
                num = num + 1
                
 
                #tiendas_hechas.append(camara)
          
            except:
                print(sys.exc_info())

                #tiendas_no_hechas.append(camara)
 



    print(tiendas_hechas)
    print(";;;;;;;;;;;;;;;;;;;;;;;;;;;;")
    print(tiendas_no_hechas)


def leer_camaras(lista_camaras,list_fecha):

    tiendas_hechas={"tienda":[]    }
    tiendas_no_hechas={"tienda":[] }
    list_all_cam=[]


    #num = 1

    for camara in lista_camaras:

        for dia in list_fecha:

            try:

                url= "http://"+camara+"/local/people-counter/.api?export-csv&date="+dia+"&res=1h"
                #url = "http://10.4.0.35/local/people-counter/.api?export-csv&date=20220228&res=1h"
                #url="http://"+camara+"/local/people-counter/.api?export-csv&date=all&res=1h"
                s = requests
                s.auth = ('root', 'c4m4r45')
                headers = {"User-Agent": "Chrome/99.0.4844.51"}
  
                f = s.get(url,headers=headers)

                print(f.status_code)


                lista_data = [ eval("'"+line.decode().replace(",","','")+"'") for line in f.iter_lines()     ]

                lista_data.pop(0)
                list_all_cam.extend(lista_data)

                #fg = open(str(num)+".csv", "w")
                #fg.write(str(f.text))
                #fg.close()

                #print(num)
                #datos.to_csv(camara+".csv")
                #num = num + 1
                
                

                #tiendas_hechas["fecha"].append(dia)
                tiendas_hechas["tienda"].append(url)


            except:
                print(str(camara)+str(sys.exc_info()))
                #tiendas_no_hechas["fecha"].append(dia)
                tiendas_no_hechas["tienda"].append(url)

                #tiendas_no_hechas.append(camara)
    



    print(tiendas_hechas)
    print(";;;;;;;;;;;;;;;;;;;;;;;;;;;;")
    print(tiendas_no_hechas)
    f = open("tiendas_hechas.csv", "w")
    f.write(str(tiendas_hechas))
    f.close()

    fg = open("tiendas_no_hechas.csv", "w")
    fg.write(str(tiendas_no_hechas))
    fg.close()

    return list_all_cam

def leer_camarasw(lista_camaras,list_fecha):

    tiendas_hechas={"tienda":[]    }
    tiendas_no_hechas={"tienda":[] }
    list_all_cam=[]


    #num = 1

    for camara in lista_camaras:

        for dia in list_fecha:

            try:

                x = requests.get('http://10.23.0.35/local/people-counter/.api?export-csv&date=20220228&res=1h', auth=HTTPBasicAuth('root', 'c4m4r45'))


                print(x)




            except:
                print(str(camara)+str(sys.exc_info()))

                #tiendas_no_hechas.append(camara)
    



    print(tiendas_hechas)
    print(";;;;;;;;;;;;;;;;;;;;;;;;;;;;")
    print(tiendas_no_hechas)
    f = open("tiendas_hechas.csv", "w")
    f.write(str(tiendas_hechas))
    f.close()

    fg = open("tiendas_no_hechas.csv", "w")
    fg.write(str(tiendas_no_hechas))
    fg.close()

    return list_all_cam

 

lista_camaras = ["10.4.0.35","10.1.16.89","10.1.16.88","10.1.16.94","10.1.16.95","10.23.0.35","10.37.0.35","10.42.0.35","10.43.0.35","10.51.0.30","10.28.0.35","192.168.82.35","10.6.0.36","10.7.0.35","10.45.0.35","10.44.0.35","10.36.0.35","10.34.0.35","10.29.0.35","10.8.0.35","10.8.0.36","192.168.92.35","10.5.0.35","10.12.0.35","10.48.0.36","10.48.0.35","10.16.0.34","192.168.11.35","10.18.1.77","10.39.0.35","10.38.0.35","192.168.88.240","10.47.0.35"]
#lista_camaras = ["10.4.0.35"]

today = datetime.datetime.now().strftime("%Y%m%d")
print(today)
list_fecha =[today]


if __name__ == "__main__":
    db.delete()
    lista_datos = leer_camaras(lista_camaras,list_fecha)

    for line in lista_datos:
        print(line)
        db.insert(line)
    #today_prc = datetime.datetime.now().strftime("%d%m%Y")
    #db.call_contingencia_Camaras(today_prc)
    #db.delete()








       







