#include <Arduino.h>
#include "step_motor.h"

StepMotor::StepMotor(int gearRatio, int i1, int i2, int i3, int i4) {
  this->gearRatio=gearRatio;
  this->i1=i1;
  this->i2=i2;
  this->i3=i3;
  this->i4=i4;
  deenergize();
};

void StepMotor::setSpeed(int speed) {
};

//it takes 8 * gearRatio steps for a full revolution of the output shaft
void StepMotor::turn(int steps) {
  bool fwd=true;
  if (steps<0) {
      fwd=false;
      steps*=-1;
  }
  while (steps>0) {
    singleStep(fwd);
    steps--;
    delay(5);
  }
  deenergize();
};

void StepMotor::deenergize() {
  digitalWrite(i1, LOW);  
  digitalWrite(i2, LOW); 
  digitalWrite(i3, LOW); 
  digitalWrite(i4, LOW); 
};

void StepMotor::singleStep(bool fwd) {
  if (fwd) {
    phase++;
    if (phase==8) {
      phase=0;
    }
  }
  else {
    phase--;
    if (phase==-1) {
      phase=7;
    }
  }
  energize();
}

void StepMotor::energize() {
   switch(phase){ 
   case 0: 
     digitalWrite(i1, LOW);  
     digitalWrite(i2, LOW); 
     digitalWrite(i3, LOW); 
     digitalWrite(i4, HIGH); 
     break;  
   case 1: 
     digitalWrite(i1, LOW);  
     digitalWrite(i2, LOW); 
     digitalWrite(i3, HIGH); 
     digitalWrite(i4, HIGH); 
     break;  
   case 2: 
     digitalWrite(i1, LOW);  
     digitalWrite(i2, LOW); 
     digitalWrite(i3, HIGH); 
     digitalWrite(i4, LOW); 
     break;  
   case 3: 
     digitalWrite(i1, LOW);  
     digitalWrite(i2, HIGH); 
     digitalWrite(i3, HIGH); 
     digitalWrite(i4, LOW); 
     break;  
   case 4: 
     digitalWrite(i1, LOW);  
     digitalWrite(i2, HIGH); 
     digitalWrite(i3, LOW); 
     digitalWrite(i4, LOW); 
     break;  
   case 5: 
     digitalWrite(i1, HIGH);  
     digitalWrite(i2, HIGH); 
     digitalWrite(i3, LOW); 
     digitalWrite(i4, LOW); 
     break;  
   case 6: 
     digitalWrite(i1, HIGH);  
     digitalWrite(i2, LOW); 
     digitalWrite(i3, LOW); 
     digitalWrite(i4, LOW); 
     break;  
   case 7: 
     digitalWrite(i1, HIGH);  
     digitalWrite(i2, LOW); 
     digitalWrite(i3, LOW); 
     digitalWrite(i4, HIGH); 
     break;
   }
}
