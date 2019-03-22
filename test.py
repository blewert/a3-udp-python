import A3MotionSimulator.MotionSimulator as sim
from math import sin

# initialise the simulator
sim.init();

# set the send rate to 20 packets a second
sim.set_rate_per_second(20);

for time in sim.update():
    
    # calculate the amount of rotation on the y-axis
    v = sin(time * 10);

    # print the acceleration values
    print(sim.packet.localAccel);

    # if the time is less than 5 seconds.. change the acceleration value
    if time < 5.0:
        sim.accel(0, v, 0);

    # otherwise close the simulation
    else:
        sim.close();


