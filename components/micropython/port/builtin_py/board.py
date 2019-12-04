class Board_Info:
    def __init__(self):
        self.pin_num = 48
        self.JTAG_TCK = 0
        self.JTAG_TDI = 1
        self.JTAG_TMS = 2
        self.JTAG_TDO = 3
        self.ISP_RX = 4
        self.ISP_TX = 5
        self.MIC_ARRAY_DATA0 = 6
        self.MIC_ARRAY_DATA1 = 7
        self.MIC_ARRAY_DATA2 = 8
        self.MIC_ARRAY_DATA3 = 9
        self.MIC_ARRAY_WS = 10
        self.MIC_ARRAY_BCK = 11
        self.MIC0_DATA = 12
        self.MIC0_WS = 13
        self.MIC0_BCK = 14
        self.PIN15 = 15
        self.PIN16 = 16
        self.PIN17 = 17
        self.PIN18 = 18
        self.PIN19 = 19
        self.PIN20 = 20
        self.PIN21 = 21
        self.PIN22 = 22
        self.PIN23 = 23
        self.PIN24 = 24
        self.LED_G = 25
        self.BOOT_KEY = 26
        self.WIFI_TX = 27
        self.WIFI_RX = 28
        self.SPI0_CLK = 29
        self.SPI0_MOSI = 30
        self.SPI0_MISO = 31
        self.SPI0_CS0 = 32
        self.I2S_DA = 33
        self.I2S_WS = 34
        self.I2S_BCK = 35
        self.LCD_CS = 36
        self.LCD_RST = 37	
        self.LCD_DC = 38
        self.LCD_WR = 39
        self.DVP_PCLK = 40
        self.DVP_XCLK = 41
        self.DVP_HSYNC = 42
        self.DVP_PWDN = 43
        self.DVP_VSYNC = 44
        self.DVP_RST = 45
        self.DVP_SCL = 46
        self.DVP_SDA = 47
        self.pin_name=['JTAG_TCK','JTAG_TDI','JTAG_TMS','JTAG_TDO','ISP_RX','ISP_TX','MIC_ARRAY_DATA0','MIC_ARRAY_DATA1','MIC_ARRAY_DATA2','MIC_ARRAY_DATA3','MIC_ARRAY_WS','MIC_ARRAY_BCK','MIC0_DATA','MIC0_WS','MIC0_BCK','PIN15','PIN16','PIN17','PIN18','PIN19','PIN20','PIN21','PIN22','PIN23','PIN24','LED_G','BOOT_KEY','WIFI_TX','WIFI_RX','SPI0_CLK','SPI0_MOSI','SPI0_MISO','SPI0_CS0','I2S_DA','I2S_WS','I2S_BCK','LCD_CS','LCD_RST','LCD_DC','LCD_WR','DVP_PCLK','DVP_XCLK','DVP_HSYNC','DVP_PWDN','DVP_VSYNC','DVP_RST','DVP_SCL','DVP_SDA']
        self.D = [4, 5, 21, 22, 23, 24, 32, 15, 14, 13, 12, 11, 10, 3]

    def pin_map(self,Pin = None):
        num_len = 10
        str_len = 23
        if Pin == None :
            num_sum_length = num_len
            str_sum_length = str_len
            Pin_str_obj = "Pin"
            Pin_str_obj_length = len(Pin_str_obj)
            Pin_str_obj_front = 3
            Pin_str_obj_rear = num_sum_length - Pin_str_obj_front - Pin_str_obj_front
            fun_str_obj = "Function"
            fun_str_obj_length = len(fun_str_obj)
            fun_str_obj_front = 5
            fun_str_obj_rear = str_sum_length - fun_str_obj_front - fun_str_obj_length
            print("|%s%s%s|%s%s%s|"%(str(Pin_str_obj_front * '-'),Pin_str_obj,str(Pin_str_obj_rear * '-'),str(fun_str_obj_front * '-'),fun_str_obj,str(fun_str_obj_rear*'-')))
            for i in range(0,len(self.pin_name)):
                num = str(i)
                num_length = len(num)
                num_front = 3
                num_rear = num_sum_length - num_front - num_length
                str_length = len(self.pin_name[i])
                str_front = 5
                str_rear = str_sum_length - str_front - str_length
                print("|%s%d%s|%s%s%s|"%(str(num_front * ' '),i,str(num_rear * ' '),str(str_front * ' '),self.pin_name[i],str(str_rear*' ')))
                print("+%s|%s+"%(str(num_sum_length*'-'),str(str_sum_length*'-')))
        elif isinstance(Pin,int) and Pin < 0 or Pin > 47:
            print("Pin num must in range[0,47]")
            return False
        elif isinstance(Pin,int):
            Pin_sum_length = num_len
            string_sum_length = str_len
            pin_str_obj = "Pin"
            pin_str_obj_length = len(pin_str_obj)
            pin_str_obj_front = 3
            pin_str_obj_rear = Pin_sum_length - pin_str_obj_front - pin_str_obj_front
            Fun_str_obj = "Function"
            Fun_str_obj_length = len(Fun_str_obj)
            Fun_str_obj_front = 5
            Fun_str_obj_rear = string_sum_length - Fun_str_obj_front - Fun_str_obj_length
            print("|%s%s%s|%s%s%s|"%(str(pin_str_obj_front * '-'),pin_str_obj,str(pin_str_obj_rear * '-'),str(Fun_str_obj_front * '-'),Fun_str_obj,str(Fun_str_obj_rear*'-')))
            Pin_str = str(Pin)
            Pin_length = len(Pin_str)
            Pin_front = 3
            Pin_rear = Pin_sum_length - Pin_front - Pin_length
            string_length = len(self.pin_name[Pin])
            string_front = 5
            string_rear = string_sum_length - string_front - string_length
            print("|%s%d%s|%s%s%s|"%(str(Pin_front * ' '),Pin,str(Pin_rear * ' '),str(string_front * ' '),self.pin_name[Pin],str(string_rear*' ')))
            print("+%s|%s+"%(str(Pin_sum_length*'-'),str(string_sum_length*'-')))
        else:
            print("Unknow error")
            return False
global board_info
board_info=Board_Info()
