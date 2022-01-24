import bluetooth

startMarker = "0"
endMarker = "255"

test = "a"

startMarker = startMarker.encode("UTF-8")
endMarker = endMarker.encode("UTF-8")

def sendToArduino(sendStr):
  global startMarker, endMarker
  txLen = chr(len(sendStr))
 # adjSendStr = encodeHighBytes(sendStr)
  adjSendStr = chr(startMarker) + txLen + sendStr + chr(endMarker)
  print(adjSendStr)


if __name__ == "__main__":
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    print(startMarker)
    print(endMarker)
    print(sendToArduino("Hello"))
