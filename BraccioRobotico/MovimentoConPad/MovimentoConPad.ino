#include <Servo.h>
#define PIN_SERVO 9
int analog=0;
Servo servo;

void setup() {
  Serial.begin(9600);
  servo.attach(PIN_SERVO);
}

void loop() {
  char comando = Serial.read();
  if(comando == 'a'){  
    analog=180;
  }
  else if(comando == 'b'){
    analog=0;
  }
  servo.write(analog);
  Serial.println(analog);
}
