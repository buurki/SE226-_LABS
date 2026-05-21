#include <LiquidCrystal.h>

LiquidCrystal lcd(36, 37, 26, 27, 28, 29);

int A = 22;
int B = 28;
int C = 27;
int D = 26;
int E = 25;
int F = 24;
int G = 23;
int DP = 22;

int gnd1 = 33;
int gnd2 = 34;
int gnd3 = 35;
int gnd4 = 36;

int dig1 = 0;
int dig2 = 0;
int dig3 = 0;
int dig4 = 0;

unsigned long previousTime = 0;
const unsigned long interval = 1000;

void clearSegments() {
  digitalWrite(A, LOW);
  digitalWrite(B, LOW);
  digitalWrite(C, LOW);
  digitalWrite(D, LOW);
  digitalWrite(E, LOW);
  digitalWrite(F, LOW);
  digitalWrite(G, LOW);
  digitalWrite(DP, LOW);
}

void turnOffDigits() {
  digitalWrite(gnd1, LOW);
  digitalWrite(gnd2, LOW);
  digitalWrite(gnd3, LOW);
  digitalWrite(gnd4, LOW);
}

void zero() {
  digitalWrite(A, LOW);
  digitalWrite(B, LOW);
  digitalWrite(C, HIGH);
  digitalWrite(D, HIGH);
  digitalWrite(E, HIGH);
  digitalWrite(F, HIGH);
  digitalWrite(G, HIGH);
  digitalWrite(DP, HIGH);
}

void one() {
  digitalWrite(A, LOW);
  digitalWrite(B, LOW);
  digitalWrite(C, LOW);
  digitalWrite(D, LOW);
  digitalWrite(E, LOW);
  digitalWrite(F, HIGH);
  digitalWrite(G, HIGH);
  digitalWrite(DP, LOW);
}

void two() {
  digitalWrite(A, LOW);
  digitalWrite(B, HIGH);
  digitalWrite(C, LOW);
  digitalWrite(D, HIGH);
  digitalWrite(E, HIGH);
  digitalWrite(F, LOW);
  digitalWrite(G, HIGH);
  digitalWrite(DP, HIGH);
}

void three() {
  digitalWrite(A, LOW);
  digitalWrite(B, HIGH);
  digitalWrite(C, LOW);
  digitalWrite(D, LOW);
  digitalWrite(E, HIGH);
  digitalWrite(F, HIGH);
  digitalWrite(G, HIGH);
  digitalWrite(DP, HIGH);
}

void four() {
  digitalWrite(A, LOW);
  digitalWrite(B, HIGH);
  digitalWrite(C, HIGH);
  digitalWrite(D, LOW);
  digitalWrite(E, LOW);
  digitalWrite(F, HIGH);
  digitalWrite(G, HIGH);
  digitalWrite(DP, LOW);
}

void five() {
  digitalWrite(A, LOW);
  digitalWrite(B, HIGH);
  digitalWrite(C, HIGH);
  digitalWrite(D, LOW);
  digitalWrite(E, HIGH);
  digitalWrite(F, HIGH);
  digitalWrite(G, LOW);
  digitalWrite(DP, HIGH);
}

void six() {
  digitalWrite(A, LOW);
  digitalWrite(B, HIGH);
  digitalWrite(C, HIGH);
  digitalWrite(D, HIGH);
  digitalWrite(E, HIGH);
  digitalWrite(F, HIGH);
  digitalWrite(G, LOW);
  digitalWrite(DP, HIGH);
}

void seven() {
  digitalWrite(A, LOW);
  digitalWrite(B, LOW);
  digitalWrite(C, LOW);
  digitalWrite(D, LOW);
  digitalWrite(E, LOW);
  digitalWrite(F, HIGH);
  digitalWrite(G, HIGH);
  digitalWrite(DP, HIGH);
}

void eight() {
  digitalWrite(A, LOW);
  digitalWrite(B, HIGH);
  digitalWrite(C, HIGH);
  digitalWrite(D, HIGH);
  digitalWrite(E, HIGH);
  digitalWrite(F, HIGH);
  digitalWrite(G, HIGH);
  digitalWrite(DP, HIGH);
}

void nine() {
  digitalWrite(A, LOW);
  digitalWrite(B, HIGH);
  digitalWrite(C, HIGH);
  digitalWrite(D, LOW);
  digitalWrite(E, HIGH);
  digitalWrite(F, HIGH);
  digitalWrite(G, HIGH);
  digitalWrite(DP, HIGH);
}

void showNumber(int num) {
  clearSegments();

  if (num == 0) zero();
  else if (num == 1) one();
  else if (num == 2) two();
  else if (num == 3) three();
  else if (num == 4) four();
  else if (num == 5) five();
  else if (num == 6) six();
  else if (num == 7) seven();
  else if (num == 8) eight();
  else if (num == 9) nine();
}

void displayDigit(int digitPin, int number) {
  turnOffDigits();

  showNumber(number);

  digitalWrite(digitPin, HIGH);
  delay(4);
  digitalWrite(digitPin, LOW);
}

void displayCounter() {
  displayDigit(gnd1, dig1);
  displayDigit(gnd2, dig2);
  displayDigit(gnd3, dig3);
  displayDigit(gnd4, dig4);
}

void incrementCounter() {
  dig1++;

  if (dig1 >= 10) {
    dig1 = 0;
    dig2++;
  }

  if (dig2 >= 10) {
    dig2 = 0;
    dig3++;
  }

  if (dig3 >= 10) {
    dig3 = 0;
    dig4++;
  }

  if (dig4 >= 10) {
    dig4 = 0;
  }
}

void updateLCD() {
  lcd.setCursor(0, 0);
  lcd.print("Counter: ");

  lcd.print(dig4);
  lcd.print(dig3);
  lcd.print(dig2);
  lcd.print(dig1);

  lcd.print("   ");
}

void setup() {
  pinMode(A, OUTPUT);
  pinMode(B, OUTPUT);
  pinMode(C, OUTPUT);
  pinMode(D, OUTPUT);
  pinMode(E, OUTPUT);
  pinMode(F, OUTPUT);
  pinMode(G, OUTPUT);
  pinMode(DP, OUTPUT);

  pinMode(gnd1, OUTPUT);
  pinMode(gnd2, OUTPUT);
  pinMode(gnd3, OUTPUT);
  pinMode(gnd4, OUTPUT);

  clearSegments();
  turnOffDigits();

  lcd.begin(16, 2);
  lcd.setCursor(0, 0);
  lcd.print("Counter: 0000");
}

void loop() {
  displayCounter();

  if (millis() - previousTime >= interval) {
    previousTime = millis();

    incrementCounter();
    updateLCD();
  }
}
