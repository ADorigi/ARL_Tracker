import serial
import time
from influxdb import InfluxDBClient
import uuid
import random
import time

client = InfluxDBClient(host='localhost', port=8086)
client.switch_database('IOT')

ser = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(0.5)
# data =[]     
lst=0;                  
while 1:
    b = ser.readline()         
    string_n = b.decode()   
    string = string_n.rstrip() 
    print(string)
    try:
        flt = float(string)
    except Exception:
        flt = 0.0 
    
    body=[
        
        {"measurement":"Sensor",
        
        "fields":{

        "value":flt

        }       
    }]
    if flt>100:
        client.write_points(body)
        # lst=flt
        
    # else:
    #     if (int)(flt)==1:
    #         if lst>950:
    #             ser.write('0')
    #         elif lst>600:
    #             ser.write('1')
    #         elif lst>350:
    #             ser.write('2')
    #         else:
    #             ser.write('3')


    # print(flt)
    # data.append(flt)           
    time.sleep(0.1)            

ser.close()




# for line in data:
#     print(line)

# print(data)

