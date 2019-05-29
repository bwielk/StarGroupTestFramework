import unittest
from lib.common import basic_post_request, basic_get_request, basic_delete_request
from resources.endpoints import endpoints
from test_utils.utils import read_json_file

class TestPostingNewFixtures(unittest.TestCase):

    def setUp(self):
        #self.existing_fixture = read_json_file("../resources/fixtures_to_add_existing_fixture.json")
        self.fixture4 = read_json_file("../resources/fixtures_to_add_fixture_4.json")
        self.fixture5 = read_json_file("../resources/fixtures_to_add_fixture_5.json")

    def test_an_additional_fixture_is_successfully_posted(self):
        response = basic_post_request(endpoints["add_fixture"], self.fixture4)
        all_fixtures = basic_get_request(endpoints["get_fixtures"])
        self.assertEqual(response.status_code, 200)
        basic_delete_request(endpoints["get_fixture_by_id"] + str(len(all_fixtures.json())))

    def test_an_additional_fixture_is_successfully_added(self):
        posting_a_fixture_response = basic_post_request(endpoints["add_fixture"], self.fixture4)
        all_fixtures = basic_get_request(endpoints["get_fixtures"])
        self.assertEqual(len(all_fixtures.json()), 4)
        self.assertEqual(posting_a_fixture_response.status_code, 200)
        basic_delete_request(endpoints["get_fixture_by_id"] + str(len(all_fixtures.json())))

    def test_two_additional_fixtures_are_successfully_added(self):
        basic_post_request(endpoints["add_fixture"], self.fixture4)
        basic_post_request(endpoints["add_fixture"], self.fixture5)
        all_fixtures = basic_get_request(endpoints["get_fixtures"]).json()
        self.assertEqual(len(all_fixtures), 5)
        basic_delete_request(endpoints["get_fixture_by_id"] + "4")
        basic_delete_request(endpoints["get_fixture_by_id"] + "5")


if __name__ == "__name__":
    unittest.main()
