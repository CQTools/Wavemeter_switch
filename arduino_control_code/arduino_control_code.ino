
void setup() {
  // initialize serial communication:
  Serial.begin(115200);
   // initialize the LED pins:
      for (int thisPin = 5; thisPin < 8; thisPin++) {
        pinMode(thisPin, OUTPUT);
      }
}

void loop() {
  // read the sensor:
  if (Serial.available() > 0) {
    int inByte = Serial.read();
    // do something different depending on the character received.  
    // The switch statement expects single number values for each case;
    // in this exmaple, though, you're using single quotes to tell
    // the controller to get the ASCII value for the character.  For
    // example 'a' = 97, 'b' = 98, and so forth:

    switch (inByte) {
    case '1':    
      digitalWrite(5, LOW);
      digitalWrite(6, LOW);
      digitalWrite(7, LOW);
      break;
    case '2':  
      digitalWrite(5, HIGH);  
      digitalWrite(6, LOW);
      digitalWrite(7, LOW);
      break;
    case '3':    
      digitalWrite(5, LOW);
      digitalWrite(6, HIGH);
      digitalWrite(7, LOW);
      break;
    case '4':    
      digitalWrite(5, HIGH);
      digitalWrite(6, HIGH);
      digitalWrite(7, LOW);
      break;
    case '5':    
      digitalWrite(5, LOW);
      digitalWrite(6, LOW);
      digitalWrite(7, HIGH);
      break;
    case '6':    
      digitalWrite(5, HIGH);
      digitalWrite(6, LOW);
      digitalWrite(7, HIGH);
      break;
    case '7':    
      digitalWrite(5, LOW);
      digitalWrite(6, HIGH);
      digitalWrite(7, HIGH);
      break;
    case '8':    
      digitalWrite(5, HIGH);
      digitalWrite(6, HIGH);
      digitalWrite(7, HIGH);
      break;
    default:
      // turn all the LEDs off:
      for (int thisPin = 5; thisPin < 7; thisPin++) {
        digitalWrite(thisPin, LOW);
      }
    }
  }
}
