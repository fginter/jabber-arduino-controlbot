import serial
import serial.tools.list_ports
import traceback

class SerialComm:

    def __init__(self):
        self.port=None
        self.openPort() #Auto-detects the serial port on which the arduino responds and opens it into self.port

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
        #if I made it to here, I have my port, handshake
        self.port=p
        self.port.timeout=None
        self.send("howdy;")
        while True:
            msg=self.waitForReply()
            if "webcambot ready" in msg:
                print "Handshake success. Using:",self.port.portstr
                break

    def send(self,msg):
        self.port.write(msg)
        self.port.flush() #Wait till everything is written

    def waitForReply(self):
        msg=[]
        while True:
            b=self.port.read()
            msg.append(b)
            if b==";":
                break
        return ("".join(msg)).strip()

    def sendAndWaitForReply(self,msg):
        self.send(msg)
        #Now read the answer
        l=self.waitForReply()
        if "OK" in l:
            return "OK"
        else:
            return "Failure: >>>"+l+"<<<"

if __name__=="__main__":
    s=SerialComm()
    s.open()
    print >> s.port, "h +360;h -360;"
