import appdirs
import os.path, os
import sys
import codecs

class CfgFile:

    def __init__(self,fileName):
        self.kvDict={} #key:value pairs from the file
        self.dir=appdirs.user_data_dir("webcambot", appauthor="FiGint", version="0.X", roaming=False)
        self.fileName=os.path.join(self.dir,fileName)
        if not os.path.exists(self.dir):
            os.makedirs(self.dir)
            print >> sys.stderr, "Initializing path:",self.dir
        if not os.path.exists(self.fileName):
            print >> sys.stderr, "Initializing config file:",self.fileName
            f=open(self.fileName,"w")
            f.close()
        self.read()
    
    def get(self,key):
        return self.kvDict.get(key)

    def set(self,key,value):
        self.kvDict[key]=value

    def write(self):
        if not self.fileName:
            raise ValueError("FileName cannot be empty")
        f=codecs.open(self.fileName,"w","utf-8")
        for k in sorted(self.kvDict):
            print >> f, k,"=",self.kvDict[k]
        f.close()
    
    def read(self):
        f=codecs.open(self.fileName,"r","utf-8")
        for line in f:
            line=line.strip()
            if not line or line.startswith(u"#"):
                pass
            try:
                k,v=line.split(u"=",1)
                k=k.strip()
                v=v.strip()
                self.kvDict[k]=v
            except:
                pass
        f.close()

config=CfgFile("webcambot_cfg.txt")
