import unittest
from lib.common import basic_post_request, basic_delete_request, basic_get_request
from resources.endpoints import endpoints
from test_utils.utils import read_json_file


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
        all_fixtures_before_deletion = basic_get_request(endpoints["get_fixtures"]).json()
        for x in range(len(all_fixtures_before_deletion), 0, -1):
            basic_delete_request(endpoints["get_fixture_by_id"] + str(x))
        all_fixtures_after_deletion = basic_get_request(endpoints["get_fixtures"]).json()
        self.assertEqual(len(all_fixtures_after_deletion), 0)

    def test_deleting_a_fixture_added_before_a_newly_added_fixture(self):
        self.posting_a_fixture4_response = basic_post_request(endpoints["add_fixture"], json_body=self.fixture5)
        all_fixtures_before_deletion = basic_get_request(endpoints["get_fixtures"]).json()
        self.assertEqual(len(all_fixtures_before_deletion), 5)
        basic_delete_request(endpoints["get_fixture_by_id"] + "4")
        all_fixtures_after_deletion = basic_get_request(endpoints["get_fixtures"]).json()
        self.assertEqual(len(all_fixtures_after_deletion), 4)


if __name__ == "__name__":
    unittest.main()
