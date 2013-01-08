#include "webcam.h"
#include "step_motor.h"
#include <Arduino.h>

Webcam::Webcam(StepMotor *hMotor) {
  this->hMotor=hMotor;
}

int Webcam::react(char *message) {
  //message is eg "h +15"
  //Let's parse the message to see if there's anything in it for us
  int msgLen=strlen(message);
  if (msgLen<3 || message[1]!=' ') { //cannot be OK
    return WCAM_ERR_CMD_MALFORMED;
  }
  int angle=atoi(message+2); //skipping the command and the space
  if (angle==0 || angle<-360 || angle>+360) {
    return WCAM_ERR_CMD_MALFORMED;
  }
  //If I made it to here, I should have a reasonable command at my hands
  
  switch (message[0]) {
    case 'h':
      hMotor->turnDegrees(angle);
      break;
    case 'v':
      break;
    default:
      return WCAM_ERR_CMD_UNKNOWN;
  }
  return WCAM_ERR_OK;
}

void Webcam::serve() {
  char message[BUFFLEN+1];
  int bytesRead=0;
  int err;
  while (true) {
    if (Serial.available() > 0) {
      bytesRead=Serial.readBytesUntil(';',message,BUFFLEN);
      if (bytesRead > 0) {
        message[bytesRead]='\0';
        err=react(message);
        if (err==WCAM_ERR_OK) {
          Serial.println("OK;");
        }
        else if (err==WCAM_ERR_CMD_UNKNOWN) {
          Serial.println("ERR Unknown command;");
        }
        else if (err==WCAM_ERR_CMD_MALFORMED) {
          Serial.println("ERR Malformed command;");
        }
      }
    }
  }
}
