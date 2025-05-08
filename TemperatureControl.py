from Fan import Fan
from Compressor import Compressor
from Sensor import Sensor


# Test Target Class
## DON'T MODIFY ##
class TemperatureControl:
    def __init__(self):
        self.s = Sensor()
        self.f = Fan()
        self.c = Compressor()


    def adjust(self, target_temp):
        current_temp = self.s.get_temperature()
        current_humi = self.s.get_humidity()

        if target_temp < 20 or target_temp >= 30:
            return
        if current_temp < 10 or current_temp > 40:
            return
        if current_humi < 20 or current_humi > 80:
            return

        diff_temp = current_temp - target_temp
        compressor_level = 3
        fan_level = 5
        
        if current_humi < 40:
            fan_level = 2
        elif current_humi < 60:
            fan_level = 3
        else:
            fan_level = 4

        if diff_temp < -1:
            compressor_level = 0
            fan_level = 0
            if current_humi >= 60:
                compressor_level = 1
                fan_level = 1
        elif diff_temp >= -1 and diff_temp < 1:
            compressor_level = 1
        elif diff_temp >= 1 and diff_temp < 3:
            compressor_level = 2
        elif diff_temp > 3:
            compressor_level = 3
            if current_humi < 60:
                fan_level = 3
            else:
                fan_level = 5

        self.c.set_level(compressor_level)
        self.f.set_air(fan_level)


