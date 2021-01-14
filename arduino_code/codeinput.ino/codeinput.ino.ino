#include <myInput.h>

const unsigned char Mode = 14;
unsigned char Up = 27;
unsigned char Down = 26;

void setup() {
  Serial.begin(9600);
  pinMode(Mode,INPUT);
  pinMode(Up,INPUT);
  pinMode(Down,INPUT);
  
}
void loop() {
  int val1 = digitalRead(Mode);
  int val2 = digitalRead(Up);
  int val3 = digitalRead(Down);
  Serial.print("SW1 = ");
  Serial.print(val1);
  Serial.print("\t");

  Serial.print("SW2 = ");
  Serial.print(val2);
  Serial.print("\t");

  Serial.print("SW3 = ");
  Serial.print(val3);
  Serial.print("\t");
  delay(100);
  
}
