#include <DHT.h>
#include <DHT_U.h>

#include "Arduino.h"

#define LED_PIN 10
#define DHT_PIN 22

DHT_Unified dht(DHT_PIN, DHT11);

void setup() {
  Serial.begin(9600);

  pinMode(LED_PIN, OUTPUT);

  dht.begin();

  sensor_t tempSensor;
  sensor_t humidSensor;

  dht.temperature().getSensor(&tempSensor);
  dht.humidity().getSensor(&humidSensor);

  digitalWrite(LED_PIN, LOW);
}

void loop() {
  char data[50];

  sensors_event_t humidEvent;
  dht.humidity().getEvent(&humidEvent);

  sensors_event_t tempEvent;
  dht.temperature().getEvent(&tempEvent);

  float humidity = humidEvent.relative_humidity;
  float temperature = tempEvent.temperature;

  Serial.println("h:" + String(humidity) + "|t:" + temperature);

  delay(100);
}
