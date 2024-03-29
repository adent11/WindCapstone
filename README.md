# WindCapstone
2022-2023 Capstone Engineering Project. 

## Table of Contents
* [Scheduled work](#documentation)
* [Code](#Code)



### Task:
Use cumulative knowledge to solve an important issue.


## Resources<ln>

* [Autonomous drone landing](https://www.suasnews.com/2018/09/mapturedrone-in-a-box-prototype-automated-take-off-and-landing-demonstration/)
* [Wind measuring Drone](optolution.com/en/news/single-view-en/optokopter/)

## Materials
* [Modern Device Wind Sensor Rev. P](https://moderndevice.com/products/Wind-Sensor-Rev-P)
* Contixo GPS F18 Drone
* Raspberry Pi Pico
* Adafruit MPL3115A2 barometric altimeter
* Adafruit PowerBoost and battery
* 3d printed and lasercut plastic

## Risk Mitigation
* The main source of risk for our project is drone flight, so we will use proper precautions and only fly in appropriate circumstances

## Tentative schedule
* November 1st - December 20th:
    * Make Onshape model of box
    * Get any sort of wind speed readings (not on a drone)
* January 6th - April 1st:
    * Have box made
    * Have drone fly with full payload
    * Have prototype for charging system
* April - End of School:
    * Have charging system
    * Be able to detect wind speeds accurately
    * Make project summary presentation
   
## Final Code
[Boot.py](https://github.com/adent11/WindCapstone/blob/main/Code/boot.py)<details><summary><b></b></summary>
   
```python
# WindCapstone boot code
# Alden Dent

import board, digitalio, storage, time

led = digitalio.DigitalInOut(board.LED) # LED setup
led.direction = digitalio.Direction.OUTPUT
led.value = False

buttonPin = digitalio.DigitalInOut(board.GP0) # Button Setup
buttonPin.direction = digitalio.Direction.INPUT
buttonPin.pull = digitalio.Pull.UP

# If button is pressed, CircuitPython can write to CIRCUITPY filesystem.
if not buttonPin.value:
    led.value = True # Turns on LED ot show that Pico is in write mode
    time.sleep(3)
    storage.remount("/", readonly=False)

while not buttonPin.value: # Waits for button release to continue
    pass
```
   
</details>
   
[Code.py](https://github.com/adent11/WindCapstone/blob/main/Code/code.py)<details><summary><b></b></summary>

```python
# WindCapstone main code
# Alden Dent

import time, board, digitalio, analogio, adafruit_mpl3115a2, busio, os

i2c = busio.I2C(board.GP17, board.GP16) # Barometric altimeter setup
b = adafruit_mpl3115a2.MPL3115A2(i2c)
b.sealevel_pressure = 103040

windIn = analogio.AnalogIn(board.GP28) # Wind sensor setup
tempIn = analogio.AnalogIn(board.GP27)

buttonPin = digitalio.DigitalInOut(board.GP0) # Mode button setup
buttonPin.direction = digitalio.Direction.INPUT
buttonPin.pull = digitalio.Pull.UP

rPin = digitalio.DigitalInOut(board.GP6) #LED setup
rPin.direction = digitalio.Direction.OUTPUT
gPin = digitalio.DigitalInOut(board.GP7)
gPin.direction = digitalio.Direction.OUTPUT
bPin = digitalio.DigitalInOut(board.GP8)
bPin.direction = digitalio.Direction.OUTPUT

red, green, blue, cyan = (1, 0, 0), (0, 1, 0), (0, 0, 1), (0, 1, 1) # variables for different colors to input to setColor function

def setColor(c): # Sets the color of the LED
    rPin.value = c[0]
    gPin.value = c[1]
    bPin.value = c[2]

def buttonPressed(): # Simplifying confusing negatives for semantic ease
    return not buttonPin.value

def getVoltage(inVal): # Converts analog input to voltage
    return (inVal * 3.3) / 65536

def voltsToArduinoIn(volts): # Converts voltage input to arduino analog reading
    return volts * 1023 / 5

flightNum = 1

try:
    while True:
        filePath = f"flight{flightNum}Data.csv"
        dataList = []
        setColor(green)
        while not buttonPressed(): # Waiting for button press
            pass
        while buttonPressed(): # Then button release
            pass
        time.sleep(.5)
        setColor(blue)
        startTime = time.time()
        while not buttonPressed(): # Records data until button is pressed
            windVolts = getVoltage(windIn.value)
            windMPH = ((voltsToArduinoIn(windVolts) - 264) / 85.6814)**3
            tempVolts = getVoltage(tempIn.value)
            tempC = (tempVolts-.4) / .0195
            dataList.append(f"{b.altitude},{windMPH},{b.temperature},{tempC},{windVolts},{time.time()-startTime}\n") # Recording data to list
        while buttonPressed(): # Wait for button release
            pass
        time.sleep(.5)
        setColor(cyan)
        with open(filePath, "w") as file: # Writes data to a file
            file.write("altitude,windMPH,barometerTemp,windTemp,windVolts,timeFromStart\n")
            for dataLine in dataList:
                file.write(dataLine)
        flightNum = flightNum + 1
except: # Shows if there has been an error
    setColor(red)
    while True:
        pass
```
</details>

# Weekly Documentation

### Week of 10.31.22
* Succesfully pivoted to new project
* Created slideshow
* Developed plan for deliverables and figured out essential vs nonessential requirements
* Relatively sure we will be purchasing the [Modern Device Wind Sensor Rev. P](https://moderndevice.com/products/Wind-Sensor-Rev-P), though getting enough power to it could be a challenge
* Next we will figure out how to connect the Rasperry Pi to the drone

### Week of 11.07.22
* Ordered wind hot wire anemometer sensor
*   Researched anemometer calibration on the [maker's website](https://moderndevice.com/blogs/documentation/wind-sensor-calibration-and-the-wind-tunnel), it is somewhat complicated and may be inaccurate in extreme weather conditions
* Tested how much the Tello drones can lift
* Realized that we will have to use another drone with GPS stabilization since it would be very difficult to correct for the drone's drifting in the wind

### Week of 11.14.22
* Test flew a couple drones, realized that we will use Will's Contixo F18 GPS since has a greater lift capacity and can use GPS to stay in one position in the wind
* Took apart Contixo F18 GPS and figured out that we can drill into the top part of the drone and attach components with bolts
* We will use a template to measure where to drill the holes

### Week of 11.21.22
* Short week, but we got the template plate for making holes in the drone to bolt the wind sensor and other components to
* Drilled the holes and put bolts through the top plate of the drone

### Week of 11.28.22
* Laser cut acrylic plate to find tolerance for holes for leg mounts - will be used in future to make legs
<img src="Media/LegPlate.jpg" width="300px" height="400" />  <br/>
* Tested how accurately we can land the drone, found that we can consistently land within an 18" square
* Thought through how our docking will work, we will now prototype a system where the drone will have four legs which will be guided into place by four funnels, alligning the drone

### Week of 12.5.22
* Printed out drone legs and attached them: <br/>
<img src="Media/droneleg1.jpg" width="300px" height="400"/> <img src="Media/droneleg2.jpg" width="300px" height="400" /> <br/>
* Ran into some clearence issues so had to dremel out a small portion of the legs. 
* Drone flew well and legs seemed to add negligible weight.
* Wrote test code to read wind speed and tempereature from wind sensor, altitude and tempereature from barometric pressure sensor
* Figured out how to record data on the Pico, it requires changing the read/write status of the Pico meaning the computer can no longer write and can only read
   
### Week of 12.12.22
* Created new legs that work well with the drone and will allow for access to charging in the future
<br/> <img src="Media/legsV2.png" width="100px" height="300"/> <br/>
* Developed funnel for legs to slot into.
<br/> <img src="Media/FunnelV1.png" width="300px" height="200" /> <br/>
* Printed one leg and funnel and succesfully tested landing in it
<br/> <img src="Media/PrintedLegAndCone.jpg" width="267" height="200" /> <br/>
* Moved towards finalizing Pico code, we can now save the wind speed, temperature, and altitude to a file; this took a lot of troubleshooting to get the file to save properly

### Week of 1.2.23
* Attached new legs to the drone and attached funnels to a large plate.
* Succesfully tested landing in the funnels
* Finalized a first version of code which can record wind speed, temperature, and altitude
* Started planning the design of the box which will house our drone
<br/> <img src="Media/Boxplan.png" width="600" height="200" /> <br/>


### Week of 1.9.23
* Determined height needed for the mast for the drone
* Created temporary stand in Onshape for holding up the wind sensor above the drone
* Re-learned how to mill out a circuit board
* Finished designing PCB in Fritzing and prepared G-Code to mill it
<br/> <img src="Media/PCBDesign.PNG" width="379" height="300" /> <br/>
* G-Code part names and uses
   * T501 - "Contour", V bit for engraving PCB
   * T112 - "Hatches", "cut", milling out all extra copper and profile
   * T609 - "Drill", Drills out the through holes

### Week of 1.16.23
* Worked on presentation describing the current state of our project and our progress during the second quarter

### Week of 1.23.23
* Tried to mill our PCB, but ran into issues with the G-Code created by Carbide Copper having extra tool changes that caused the bit to stop spinning and break, issues with zeroing the z-axis and with the consistency of the width of the copper layer
* Finished milling the PCB and sanded copper off the back of the plate
* <br/> <img src="Media/PCB.png" width="300" height="400"/> <br/>
* Printed out the stand for the wind sensor that we will bolt to the top of the drone
* <br/> <img src="Media/circledHolder.png" width="400" height="300"/> <br/>


### Week of 1.30.23
* Sanded down the dowel to fit into the drone sensor holder
* Created the onshape model for the clamp to wrap around the drone 
<br/> <img src="Media/sensorClamp.png" /> <br/>

### Week of 2.6.2023
* Test flew the drone with the pillar of sensor on top, had some wobble because it was not screwed together all the way
* Screwed drone and added tape to reduce vibrations and wibble wobble during flight
* Designed the PCB bracket in Onshape and laser cut the bracket piece

### Week of 2.13.2023
* Test flew drone with pillar for the sensor on top AND the PCB and 9v battery on the bottom.
* First flight with the sensor at the top of the mast was very unstable and we momentarily lost control of the drone, which may or not be related to the instability
* Realized that our tests with the sensor at different heights was useless since the PCB trace connecting the wind sensor to power cracked
* Soldered together the two sides of the cracked wire on the PCB
* Did some much needed cleaning to prepare for the next stage of our project, designing the drone housing box

### Week of 2.20.2023  
* Test flew drone again in order to get proper wind detection data
* Realized that the altitude sensor readings were too slow, causing not enough data to be collected
* Edited barometric pressure altitude sensor library to take more readings per second
* Test felw again, but the code had an error midway through the flight
* Code issue was that with the new sensor reading speed, the list it was saving data to became too large, causing an error
* Changed code to save readings to a file mid-flight when the list gets close to the maximum size

### Week of 3.27.2023
* Tested gathering data with the wind sensor at different distances from the propellers; it is ideal to put it as close as possibile while still taking accurate wind readings so the housing box can be as small as possible and to increase stability
* Graphed the wind speed reading and altitude at each sensor position to see if the propeller spinning affected the wind speed reading
<br/> <img src="Media/WindSpeedAltitudeChartLow.png" width="400" height="200"/>       <img src="Media/WindSpeedAltitudeChartMiddle.png" width="400" height="200"/><img src="Media/WindSpeedAltitudeChartHigh.png" width="400" height="200"/>
* Found that the wind created by the drone moving does affect the readings, but when it is flying in a stable position it doesn't, so the lowest position works for our purposes: gathering data while flying at a stable altitude
* Brainstormed different options for box design and getting the landing platform far enough from the walls of the box

### Week of 3.6.23
* Decided to use a canopy to fold out and cover the drone after it lands, which will mean that the drone won't have to be raised or lowered to provide clearance for landing
* Designed, 3d printed, and assembled a scale prototype for the canopy
* Attached plastic between the ribs of the canopy to waterproof, in the full size version we will material from a tarp
* For the final version we will have to divide each rib into multiple segments to fit in the 3d printer
<br/> <img src="Media/ScaleRibs.PNG" width="306" height="200"/> <img src="Media/ScaleRibVideo.gif" width="355" height="200"/>

### Week of 3.13.23
* Began designing full scale version of the canopy, taking into account the constraints of minimum and maximum dimensions in different directions based on the drone's landing platform
* Each rib will have to be divided into eight parts to fit on the print bed, although several of the parts will be duplicates, which will make designing it more efficient
* Printed smaller pieces to test the fit of the connector between each segment of the ribs
* Printed and assembled one full rib, which had a couple design flaws: not all of the holes being countersunk and forgetting to add holes to attach the canopy to, but is otherwise functional

### Week of 3.20.23
* Attached the plastic tarp to the rib that we printed using bolts and washers
* Continued designing the other sets of ribs
* Tested the dimensions of the end of the motor to create an adapter to connect it to the axle
* Changed the dimensions of all the rings to make the ring that we already printed the second largest rather than the largest, which gives us more space for the tarp to be when the canopy is closed

### Week of 3.27.23
* Planned for CERN, was a short week. Was extremely hectic planning for Europe

### Week of 4.10.23
* jet lag is not friendly
* Changed diameter of axel hole in rib to reduce friction
* Started printing our ribs, printed first (and largest) rib on 4.13
* Will see if there is anything to alter after print. Hopefully will have full carriage manufactured by end of April.

### Week of 4.17.23
* Alden got surgery so productivity plummeted by roughly 70%
* Printed out all common parts and the third rib on 4.20 (Nice)
* Put plastic on the largest rib to try to construct half of the carriage but decided to wait on fully assembling the carriage until alden gets back.

