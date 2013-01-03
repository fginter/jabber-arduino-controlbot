#include "step_motor.h"


StepMotor stepper(64*8, 10, 11, 12, 13);

void setup() {
   stepper.setSpeed(15L);
}

void loop() {
  long degs=360L;
  while (true) {
    stepper.turnDegrees(degs);
    degs*=-1;
    delay(500);
  }
  //stepper.turn(-3000000);
}

