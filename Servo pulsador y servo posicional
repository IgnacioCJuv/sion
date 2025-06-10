#include <Servo.h>

Servo servo1;  // Primer servo
Servo servo2;  // Segundo servo
const int LDR_PIN = A0;  // Pin del LDR
const int UMBRAL_LUZ = 7000;  // Ajusta según tu ambiente (mayor = más oscuro)

void setup() {
  servo1.attach(9);   // Servo 1 en pin 9
  servo2.attach(10);  // Servo 2 en pin 10
}

void loop() {
  int valorLDR = analogRead(LDR_PIN);  // Leer LDR (0-1023)

  if (valorLDR < UMBRAL_LUZ) {  // Si hay LUZ
    servo1.write(180);          // Gira hacia adelante (360°)
    servo2.writeMicroseconds(2000);
  } else {                      // Si está OSCURO
    servo1.write(0);            // Gira hacia atrás (0°)
    servo2.writeMicroseconds(1000);
  }
  delay(100);  // Pequeña pausa para estabilidad
}
