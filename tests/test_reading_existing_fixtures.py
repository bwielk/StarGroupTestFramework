import unittest
from resources.endpoints import endpoints
from lib.common import basic_get_request


class TestFixtures(unittest.TestCase):

    def setUp(self):
        fixtures_url = endpoints["get_fixtures"]
        self.non_json_response = basic_get_request(fixtures_url)
        self.json_response = self.non_json_response.json()

    def test_the_endpoint_works(self):
        self.assertEqual(self.non_json_response.status_code, 200)

    def test_check_the_endpoint_returns_3_fixtures(self):
        self.assertEqual(len(self.json_response), 3)

    def test_check_the_endpoint_does_not_return_a_number_greater_or_less_than_the_actual_amount_of_fixtures(self):
        self.assertNotEqual(len(self.json_response), 1)
        self.assertNotEqual(len(self.json_response), 2)
        self.assertNotEqual(len(self.json_response), 4)

    def test_check_that_each_fixture_contains_the_fixtureId_key(self):
        results = []
        for fixture in self.json_response:
            results.append(True) if "fixtureId" in fixture else False
        self.assertEqual(all(result == True for result in results), True)

    def test_check_that_each_fixture_contains_different_fixtureId_value(self):
        results = []
        for fixture in self.json_response:
            results.append(fixture["fixtureId"])
        self.assertEqual(len(set(results)), 3)


if __name__ == '__name__':
    unittest.main()
