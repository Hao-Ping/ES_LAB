## Overview
The ble_scan_connect.py can do some CCCD operation including: scanning ble devices nearby, connecting to your device, sending/receiving data to/from the device

## Step
1. Open app "BLE Scanner" on your phone and input the message you want to send, then start advertising
2. Remember the UUID of the device and the service
3. Modify UUID on line 33, 37 with device's UUID and service's UUID
4. Find your device's mac address using
```
sudo hcitool lescan
```
5. Run ble_scan_connect.py
```
sudo python ble_scan_connect.py
```
6. Enter the number of device's mac address
7. Check if the message is correct
