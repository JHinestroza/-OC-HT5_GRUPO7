const int ledPin = 3;



void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  if (Serial.available()>0)
  {
    char data = Serial.read();
    Serial.println(data);
    if (data == '1'){
      digitalWrite(ledPin, HIGH);
    }
    else if (data == '0'){
      digitalWrite(ledPin, LOW);
    }
  }
}
