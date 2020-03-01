from aria2xml import aria2
token = None # change with an actuall secret token
aria = aria2(secret=token)

print(aria.status('2ed43624c26ec875'))  # Replace this with actual gid
print(aria.addMagnet(
    [''] # Actual Magent Link
            ))
print(aria.removeDownloadResult('90125715d4d2dc8c')) # Replace with actual gid