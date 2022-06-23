print("[PROGRAM] Starting")
import threading
import time
# from serial_spd_thread import serial_main_thread
from led_thead import led_main_thread

# spd_main = serial_main_thread()
led_main = led_main_thread()

# spd_main.start()

try:
	led_main.start()
except IndexError:
	pass
	print("Something Wrong")
