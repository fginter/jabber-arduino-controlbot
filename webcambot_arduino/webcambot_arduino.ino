#include "step_motor.h"


StepMotor stepper(64, 10, 11, 12, 13);

void setup() {
   stepper.setSpeed(30);
}

void loop() {
  stepper.turn(30);
}

