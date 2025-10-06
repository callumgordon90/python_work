import unittest
from city_functions import city_country

class TestCityCountry(unittest.TestCase):
    """Tests that the function 'city_country' works"""
    
    def test_city_country(self):
        """Do cases like 'Valencia, Spain' work?"""
        result_wasp = city_country("Valencia", "Spain")
        self.assertEqual(result_wasp, "Valencia, Spain, default value")

    def test_city_country_population(self):
        """hyes"""
        resut = city_country("Valencia", "Spain", "55")
        self.assertEqual(resut, "Valencia, Spain, 55")


if __name__ =='__main__':
    unittest.main()