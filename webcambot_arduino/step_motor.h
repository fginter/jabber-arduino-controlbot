#ifndef _step_motor_h_
#define _step_motor_h_

class StepMotor {
  public:
    int gearRatio, i1, i2, i3, i4;
    unsigned long stepDelay; //Delay in microseconds between steps, for the given speed (as set by setSpeed())
    int phase; //0-7: phase in the cycle of the motor
    StepMotor(int gearRatio, int i1, int i2, int i3, int i4);
    void setSpeed(int speed);
    void turn(long step);
    void turnDegrees(long degrees);
    void deenergize(); //all coils off
    void energize(); //energize coils according to phase
    void singleStep(bool fwd);
};

#endif
