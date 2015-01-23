Wavemeter switch control software
=================================

This software is used to communicate with an arduino, which provides TTL pulse to switch the channels of a lightwave link fibre switch. The common output of the fibre switch is connected to the fibre switch of our WS7 wavemeter. This allows us to expanded the capacity of our wavemeter to 16 channels. The secondary switch acts to give quick view of a wavelength. The update rate is around 1 second depending on the total exposure time of all 8 primary channels. 

The secondary switch is controlled by a web interface that is acceable on the local network. The web interface is written using python Flask and bootstrap css. The python server communicates with the arduino through a serial connection. The wavelength are read from the wavemeter through a serial connection and writen to a file on a server. This file can be read through CGI straight into the python program. The Javascript updates the wavelength every second and send switch presses back to the python server. 

The code is very basic and not very well written or pretty but it works. My first effort working with Javascript and HTML. 

Requirements
----    

Python Flask