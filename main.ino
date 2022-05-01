int buttonVal = 0;
int bounceWait = 10;
int buttonPin1 = 2;
int buttonPin2 = 3;
int buttonPin3 = 10;
int buttonPin4 = 8;
int shakePin1 = 6;
int shakePin2 = 12;

String pinVal1;
String pinVal2;
String pinVal3;
String pinVal4;
String shakeVal1;
String shakeVal2;

int currentPotVal;
int newPotVal;

void setup() {


    pinMode(buttonPin1, INPUT_PULLUP);
    pinMode(buttonPin2, INPUT_PULLUP);
    pinMode(buttonPin3, INPUT_PULLUP);
    pinMode(buttonPin4, INPUT_PULLUP);
    pinMode(shakePin1, INPUT);
    pinMode(shakePin2, INPUT);
    Serial.begin(9600);
    
}

void loop() {


    pinVal1 = String(digitalRead(buttonPin1));
    pinVal2 = String(digitalRead(buttonPin2));
    pinVal3 = String(digitalRead(buttonPin3));
    pinVal4 = String(digitalRead(buttonPin4));
    shakeVal1 = String(digitalRead(shakePin1));
    shakeVal2 = String(digitalRead(shakePin2));


    Serial.println(pinVal1 + pinVal2 + pinVal3 + pinVal4 + shakeVal1 + shakeVal2);
    


}