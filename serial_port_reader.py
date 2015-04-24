#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import serial, io, time

port = "/dev/serial/by-id/usb-058f_9720-if00"

ser = serial.Serial(port, timeout=1)

f= open('/home/qitlab/www/outfile','w')
while(True):
    data_list =[]    
    for i in range(1,9,1):
        value = []
        data = ''
        while data != '\r': # readdata untile all 8 channels read
            data = ser.read()
            value.append(data)
        data_list.append(''.join(value))
    result = {}  
    wavelength = str(data_list)
    try: #create correct formated wavelength data from serial read
        for k, v in [s.split('@') for s in wavelength.split(',')]:
            k = k.strip(" '")
            k = k.strip("'[")    
            v = v.strip("[]")
            v = v.strip("\/r'")   
            result[k] = 'wavelength['+k+'] = ' + v +', time = '+ str(time.time())+'\n'
    except ValueError: #ignores incorrect read issues
        pass 
    for i in range(1,9,1): #loop to handle case of channel off
        if str(i) not in result.keys():
            result[str(i)] = 'wavelength['+str(i)+'] = -2.0000, time = '+ str(time.time())+'\n'
            #print "channel " + str(i)+ " off"
    a = sorted(result.values())
    b = ''.join(a)
    print b
    f.seek(0,0)
    f.write(b)
ser.close()
f.close()
"""
wavelength[3] = -3.00000, time = 1428566150.374853
wavelength[4] = -3.00000, time = 1428566150.375197
wavelength[5] = 847.81523, time = 1428566150.375511
wavelength[6] = 493.54586, time = 1428566150.375744
wavelength[7] = 649.86905, time = 1428566150.376035
wavelength[0] = 646.72199, time = 1428566150.376253
wavelength[1] = -3.00000, time = 1428566150.376423
wavelength[2] = -3.00000, time = 1428566150.376597
wavelength[3] = -3.00000, time = 1428566150.376770
wavelength[4] = -3.00000, time = 1428566150.376991
wavelength[5] = 847.81523, time = 1428566150.377205
wavelength[6] = 493.54586, time = 1428566150.377418
wavelength[7] = 649.86905, time = 1428566150.377591
wavelength[0] = 646.72198, time = 1428566150.377775
wavelength[1] = -3.00000, time = 1428566150.378027
wavelength[2] = -3.00000, time = 1428566150.378218
"""