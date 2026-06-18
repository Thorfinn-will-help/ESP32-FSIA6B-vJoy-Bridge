# ESP32 FS-IA6B to vJoy Bridge

Use a FlySky FS-i6 transmitter as a Windows joystick for RC flight simulators.

This project uses an ESP32 to read iBUS data from a FlySky FS-IA6B receiver and send it to a PC over USB Serial. A Python script then converts the received channel data into a vJoy virtual joystick, allowing RC simulators such as PicaSim to be controlled directly from the transmitter.

---

## Features

* Reads FlySky iBUS data using an ESP32
* Converts transmitter inputs into a Windows joystick
* Compatible with vJoy
* Works with RC simulators such as PicaSim
* Low-cost hardware solution

---

## Hardware Used

* FlySky FS-i6 Transmitter
* FlySky FS-IA6B Receiver
* ESP32 DevKit V1
* USB Cable
* Windows PC

---

## Wiring

Connect the FS-IA6B receiver to the ESP32 using the **iBUS Servo** port.

| FS-IA6B Pin | ESP32 DevKit V1 Pin |
| ----------- | ------------------- |
| Signal (S)  | GPIO16 (RX2)        |
| VCC (+5V)   | VIN                 |
| GND (-)     | GND                 |

### Wiring Diagram

```text
FS-IA6B iBUS Servo Port

Signal (S) ----------> GPIO16 (RX2)

VCC (+5V) -----------> VIN

GND (-) -------------> GND
```

### Notes

* Use the **iBUS Servo** port on the receiver.
* Do not use CH1-CH6 outputs.
* UART2 is used for communication.
* RX pin: GPIO16
* TX pin: Not used
* Baud rate: 115200
* Receiver power is supplied from the ESP32 VIN pin.
* ESP32 is powered through USB from the PC.

---

## Data Flow

```text
FlySky FS-i6 Transmitter
            │
            ▼
      FS-IA6B Receiver
            │
        iBUS Data
            │
            ▼
      ESP32 DevKit V1
            │
       USB Serial
            │
            ▼
      Python Bridge
            │
            ▼
   vJoy Virtual Joystick
            │
            ▼
      RC Flight Simulator
```

---

## Development Environment

This project was developed using:

* Visual Studio Code
* PlatformIO Extension
* Python 3.13
* Windows 11

---

## PlatformIO Configuration

`platformio.ini`

```ini
[env:esp32dev]
platform = espressif32
board = esp32dev
framework = arduino
monitor_speed = 115200

lib_deps =
    bmellink/IBusBM
```

---

## Software Requirements

### Visual Studio Code

Install:

* Visual Studio Code
* PlatformIO Extension

### Python

Install required packages:

```bash
pip install pyserial pyvjoy
```

### vJoy

Install vJoy and create one virtual device with:

* X Axis
* Y Axis
* Z Axis
* RX Axis

---

## Repository Structure

```text
ESP32-FSIA6B-vJoy-Bridge/
│
├── platformio.ini
├── src/
│   └── main.cpp
├── rc_to_vjoy.py
├── LICENSE
└── README.md
```

---

## Building and Uploading

1. Open the project folder in Visual Studio Code.
2. Install the PlatformIO extension.
3. Connect the ESP32 through USB.
4. Build the project.
5. Upload the firmware.
6. Open the Serial Monitor if desired.

The ESP32 should begin outputting iBUS channel values over USB Serial.

---

## Running the Python Bridge

Edit the COM port in `rc_to_vjoy.py` if required:

```python
PORT = "COM6"
```

Run:

```bash
python rc_to_vjoy.py
```

After launching the script, transmitter stick movement should appear in Windows Game Controllers and RC simulators.

---

## Default Channel Mapping

| Channel | Function         |
| ------- | ---------------- |
| CH1     | Roll (Aileron)   |
| CH2     | Pitch (Elevator) |
| CH3     | Throttle         |
| CH4     | Yaw (Rudder)     |

Channel mapping can be modified in the Python script.

---

## Tested Configuration

* FlySky FS-i6
* FlySky FS-IA6B
* ESP32 DevKit V1
* Windows 11
* Python 3.13
* PlatformIO
* vJoy
* PicaSim

---

## Known Issues

* COM port numbers may differ between systems.
* Axis calibration may be required in Windows.
* Some simulators may require axis inversion or remapping.

---

## Future Improvements

* Automatic COM port detection
* Calibration utility
* Configurable channel mapping
* Additional iBUS channel support
* Multiple simulator profiles

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgements

This project uses:

* IBusBM
* pyserial
* pyvjoy
* Chatgpt as well (Everything was done by Him)

Thanks to the RC community for documenting the FlySky iBUS protocol and helping make low-cost simulator setups possible.
