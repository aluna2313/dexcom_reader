import readdata
import util
import constants
# import time

x = util.find_usbserial(constants.DEXCOM_USB_VENDOR, constants.DEXCOM_USB_PRODUCT)
x = readdata.DexcomG6(x)
x.LocateAndDownload()
print(x.ReadDatabasePageRange('SENSOR_DATA'))
print(x.ReadDatabasePageRange('EGV_DATA'))
print(x.ReadDatabasePageRange('METER_DATA'))
#readdata.Dexcom.LocateAndDownload()
#x = util.find_usbserial(constants.DEXCOM_USB_VENDOR, constants.DEXCOM_USB_PRODUCT)
#x = readdata.Dexcom(x)
#x.flush()
#print(x.ReadDatabasePageRange('RECEIVER_LOG_DATA'))
#print(x.ReadDatabasePageRange('USER_SETTING_DATA'))
#x.Disconnect()
#x.Connect()
# readdata.Dexcom.LocateAndDownload()
# time.sleep(60)