import serial
import time
import pyvjoy

# vJoy Device 1
j = pyvjoy.VJoyDevice(1)

print("Opening COM6...")

ser = serial.Serial("COM6", 115200, timeout=1)

print("Waiting for ESP32...")
time.sleep(5)

ser.reset_input_buffer()

# Convert 1000-2000 to vJoy range
def map_axis(value):
    value = max(1000, min(2000, value))
    return int((value - 1000) * 32767 / 1000)

# Remap one range to another
def remap(value, in_min, in_max):
    value = max(in_min, min(in_max, value))
    return int((value - in_min) * 1000 / (in_max - in_min) + 1000)

print("Running...")

while True:

    line = ser.readline().decode(errors="ignore").strip()

    if "," not in line:
        continue

    try:
        parts = line.split(",")

        if len(parts) != 4:
            continue

        ch1, ch2, ch3, ch4 = map(int, parts)

        # Center CH2
        

        # Ignore invalid packets
        if ch1 == 0 and ch2 == 0 and ch3 == 0 and ch4 == 0:
            continue

        # CH2 calibration
        ch2 = remap(ch2, 1440, 2000)

        # CH3 calibration (Throttle)
        ch3 = remap(ch3, 1505, 1997)

        # CH1 - Aileron
        j.set_axis(
            pyvjoy.HID_USAGE_X,
            map_axis(ch1)
        )

        # CH2 - Elevator (reversed)
        j.set_axis(
    pyvjoy.HID_USAGE_Y,
    map_axis(ch2)

        )

        # CH3 - Throttle
        j.set_axis(
            pyvjoy.HID_USAGE_Z,
            map_axis(ch3)
        )

        # CH4 - Rudder
        j.set_axis(
            pyvjoy.HID_USAGE_RX,
            map_axis(ch4)
        )

    except Exception as e:
        print("Error:", e)
        continue