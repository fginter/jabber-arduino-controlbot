#include "step_motor.h"
#include "webcam.h"

StepMotor stepper(64*8, 10, 11, 12, 13);
Webcam wCam(&stepper);

void setup() {
  Serial.begin(9600);
  stepper.setSpeed(15L);
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

