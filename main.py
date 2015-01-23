# -*- coding: utf-8 -*-
"""
Created on Mon Sep 29 14:52:13 2014

@author: nick
"""


from flask import Flask, render_template, jsonify
import requests
import switchcontrol
import time

app = Flask(__name__)
port ='/dev/serial/by-id/usb-Arduino__www.arduino.cc__0043_5543131303835141E011-if00' #hardwire address as arduino fixed into switch

switch  = switchcontrol.wavemeterswitch(port) #connect to wavemeter
time.sleep(5) #delay to allow for connection







webserver = 'http://charsiew.qoptics.quantum.nus.edu.sg/cgi-bin/wavelength.cgi?' #hard coded wbserver as never changes

channel = 2 #current free wavemeter port on primary switch

app = Flask(__name__)


@app.route('/')
def home(): #create webpage on index
    return render_template('index.html') #webpage temaplate
global channel_data
channel_data = '5'
    
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
    data  = {'wavelength': get_wavelength(read_webdata(3)),
    'freq': get_frequency(read_webdata(3)),'channel': channel_data} 
    return jsonify(data)



def read_webdata(channel):
    data = requests.get(webserver + str(channel))
    return data.text

def get_wavelength(webdata):
    s = webdata.split('/')
    s = round(float(s[1]),5)
    return str(s) + ' nm' 

def get_time(webdata):
    s = webdata.split('/')
    return s[2]

def get_channel(webdata):
    s = webdata.split('/')
    return s[0]

def get_frequency(webdata):
    w = float(webdata.split('/')[1])
    c = 2.99792458e8
    f = round(c/(w*1e-9)/1e12,5)
    f = str(f)
    return f + ' THz' 

if __name__ == '__main__':
    app.run()


if __name__ == '__main__':
    app.run()
