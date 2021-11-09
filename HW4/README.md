## Overview
HW4 shows 3 functionality 
(Run source file on STM; **ble_scan_HW4.py** on raspberry pi):
* Enter '1' or '0' on raspberry pi to control STM's LED2. (Use raspberry pi as central, STM32L4 IoT node as BLE peripheral.)
* Test STM's notification function
* A service in STM32L4 IoT node so that it can send my student ID to raspberry pi through BLE

## Execution
1. Modify line 14 in ble_scan_HW4.py
```python
DEVICE_NAME = "Button_HaoPing" #DEVICE_NAME need to be align with line 28 in source/main.cpp
```
2. Compile and run the source code on STM
3. run ble_scan_HW4.py on raspberry pi
```
sudo python ble_scan_HW4.py
```
4. follow the instruction to test different functionalities: 
* input 1 to test LED toggle, "1" for on; "0" for off (Ctrl+C to choose test mode again)
* input 2 to test button notification and reading student ID (Ctrl+C to choose test mode again)
* input 3 to test LED1 notification (Ctrl+C to choose test mode again)
