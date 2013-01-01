#include <Stepper.h>

#define STEPS 100

Stepper stepper(STEPS, 10, 11, 12, 13);

void setup() {
   stepper.setSpeed(30);
}

void loop() {
  stepper.step(30);
}

