from . import TunicTestBase


class TestAccess(TunicTestBase):
    # test whether you can get into the temple without laurels
    def test_temple_access(self):
        self.collect_all_but(["Hero's Laurels", "Lantern"])
        self.assertFalse(self.can_reach_location("Sealed Temple - Page Pickup"))
        self.collect_by_name(["Lantern"])
        self.assertTrue(self.can_reach_location("Sealed Temple - Page Pickup"))

    def test_wells(self):
        # test that the wells function properly. Since fairies is written the same way, that should succeed too
        locations = ["Coins in the Well - 3 Coins", "Coins in the Well - 6 Coins", "Coins in the Well - 10 Coins",
                     "Coins in the Well - 15 Coins"]
        items = [["Golden Coin"]]
        self.assertAccessDependency(locations, items)


class TestHexQuestNoShuffle(TunicTestBase):
    options = {"hexagon_quest": "true",
               "ability_shuffling": "false"}

    # test that you need the gold hexes to reach the Heir in Hex Quest
    def test_hexquest_victory(self):
        location = ["The Heir"]
        item = [["Gold Questagon"]]
        self.assertAccessDependency(location, item)

    # test that you can get the item behind the overworld hc door with nothing and no ability shuffle
    def test_hc_door_no_shuffle(self):
        self.assertTrue(self.can_reach_location("Fountain Cross Door - Page Pickup"))


class TestStandardNoShuffle(TunicTestBase):
    options = {"hexagon_quest": "false",
               "ability_shuffling": "false"}

    # test that you can get the item behind the overworld hc door with nothing and no ability shuffle
    def test_hc_door_no_shuffle(self):
        self.assertTrue(self.can_reach_location("Fountain Cross Door - Page Pickup"))

    # test that you need the three colored hexes to reach the Heir in standard
    def test_normal_goal(self):
        location = ["The Heir"]
        items = [["Red Questagon", "Blue Questagon", "Green Questagon"]]
        self.assertAccessDependency(location, items)


class TestStandardShuffle(TunicTestBase):
    options = {"ability_shuffling": "true"}

    # test that you need to get holy cross to open the hc door in overworld
    def test_hc_door(self):
        self.assertFalse(self.can_reach_location("Fountain Cross Door - Page Pickup"))
        self.collect_by_name("Pages 42-43 (Holy Cross)")
        self.assertTrue(self.can_reach_location("Fountain Cross Door - Page Pickup"))


class TestHexQuestShuffle(TunicTestBase):
    options = {"ability_shuffling": "true",
               "hexagon_quest": "true"}

    # test that you need the gold questagons to open the hc door in overworld
    def test_hc_door_hex_shuffle(self):
        self.assertFalse(self.can_reach_location("Fountain Cross Door - Page Pickup"))
        self.collect_by_name("Gold Questagon")
        self.assertTrue(self.can_reach_location("Fountain Cross Door - Page Pickup"))
