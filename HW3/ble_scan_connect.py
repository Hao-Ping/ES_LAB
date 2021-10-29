from bluepy.btle import Peripheral, UUID
from bluepy.btle import Scanner, DefaultDelegate
class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)
    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print("Discovered device", dev.addr)
        elif isNewData:
            print("Received new data from", dev.addr)
            
scanner = Scanner().withDelegate(ScanDelegate())
devices = scanner.scan(10.0)
n=0
for dev in devices:
    print("%d: Device %s (%s), RSSI=%d dB" % (n, dev.addr,dev.addrType, dev.rssi))
    

    for (adtype, desc, value) in dev.getScanData():
        if value == "Health Thermometer":
            print('-------------------')
            print(n, desc, value) 
            print('-------------------')

            #print(" %s = %s" % (desc, value))
    n += 1
    
number = input('Enter your device number: ')
print('Device', number)
print('Device address: ',  devices[number].addr)

print("Connecting...")
dev = Peripheral(devices[number].addr, 'random')
        
print("Services...")
for svc in dev.services:
    print(str(svc))
 
try:
    testService = dev.getServiceByUUID(UUID(0x1809))
    for ch in testService.getCharacteristics():
        print(str(ch))
            
    ch = dev.getCharacteristics(uuid=UUID(0x2A1E))[0]
    if (ch.supportsRead()):
        print('ch.read: ', ch.read())

    ch2 = dev.getCharacteristics(uuid=UUID(0x2A1C))[0]
    ch2.write('0000000')
            
finally:
    dev.disconnect() 
