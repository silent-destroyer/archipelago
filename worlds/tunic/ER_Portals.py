from typing import Dict, NamedTuple, List, Set, Tuple, TYPE_CHECKING
from .ER_Regions import tunic_er_regions, add_dependent_regions
if TYPE_CHECKING:
    from . import TunicWorld
else:
    TunicWorld = object


class Portal(NamedTuple):
    name: str  # human-readable name
    region: str  # AP region
    destination: str  # vanilla destination scene
    tag: str  # vanilla destination tag, empty string if no tag
    dead_end: bool = False  # dead end means there is only one exit from the room
    # dead ends need to be prevented from connecting to each other
    
    def scene(self) -> str:  # the actual scene name in Tunic
        return tunic_er_regions[self.region].game_scene

    def scene_destination_tag(self) -> str:  # full, nonchanging name to interpret by the mod
        return self.scene() + ", " + self.destination + "_" + self.tag


portal_mapping: List[Portal] = [
    Portal(name="Stick House Entrance", region="Overworld",
           destination="Sword Cave", tag=""),
    Portal(name="Windmill Entrance", region="Overworld",
           destination="Windmill", tag=""),
    Portal(name="Well Ladder Entrance", region="Overworld",
           destination="Sewer", tag="entrance"),
    Portal(name="Entrance to Well from Well Rail", region="Overworld Well to Furnace Rail",
           destination="Sewer", tag="west_aqueduct"),
    Portal(name="Old House Entry Door", region="Overworld Old House Door",
           destination="Overworld Interiors", tag="house"),
    Portal(name="Old House Waterfall Entrance", region="Overworld",
           destination="Overworld Interiors", tag="under_checkpoint"),
    Portal(name="Entrance to Furnace from Well Rail", region="Overworld Well to Furnace Rail",
           destination="Furnace", tag="gyro_upper_north"),
    Portal(name="Entrance to Furnace from Windmill", region="Overworld",
           destination="Furnace", tag="gyro_upper_east"),
    Portal(name="Entrance to Furnace from West Garden", region="Overworld to West Garden from Furnace",
           destination="Furnace", tag="gyro_west"),
    Portal(name="Entrance to Furnace from Beach", region="Overworld",
           destination="Furnace", tag="gyro_lower"),
    Portal(name="Rotating Lights Entrance", region="Overworld",
           destination="Overworld Cave", tag=""),
    Portal(name="Swamp Upper Entrance", region="Overworld Laurels",
           destination="Swamp Redux 2", tag="wall"),
    Portal(name="Swamp Lower Entrance", region="Overworld",
           destination="Swamp Redux 2", tag="conduit"),
    Portal(name="Ruined Hall Entrance Not-Door", region="Overworld",
           destination="Ruins Passage", tag="east"),
    Portal(name="Ruined Hall Entrance Door", region="Overworld Ruined Hall Door",
           destination="Ruins Passage", tag="west"),
    Portal(name="Atoll Upper Entrance", region="Overworld",
           destination="Atoll Redux", tag="upper"),
    Portal(name="Atoll Lower Entrance", region="Overworld",
           destination="Atoll Redux", tag="lower"),
    Portal(name="Special Shop Entrance", region="Overworld Laurels",
           destination="ShopSpecial", tag=""),
    Portal(name="Maze Cave Entrance", region="Overworld",
           destination="Maze Room", tag=""),
    Portal(name="West Garden Entrance by Belltower", region="Overworld Belltower",
           destination="Archipelagos Redux", tag="upper"),
    Portal(name="West Garden Entrance by Dark Tomb", region="Overworld to West Garden from Furnace",
           destination="Archipelagos Redux", tag="lower"),
    Portal(name="West Garden Laurel Entrance", region="Overworld Laurels",
           destination="Archipelagos Redux", tag="lowest"),
    Portal(name="Temple Door Entrance", region="Overworld Temple Door",
           destination="Temple", tag="main"),
    Portal(name="Temple Rafters Entrance", region="Overworld",
           destination="Temple", tag="rafters"),
    Portal(name="Ruined Shop Entrance", region="Overworld",
           destination="Ruined Shop", tag=""),
    Portal(name="Patrol Cave Entrance", region="Overworld",
           destination="PatrolCave", tag=""),
    Portal(name="Hourglass Cave Entrance", region="Overworld",
           destination="Town Basement", tag="beach"),
    Portal(name="Changing Room Entrance", region="Overworld",
           destination="Changing Room", tag=""),
    Portal(name="Cube Room Entrance", region="Overworld",
           destination="CubeRoom", tag=""),
    Portal(name="Stairs from Overworld to Mountain", region="Overworld",
           destination="Mountain", tag=""),
    Portal(name="Overworld to Fortress", region="Overworld",
           destination="Fortress Courtyard", tag=""),
    Portal(name="Fountain HC Entrance", region="Overworld Fountain Cross Door",
           destination="Town_FiligreeRoom", tag=""),
    Portal(name="Glass Cannon HC Room Entrance", region="Overworld Southeast Cross Door",
           destination="EastFiligreeCache", tag=""),
    Portal(name="Overworld to Quarry Connector", region="Overworld",
           destination="Darkwoods Tunnel", tag=""),
    Portal(name="Dark Tomb Main Entrance", region="Overworld",
           destination="Crypt Redux", tag=""),
    Portal(name="Overworld to Forest Belltower", region="Overworld",
           destination="Forest Belltower", tag=""),
    Portal(name="Town Portal", region="Overworld Town Portal",
           destination="Transit", tag="teleporter_town"),
    Portal(name="Spawn Portal", region="Overworld Spawn Portal",
           destination="Transit", tag="teleporter_starting island"),
    Portal(name="Entrance to Fairy Cave", region="Overworld",
           destination="Waterfall", tag=""),
    Portal(name="Fairy Cave Exit", region="Secret Gathering Place",
           destination="Overworld Redux", tag="",
           dead_end=True),
    Portal(name="Windmill Exit", region="Windmill",
           destination="Overworld Redux", tag=""),
    Portal(name="Windmill Shop", region="Windmill",
           destination="Shop", tag=""),
    Portal(name="Exit from Old House Front Door", region="Old House Front",
           destination="Overworld Redux", tag="house"),
    Portal(name="Teleport to Secret Treasure Room", region="Old House Front",
           destination="g_elements", tag=""),
    Portal(name="Exit from Old House Back Door", region="Old House Back",
           destination="Overworld Redux", tag="under_checkpoint"),
    Portal(name="Secret Treasure Room Exit", region="Relic Tower",
           destination="Overworld Interiors", tag="",
           dead_end=True),
    Portal(name="Changing Room Exit", region="Changing Room",
           destination="Overworld Redux", tag="",
           dead_end=True),
    Portal(name="Fountain HC Room Exit", region="Fountain Cross Room",
           destination="Overworld Redux", tag="",
           dead_end=True),
    Portal(name="Cube Room Exit", region="Cube Cave",
           destination="Overworld Redux", tag="",
           dead_end=True),
    Portal(name="Guard Patrol Cave Exit", region="Patrol Cave",
           destination="Overworld Redux", tag="",
           dead_end=True),
    Portal(name="Ruined Shop Exit", region="Ruined Shop",
           destination="Overworld Redux", tag="",
           dead_end=True),
    Portal(name="Furnace to Well Rail", region="Furnace Fuse",
           destination="Overworld Redux", tag="gyro_upper_north"),
    Portal(name="Furnace to Dark Tomb", region="Furnace Walking Path",
           destination="Crypt Redux", tag=""),
    Portal(name="Furnace to West Garden", region="Furnace Walking Path",
           destination="Overworld Redux", tag="gyro_west"),
    Portal(name="Furnace to Beach", region="Furnace Ladder Area",
           destination="Overworld Redux", tag="gyro_lower"),
    Portal(name="Furnace to Windmill", region="Furnace Ladder Area",
           destination="Overworld Redux", tag="gyro_upper_east"),
    Portal(name="Stick House Exit", region="Stick House",
           destination="Overworld Redux", tag="",
           dead_end=True),
    Portal(name="Ruined Passage Door Exit", region="Ruined Passage",
           destination="Overworld Redux", tag="east"),
    Portal(name="Ruined Passage Not-door Exit", region="Ruined Passage",
           destination="Overworld Redux", tag="west"),
    Portal(name="Glass Cannon HC Room Exit", region="Southeast Cross Room",
           destination="Overworld Redux", tag="",
           dead_end=True),
    Portal(name="Rotating Lights Exit", region="Caustic Light Cave",
           destination="Overworld Redux", tag="",
           dead_end=True),
    Portal(name="Maze Cave Exit", region="Maze Cave",
           destination="Overworld Redux", tag="",
           dead_end=True),
    Portal(name="Hourglass Cave Exit", region="Hourglass Cave",
           destination="Overworld Redux", tag="beach",
           dead_end=True),
    Portal(name="Special Shop Exit", region="Special Shop",
           destination="Overworld Redux", tag="",
           dead_end=True),
    Portal(name="Temple Rafters Exit", region="Sealed Temple Rafters",
           destination="Overworld Redux", tag="rafters"),
    Portal(name="Temple Door Exit", region="Sealed Temple",
           destination="Overworld Redux", tag="main"),
    Portal(name="Well Ladder Exit", region="Bottom of the Well Front",
           destination="Overworld Redux", tag="entrance"),
    Portal(name="Well to Well Boss", region="Bottom of the Well Back",
           destination="Sewer_Boss", tag=""),
    Portal(name="Well Rail Exit", region="Bottom of the Well Back",
           destination="Overworld Redux", tag="west_aqueduct"),
    Portal(name="Well Boss to Well", region="Well Boss",
           destination="Sewer", tag=""),
    Portal(name="Checkpoint to Dark Tomb", region="Dark Tomb Checkpoint",
           destination="Crypt Redux", tag=""),
    Portal(name="Dark Tomb to Overworld", region="Dark Tomb Entry Point",
           destination="Overworld Redux", tag=""),
    Portal(name="Dark Tomb to Furnace", region="Dark Tomb Dark Exit",
           destination="Furnace", tag=""),
    Portal(name="Dark Tomb to Checkpoint", region="Dark Tomb Entry Point",
           destination="Sewer_Boss", tag=""),
    Portal(name="West Garden Exit near Hero's Grave", region="West Garden",
           destination="Overworld Redux", tag="lower"),
    Portal(name="Magic Dagger House Entrance", region="West Garden",
           destination="archipelagos_house", tag=""),
    Portal(name="West Garden after Boss", region="West Garden after Boss",
           destination="Overworld Redux", tag="upper"),
    Portal(name="West Garden Shop", region="West Garden",
           destination="Shop", tag=""),
    Portal(name="West Garden Laurels Exit", region="West Garden Laurels Exit",
           destination="Overworld Redux", tag="lowest"),
    Portal(name="West Garden Hero's Grave", region="West Garden Hero's Grave",
           destination="RelicVoid", tag="teleporter_relic plinth"),
    Portal(name="West Garden Portal", region="West Garden Portal Area",
           destination="Transit", tag="teleporter_archipelagos_teleporter",
           dead_end=True),
    Portal(name="Magic Dagger House Exit", region="Magic Dagger House",
           destination="Archipelagos Redux", tag="",
           dead_end=True),
    Portal(name="Upper Atoll Exit", region="Ruined Atoll",
           destination="Overworld Redux", tag="upper"),
    Portal(name="Lower Atoll Exit", region="Ruined Atoll Lower Entry Area",
           destination="Overworld Redux", tag="lower"),
    Portal(name="Atoll Shop", region="Ruined Atoll",
           destination="Shop", tag=""),
    Portal(name="Atoll Portal", region="Ruined Atoll Portal",
           destination="Transit", tag="teleporter_atoll"),
    Portal(name="Atoll to Library", region="Ruined Atoll",
           destination="Library Exterior", tag=""),
    Portal(name="Frog Eye Entrance", region="Ruined Atoll",
           destination="Frog Stairs", tag="eye"),
    Portal(name="Frog Mouth Entrance", region="Ruined Atoll Frog Mouth",
           destination="Frog Stairs", tag="mouth"),
    Portal(name="Frog Eye Exit", region="Frog's Domain Entry",
           destination="Atoll Redux", tag="eye"),
    Portal(name="Frog Mouth Exit", region="Frog's Domain Entry",
           destination="Atoll Redux", tag="mouth"),
    Portal(name="Upper Frog to Lower Frog Entrance", region="Frog's Domain Entry",
           destination="frog cave main", tag="Entrance"),
    Portal(name="Upper Frog to Lower Frog Exit", region="Frog's Domain Entry",
           destination="frog cave main", tag="Exit"),
    Portal(name="Lower Frog Ladder Exit", region="Frog's Domain",
           destination="Frog Stairs", tag="Entrance"),
    Portal(name="Lower Frog Orb Exit", region="Frog's Domain Back",
           destination="Frog Stairs", tag="Exit"),
    Portal(name="Library to Atoll", region="Library Exterior Tree",
           destination="Atoll Redux", tag=""),
    Portal(name="Library Entry Ladder", region="Library Exterior Ladder",
           destination="Library Hall", tag=""),
    Portal(name="Library Bookshelf Exit", region="Library Hall",
           destination="Library Exterior", tag=""),
    Portal(name="Library Hero's Grave", region="Library Hero's Grave",
           destination="RelicVoid", tag="teleporter_relic plinth"),
    Portal(name="Lower Library to Rotunda", region="Library Hall",
           destination="Library Rotunda", tag=""),
    Portal(name="Library Rotunda Lower Exit", region="Library Rotunda",
           destination="Library Hall", tag=""),
    Portal(name="Library Rotunda Upper Exit", region="Library Rotunda",
           destination="Library Lab", tag=""),
    Portal(name="Upper Library to Rotunda", region="Library Lab Lower",
           destination="Library Rotunda", tag=""),
    Portal(name="Library Portal", region="Library Portal",
           destination="Transit", tag="teleporter_library teleporter"),
    Portal(name="Upper Library to Librarian", region="Library Lab",
           destination="Library Arena", tag=""),
    Portal(name="Librarian Arena Exit", region="Library Arena",
           destination="Library Lab", tag="",
           dead_end=True),
    Portal(name="Forest to Belltower", region="East Forest",
           destination="Forest Belltower", tag=""),
    Portal(name="Forest Guard House 1 Lower Entrance", region="East Forest",
           destination="East Forest Redux Laddercave", tag="lower"),
    Portal(name="Forest Guard House 1 Gate Entrance", region="East Forest",
           destination="East Forest Redux Laddercave", tag="gate"),
    Portal(name="Forest Fox Dance Outside Doorway", region="East Forest Dance Fox Spot",
           destination="East Forest Redux Laddercave", tag="upper"),
    Portal(name="Forest Portal", region="East Forest Portal",
           destination="Transit", tag="teleporter_forest teleporter"),
    Portal(name="Forest Guard House 2 Lower Entrance", region="East Forest",
           destination="East Forest Redux Interior", tag="lower"),
    Portal(name="Forest Guard House 2 Upper Entrance", region="East Forest",
           destination="East Forest Redux Interior", tag="upper"),
    Portal(name="Forest Grave Path Lower Entrance", region="East Forest",
           destination="Sword Access", tag="lower"),
    Portal(name="Forest Grave Path Upper Entrance", region="East Forest",
           destination="Sword Access", tag="upper"),
    Portal(name="Guard House 1 Dance Exit", region="Guard House 1 West",
           destination="East Forest Redux", tag="upper"),
    Portal(name="Guard House 1 Lower Exit", region="Guard House 1 West",
           destination="East Forest Redux", tag="lower"),
    Portal(name="Guard House 1 Upper Forest Exit", region="Guard House 1 East",
           destination="East Forest Redux", tag="gate"),
    Portal(name="Guard House 1 to Guard Captain Room", region="Guard House 1 East",
           destination="Forest Boss Room", tag=""),
    Portal(name="Upper Forest Grave Path Exit", region="Forest Grave Path Upper",
           destination="East Forest Redux", tag="upper"),
    Portal(name="Lower Forest Grave Path Exit", region="Forest Grave Path Main",
           destination="East Forest Redux", tag="lower"),
    Portal(name="East Forest Hero's Grave", region="Forest Hero's Grave",
           destination="RelicVoid", tag="teleporter_relic plinth"),
    Portal(name="Guard House 2 Lower Exit", region="Guard House 2",
           destination="East Forest Redux", tag="lower"),
    Portal(name="Guard House 2 Upper Exit", region="Guard House 2",
           destination="East Forest Redux", tag="upper"),
    Portal(name="Guard Captain Room Non-Gate Exit", region="Forest Boss Room",
           destination="East Forest Redux Laddercave", tag=""),
    Portal(name="Guard Captain Room Gate Exit", region="Forest Boss Room",
           destination="Forest Belltower", tag=""),
    Portal(name="Forest Belltower to Fortress", region="Forest Belltower Main",
           destination="Fortress Courtyard", tag=""),
    Portal(name="Forest Belltower to Forest", region="Forest Belltower Lower",
           destination="East Forest Redux", tag=""),
    Portal(name="Forest Belltower to Overworld", region="Forest Belltower Main",
           destination="Overworld Redux", tag=""),
    Portal(name="Forest Belltower to Guard Captain Room", region="Forest Belltower Upper",
           destination="Forest Boss Room", tag=""),
    Portal(name="Lower Fortress Grave Path Entrance", region="Fortress Courtyard",
           destination="Fortress Reliquary", tag="Lower"),
    Portal(name="Upper Fortress Grave Path Entrance", region="Fortress Courtyard Upper",
           destination="Fortress Reliquary", tag="Upper"),
    Portal(name="Fortress Courtyard to Fortress Interior", region="Fortress Courtyard",
           destination="Fortress Main", tag="Big Door"),
    Portal(name="Fortress Courtyard to Fortress East", region="Fortress Courtyard Upper",
           destination="Fortress East", tag=""),
    Portal(name="Fortress Courtyard to Beneath the Earth", region="Fortress Exterior near cave",
           destination="Fortress Basement", tag=""),
    Portal(name="Fortress Courtyard to Forest Belltower", region="Fortress Exterior from East Forest",
           destination="Forest Belltower", tag=""),
    Portal(name="Fortress Courtyard to Overworld", region="Fortress Exterior from Overworld",
           destination="Overworld Redux", tag=""),
    Portal(name="Fortress Courtyard Shop", region="Fortress Exterior near cave",
           destination="Shop", tag=""),
    Portal(name="Beneath the Earth to Fortress Interior", region="Beneath the Vault Back",
           destination="Fortress Main", tag=""),
    Portal(name="Beneath the Earth to Fortress Courtyard", region="Beneath the Vault Front",
           destination="Fortress Courtyard", tag=""),
    Portal(name="Fortress Main Exit", region="Eastern Vault Fortress",
           destination="Fortress Courtyard", tag="Big Door"),
    Portal(name="Fortress Interior to Beneath the Earth", region="Eastern Vault Fortress",
           destination="Fortress Basement", tag=""),
    Portal(name="Fortress Interior to Siege Engine", region="Eastern Vault Fortress Gold Door",
           destination="Fortress Arena", tag=""),
    Portal(name="Fortress Interior Shop", region="Eastern Vault Fortress",
           destination="Shop", tag=""),
    Portal(name="Fortress Interior to East Fortress Upper", region="Eastern Vault Fortress",
           destination="Fortress East", tag="upper"),
    Portal(name="Fortress Interior to East Fortress Lower", region="Eastern Vault Fortress",
           destination="Fortress East", tag="lower"),
    Portal(name="East Fortress to Interior Lower", region="Fortress East Shortcut Lower",
           destination="Fortress Main", tag="lower"),
    Portal(name="East Fortress to Courtyard", region="Fortress East Shortcut Upper",
           destination="Fortress Courtyard", tag=""),
    Portal(name="East Fortress to Interior Upper", region="Fortress East Shortcut Upper",
           destination="Fortress Main", tag="upper"),
    Portal(name="Lower Fortress Grave Path Exit", region="Fortress Grave Path",
           destination="Fortress Courtyard", tag="Lower"),
    Portal(name="Fortress Hero's Grave", region="Fortress Grave Path",
           destination="RelicVoid", tag="teleporter_relic plinth"),
    Portal(name="Fortress Grave Path Dusty Entrance", region="Fortress Grave Path Dusty Entrance",
           destination="Dusty", tag=""),
    Portal(name="Dusty Exit", region="Fortress Leaf Piles",
           destination="Fortress Reliquary", tag="",
           dead_end=True),
    Portal(name="Upper Fortress Grave Path Exit", region="Fortress Grave Path Upper",
           destination="Fortress Courtyard", tag="Upper",
           dead_end=True),
    Portal(name="Siege Engine Arena to Fortress", region="Fortress Arena",
           destination="Fortress Main", tag=""),
    Portal(name="Fortress Portal", region="Fortress Arena Portal",
           destination="Transit", tag="teleporter_spidertank"),
    Portal(name="Stairs to Top of the Mountain", region="Lower Mountain Stairs",
           destination="Mountaintop", tag=""),
    Portal(name="Mountain to Quarry", region="Lower Mountain",
           destination="Quarry Redux", tag=""),
    Portal(name="Mountain to Overworld", region="Lower Mountain",
           destination="Overworld Redux", tag=""),
    Portal(name="Top of the Mountain Exit", region="Top of the Mountain",
           destination="Mountain", tag="",
           dead_end=True),
    Portal(name="Quarry Connector to Overworld", region="Quarry Connector",
           destination="Overworld Redux", tag=""),
    Portal(name="Quarry Connector to Quarry", region="Quarry Connector",
           destination="Quarry Redux", tag=""),
    Portal(name="Quarry to Overworld Exit", region="Quarry",
           destination="Darkwoods Tunnel", tag=""),
    Portal(name="Quarry Shop", region="Quarry",
           destination="Shop", tag=""),
    Portal(name="Quarry to Monastery Front", region="Quarry",
           destination="Monastery", tag="front"),
    Portal(name="Quarry to Monastery Back", region="Monastery Rope",
           destination="Monastery", tag="back"),
    Portal(name="Quarry to Mountain", region="Quarry",
           destination="Mountain", tag=""),
    Portal(name="Quarry Zig Entrance", region="Lower Quarry Zig Door",
           destination="ziggurat2020_0", tag=""),
    Portal(name="Quarry Portal", region="Quarry Portal",
           destination="Transit", tag="teleporter_quarry teleporter"),
    Portal(name="Monastery Rear Exit", region="Monastery Back",
           destination="Quarry Redux", tag="back"),
    Portal(name="Monastery Front Exit", region="Monastery Front",
           destination="Quarry Redux", tag="front"),
    Portal(name="Monastery Hero's Grave", region="Monastery Hero's Grave",
           destination="RelicVoid", tag="teleporter_relic plinth"),
    Portal(name="Zig Entry Hallway to Zig 1", region="Rooted Ziggurat Entry",
           destination="ziggurat2020_1", tag=""),
    Portal(name="Zig Entry Hallway to Quarry", region="Rooted Ziggurat Entry",
           destination="Quarry Redux", tag=""),
    Portal(name="Zig 1 to Zig Entry", region="Rooted Ziggurat Upper Front",
           destination="ziggurat2020_0", tag=""),
    Portal(name="Zig 1 to Zig 2", region="Rooted Ziggurat Upper Back",
           destination="ziggurat2020_2", tag=""),
    Portal(name="Zig 2 to Zig 1", region="Rooted Ziggurat Middle Top",
           destination="ziggurat2020_1", tag=""),
    Portal(name="Zig 2 to Zig 3", region="Rooted Ziggurat Middle Bottom",
           destination="ziggurat2020_3", tag=""),
    Portal(name="Zig Portal Room Entrance", region="Rooted Ziggurat Portal Room Entrance",
           destination="ziggurat2020_FTRoom", tag=""),
    Portal(name="Zig 3 to Zig 2", region="Rooted Ziggurat Lower Front",
           destination="ziggurat2020_2", tag=""),
    Portal(name="Zig Portal Room Exit", region="Rooted Ziggurat Portal Room Exit",
           destination="ziggurat2020_3", tag=""),
    Portal(name="Zig Portal", region="Rooted Ziggurat Portal",
           destination="Transit", tag="teleporter_ziggurat teleporter"),
    Portal(name="Lower Swamp Exit", region="Swamp",
           destination="Overworld Redux", tag="conduit"),
    Portal(name="Swamp to Cathedral Main Entrance", region="Swamp to Cathedral Main Entrance",
           destination="Cathedral Redux", tag="main"),
    Portal(name="Swamp to Cathedral Treasure Room Entrance", region="Swamp to Cathedral Treasure Room",
           destination="Cathedral Redux", tag="secret"),
    Portal(name="Swamp to Gauntlet", region="Back of Swamp",
           destination="Cathedral Arena", tag=""),
    Portal(name="Swamp Shop", region="Swamp",
           destination="Shop", tag=""),
    Portal(name="Upper Swamp Exit", region="Back of Swamp Laurels Area",
           destination="Overworld Redux", tag="wall"),
    Portal(name="Swamp Hero's Grave", region="Swamp Hero's Grave",
           destination="RelicVoid", tag="teleporter_relic plinth"),
    Portal(name="Cathedral Main Exit", region="Cathedral",
           destination="Swamp Redux 2", tag="main"),
    Portal(name="Cathedral Elevator", region="Cathedral",
           destination="Cathedral Arena", tag=""),
    Portal(name="Cathedral Treasure Room Exit", region="Cathedral Secret Legend Room",
           destination="Swamp Redux 2", tag="secret",
           dead_end=True),
    Portal(name="Gauntlet to Swamp", region="Cathedral Gauntlet Exit",
           destination="Swamp Redux 2", tag="",
           dead_end=True),
    Portal(name="Gauntlet Elevator", region="Cathedral Gauntlet Checkpoint",
           destination="Cathedral Redux", tag=""),
    Portal(name="Gauntlet Shop", region="Cathedral Gauntlet Checkpoint",
           destination="Shop", tag=""),
    Portal(name="Hero Relic to Fortress", region="Hero Relic - Fortress",
           destination="Fortress Reliquary", tag="teleporter_relic plinth",
           dead_end=True),
    Portal(name="Hero Relic to Monastery", region="Hero Relic - Quarry",
           destination="Monastery", tag="teleporter_relic plinth",
           dead_end=True),
    Portal(name="Hero Relic to West Garden", region="Hero Relic - West Garden",
           destination="Archipelagos Redux", tag="teleporter_relic plinth",
           dead_end=True),
    Portal(name="Hero Relic to East Forest", region="Hero Relic - East Forest",
           destination="Sword Access", tag="teleporter_relic plinth",
           dead_end=True),
    Portal(name="Hero Relic to Library", region="Hero Relic - Library",
           destination="Library Hall", tag="teleporter_relic plinth",
           dead_end=True),
    Portal(name="Hero Relic to Swamp", region="Hero Relic - Swamp",
           destination="Swamp Redux 2", tag="teleporter_relic plinth",
           dead_end=True),
    Portal(name="Far Shore to West Garden", region="Far Shore to West Garden",
           destination="Archipelagos Redux", tag="teleporter_archipelagos_teleporter"),
    Portal(name="Far Shore to Library", region="Far Shore to Library",
           destination="Library Lab", tag="teleporter_library teleporter"),
    Portal(name="Far Shore to Quarry", region="Far Shore to Quarry",
           destination="Quarry Redux", tag="teleporter_quarry teleporter"),
    Portal(name="Far Shore to East Forest", region="Far Shore to East Forest",
           destination="East Forest Redux", tag="teleporter_forest teleporter"),
    Portal(name="Far Shore to Fortress", region="Far Shore to Fortress",
           destination="Fortress Arena", tag="teleporter_spidertank"),
    Portal(name="Far Shore to Atoll", region="Far Shore",
           destination="Atoll Redux", tag="teleporter_atoll"),
    Portal(name="Far Shore to Zig", region="Far Shore",
           destination="ziggurat2020_FTRoom", tag="teleporter_ziggurat teleporter"),
    Portal(name="Far Shore to Heir", region="Far Shore",
           destination="Spirit Arena", tag="teleporter_spirit arena"),
    Portal(name="Far Shore to Town", region="Far Shore",
           destination="Overworld Redux", tag="teleporter_town"),
    Portal(name="Far Shore to Spawn", region="Far Shore to Spawn",
           destination="Overworld Redux", tag="teleporter_starting island"),
    Portal(name="Heir Arena Exit", region="Spirit Arena",
           destination="Transit", tag="teleporter_spirit arena",
           dead_end=True),
    Portal(name="Purgatory Bottom Exit", region="Purgatory",
           destination="Purgatory", tag="bottom"),
    Portal(name="Purgatory Top Exit", region="Purgatory",
           destination="Purgatory", tag="top"),
]


# pairing off portals, starting with dead ends
def pair_portals(world: TunicWorld) -> Dict[Portal, Portal]:
    # separate the portals into dead ends and non-dead ends
    portal_pairs: Dict[Portal, Portal] = {}
    dead_ends: List[Portal] = []
    two_plus: List[Portal] = []

    # create separate lists for dead ends and non-dead ends
    for portal in portal_mapping:
        if portal.dead_end:
            dead_ends.append(portal)
        else:
            two_plus.append(portal)

    connected_regions: Set[str] = set()
    # todo: better start region when/if implementing random start
    start_region = "Overworld"
    connected_regions.update(add_dependent_regions(start_region))

    # we want to start by making sure every region is accessible
    non_isolated_regions = set()
    for region_name, region_info in tunic_er_regions.items():
        if not region_info.isolated:
            non_isolated_regions.add(region_name)

    check_success = 0
    portal1 = None
    portal2 = None
    while len(connected_regions) < len(non_isolated_regions):
        # find a portal in an inaccessible region
        if check_success == 0:
            for portal in two_plus:
                if portal.region not in connected_regions:
                    # if there's risk of self-locking, start over
                    if lock_before_key(portal, two_plus):
                        world.random.shuffle(two_plus)
                        break
                    portal1 = portal
                    two_plus.remove(portal)
                    check_success = 1
                    break

        # then we find a portal in a connected region
        if check_success == 1:
            for portal in two_plus:
                if portal.region in connected_regions:
                    # if there's risk of self-locking, shuffle and try again
                    if lock_before_key(portal, two_plus):
                        world.random.shuffle(two_plus)
                        break
                    portal2 = portal
                    two_plus.remove(portal)
                    check_success = 2
                    break

        # once we have both portals, connect them and add the new region(s) to connected_regions
        if check_success == 2:
            connected_regions.update(add_dependent_regions(portal1.region))
            portal_pairs[portal1] = portal2
            check_success = 0
            world.random.shuffle(two_plus)

    # add 6 shops, connect them to unique scenes
    # this is due to a limitation in Tunic -- you wrong warp if there's multiple shops
    shop_scenes: Set[str] = set()
    for i in range(6):
        portal1 = None
        for portal in two_plus:
            if portal.scene() not in shop_scenes:
                shop_scenes.add(portal.scene())
                portal1 = portal
                two_plus.remove(portal)
                break
        if portal1 is None:
            raise Exception("Too many shops in the pool, or something else went wrong")
        portal2 = Portal(name="Shop Portal", region="Shop", destination="Previous Region", tag="")
        portal_pairs[portal1] = portal2
    
    # connect dead ends to random non-dead ends
    # none of the key events are in dead ends, so we don't need to do lock_before_key
    while len(dead_ends) > 0:
        portal1 = two_plus.pop()
        portal2 = dead_ends.pop()
        portal_pairs[portal1] = portal2

    # then randomly connect the remaining portals to each other
    # every region is accessible, so lock_before_key is not necessary
    while len(two_plus) > 1:
        portal1 = two_plus.pop()
        portal2 = two_plus.pop()
        portal_pairs[portal1] = portal2

    if len(two_plus) == 1:
        raise Exception("two plus had an odd number of portals, investigate this")

    for portal1, portal2 in portal_pairs.items():
        world.multiworld.spoiler.set_entrance(portal1.name, portal2.name, "both", world.player)
    
    return portal_pairs


# todo: get this to work after 2170 is merged
def plando_connect(world: TunicWorld) -> Tuple[Dict[Portal, Portal], Set[str]]:
    player = world.player
    plando_pairs = {}
    plando_names = set()
    for plando_cxn in world.plando_connections[player]:
        print(type(plando_cxn))
        print(type(plando_cxn.entrance))
        print(plando_cxn.entrance)
        print(plando_cxn.exit)
        portal1_name = plando_cxn.entrance
        portal2_name = plando_cxn.exit
        plando_names.add(plando_cxn.entrance)
        plando_names.add(plando_cxn.exit)
        portal1 = None
        portal2 = None
        for portal in portal_mapping:
            if portal1_name == portal.name:
                portal1 = portal
            if portal2_name == portal.name:
                portal2 = portal
        if portal1 is None and portal2 is None:
            raise Exception(f"Could not find entrances named {portal1_name} and {portal2_name}, "
                            "please double-check their names.")
        if portal1 is None:
            raise Exception(f"Could not find entrance named {portal1_name}, please double-check its name.")
        if portal2 is None:
            raise Exception(f"Could not find entrance named {portal2_name}, please double-check its name.")
        plando_pairs[portal1] = portal2
    plando_info = (plando_pairs, plando_names)
    return plando_info


# loop through our list of paired portals and make two-way connections
def create_randomized_entrances(portal_pairs: Dict[Portal, Portal], world: TunicWorld) -> None:
    for portal1, portal2 in portal_pairs.items():
        region1 = world.multiworld.get_region(portal1.region, world.player)
        region2 = world.multiworld.get_region(portal2.region, world.player)
        region1.connect(region2, f"{portal1.name} -> {portal2.name}")
        # prevent the logic from thinking you can get to any shop-connected region from the shop
        if portal2.name != "Shop":
            region2.connect(region1, f"{portal2.name} -> {portal1.name}")


# we're checking if an event-locked portal is being placed before the regions where its key(s) is/are
# doing this ensures the keys will not be locked behind the event-locked portal
def lock_before_key(check_portal: Portal, two_plus: List[Portal]) -> bool:
    # the western belltower cannot be locked since you can access it with laurels
    # so we only need to make sure the forest belltower isn't locked
    if check_portal.scene_destination_tag == "Overworld Redux, Temple_main":
        i = 0
        for portal in two_plus:
            if portal.scene_destination_tag == "Forest Belltower, Forest Boss Room_":
                i += 1
                break
        if i == 1:
            return True

    # fortress big gold door needs 2 scenes and one of the two upper portals of the courtyard
    elif check_portal.scene_destination_tag == "Fortress Main, Fortress Arena_":
        i = j = k = 0
        for portal in two_plus:
            if portal.scene_destination_tag in {"Fortress Courtyard, Fortress Reliquary_upper",
                                                "Fortress Courtyard, Fortress East_"}:
                i += 1
            if portal.scene == "Fortress Basement":
                j += 1
            if portal.scene == "Fortress Main":
                k += 1
        if i == 2 or j == 2 or k == 6:
            return True

    # fortress teleporter needs only the left fuses
    elif check_portal.scene_destination_tag in {"Fortress Arena, Transit_teleporter_spidertank",
                                                "Transit, Fortress Arena_teleporter_spidertank"}:
        i = j = k = 0
        for portal in two_plus:
            if portal.scene == "Fortress Courtyard":
                i += 1
            if portal.scene == "Fortress Basement":
                j += 1
            if portal.scene == "Fortress Main":
                k += 1
        if i == 8 or j == 2 or k == 6:
            return True

    # Cathedral door needs Overworld and the front of Swamp
    # Overworld is currently guaranteed, so no need to check it
    elif check_portal.scene_destination_tag == "Swamp Redux 2, Cathedral Redux_main":
        i = 0
        for portal in two_plus:
            if portal.region == "Swamp":
                i += 1
        if i == 4:
            return True

    # Zig portal room exit needs Zig 3 to be accessible to hit the fuse
    elif check_portal.scene_destination_tag == "ziggurat2020_FTRoom, ziggurat2020_3":
        i = 0
        for portal in two_plus:
            if portal.scene == "ziggurat2020_3":
                i += 1
        if i == 2:
            return True

    # Quarry teleporter needs you to hit the Darkwoods fuse
    # Since it's physically in Quarry, we don't need to check for it
    elif check_portal.scene_destination_tag == "Quarry Redux, Transit_teleporter_quarry teleporter":
        i = 0
        for portal in two_plus:
            if portal.scene == "Darkwoods Tunnel":
                i += 1
        if i == 2:
            return True

    # Same as above, but Quarry isn't guaranteed here
    elif check_portal.scene_destination_tag == "Transit, Quarry Redux_teleporter_quarry teleporter":
        i = j = 0
        for portal in two_plus:
            if portal.scene == "Darkwoods Tunnel":
                i += 1
            if portal.scene == "Quarry Redux":
                j += 1
        if i == 2 or j == 7:
            return True

    # Need Library fuse to use this teleporter
    elif check_portal.scene_destination_tag == "Transit, Library Lab_teleporter_library teleporter":
        i = 0
        for portal in two_plus:
            if portal.scene == "Library Lab":
                i += 1
        if i == 3:
            return True

    # Need West Garden fuse to use this teleporter
    elif check_portal.scene_destination_tag == "Transit, Archipelagos Redux_teleporter_archipelagos_teleporter":
        i = 0
        for portal in two_plus:
            if portal.scene == "Archipelagos Redux":
                i += 1
        if i == 7:
            return True

    # false means you're good to place the portal
    return False
        
