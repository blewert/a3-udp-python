import struct
from functools import reduce

class vec3:

    def __init__(self, x, y, z):
        self.x = x;
        self.y = y;
        self.z = z;

    def bytes(self):
        return [self.x, self.y, self.z];

    def __str__(self):
        return "(%f, %f, %f)" % (self.x, self.y, self.z);

class mat3:

    def __init__(self, value):
        
        self.rows = [
            [ value, 0, 0 ],
            [ 0, value, 0 ],
            [ 0, 0, value ]
        ];

    def __str__(self):
        return "%s;%s;%s" % (self.rows[0], self.rows[1], self.rows[2]);
    
    def bytes(self):
        return reduce(lambda x, y: x + y, self.rows);

#bool useLocalVals; 			// 4 byte bool value.  First byte = val, followed by 3 padding bytes. 
#float localAccel[3];			// 12 byte (3 x 4 byte) float vector.
#float localVel[3];			    // 12 byte (3 x 4 byte) float vector.
#float globalVel[3];			// 12 byte (3 x 4 byte) float vector.
#float rotationMatrix[3][3];	// 36 byte (9 x 4 byte) float matrix.
#DWORD packetTimeMillis;		// 4 byte integer value.

class SimphynityPacket:

    def __init__(self):
        self.useLocalVals = True;
        self.localAccel = vec3(0, 0, 0);
        self.localVel = vec3(0, 0, 0);
        self.globalVel = vec3(0, 0, 0);
        self.rotationMatrix = mat3(1);
        self.packetTimeMillis = 255;

    def get_bytes(self):

        data = [    self.useLocalVals, 
                    *self.localAccel.bytes(),
                    *self.localVel.bytes(),
                    *self.globalVel.bytes(),
                    *self.rotationMatrix.bytes(),
                    self.packetTimeMillis   ];

        return struct.pack("i 3f 3f 3f 9f i", *data);