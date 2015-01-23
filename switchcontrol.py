# -*- coding: utf-8 -*-
"""
Created on Tue Jan 20 19:46:21 2015

@author: nick
"""

import serial

class wavemeterswitch(object):
# Module for communicating with the power meter           
    
    def __init__(self,port):
        self.serial = self._open_port(port)
        self.serial_write(1)# set to channel 1
        
    def _open_port(self, port):
        ser = serial.Serial(port,baudrate = 115200, timeout=5)
        return ser
        
    def close_port(self):
        self.serial.close()

        
    
    def serial_write(self, value):
        self.serial.write(str(value))
    