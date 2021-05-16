
import network
#  This sets up an access point to use later
net = network.WLAN(network.AP_IF)
net.config(essid='ESP32-3')
net.active(True)
