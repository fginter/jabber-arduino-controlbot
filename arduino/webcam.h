#ifndef _webcam_h_
#define _webcam_h_

#include "step_motor.h"

//Maximal length of single command
#define BUFFLEN 25

#define WCAM_ERR_OK 0
#define WCAM_ERR_CMD_UNKNOWN 2
#define WCAM_ERR_CMD_MALFORMED 3

class Webcam {
  public:
    StepMotor *hMotor;
    StepMotor *vMotor;
    Webcam(StepMotor *hMotor, StepMotor *vMotor);
    void serve();
    int react(char *cmd);
  
};

#endif
