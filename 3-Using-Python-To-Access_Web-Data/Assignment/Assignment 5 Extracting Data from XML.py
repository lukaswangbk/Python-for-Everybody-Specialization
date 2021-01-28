"""Extracting Data from XML"""

'''
In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.

We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_1146874.xml (Sum ends with 98)
You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis."""
'''

#Enter location: http://py4e-data.dr-chuck.net/comments_1146874.xml
#Retrieving http://py4e-data.dr-chuck.net/comments_1146874.xml
#Retrieved 4220 characters
#Count: 50
#Sum: 2259

import urllib.request as ur
import xml.etree.ElementTree as ET

url = input('Enter location: ')

total_number = 0
sum = 0

print('Retrieving', url)
xml = ur.urlopen(url).read()
print('Retrieved', len(xml), 'characters')

tree = ET.fromstring(xml)
counts = tree.findall('.//count')
for count in counts:
    sum += int(count.text)
    total_number += 1

print('Count:', total_number)
print('Sum:', sum)