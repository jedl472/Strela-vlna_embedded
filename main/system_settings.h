//soubor pro definovani systemovych nastaveni

//-------------------------------- obecne ----------------------------------------
#define DEBUG_MODE 1 //zatim nic moc nedela, ale bude

#define DEVICE_ID 1

inline const char* wifi_ssid = "Acd";
inline const char* wifi_password = "Zabozrout123+";
inline String serverName = "http://192.168.180.52:80";

//--------------------------------- piny -----------------------------------------
#define display_clk 18   // Clock: RS   (označení pinů na samotné desce displeje)
#define display_data 23  // Data:  PW
#define display_cs 5     // CS:    E

#define TL0 27  //doprava
#define TL1 26  //doleva
#define TL2 14  //nahoru
#define TL3 33  //dolu
#define TL4 32  //enter
#define TL5 25  //esc

