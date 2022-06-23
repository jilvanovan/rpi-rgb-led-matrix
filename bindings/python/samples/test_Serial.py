import serial
import threading


class TestSerial(threading.Thread):
    def __init__(self):
        super().__init__()
        self._s = serial.Serial("/dev/ttyUSB0", 9600, timeout=1)
        self.active = False

    def stop():
        self.active = False
        self.join()

    def run(self):
        self.active = True
        while self.active:
            x = self._s.read(1024)
            if x:
                print(f"received {x}")
        self._s.close()
