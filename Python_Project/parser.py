# Author: Bijan Vafaei
# Purpose: Parse the XMl "stream.xml" we create in the prior part of HW#1
# and print the Detector_ID and Status


import os
import sys
import time
import urllib2
import xml.etree.ElementTree as ET
import csv

Detector_ID = []
Status = []

path = os.getcwd()

#Get the root node of the XML hierarchy
tree = ET.parse('stream.xml')
root = tree.getroot()

#Get the 'Detector-id' and its 'status' from XML
for i in range(0,100,1):
    z = root.getchildren()[2].getchildren()[0].getchildren()[3].getchildren()[i]
    print z.getchildren()[0].text, '|', z.getchildren()[1].text

    Detector_ID.append(z.getchildren()[0].text)
    Status.append (z.getchildren()[1].text)

if not os.path.exists(path + "\\" + "streamdata.csv"):
    csv = open('streamdata.csv', 'w')

row = []
row.append(['Detector_ID', 'Status'])
for i in range (len(Detector_ID)):
     row.append([str(Detector_ID[i]), str(Status[i])])


writer = csv.writer(open('streamdata.csv', 'w'), delimiter ='\n', )
writer.writerow(row)


    

