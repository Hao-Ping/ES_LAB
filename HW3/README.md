## Overview
The ble_scan_connect.py can do some CCCD operation including: scanning ble devices nearby, connecting to your device, sending/receiving data to/from the device

## Step
1. Open app "BLE Scanner" on your phone and input the message you want to send, then start advertising
2. Find your device's mac address using
```
sudo hcitool lescan
```
3. Run ble_scan_connect.py
```
sudo python ble_scan_connect.py
```
4. Enter the number of device's mac address
5. Check if the message is correct
