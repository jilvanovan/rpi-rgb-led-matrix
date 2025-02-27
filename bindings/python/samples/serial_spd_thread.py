import serial
import time
import threading
from datetime import datetime

class serial_main_thread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        print("[Serial] Init ..........)")        
        self.active = False
        time.sleep(1)
        self.spd_buff = 0
        self.emote_status = 0
        self.ser = serial.Serial('/dev/speed_sensor', 9600, timeout=1)
        print("[Serial] Initialization completed")

    @staticmethod
    def data_logging(input_speed):
        print(["Data Log Start"])
        f = open("/home/pi/display16x32/rpi-rgb-led-matrix/bindings/python/samples/datalog.csv", "a")
        f.write(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))+","+str(input_speed)+"\n")
        f.close()

    def close(self):
        self.active = False
        self.db.close()
        print("[Serial] Thread closed")

    def get_speed_data(self):
            max=0
            min=0
            try:
                while True:
                    self.spd_buff=0
                    intreturn=0
                    if self.ser.in_waiting > 0:
                        bytetoread=self.ser.inWaiting()
                        line = self.ser.read_until(b'efef') 
                        output = line.split(b'~~')            
                        for parsing in output:
                            if parsing != b'':
                                # print(parsing[0:2])
                                if parsing[0] == 0x03 and parsing[1]==0x01:
                                    print("[Serial] Data received : ",parsing)
                                    intreturn=int.from_bytes(parsing[4:6], "big")
                                    # print(intreturn)
                                    if intreturn < 70:
                                        # print(intreturn)
                                        intreturn=intreturn
                                    if intreturn>0:
                                        if min==0:
                                            min=intreturn
                                        if intreturn<=min:
                                            min=intreturn
                                        if intreturn>=max:
                                            max=intreturn
                                self.spd_buff=intreturn
                                time.sleep(0.09)
                                if intreturn > 0 and intreturn < 20:
                                    self.emote_status=0 #senyum
                                if intreturn > 20 and intreturn < 40:
                                    self.emote_status=1 #biasa
                                if intreturn > 40:
                                    self.emote_status=2 #manyun
                        if intreturn>0:
                            self.data_logging(intreturn)


            except (IndexError,OSError):
                pass
                print("[Serial Thread] Error")
                print("Kill this thread")
                self.close()
                self.active=False
    def run(self):
        print(f"[Serial] Thread started")
        self.active = True
        while self.active:
            self.get_speed_data()






















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
