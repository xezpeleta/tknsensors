#include <OneWire.h>
#include <DallasTemperature.h>


#define ONE_WIRE_BUS 3
#define AC_POWER 4
#define AC_FILTER 5

OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature tempsensors(&oneWire);

int startbyte = 0;
int sensor = 0;

void setup(void)
{
  Serial.begin(9600);
  // Switch on LED
  digitalWrite(13, HIGH);

  tempsensors.begin();
  pinMode(AC_POWER, INPUT);
  pinMode(AC_FILTER, INPUT);
}

//
// Debug-erako dago konfiguratua: bukatzean KENDU startbyte == 32, case 49, case 50, case 51...
//

void loop(void)
{
  if (Serial.available() > 1) {
    startbyte = Serial.read();
    //if (startbyte == 32 || startbyte == 255) {
    if (startbyte == 255) {
      sensor = Serial.read();
      
      switch (int(char(sensor))) {
        //case 49:
        case 1:
          // Get temperature
          tempsensors.requestTemperatures(); // Send the command to get temperatures
          Serial.println(tempsensors.getTempCByIndex(0));
          break;
        //case 50:
        case 2:
          // Get AC-power status
          if (digitalRead(AC_POWER) == LOW) {
            //Serial.println("AC-Power status: OFF");
            Serial.println("1");
            // Led blinking? Sound?
          } else if (digitalRead(AC_POWER) == HIGH) {
            //Serial.println("AC-Power status: ON");
            Serial.println("0");
          }
          break;
        //case 51:
        case 3:
          // Get AC-filter status
          if (digitalRead(AC_FILTER) == LOW) {
            //Serial.println("AC-Filter status: BROKEN");
            Serial.println("1");
            // Led blinking? Sound?
          } else if (digitalRead(AC_FILTER) == HIGH) {
            //Serial.println("AC-Filter status: OK");
            Serial.println("0");
          }
          break;
      }
    }
  }
  
}
