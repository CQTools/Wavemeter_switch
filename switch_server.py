"""
Created on Mon Sep 29 14:52:13 2014

@author: nick
"""


from flask import Flask, render_template, jsonify
import requests
import switchcontrol
import time
import ctypes
import re

wlm = ctypes.windll.wlmData # load the DLL

uInt32 = ctypes.c_ulong
uInt64 = ctypes.c_ulonglong
double = ctypes.c_double
long = ctypes.c_long


LZERO = long(0)
DZERO = double(0)
cInstCheckForWLM = long(-1)
cInstResetCalc = long(0)
cInstReturnMode = cInstResetCalc
cInstNotification = long(1)
cInstCopyPattern = long(2)
cInstCopyAnalysis = cInstCopyPattern
cInstControlWLM = long(3)
cInstControlDelay = long(4)
cInstControlPriority = long(5)


getfreq = wlm.GetFrequencyNum
getfreq.restype = double

getwave = wlm.GetWavelengthNum
getwave.restype = double

getpat = wlm.GetPatternNum
getpat.restype = long

wlm.SetSwitcherSignalStates(2,1,0) #sets channel 2 on
wlm.SetSwitcherSignalStates(6,1,0) #sets channel 6 on
wlm.SetSwitcherSignalStates(7,1,0) #sets channel 7 on
wlm.SetSwitcherSignalStates(8,1,1) #sets channel 8 on

app = Flask(__name__)

#port ='/dev/serial/by-id/usb-Arduino__www.arduino.cc__0043_5543131303835141E011-if00' #hardwire address as arduino fixed into switch
port = 'COM5'
switch  = switchcontrol.wavemeterswitch(port) #connect to wavemeter
time.sleep(1) #delay to allow for connection
switch.serial_write(1)



channel = 2 #current free wavemeter port on primary switch




@app.route('/')
def home(): #create webpage on index
    return render_template('index.html') #webpage temaplate
global channel_data
channel_data = '1'
    
@app.route('/switch_1') # dont know how to do this for many switches so will be copy paste of function
def switch1():   
    global channel_data
    print 'switch 1 pressed'
    switch.serial_write(1)
    channel_data = '1'
    return channel_data
    
@app.route('/switch_2') 
def switch2():
    global channel_data
    print 'switch 2 pressed'
    switch.serial_write(2)
    channel_data = '2'
    return channel_data
    
@app.route('/switch_3') 
def switch3():
    global channel_data
    switch.serial_write(3)
    channel_data = '3'
    return 
    
@app.route('/switch_4') 
def switch4():
    global channel_data
    switch.serial_write(4)
    channel_data = '4'
    return 
    
@app.route('/switch_5')
def switch5():   
    global channel_data
    switch.serial_write(5)
    channel_data = '5'
    return 
    
@app.route('/switch_6') 
def switch6():
    global channel_data
    switch.serial_write(6)
    channel_data = '6'
    print '6'
    return 
    
@app.route('/switch_7') 
def switch7():
    global channel_data
    switch.serial_write(7)
    channel_data = '7'
    return 
    
@app.route('/switch_8') 
def switch8():
    global channel_data
    switch.serial_write(8)
    channel_data = '8'
    return 
        

    
@app.route("/data", methods= ['GET'])
def get_data():
    data  = {'wavelength': get_wavelength(),
    'freq': get_frequency(),'channel': channel_data} 
    return jsonify(data)



def get_wavelength():
    s = float(getwave(2,DZERO))
    s = round(s,5)
    return str(s) + ' nm' 


def get_frequency():
    s = float(getfreq(2,DZERO))
    s = round(s,5)
    return str(s) + ' THz' 

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)


