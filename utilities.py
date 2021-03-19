import bluetooth

# Shows us bluetooth devices nearby
def find_bluetooth():
    """ This function finds the nearby bluetooth devices """
    devices = bluetooth.discover_devices(lookup_names=True)
    print(devices)


find_bluetooth()