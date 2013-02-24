#include "step_motor.h"
#include "webcam.h"

StepMotor stepperV(64*8, 13, 12, 11, 10);
StepMotor stepperH(64*8, 9, 8, 7, 6);
Webcam wCam(&stepperH,&stepperV);

void handshake() {
  char message[60];
  int readLen=0;
  while (true) {
    Serial.println("webcambot waiting;");
    readLen=Serial.readBytesUntil(';',message,59);
    if (readLen > 0) {
      message[readLen]='\0';
      if (!strcmp(message,"howdy")) {
        Serial.println("webcambot ready;");
        break;
      }
    }
  }
}
    

void setup() {
  Serial.begin(9600);
  stepperH.setSpeed(3L);
  stepperV.setSpeed(3L);
  handshake();
}

void loop() {
  wCam.serve();
}

/*
void loop() {
  long degs=360L;
  while (true) {
    stepper.turnDegrees(degs);
    degs*=-1;
    delay(500);
  }
  //stepper.turn(-3000000);
}
*/

