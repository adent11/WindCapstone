# WindCapstone
2022-2023 Capstone Engineering Project. 

## Table of Contents
* [Scheduled work](#documentation)
* [Code](#Code)



### Task:
Use cumulative knowledge to solve an important issue.


# Resources<ln>

* [Autonomous drone landing](https://www.suasnews.com/2018/09/mapturedrone-in-a-box-prototype-automated-take-off-and-landing-demonstration/)
* [Wind measuring Drone](optolution.com/en/news/single-view-en/optokopter/)

## Materials
* 

## Risk Mitigation
* The main source of risk for our project is drone flight, so we will use proper precautions and only fly in appropriate circumstances

# To-Do
* 

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


# Code

# Documentation

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
* Thought through how our docking will work, we will now prototype a system where each of the drone's rotors has a leg coming down from it which will each have a funnel that will allign it upon landing
