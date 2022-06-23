import serial
import time

max=0
min=0

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    while True:
        if ser.in_waiting > 0:
             # intreturn = -1
            bytetoread=ser.inWaiting()
            line = ser.read_until(b'efef') 
            output = line.split(b'~~')            
            for parsing in output:
                if parsing != b'':
                    print(parsing[0:2])
                    if parsing[0] == 0x03 and parsing[1]==0x01:
                        print(parsing)
                        intreturn=int.from_bytes(parsing[4:6], "big")
                        print(intreturn)
                        if intreturn < 70:
                            print(intreturn)
                        if intreturn>0:
                            if min==0:
                                min=intreturn
                            if intreturn<=min:
                                min=intreturn
                            if intreturn>=max:
                                max=intreturn

























# import serial
# import binascii
# import struct
# import time
# from database import *

# db_connect()

# if __name__ == '__main__':
#     ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
#     while True:
# #        time.sleep(0.3)
#         f = open("/home/pi/webspd/value.json", "w")
#         f.write("0")
#         f.close()
#         time.sleep(0.5)

#         if ser.in_waiting > 0:
#             intreturn = -1
#             bytetoread=ser.inWaiting()
#             line = ser.read_until(b'efef') 
#             output = line.split(b'~~')
#             for parsing in output:
#                 print(parsing)
#                 intreturn=int.from_bytes(parsing[4:6], "big")
#                 print(intreturn)
#                 if intreturn < 256:
#                  f = open("/home/pi/webspd/value.json", "w")
#                  f.write(str(intreturn))
#                  f.close()
# #                 time.sleep(0.1)
#             # open and read the file after the appending:
#   #              f = open("/home/pi/webspd/value.json", "r")
#    #             print(f.read())
#                  time.sleep(0.01) 
# #            if intreturn != -1:
#  #               db_query(int(intreturn))
#                 # print("jumlah kednaraan: ", count)
#                     # count = count + 1
#                 # url = '10.1.1.170:8181'
#                 # myobj = {'postData': 'Intreturn'}
#                 # x = requests.post(url, data = myobj)
#                 # print(x)
