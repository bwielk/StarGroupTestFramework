import unittest
from lib.common import basic_post_request, basic_delete_request, basic_get_request
from resources.endpoints import endpoints
from test_utils.utils import read_json_file, delete_all_fixtures


class TestPostingNewFixtures(unittest.TestCase):

    def setUp(self):
        self.fixture4 = read_json_file("../resources/fixtures_to_add_fixture_4.json")
        self.fixture5 = read_json_file("../resources/fixtures_to_add_fixture_5.json")
        self.posting_a_fixture4_response = basic_post_request(endpoints["add_fixture"], json_body=self.fixture4)

    def test_deleting_a_newly_added_fixture(self):
        all_fixtures_before_deletion = basic_get_request(endpoints["get_fixtures"]).json()
        self.assertEqual(len(all_fixtures_before_deletion), 4)
        basic_delete_request(endpoints["get_fixture_by_id"] + "4")
        all_fixtures_after_deletion = basic_get_request(endpoints["get_fixtures"]).json()
        self.assertEqual(len(all_fixtures_after_deletion), 3)

    def test_deleting_all_existing_fixtures(self):
        delete_all_fixtures()
        all_fixtures_after_deletion = basic_get_request(endpoints["get_fixtures"]).json()
        self.assertEqual(len(all_fixtures_after_deletion), 0)
        base_fixtures = read_json_file("../resources/base_fixtures.json")
        for fixture in base_fixtures:
            basic_post_request(endpoints["add_fixture"], json_body=fixture)

    def test_deleting_a_fixture_added_before_a_newly_added_fixture(self):
        basic_post_request(endpoints["add_fixture"], json_body=self.fixture5)
        all_fixtures_before_deletion = basic_get_request(endpoints["get_fixtures"]).json()
        self.assertEqual(len(all_fixtures_before_deletion), 5)
        basic_delete_request(endpoints["get_fixture_by_id"] + "4")
        all_fixtures_after_deletion = basic_get_request(endpoints["get_fixtures"]).json()
        self.assertEqual(len(all_fixtures_after_deletion), 4)
        basic_delete_request(endpoints["get_fixture_by_id"] + "5")

    def test_attempting_to_delete_a_fixture_that_does_not_exist_returns_an_appropriate_message(self):
        all_fixtures_before_deletion = basic_get_request(endpoints["get_fixtures"]).json()
        responses = [basic_delete_request(endpoints["get_fixture_by_id"] + "10"),
                     basic_delete_request(endpoints["get_fixture_by_id"] + "5"),
                     basic_delete_request(endpoints["get_fixture_by_id"] + "0")]
        self.assertEqual(len(all_fixtures_before_deletion), 4)
        self.assertEqual(all(x.status_code == 404 for x in responses), True)
        self.assertEqual(all(x.text == "Fixture not found" for x in responses), True)
        basic_delete_request(endpoints["get_fixture_by_id"] + "4")


if __name__ == "__name__":
    unittest.main()
