#include "step_motor.h"
#include "webcam.h"

StepMotor stepper(64*8, 10, 11, 12, 13);
Webcam wCam(&stepper);

void handshake() {
  char message[20];
  int readLen=0;
  while (true) {
    Serial.println("webcambot waiting;");
    readLen=Serial.readBytesUntil(';',message,19);
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
  stepper.setSpeed(15L);
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

