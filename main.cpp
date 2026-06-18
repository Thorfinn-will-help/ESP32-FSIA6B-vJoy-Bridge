#include <Arduino.h>
#include <IBusBM.h>

IBusBM ibus;

void setup()
{
    Serial.begin(115200);

    Serial2.begin(
        115200,
        SERIAL_8N1,
        16,
        -1
    );

    ibus.begin(Serial2);
}

void loop()
{
    Serial.print(ibus.readChannel(0));
    Serial.print(",");

    Serial.print(ibus.readChannel(1));
    Serial.print(",");

    Serial.print(ibus.readChannel(2));
    Serial.print(",");

    Serial.println(ibus.readChannel(3));

    delay(10);
}