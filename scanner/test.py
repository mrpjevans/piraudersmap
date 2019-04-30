import time
from beacontools import BeaconScanner


def callback(bt_addr, rssi, packet, additional_info):
    print("<%s, %d> %s %s" % (bt_addr, rssi, packet, additional_info))

# scan for all advertisements from beacons
scanner = BeaconScanner(callback)
scanner.start()
time.sleep(5)
scanner.stop()
