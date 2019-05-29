import unittest
from lib.common import basic_post_request, basic_get_request, basic_delete_request
from resources.endpoints import endpoints
from test_utils.utils import read_json_file

class TestPostingNewFixtures(unittest.TestCase):

    # the commented out json file is for a literal copy of one of the fixtures. Considering I am not sure of
    # how the business logic deals with fixture duplicates, I am going to skip that test scenario out.
    # However, it looks like the duplicates are accepted - is it a bug?

    def setUp(self):
        #self.existing_fixture = read_json_file("../resources/fixtures_to_add_existing_fixture.json")
        self.fixture4 = read_json_file("../resources/fixtures_to_add_fixture_4.json")
        self.fixture5 = read_json_file("../resources/fixtures_to_add_fixture_5.json")
        self.posting_a_fixture4_response = basic_post_request(endpoints["add_fixture"], json_body=self.fixture4)

    def test_an_additional_fixture_is_successfully_posted(self):
        all_fixtures = basic_get_request(endpoints["get_fixtures"])
        self.assertEqual(self.posting_a_fixture4_response.status_code, 200)
        basic_delete_request(endpoints["get_fixture_by_id"] + str(len(all_fixtures.json())))

    def test_an_additional_fixture_is_successfully_added(self):
        all_fixtures = basic_get_request(endpoints["get_fixtures"])
        self.assertEqual(len(all_fixtures.json()), 4)
        self.assertEqual(self.posting_a_fixture4_response.status_code, 200)
        basic_delete_request(endpoints["get_fixture_by_id"] + str(len(all_fixtures.json())))

    def test_two_additional_fixtures_are_successfully_added(self):
        basic_post_request(endpoints["add_fixture"], json_body=self.fixture5)
        all_fixtures = basic_get_request(endpoints["get_fixtures"]).json()
        self.assertEqual(len(all_fixtures), 5)
        basic_delete_request(endpoints["get_fixture_by_id"] + "4")
        basic_delete_request(endpoints["get_fixture_by_id"] + "5")

    def test_an_information_on_newly_added_fixture_can_be_retrieved(self):
        response_getting_the_new_fixture = basic_get_request(endpoints["get_fixture_by_id"] + "4").json()
        fixture_id = response_getting_the_new_fixture["fixtureId"]
        home_team = response_getting_the_new_fixture["footballFullState"]["homeTeam"]
        away_team = response_getting_the_new_fixture["footballFullState"]["awayTeam"]
        clock_time = response_getting_the_new_fixture["footballFullState"]["goals"][0]["clockTime"]
        self.assertEqual(fixture_id, str(4))
        self.assertEqual(home_team, "Fixture4 Team")
        self.assertEqual(away_team, "FC United")
        self.assertEqual(clock_time, 780)
        basic_delete_request(endpoints["get_fixture_by_id"] + "4")

    def test_first_element_of_teams_array_has_HOME_as_teamID_value(self):
        basic_post_request(endpoints["add_fixture"], json_body=self.fixture5)
        all_fixtures = basic_get_request(endpoints["get_fixtures"]).json()
        results = []
        for fixtures in all_fixtures:
            home_team_id = fixtures["footballFullState"]["teams"][0]["teamId"]
            results.append(home_team_id)
        self.assertEqual(all(x == "HOME" for x in results), True)
        self.assertEqual(len(results), 5)
        basic_delete_request(endpoints["get_fixture_by_id"] + "4")
        basic_delete_request(endpoints["get_fixture_by_id"] + "5")


if __name__ == "__name__":
    unittest.main()
