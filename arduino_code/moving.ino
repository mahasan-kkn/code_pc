int ledPin = 4;
int digitalPin = 5;
int val = 0;
void setup() {
pinMode(ledPin, OUTPUT); // sets the pin as output
pinMode(digitalPin, INPUT); // sets the pin as input
Serial.begin(9600);

}

void loop() {
val = digitalRead(digitalPin); 
Serial.print("val = "); 
Serial.println(val);
if (val == 0) { // 
digitalWrite(ledPin, HIGH);
}
else {
digitalWrite(ledPin, LOW); 
}
delay(1000);

}
