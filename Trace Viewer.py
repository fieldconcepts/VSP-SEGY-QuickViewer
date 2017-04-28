# from obspy import read
import obspy
import matplotlib.pyplot as plt
import pylab

#importing segy file fromm file

data = obspy.read("C:/Users/ben.kaack/Documents/Operations/3. Projects/20170127 Precision Impulse/Dataset.sgy", format="SEGY")
st = data[0:25]
meta = str(st[0])

#Grab the number of traces per shot by analysing the date and times of first group of traces.

timelist = []
for i in range(len(st)):
    td = str(st[i])
    timedate = td[25:44]
    timelist.append(timedate)
 
t = str(st[0])[25:44]
tracespershot = timelist.count(t)


#User select shot number from segy dataset

print "Input shot number between 1 and " + str((len(data))/tracespershot) + "..."
shotselect = input()
shotend = shotselect * tracespershot
shotstart = (shotselect - 1) * tracespershot
st = data[shotstart:shotend]

#User select components from segy dataset
print "\n" + "Select component...."
print "1. VZ"
print "2. HX"
print "3. HY"
twig = (int(input()))-1

#User select zoom start  & end points
print "\n" + "Choose zoom start point (0 for default)...."
zoomstart = int(input())
print "\n" + "Choose zoom end point (0 for default)...."
zend = int(input())
if zend == 0:
    zoomend == int(meta[96:100])
elif zend > 0:
    zoomend == zend

#Pulling out the meta data for selected shot


print "\n" + "----------------------------------------META DATA--------------------------------------------" + "\n"
print "Shot Number: " + str(shotselect)
print "Date: " + meta[25:35]
print "Time: " + meta[36:44]
if twig == 0:
    print "Component: VZ"
elif twig == 1:
    print "Component: HX"
elif twig == 2:
    print "Component: HY"
print "Sample Rate: " + str(float(meta[85:89])) + " Hz"
print "Sample Interval:  " + str(1000/(float(meta[96:100]))) + " ms"
print "Number of Samples: " + meta[96:100]
print "Record Length: " + str(1000*(float(meta[85:89]))/float(meta[96:100])) + " ms"
print "Number of traces in selected shot: " + str(len(st))
print "Number of traces entire dataset: " + str(len(data))

print "\n" + "---------------------------------------SHOT #" + str(shotselect) + " -------------------------------------------" + "\n"


#plot Time break and surface geo, then every 5th trace. the VZ/HX/HY channel from 5 tools.

count = 2
subplot = 2

for i in range(len(st)):
    if i % 5 == 0:
        count += 1    

plt.figure(1)

plt.subplot(str(count) + "11")
plt.plot(st[4])
    
plt.subplot(str(count) + "12")
plt.plot(st[3])


for i in range(len(st)):

    if i % 5 == 0:   
        tr = st[i + twig][zoomstart:zoomend]
        subplot += 1
         
        plt.subplot(str(count) + "1" + str(subplot))
        plt.plot(tr, color = '0.4')

plt.show()
