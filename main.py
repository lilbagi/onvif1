from onvif import ONVIFCamera
import control
from onvif import ONVIFService

mycam = ONVIFCamera('192.168.15.42',80,'boshandi7','***','C:/Python27/wsdl/')
#mycam = ONVIFCamera('192.168.15.42',80,'boshandi7','***','C:/Program Files (x86)/Python37-32/Lib/site-packages/wsdl/')
print (mycam.devicemgmt.GetDeviceInformation())


control.instlinfo(mycam)
control.absolute_move(mycam, -0.2, -0.6, 0)
control.get_status(mycam)
control.absolute_move(mycam, -0.2, -0.6, 0.5)
control.get_status(mycam)
control.absolute_move(mycam, -0.2, -0.6, 0)
control.get_status(mycam)
control.continuous_move(mycam, 'tilt', 0.2, 4)
control.absolute_focus(mycam, 2.4)
control.continuous_focus(mycam, 0.5)


