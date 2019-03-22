import socket;
from time import sleep;
from A3MotionSimulator.SimphynityPacket import *;

# ip / ports
UDP_IP = "127.0.0.1";
UDP_PORT = 20777;

# send rates
TICK_SEND_RATE   = 1.0 / 20.0;
TICK_SAMPLE_RATE = 1.0 / 5.0;

# time
time = 0;

# socket
sock = None;

# The packet
packet = SimphynityPacket();


def init():

    global sock;

    # open up the udp socket (datagram)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);

    # get the bytes to send
    data = packet.get_bytes();

    # send an initial packet
    sock.sendto(data, (UDP_IP, UDP_PORT));


def set_rate_per_second(rate):
    global TICK_SEND_RATE;
    TICK_SEND_RATE = 1.0 / rate;



def send_data():

    # make sock global
    global sock;

    # sock is closed? return
    if sock == None:
        return;

     # get the bytes to send
    data = packet.get_bytes();

    # send the data
    sock.sendto(data, (UDP_IP, UDP_PORT));



def set_zeros():

    # make packet global
    global packet;

    # set all variables to defaults
    packet.rotationMatrix = mat3(1);
    packet.localAccel = vec3(0, 0, 0);
    packet.localVel = vec3(0, 0, 0);
    packet.globalVel = vec3(0, 0, 0);

def accel(x, y, z):
    global packet;
    packet.localAccel.x = x;
    packet.localAccel.y = y;
    packet.localAccel.z = z;
    

def close():

    # set sock to global
    global sock;
    
    # and close it, set to None
    sock.close();
    sock = None;



def update():

    global TICK_SEND_RATE, time, sock, packet;

    while (sock != None):
        
        sleep(TICK_SEND_RATE);
        time += TICK_SEND_RATE;
        packet.packetTimeMillis = int(time * 1000);

        yield time;

        send_data();

        
