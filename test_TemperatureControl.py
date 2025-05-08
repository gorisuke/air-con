from TemperatureControl import TemperatureControl
from unittest import mock

def test_compressor1_fan3_adjust():
    tc = TemperatureControl()
    tc.s = mock.MagicMock()
    tc.s.get_temperature.return_value = 20
    tc.s.get_humidity.return_value = 45

    tc.f = mock.MagicMock()
    tc.c = mock.MagicMock()
    
    tc.adjust(20)
    tc.f.set_air.assert_called_once_with(3)
    tc.c.set_level.assert_called_once_with(1)

def test_target_temp_is_too_low():
    tc = TemperatureControl()
    tc.s = mock.MagicMock()
    tc.s.get_temperature.return_value = 22
    tc.s.get_humidity.return_value = 45

    tc.f = mock.MagicMock()
    tc.c = mock.MagicMock()
    
    tc.adjust(5)
    tc.f.set_air.assert_not_called()
    tc.c.set_level.assert_not_called()
