import unittest
from unittest.mock import Mock

class Test_API(unittest.TestCase):
    # Create a fake (mock) object
    fake_api = Mock()


    # Make it return a fixed value
    fake_api.get_data.return_value = {"temp": 25}


    # Use the mock instead of the real API
    def test_weather_api(self):
        result = self.fake_api.get_data()
        assert result == {"temp": 25}  # Passes (no real API call!)