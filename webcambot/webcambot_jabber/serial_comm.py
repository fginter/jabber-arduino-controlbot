import serial
import serial.tools.list_ports
import traceback

class SerialComm:

    def __init__(self):
        self.port=None
        self.open() #Auto-detects the serial port on which the arduino responds and opens it into self.port

    def openPort(self):
        for path,comment,HWID in serial.tools.list_ports.comports():
            try:
                p=serial.Serial(path,9600,timeout=3)
                #Got an open port, listen
                print "Trying", path
                l=p.readline()
                if "webcambot waiting" in l:
                    #FOUND!
                    break
            except serial.SerialException:
                pass
        else:
            raise RuntimeError("No port found, bailing out.")
        #if I made it to here, I have my port
        print >> p, "howdy;",
        p.flush()
        l=p.readline()
        if "webcambot ready" in l:
            p.flushInput()
            p.flushOutput()
            return p
        else:
            raise RuntimeError("Handshake failed")
    
    def open(self):
        self.port=self.openPort()
        print "Handshake successful. Using:",self.port.portstr

    def sendMsg(self,msg):
        print "comm:",msg+";"
        self.port.write(msg)
        self.port.timeout=10
        l=self.port.readline()
        self.port.flushInput()
        self.port.flushOutput()
        if "OK" in l:
            return "OK"
        else:
            return "Failure: >>>"+l+"<<<"

if __name__=="__main__":
    s=SerialComm()
    s.open()
    print >> s.port, "h +360;h -360;"
