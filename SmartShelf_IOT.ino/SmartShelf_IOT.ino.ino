#include <SPI.h>
#include <MFRC522.h>           // 引用MFRC522程式庫
#include <SoftwareSerial.h>    // 引用软件（虚拟）串口库
#define RST_PIN      A0        // 设置读卡器重置引脚RST
#define SS_PIN       10        // 设置片选引脚SDA
#define BUZZER       7         // 设置蜂鸣器以及RGB指示灯引脚
#define RGB          6
 
MFRC522 mfrc522(SS_PIN, RST_PIN);  // 以已设置的引脚实例化MFRC522对象
MFRC522::MIFARE_Key key;           // 实例化密钥对象

SoftwareSerial BT(8, 9);  // 实例化软串口对象，接收脚为8，发送脚为9

//设置读/写的区段（1-15）（区段0为UID等信息,读/写的区块 （0-2）（区块3为密钥等信息）
byte name_sector=1;      // 描述区块放于区段1   
byte weight_sector=15;   // 重量数据存放于区段15
byte block=0;            // 所有数据将存放于区块0

typedef struct {         //定义结构体用于存储物品相关信息
  byte uid[4];
  byte gname[16];
  byte weight[16];
} RFIDTag;

/*============================Functions==========================*/
String receiveFromSerial()
{
  String val="";
  char c;
    //如果串口接收到数据，就输出到蓝牙串口
  while (Serial.available()) 
  {
  c = char(Serial.read());
  val += c;
  delay(2);
  }
  return val;
}


String recv()
{
  char c;         //用于每次读取
  String val="";  //将接收到的字符存储为字符串
  
  while (BT.available()) 
  {
    c = char(BT.read());
    val += c;
    delay(2);
  }
  return val;
}


byte* recv2arr()
{
  byte c;
  byte i = 0;
  byte *id;
  Serial.print("Received ID:");
  while (BT.available()) 
  {
    c = BT.read();
    Serial.print(c,HEX);
    delay(2);
    id[i] = c;
    i++;
  }
  Serial.println();
  return id;
}


String recvAndReply()
{
  char c;         //用于每次读取
  String val="";  //将接收到的字符存储为字符串
  
  while (BT.available()) 
  {
    c = char(BT.read());
    val += c;
    delay(2);
  }
  if (val.length()>0&&val!="hello,Arduino!")
  {
      BT.print("OK");
      Serial.println("Reply:<OK>");
  }
//  else if(val="")
//  {
//    BT.print("FAILED");
//    Serial.println("Received Error!");
//  }

  if (val == "FAILED")
  {
    return val;
  }

  
  return val;
}


void wait()
{
    while (!BT.available())
    { 
    }
}


void waiting()
{
    Serial.println("Waiting for more CMD");
    wait();
}



void cmdOperation(String val)
{

    if(val=="hello,Arduino!")
    {
        Serial.println("Message received:<" +val+">");  
        Serial.println("hello my lord");
        // 测试用，故不通过蓝牙串口发送
    }
    else if (val=="SIGNUP")
    {
        Serial.println("Command accpted:<SIGN-UP>");
        signup_cmd();
    }
    else if (val=="WRITETAG")
    {
        Serial.println("Command accpted:<WRITE-TAG>");
        writeTag_cmd();
    }
    else if (val=="SEARCH")
    {       
        Serial.println("Command accpted:<SEARCH-TAG>");
        search_cmd();
    }
    else if (val=="SHINENBUZZ")
    {
        Serial.println("Command accpted:<SHINE-BUZZ>");
        shinebuzz_cmd();
    }
    else
    {
        Serial.println("Command error:No such kind of cmd");
        BT.print("FALSE");
    }
}


void shinebuzz_cmd()
{
    String cmdStr;

    waiting();
    cmdStr = recv();
    Serial.println("Received str：" + cmdStr);
    if(cmdStr=="CONTINUE")
    {
        Serial.println("Continue processing");
        digitalWrite(BUZZER,HIGH);
        digitalWrite(RGB,HIGH);
        BT.print("SUCCESS");
        delay(2000);
        digitalWrite(BUZZER,LOW);
        digitalWrite(RGB,LOW);

    }
    else
    {
        BT.print("FAILED");
        Serial.println("Command <SHINE-BUZZ> FAILED");
    }
}


void search_cmd()
{
    PROGMEM String Tags[2]={""};
    String cmdStr;
    String tar_id;
    bool stat = false;
    byte i = 0;
//    mfrc522.PCD_StopCrypto1();
//    mfrc522.PICC_HaltA();
//    delay(100);
    mfrc522.PCD_Reset();
    delay(100);
    mfrc522.PCD_Init();        // 初始化MFRC522卡片
    delay(100);
    while (mfrc522.PICC_IsNewCardPresent() && mfrc522.PICC_ReadCardSerial())
    {
      byte *id = mfrc522.uid.uidByte;
      Serial.print("Read the No.");
      Serial.print(i);
      Serial.print(" UID:");
      delay(100);
      for (byte j = 0;j < 4;j++)
      {
//          Serial.print(id[j],HEX);
          Serial.print("  Use tohex(): ");
          Serial.print(tohex(id[j]));
          Tags[i] += tohex(id[j]);
          mfrc522.PCD_StopCrypto1();
          mfrc522.PICC_HaltA();
          delay(100);
      }
      i++;
      Serial.println();
    }
    waiting();
    cmdStr = recv();
    if(cmdStr=="CONTINUE")
    {
      Serial.println("Continue processing");
      waiting();
      delay(200);
      tar_id = recv();
      Serial.println("Received target uid:"+ tar_id);
      for (byte i=0;i<2;i++)
      {
        if (Tags[i]==tar_id)
        {
          stat = true;
        }
      }
      if (stat)
      {
          BT.print("FOUND");
      }
      else
      {
          BT.print("FAILED");
      }
    }
    
}


void writeTag_cmd()
{
    RFIDTag newitem;
    String nameStr;
    String weightStr;
    String cmdStr;
    bool status1;
    bool status2;
    char namearr[16]={0};
    char weightarr[16]={0};

    waiting();
    cmdStr=recv();
    Serial.println("Received str：" + cmdStr);
    if(cmdStr=="CONTINUE")
    {
        Serial.println("CONTINUE Processing");
        waiting();
        nameStr=recvAndReply();
        if (nameStr == "FAILED")
        {
          Serial.print("Data received error!");
          return;
        }
        Serial.println("Received str："+nameStr);
        nameStr.toCharArray(namearr,16);
        //Serial.print("nameStr length:"+ sizeof(nameStr));
        Serial.print("change to Array successfully:");
        for(byte i =0;i<16;i++)
        {
          Serial.write(namearr[i]);
        }
        Serial.println();
        waiting();
        weightStr=recvAndReply();
        if (weightStr == "FAILED")
        {
          Serial.print("Data received error!");
          return;
        }
        Serial.println("Received str："+weightStr);
        weightStr.toCharArray(weightarr,16);
        //Serial.print("nameStr length:"+ sizeof(weightStr));
        Serial.println("change to Array successfully");
        for(byte i =0;i<16;i++)
        {
          Serial.write(weightarr[i]);
        }
        Serial.println();
        waiting();
        cmdStr=recv();
        Serial.println("Received str：" + cmdStr);
        if(cmdStr=="CONTINUE")
        {
          Serial.println("CONTINUE Processing");
           // 查看是否感應到卡片
          if ( ! mfrc522.PICC_IsNewCardPresent()) 
          {
              Serial.println("No Card nearby");
              BT.print("FAILED");
              Serial.println("Command <WRITE-TAG> FAILED");
              return;
           }
           if ( ! mfrc522.PICC_ReadCardSerial()) 
           { 
               Serial.println("Read UID Failed");
               BT.print("FAILED");
               Serial.println("Command <WRITE-TAG> FAILED");
               return;
           }
            status1=writeTag(name_sector, block, (byte*)namearr);
            Serial.println("First writing is" + char(status1));
            status2=writeTag(weight_sector, block, (byte*)weightarr);
            Serial.println("First writing is" + char(status2));
            mfrc522.PCD_StopCrypto1();
            mfrc522.PICC_HaltA();
            if(status1==true && status2==true)
            {
                BT.print("SUCCESS");
                Serial.println("Command <WRITE-TAG> SUCCESS");
            }
            else
            {
                BT.print("FAILED");
                Serial.println("Command <WRITE-TAG> FAILED");
                return;
            }
        }
        else
        {
            Serial.println("Continue Failed");
        }
    }
    else
    {
        Serial.println("Continue Failed");
    }
}


bool  writeTag(byte _sector, byte _block, byte _blockData[])
{
  bool stat=false;
  byte Goods_block[16];
  MFRC522::StatusCode status;
  if (_sector < 0 || _sector > 15 || _block < 0 || _block > 3) {
    // 超出范围报错
    Serial.println(F("Wrong sector or block number."));
    return stat;
  }
 
  if (_sector == 0 && _block == 0) {
    // 区段0的区块0只读，无法读取
    Serial.println(F("First block is read-only."));
    return stat;
  }
 
  byte blockNum = _sector * 4 + _block;  // 计算区块总编号
  byte trailerBlock = _sector * 4 + 3;   // 计算该区段对应的控制区块编号
  // 验证密钥
  status = (MFRC522::StatusCode) mfrc522.PCD_Authenticate(MFRC522::PICC_CMD_MF_AUTH_KEY_A, trailerBlock, &key, &(mfrc522.uid));
  // 未通过验证时报错并结束写入
  if (status != MFRC522::STATUS_OK) {
    Serial.print(F("PCD_Authenticate() failed: "));
    Serial.println(mfrc522.GetStatusCodeName(status));
    return stat;
  }
  //在指定位置写入16位U_char 或说是 byte 数组数据
  status = (MFRC522::StatusCode) mfrc522.MIFARE_Write(blockNum, _blockData, 16);
  // 写入失败时报错并结束写入
  if (status != MFRC522::STATUS_OK) {
    Serial.print(F("MIFARE_Write() failed: "));
    Serial.println(mfrc522.GetStatusCodeName(status));
    return stat;
  }
  Serial.println(F("Data was written.")); //此处的F表示直接再flash调用字符串而不适用ram
  stat = true;
  return stat;
}


void signup_cmd()
{
    String cmdStr;
    byte buffer[18];
    String nameStr;
    String weightStr;
    bool stat1=false;
    bool stat2=false;
    bool stat3=false;
    waiting();
    cmdStr = recv();
    Serial.println("Received str：" + cmdStr);
    if(cmdStr=="CONTINUE")
    {
        Serial.println("CONTINUE Processing");
        stat1 = readUid();
        if(!stat1)
        {
          return;
        }
        waiting();
        cmdStr = recv();
        if(cmdStr == "OK")
        {
           stat2 = readTag(name_sector,block,buffer); 
        }
        else
        {
          Serial.println("command:<SIGN-IP> FAILED:The PC didnt receive the UID");
          return;
        }
        if(!stat2)
        {
          return;
        }
        waiting();
        cmdStr = recv();
        if(cmdStr == "OK")
        {
            stat3 = readTag(weight_sector,block,buffer);
        }
        else
        {
          Serial.println("command:<SIGN-IP> FAILED:<SIGN-IP> FAILED:The PC didnt receive the name");
          BT.print("FAILED");
          return;
        }
        if(!stat3)
        {
          return;
        }
        mfrc522.PCD_StopCrypto1();
        mfrc522.PICC_HaltA();
        waiting();
        cmdStr=recv();
        if(cmdStr="OK")
        {
            Serial.println("command:<SIGN-UP> SUCCESS!");
            BT.print("SUCCESS");
        }
        else
        {
            Serial.println("command:<SIGN-IP> FAILED:<SIGN-IP> FAILED:The PC didnt receive the weight");
            BT.print("FAILED");
            return;
        }
    }
    else
    {
      Serial.println("Continue failed");
      BT.print("FAILED");
    }
}



bool readUid()
{
  bool stat = false;
  String uidStr;
  String cmdStr;
  if ( ! mfrc522.PICC_IsNewCardPresent()) 
    {
        Serial.println("No Card nearby");
        BT.print("FAILED");
        Serial.println("Command <SIGN-UP> FAILED");
        return stat;
     }
  if ( ! mfrc522.PICC_ReadCardSerial()) 
   { 
      Serial.println("Read UID Failed");
      BT.print("FAILED");
      Serial.println("Command <WRITE-TAG> FAILED");
      return stat;
   }
     byte *id = mfrc522.uid.uidByte;
     byte idSize = mfrc522.uid.size;

     MFRC522::PICC_Type piccType = mfrc522.PICC_GetType(mfrc522.uid.sak);
     Serial.println(mfrc522.PICC_GetTypeName(piccType));
     Serial.print("UID Size: ");       //显示uid长度
     Serial.println(idSize);
     BT.print("OK");
     waiting();
     cmdStr = recv();
     if(cmdStr=="CONTINUE")
     {
         for (byte i = 0; i < idSize; i++) 
         {  // 逐一顯示UID碼
             Serial.print("id[");
             Serial.print(i);
             Serial.print("]: ");
             Serial.println(id[i], HEX);  //16进制显示Uid
             BT.print(id[i],HEX);
         }
         Serial.println();
         stat = true;

     }
     else
     {
      Serial.println("Contimue Failed!");
     }
     return stat;
}


bool readTag(byte _sector, byte _block, byte _blockData[])
{
    MFRC522::StatusCode status;
    bool stat=false;
    String cmdStr;
    if (_sector < 0 || _sector > 15 || _block < 0 || _block > 3) 
    {
        // 超出范围报错
        Serial.println(F("Wrong sector or block number."));
        BT.print("FAILED");
        return stat;
    }
 
    if (_sector == 0 && _block == 0) 
    {
        // 区段0的区块0只读，无法读取
        Serial.println(F("First block is read-only."));
        BT.print("FAILED");
        return stat;
    }
    byte blockNum = _sector * 4 + _block;  // 计算区块总编号
    byte trailerBlock = _sector * 4 + 3;   // 计算该区段对应的控制区块编号
    status = (MFRC522::StatusCode) mfrc522.PCD_Authenticate(MFRC522::PICC_CMD_MF_AUTH_KEY_A, trailerBlock, &key, &(mfrc522.uid));
    // 未通过验证时报错并结束写入
    if (status != MFRC522::STATUS_OK) 
    {
        Serial.print(F("PCD_Authenticate() failed: "));
        Serial.println(mfrc522.GetStatusCodeName(status));
        BT.print("FAILED");
        return stat;
    }

     // 开始读取
     byte buffersize = 18;
     status = (MFRC522::StatusCode) mfrc522.MIFARE_Read(blockNum, _blockData, &buffersize);
 
     // 读取失败时报错并结束读取
     if (status != MFRC522::STATUS_OK) 
     {
         Serial.print(F("MIFARE_read() failed: "));
         Serial.println(mfrc522.GetStatusCodeName(status));
         BT.print("FAILED");
         return stat;
     }

     Serial.println(F("Data was read."));
     BT.print("OK");
     waiting();
     cmdStr = recv();
     if(cmdStr=="CONTINUE")
     {
         for(byte i = 0;i < 16; i++)
         {
          BT.write(_blockData[i]);
          Serial.print("Data has been send :");
          Serial.write(_blockData[i]);
          Serial.println();
         }
         stat = true;

     }
     else
     {
       Serial.println("Contimue Failed!");
     }
     return stat;
}
//十进制转十六进制
String tohex(int n) 
{
  if (n == 0) 
  {
    return "00"; //n为0
  }
  String result = "";
  char _16[] = {
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'};
  const int radix = 16;
  while (n) {
    int i = n % radix;          // 余数
    result = _16[i] + result;   // 将余数对应的十六进制数字加入结果
    n /= radix;                 // 除以16获得商，最为下一轮的被除数
  }
  if (result.length() < 2) {
    result = '0' + result; //不足两位补零
  }
  return result;
}



void scanCard()
{
  BT.print("A7B3199701");
}


/*============================Main==========================*/
void setup() {
  Serial.begin(9600);   //与电脑的串口连接
  Serial.println("BT is ready!");
  BT.begin(9600);  //设置波特率
  SPI.begin();     //初始化SPI
  mfrc522.PCD_Init();        // 初始化MFRC522卡片
  pinMode(RGB,OUTPUT);    //设置蜂鸣器以及指示灯引脚模式
  pinMode(BUZZER,OUTPUT);    //设置蜂鸣器以及指示灯引脚模式
  digitalWrite(RGB,LOW);
  digitalWrite(BUZZER,LOW);
  for (byte i = 0;i<6;i++)
  {                                  // 初始化密钥对象,设置为默认密钥
      key.keyByte[i] = 0xFF;
  }
}

void loop() {
  String cmd = "";
  if (BT.available())
  {
    cmd = recvAndReply();
  }

  if(cmd!="")
  {
    Serial.println("Received something:"+cmd);
    cmdOperation(cmd);
  }
}
