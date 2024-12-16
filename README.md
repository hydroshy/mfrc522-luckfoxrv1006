# mfrc522-luckfoxrv1006
Python library for LuckFox Pico Pro/Max RV1006, based on MFRC522-python library of pimylifeup.

I have made some modifications to the library to enable it to run on the LuckFox Pico Pro/Max kit. Thanks to pimylifeup for providing a great library for the MFRC522 module.

## Notes:

* The library may depend on the `periphery` library for SPI and GPIO access.
* You need to enable the SPI pins on the development kit. If you don't know how, follow these steps.

~~~
# You need to have sudo privileges. Open the config I/O
sudo luckfox-config
~~~
Choose Advance Options -> SPI. Now Enable it. Set the speed for 1000000.

You should check SPI I/O is open once time again. If its have (*) that is opened.
## Pinout

|MFRC522| Board's Pin Number|Pin Function|
|:---|:---|:---|
|SDA|Pin 12| (SPI0\_CS0\_M0)|
|SCK|Pin 14| (SPI0\_CLK\_M0)|
|RST|Pin 17| (UART0\_RX\_M1\)(OPTIONAL)|
|MISO|Pin 16| (SPI0\_MISO\_M0)|
|MOSI|Pin 15| (SPI0\_MOSI\_M0)|
|GND|Pin 13| (GND)|
|3.3v|Pin 36| (3.3v)|

## Installation









