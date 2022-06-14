#include <SPI.h>
#include <PN532_SPI.h>
#include <PN532Interface.h>
#include <Adafruit_PN532.h>
#include <PN532.h>


#include <Wire.h>
#define NUMFLAKES 10
#define XPOS 0
#define YPOS 1
#define DELTAY 2

#define PN532_SCK  (13)
#define PN532_MOSI (12)
#define PN532_SS   (10)
#define PN532_MISO (11)

String text;

#define LOGO16_GLCD_HEIGHT 16 
#define LOGO16_GLCD_WIDTH  16 
static const unsigned char PROGMEM logo16_glcd_bmp[] =
{ B00000000, B11000000,
  B00000001, B11000000,
  B00000001, B11000000,
  B00000011, B11100000,
  B11110011, B11100000,
  B11111110, B11111000,
  B01111110, B11111111,
  B00110011, B10011111,
  B00011111, B11111100,
  B00001101, B01110000,
  B00011011, B10100000,
  B00111111, B11100000,
  B00111111, B11110000,
  B01111100, B11110000,
  B01110000, B01110000,
  B00000000, B00110000 };
  
Adafruit_PN532 nfc(PN532_SCK, PN532_MISO, PN532_MOSI, PN532_SS);


void setup()
{    
    Serial.begin(115200);
   
    Serial.println(F("This is the Hardware demonstration for Final Year Project"));
    delay(500);
   
    nfc.begin();
    
    uint32_t versiondata = nfc.getFirmwareVersion();
    if (! versiondata) {
      Serial.print(F("Didn't find PN53x board"));
      while (1); // halt

    }
    
    // Got ok data, print it out!
    //Serial.print(F("Connection to Arduino to PN532 Found!!!")); 
    //Serial.println((versiondata>>24) & 0xFF, HEX); 
    //Serial.print(F("Firmware ver. ")); 
    //Serial.print((versiondata>>16) & 0xFF, DEC); 
    //Serial.print(F("."));
    //Serial.println((versiondata>>8) & 0xFF, DEC);
    
    // Set the max number of retry attempts to read from a card
    // This prevents us from waiting forever for a card, which is
    // the default behaviour of the PN532.
    //nfc.setPassiveActivationRetries(0xFF);
    
    // configure board to read RFID tags
    nfc.SAMConfig();
}

void loop()
{
  bool success;
  
  uint8_t responseLength = 32;
  
  //Serial.println("Waiting for an ISO14443A card");
  // set shield to inListPassiveTarget
  success = nfc.inListPassiveTarget();

  if(success) {
   
     //Serial.println("Found something!");
                  
    uint8_t selectApdu[] = { 0x00, /* CLA */
                              0xA4, /* INS */
                              0x04, /* P1  */
                              0x00, /* P2  */
                              0x07, /* Length of AID  */
                              0xF0, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, /* AID defined on Android App */
                              0x00  /* Le  */ };
                              
    uint8_t response[32];  
     
    success = nfc.inDataExchange(selectApdu, sizeof(selectApdu), response, &responseLength);
    
    if(success) {
        
      //Serial.print("responseLength: "); 
      //Serial.println(responseLength);
       
      //nfc.PrintHexChar(response, responseLength);
      PHC(response,responseLength);
      
    }
    else {
     
      //Serial.println("Failed sending SELECT AID"); 
    }
  }
  else {
   
    Serial.println("Didn't find anything!");

    delay(1000);
 
  }

  delay(1000);
}

void printResponse(uint8_t *response, uint8_t responseLength) {
  
   String respBuffer;

    for (int i = 0; i < responseLength; i++) {
      
      if (response[i] < 0x10) 
        respBuffer = respBuffer + "0"; //Adds leading zeros if hex value is smaller than 0x10
      
      respBuffer = respBuffer + String(response[i], HEX) + " ";                        
    }

    //Serial.print("response: "); 
    //Serial.println(respBuffer);
}

void setupNFC() {
 
  nfc.begin();
    
  uint32_t versiondata = nfc.getFirmwareVersion();
  if (! versiondata) {
    //Serial.print("Didn't find PN53x board");
    while (1); // halt
  }
  
  // Got ok data, print it out!
  //Serial.print("Found chip PN5"); Serial.println((versiondata>>24) & 0xFF, HEX); 
  //Serial.print("Firmware ver. "); Serial.print((versiondata>>16) & 0xFF, DEC); 
  //Serial.print('.'); Serial.println((versiondata>>8) & 0xFF, DEC);
  
  // configure board to read RFID tags
  nfc.SAMConfig(); 
}
void PHC(const byte * data, const long numBytes)
{
  char rxkey[8];
  char key1[4]={'1','2','3','4'};
  char key2[4]={'9','2','3','4'};
  
  uint8_t j=0;
  uint8_t k=0;
  
  for(int i=0;i< 8; i++)
  {
    rxkey[i] = (char)data[i];
    
   }
   for(int i=0; i<8; i++){
    Serial.print(rxkey[i]);
   }
   Serial.println("");
    if(numBytes < 8)
    {
      for(int i=0;i<8;i++)
      { 
        if(key1[i]==rxkey[i])
        j++;
       }
       for(int i=0;i<8;i++)
      { 
        if(key2[i]==rxkey[i])
        k++;
       }
      
       if(j == 7 || k==7)
       {
        //Serial.println("");
        //Serial.println(F("---------Access Granted---------"));
             
       }  
       
       else{
        //Serial.println("");
        //Serial.println(F("---------Access Denied---------"));
        
       }
     }
}
