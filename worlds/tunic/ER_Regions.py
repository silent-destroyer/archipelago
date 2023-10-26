from typing import Dict, NamedTuple, List, Callable, Set, Tuple, TYPE_CHECKING
from BaseClasses import CollectionState, Region, MultiWorld
from .Rules import prayer, holy_cross, has_sword, has_ability, red_hexagon, blue_hexagon, green_hexagon, gold_hexagon
from .Options import TunicOptions
if TYPE_CHECKING:
    from . import TunicWorld
else:
    TunicWorld = object


class RegionInfo(NamedTuple):
    game_scene: str  # the name of the scene in the actual game
    isolated: bool = False  # if this region has 1 entrance, coincides with the portal dead_ends


# first string is the AP Region name, second string is the Scene name in-game
tunic_er_regions: Dict[str, RegionInfo] = {
    "Menu": RegionInfo("Fake", True),
    "Overworld": RegionInfo("Overworld Redux"),
    "Overworld Holy Cross": RegionInfo("Fake", True),
    "Overworld Belltower": RegionInfo("Overworld Redux"),  # the area with the belltower and chest
    "Overworld Laurels": RegionInfo("Overworld Redux"),  # all spots in Overworld that you need laurels to reach
    "Overworld to West Garden from Furnace": RegionInfo("Overworld Redux"),  # that little connector after Dark Tomb
    "Overworld Well to Furnace Rail": RegionInfo("Overworld Redux"),  # the tiny rail passageway
    "Overworld Ruined Hall Door": RegionInfo("Overworld Redux"),  # the small space betweeen the door and the portal
    "Overworld Old House Door": RegionInfo("Overworld Redux"),  # the too-small space between the door and the portal
    "Overworld Southeast Cross Door": RegionInfo("Overworld Redux"),  # the small space betweeen the door and the portal
    "Overworld Fountain Cross Door": RegionInfo("Overworld Redux"),
    "Overworld Temple Door": RegionInfo("Overworld Redux"),  # the small space betweeen the door and the portal
    "Overworld Town Portal": RegionInfo("Overworld Redux"),
    "Overworld Spawn Portal": RegionInfo("Overworld Redux"),
    "Stick House": RegionInfo("Sword Cave", True),
    "Windmill": RegionInfo("Windmill"),
    "Old House Back": RegionInfo("Overworld Interiors"),  # part with the hc door
    "Old House Front": RegionInfo("Overworld Interiors"),  # part with the bedroom
    "Relic Tower": RegionInfo("g_elements", True),
    "Furnace Fuse": RegionInfo("Furnace"),  # top of the furnace
    "Furnace Ladder Area": RegionInfo("Furnace"),  # the two portals accessible by the ladder
    "Furnace Walking Path": RegionInfo("Furnace"),  # dark tomb to west garden
    "Secret Gathering Place": RegionInfo("Waterfall", True),
    "Changing Room": RegionInfo("Changing Room", True),
    "Patrol Cave": RegionInfo("PatrolCave", True),
    "Ruined Shop": RegionInfo("Ruined Shop", True),
    "Ruined Passage": RegionInfo("Ruins Passage"),
    "Special Shop": RegionInfo("ShopSpecial", True),
    "Caustic Light Cave": RegionInfo("Overworld Cave", True),
    "Maze Cave": RegionInfo("Maze Room", True),
    "Cube Cave": RegionInfo("CubeRoom", True),
    "Southeast Cross Room": RegionInfo("EastFiligreeCache", True),
    "Fountain Cross Room": RegionInfo("Town_FiligreeRoom", True),
    "Hourglass Cave": RegionInfo("Town Basement", True),
    "Sealed Temple": RegionInfo("Temple"),
    "Sealed Temple Rafters": RegionInfo("Temple"),
    "Forest Belltower Upper": RegionInfo("Forest Belltower"),
    "Forest Belltower Main": RegionInfo("Forest Belltower"),
    "Forest Belltower Lower": RegionInfo("Forest Belltower"),
    "East Forest": RegionInfo("East Forest Redux"),
    "East Forest Dance Fox Spot": RegionInfo("East Forest Redux"),
    "East Forest Portal": RegionInfo("East Forest Redux"),
    "Guard House 1 East": RegionInfo("East Forest Redux Laddercave"),
    "Guard House 1 West": RegionInfo("East Forest Redux Laddercave"),
    "Guard House 2": RegionInfo("East Forest Redux Interior"),
    "Forest Boss Room": RegionInfo("Forest Boss Room"),
    "Forest Grave Path Main": RegionInfo("Sword Access"),
    "Forest Grave Path Upper": RegionInfo("Sword Access"),
    "Forest Grave Path by Grave": RegionInfo("Sword Access"),
    "Forest Hero's Grave": RegionInfo("Sword Access"),
    "Dark Tomb Entry Point": RegionInfo("Crypt Redux"),  # top exit & checkpoint exit
    "Dark Tomb Main": RegionInfo("Crypt Redux"),
    "Dark Tomb Dark Exit": RegionInfo("Crypt Redux"),
    "Dark Tomb Checkpoint": RegionInfo("Sewer_Boss"),  # can laurels backwards
    "Well Boss": RegionInfo("Sewer_Boss"),  # can walk through (with bombs at least)
    "Bottom of the Well Front": RegionInfo("Sewer"),
    "Bottom of the Well Back": RegionInfo("Sewer"),  # add this in the other spots
    "West Garden": RegionInfo("Archipelagos Redux"),
    "Magic Dagger House": RegionInfo("archipelagos_house", True),
    "West Garden Portal Area": RegionInfo("Archipelagos Redux", True),
    "West Garden Laurels Exit": RegionInfo("Archipelagos Redux"),
    "West Garden after Boss": RegionInfo("Archipelagos Redux"),
    "West Garden Hero's Grave": RegionInfo("Archipelagos Redux"),
    "Ruined Atoll": RegionInfo("Atoll Redux"),
    "Ruined Atoll Lower Entry Area": RegionInfo("Atoll Redux"),
    "Ruined Atoll Frog Mouth": RegionInfo("Atoll Redux"),
    "Ruined Atoll Portal": RegionInfo("Atoll Redux"),
    "Frog's Domain Entry": RegionInfo("Frog Stairs"),
    "Frog's Domain": RegionInfo("frog cave main"),
    "Frog's Domain Back": RegionInfo("frog cave main"),
    "Library Exterior Tree": RegionInfo("Library Exterior"),
    "Library Exterior Ladder": RegionInfo("Library Exterior"),
    "Library Hall": RegionInfo("Library Hall"),
    "Library Hero's Grave": RegionInfo("Library Hall"),
    "Library Rotunda": RegionInfo("Library Rotunda"),
    "Library Lab": RegionInfo("Library Lab"),
    "Library Lab Lower": RegionInfo("Library Lab"),
    "Library Portal": RegionInfo("Library Lab"),
    "Library Arena": RegionInfo("Library Arena", True),
    "Fortress Exterior from East Forest": RegionInfo("Fortress Courtyard"),
    "Fortress Exterior from Overworld": RegionInfo("Fortress Courtyard"),
    "Fortress Exterior near cave": RegionInfo("Fortress Courtyard"),  # where the shop and beneath the earth entry are
    "Fortress Courtyard": RegionInfo("Fortress Courtyard"),
    "Fortress Courtyard Upper": RegionInfo("Fortress Courtyard"),
    "Beneath the Vault Front": RegionInfo("Fortress Basement"),  # the vanilla entry point
    "Beneath the Vault Back": RegionInfo("Fortress Basement"),  # the vanilla exit point
    "Eastern Vault Fortress": RegionInfo("Fortress Main"),
    "Eastern Vault Fortress Gold Door": RegionInfo("Fortress Main"),
    "Fortress East Shortcut Upper": RegionInfo("Fortress East"),
    "Fortress East Shortcut Lower": RegionInfo("Fortress East"),
    "Fortress Grave Path": RegionInfo("Fortress Reliquary"),
    "Fortress Grave Path Upper": RegionInfo("Fortress Reliquary", True),
    "Fortress Grave Path Dusty Entrance": RegionInfo("Fortress Reliquary"),
    "Fortress Hero's Grave": RegionInfo("Fortress Reliquary"),
    "Fortress Leaf Piles": RegionInfo("Dusty", True),
    "Fortress Arena": RegionInfo("Fortress Arena"),
    "Fortress Arena Portal": RegionInfo("Fortress Arena"),
    "Lower Mountain": RegionInfo("Mountain"),
    "Lower Mountain Stairs": RegionInfo("Mountain"),
    "Top of the Mountain": RegionInfo("Mountaintop", True),
    "Quarry Connector": RegionInfo("Darkwoods Tunnel"),
    "Quarry": RegionInfo("Quarry Redux"),
    "Quarry Portal": RegionInfo("Quarry Redux"),
    "Monastery Front": RegionInfo("Monastery"),
    "Monastery Back": RegionInfo("Monastery"),
    "Monastery Hero's Grave": RegionInfo("Monastery"),
    "Monastery Rope": RegionInfo("Quarry Redux"),
    "Lower Quarry": RegionInfo("Quarry Redux"),
    "Lower Quarry Zig Door": RegionInfo("Quarry Redux"),
    "Rooted Ziggurat Entry": RegionInfo("ziggurat2020_0"),
    "Rooted Ziggurat Upper Front": RegionInfo("ziggurat2020_1"),
    "Rooted Ziggurat Upper Back": RegionInfo("ziggurat2020_1"),  # after the administrator
    "Rooted Ziggurat Middle Top": RegionInfo("ziggurat2020_2"),
    "Rooted Ziggurat Middle Bottom": RegionInfo("ziggurat2020_2"),
    "Rooted Ziggurat Lower Front": RegionInfo("ziggurat2020_3"),  # the vanilla entry point side
    "Rooted Ziggurat Lower Back": RegionInfo("ziggurat2020_3"),  # the boss side
    "Rooted Ziggurat Portal Room Entrance": RegionInfo("ziggurat2020_3"),  # the door itself on the zig 3 side
    "Rooted Ziggurat Portal": RegionInfo("ziggurat2020_FTRoom"),
    "Rooted Ziggurat Portal Room Exit": RegionInfo("ziggurat2020_FTRoom"),
    "Swamp": RegionInfo("Swamp Redux 2"),
    "Swamp to Cathedral Treasure Room": RegionInfo("Swamp Redux 2"),
    "Swamp to Cathedral Main Entrance": RegionInfo("Swamp Redux 2"),
    "Back of Swamp": RegionInfo("Swamp Redux 2"),  # the area with hero grave and gauntlet entrance
    "Swamp Hero's Grave": RegionInfo("Swamp Redux 2"),
    "Back of Swamp Laurels Area": RegionInfo("Swamp Redux 2"),  # the spots you need laurels to traverse
    "Cathedral": RegionInfo("Cathedral Redux"),
    "Cathedral Secret Legend Room": RegionInfo("Cathedral Redux", True),
    "Cathedral Gauntlet Checkpoint": RegionInfo("Cathedral Arena"),
    "Cathedral Gauntlet": RegionInfo("Cathedral Arena"),
    "Cathedral Gauntlet Exit": RegionInfo("Cathedral Arena"),
    "Far Shore": RegionInfo("Transit"),
    "Far Shore to Spawn": RegionInfo("Transit"),
    "Far Shore to East Forest": RegionInfo("Transit"),
    "Far Shore to Quarry": RegionInfo("Transit"),
    "Far Shore to Fortress": RegionInfo("Transit"),
    "Far Shore to Library": RegionInfo("Transit"),
    "Far Shore to West Garden": RegionInfo("Transit"),
    "Hero Relic - Fortress": RegionInfo("RelicVoid", True),
    "Hero Relic - Quarry": RegionInfo("RelicVoid", True),
    "Hero Relic - West Garden": RegionInfo("RelicVoid", True),
    "Hero Relic - East Forest": RegionInfo("RelicVoid", True),
    "Hero Relic - Library": RegionInfo("RelicVoid", True),
    "Hero Relic - Swamp": RegionInfo("RelicVoid", True),
    "Purgatory": RegionInfo("Purgatory"),
    "Shop": RegionInfo("Shop", True),
    "Spirit Arena": RegionInfo("Spirit Arena", True),
    "Spirit Arena Victory": RegionInfo("Spirit Arena", True)
}


# todo: give a default for reqs, remove the extraneous []s
# todo: add origin=, destination=, etc.
class StaticCxn(NamedTuple):
    origin: str
    destination: str
    reqs: List[List[str]] = []
    region_reqs: List[str] = []
    reverse: bool = False  # if the reverse connection has the same requirements


er_static_cxns: List[StaticCxn] = [
    StaticCxn(origin="Menu", destination="Overworld"),
    StaticCxn(origin="Overworld Belltower", destination="Overworld"),
    StaticCxn(origin="Overworld", destination="Overworld Belltower", 
              reqs=[["Hero's Laurels"]]),
    StaticCxn(origin="Overworld", destination="Overworld Holy Cross", 
              reqs=[["Holy Cross"]]),
    StaticCxn(origin="Overworld", destination="Overworld Ruined Hall Door", 
              reqs=[["Key"]]),  # one-way because the reverse isn't necessary
    StaticCxn(origin="Overworld Laurels", destination="Overworld", 
              reqs=[["Hero's Laurels"]], reverse=True),
    StaticCxn(origin="Overworld", destination="Overworld Old House Door", 
              reqs=[["Old House Key"]]),
    StaticCxn(origin="Overworld Southeast Cross Door", destination="Overworld", 
              reqs=[["Holy Cross"]], reverse=True),
    StaticCxn(origin="Overworld Fountain Cross Door", destination="Overworld"),  # can exit with nothing
    StaticCxn(origin="Overworld", destination="Overworld Fountain Cross Door", 
              reqs=[["Holy Cross"]]),  # needs holy cross to enter it
    StaticCxn(origin="Overworld Town Portal", destination="Overworld"),  # can exit from it with nothing
    StaticCxn(origin="Overworld", destination="Overworld Town Portal", 
              reqs=[["Prayer"]]),  # but needs prayer to enter it
    StaticCxn(origin="Overworld Spawn Portal", destination="Overworld"),
    StaticCxn(origin="Overworld", destination="Overworld Spawn Portal", 
              reqs=[["Prayer"]]),
    StaticCxn(origin="Overworld Temple Door", destination="Overworld", 
              reqs=[["Stick"], ["Magic Wand"]],
              region_reqs=["Overworld Belltower", "Forest Belltower Upper"], reverse=True),
    StaticCxn(origin="Old House Front", destination="Old House Back"),
    StaticCxn(origin="Sealed Temple", destination="Sealed Temple Rafters"),
    StaticCxn(origin="Sealed Temple Rafters", destination="Sealed Temple", 
              reqs=[["Hero's Laurels"]]),
    StaticCxn(origin="Furnace Ladder Area", destination="Furnace Walking Path", 
              reqs=[["Hero's Laurels"]], reverse=True),
    StaticCxn(origin="Furnace Ladder Area", destination="Furnace Fuse", 
              reqs=[["Hero's Laurels"]], reverse=True),
    StaticCxn(origin="Furnace Fuse", destination="Furnace Walking Path", 
              reqs=[["Hero's Laurels"]], reverse=True),
    StaticCxn(origin="Forest Belltower Upper", destination="Forest Belltower Main"),
    StaticCxn(origin="Forest Belltower Main", destination="Forest Belltower Lower"),
    StaticCxn(origin="East Forest", destination="East Forest Dance Fox Spot", 
              reqs=[["Hero's Laurels"]], reverse=True),
    StaticCxn(origin="East Forest", destination="East Forest Portal", 
              reqs=[["Prayer"]]),
    StaticCxn(origin="East Forest Portal", destination="East Forest"),
    StaticCxn(origin="Guard House 1 East", destination="Guard House 1 West"),
    StaticCxn(origin="Guard House 1 West", destination="Guard House 1 East", 
              reqs=[["Hero's Laurels"]]),
    StaticCxn(origin="Forest Grave Path Upper", destination="Forest Grave Path Main", 
              reqs=[["Hero's Laurels"]], reverse=True),
    StaticCxn(origin="Forest Grave Path Main", destination="Forest Grave Path by Grave"),
    StaticCxn(origin="Forest Grave Path by Grave", destination="Forest Hero's Grave", 
              reqs=[["Prayer"]]),
    StaticCxn(origin="Forest Hero's Grave", destination="Forest Grave Path by Grave"),
    StaticCxn(origin="Bottom of the Well Front", destination="Bottom of the Well Back", 
              reqs=[["Stick"]], reverse=True),
    StaticCxn(origin="Well Boss", destination="Dark Tomb Checkpoint"),
    StaticCxn(origin="Dark Tomb Checkpoint", destination="Well Boss", 
              reqs=[["Hero's Laurels"]]),
    StaticCxn(origin="Dark Tomb Entry Point", destination="Dark Tomb Main", 
              reqs=[["Lantern"]], reverse=True),
    StaticCxn(origin="Dark Tomb Main", destination="Dark Tomb Dark Exit", 
              reqs=[["Lantern"]], reverse=True),
    StaticCxn(origin="West Garden Laurels Exit", destination="West Garden", 
              reqs=[["Hero's Laurels"]], reverse=True),
    StaticCxn(origin="West Garden after Boss", destination="West Garden", 
              reqs=[["Hero's Laurels"]]),
    StaticCxn(origin="West Garden", destination="West Garden after Boss", 
              reqs=[["Hero's Laurels"], ["Sword"]]),
    StaticCxn(origin="West Garden", destination="West Garden Hero's Grave", 
              reqs=[["Prayer"]]),
    StaticCxn(origin="West Garden Hero's Grave", destination="West Garden"),
    StaticCxn(origin="Ruined Atoll", destination="Ruined Atoll Lower Entry Area", 
              reqs=[["Hero's Laurels"]]),
    StaticCxn(origin="Ruined Atoll Frog Mouth", destination="Ruined Atoll", 
              reqs=[["Hero's Laurels"], ["Magic Orb"]], reverse=True),
    StaticCxn(origin="Ruined Atoll Lower Entry Area", destination="Ruined Atoll", 
              reqs=[["Hero's Laurels"], ["Magic Orb"]], reverse=True),
    StaticCxn(origin="Ruined Atoll", destination="Ruined Atoll Portal", 
              reqs=[["Prayer"]]),
    StaticCxn(origin="Ruined Atoll Portal", destination="Ruined Atoll"),
    StaticCxn(origin="Frog's Domain", destination="Frog's Domain Back", 
              reqs=[["Magic Orb"]]),
    StaticCxn(origin="Library Exterior Tree", destination="Library Exterior Ladder", 
              reqs=[["Magic Orb"], ["Hero's Laurels"]]),
    StaticCxn(origin="Library Exterior Ladder", destination="Library Exterior Tree", 
              reqs=[["Magic Orb", "Prayer"], ["Hero's Laurels", "Prayer"]]),
    StaticCxn(origin="Library Hall", destination="Library Hero's Grave", 
              reqs=[["Prayer"]]),
    StaticCxn(origin="Library Hero's Grave", destination="Library Hall"),
    StaticCxn(origin="Library Lab Lower", destination="Library Lab", 
              reqs=[["Hero's Laurels"], ["Magic Orb"]]),
    StaticCxn(origin="Library Lab", destination="Library Lab Lower", 
              reqs=[["Hero's Laurels"]]),
    StaticCxn(origin="Library Lab", destination="Library Portal", 
              reqs=[["Prayer"]]),
    StaticCxn(origin="Library Portal", destination="Library Lab"),
    StaticCxn(origin="Fortress Exterior from East Forest", destination="Fortress Exterior from Overworld",
              reqs=[["Hero's Laurels"], ["Magic Orb"]]),
    StaticCxn(origin="Fortress Exterior from Overworld", destination="Fortress Exterior from East Forest", 
              reqs=[["Hero's Laurels"]]),
    StaticCxn(origin="Fortress Exterior from Overworld", destination="Fortress Exterior near cave", 
              reqs=[["Hero's Laurels"], ["Prayer"]]),
    StaticCxn(origin="Fortress Exterior near cave", destination="Fortress Exterior from Overworld", 
              reqs=[["Hero's Laurels"]]),
    StaticCxn(origin="Fortress Exterior from Overworld", destination="Fortress Courtyard", 
              reqs=[["Hero's Laurels"]], reverse=True),
    StaticCxn(origin="Fortress Courtyard Upper", destination="Fortress Courtyard"),
    StaticCxn(origin="Fortress Courtyard Upper", destination="Fortress Exterior from Overworld"),
    StaticCxn(origin="Beneath the Vault Front", destination="Beneath the Vault Back", 
              reqs=[["Lantern"]]),
    StaticCxn(origin="Beneath the Vault Back", destination="Beneath the Vault Front"),
    StaticCxn(origin="Fortress East Shortcut Upper", destination="Fortress East Shortcut Lower"),
    StaticCxn(origin="Eastern Vault Fortress", destination="Eastern Vault Fortress Gold Door", 
              reqs=[["Prayer"]],
              region_reqs=["Fortress Exterior from Overworld", "Fortress Courtyard Upper", 
                           "Beneath the Vault Back", "Eastern Vault Fortress"], reverse=True),
    StaticCxn(origin="Fortress Grave Path", destination="Fortress Grave Path Dusty Entrance", 
              reqs=[["Hero's Laurels"]], reverse=True),
    StaticCxn(origin="Fortress Grave Path", destination="Fortress Hero's Grave", 
              reqs=[["Prayer"]]),
    StaticCxn(origin="Fortress Hero's Grave", destination="Fortress Grave Path"),
    StaticCxn(origin="Fortress Arena", destination="Fortress Arena Portal", 
              reqs=[["Prayer"]],
              region_reqs=["Fortress Exterior from Overworld", "Beneath the Vault Back", "Eastern Vault Fortress"]),
    StaticCxn(origin="Fortress Arena Portal", destination="Fortress Arena"),
    StaticCxn(origin="Lower Mountain", destination="Lower Mountain Stairs", 
              reqs=[["Holy Cross"]], reverse=True),
    StaticCxn(origin="Quarry", destination="Lower Quarry", 
              reqs=[["Scavenger Mask", "Sword"], ["Scavenger Mask", "Magic Wand"]], reverse=True),
    StaticCxn(origin="Quarry", destination="Quarry Portal", 
              reqs=[["Prayer", "Magic Orb"]], 
              region_reqs=["Quarry Connector"]),
    StaticCxn(origin="Quarry Portal", destination="Quarry"),
    StaticCxn(origin="Lower Quarry", destination="Lower Quarry Zig Door", 
              reqs=[["Magic Orb", "Prayer"]],
              region_reqs=["Quarry Connector", "Quarry"], reverse=True),
    StaticCxn(origin="Monastery Rope", destination="Quarry"),
    StaticCxn(origin="Monastery Front", destination="Monastery Back"),
    StaticCxn(origin="Monastery Back", destination="Monastery Front", 
              reqs=[["Hero's Laurels"]]),
    StaticCxn(origin="Monastery Back", destination="Monastery Hero's Grave", 
              reqs=[["Prayer"]]),
    StaticCxn(origin="Monastery Hero's Grave", destination="Monastery Back"),
    StaticCxn(origin="Rooted Ziggurat Upper Front", destination="Rooted Ziggurat Upper Back", 
              reqs=[["Hero's Laurels"], ["Sword"]]),
    StaticCxn(origin="Rooted Ziggurat Upper Back", destination="Rooted Ziggurat Upper Front", 
              reqs=[["Hero's Laurels"]]),
    StaticCxn(origin="Rooted Ziggurat Middle Top", destination="Rooted Ziggurat Middle Bottom"),
    StaticCxn(origin="Rooted Ziggurat Lower Front", destination="Rooted Ziggurat Lower Back", 
              reqs=[["Hero's Laurels"], ["Sword", "Prayer"]]),
    StaticCxn(origin="Rooted Ziggurat Lower Back", destination="Rooted Ziggurat Lower Front", 
              reqs=[["Hero's Laurels"]]),
    StaticCxn(origin="Rooted Ziggurat Lower Back", destination="Rooted Ziggurat Portal Room Entrance", 
              reqs=[["Prayer"]]),
    StaticCxn(origin="Rooted Ziggurat Portal Room Entrance", destination="Rooted Ziggurat Lower Back"),
    StaticCxn(origin="Rooted Ziggurat Portal", destination="Rooted Ziggurat Portal Room Exit", 
              reqs=[["Prayer"]],
              region_reqs=["Rooted Ziggurat Lower Back"]),
    StaticCxn(origin="Rooted Ziggurat Portal Room Exit", destination="Rooted Ziggurat Portal", 
              reqs=[["Prayer"]]),
    StaticCxn(origin="Swamp", destination="Swamp to Cathedral Main Entrance", 
              reqs=[["Prayer"]], 
              region_reqs=["Overworld Laurels", "Swamp"], reverse=True),
    StaticCxn(origin="Swamp", destination="Swamp to Cathedral Treasure Room", 
              reqs=[["Holy Cross"]]),
    StaticCxn(origin="Swamp to Cathedral Treasure Room", destination="Swamp"),
    StaticCxn(origin="Back of Swamp", destination="Back of Swamp Laurels Area", 
              reqs=[["Hero's Laurels"]], reverse=True),
    StaticCxn(origin="Back of Swamp", destination="Swamp Hero's Grave",
              reqs=[["Prayer"]]),
    StaticCxn(origin="Swamp Hero's Grave", destination="Back of Swamp"),
    StaticCxn(origin="Cathedral Gauntlet Checkpoint", destination="Cathedral Gauntlet"),
    StaticCxn(origin="Cathedral Gauntlet", destination="Cathedral Gauntlet Exit", 
              reqs=[["Hero's Laurels"]], reverse=True),
    StaticCxn(origin="Far Shore", destination="Far Shore to Spawn", 
              reqs=[["Hero's Laurels"]], reverse=True),
    StaticCxn(origin="Far Shore", destination="Far Shore to East Forest", 
              reqs=[["Hero's Laurels"]], reverse=True),
    StaticCxn(origin="Far Shore", destination="Far Shore to West Garden", 
              reqs=[["Prayer"]], 
              region_reqs=["West Garden"]),
    StaticCxn(origin="Far Shore to West Garden", destination="Far Shore"),
    StaticCxn(origin="Far Shore", destination="Far Shore to Quarry", 
              reqs=[["Prayer", "Magic Orb"]], 
              region_reqs=["Quarry", "Quarry Connector"]),
    StaticCxn(origin="Far Shore to Quarry", destination="Far Shore"),
    StaticCxn(origin="Far Shore", destination="Far Shore to Fortress", 
              reqs=[["Prayer"]],
              region_reqs=["Fortress Exterior from Overworld", "Beneath the Vault Back", "Eastern Vault Fortress"]),
    StaticCxn(origin="Far Shore to Fortress", destination="Far Shore"),
    StaticCxn(origin="Far Shore", destination="Far Shore to Library", 
              reqs=[["Prayer"]], 
              region_reqs=["Library Lab"]),
    StaticCxn(origin="Far Shore to Library", destination="Far Shore"),
  ]


def create_er_regions(player: int, multiworld: MultiWorld) -> None:
    for region_name in tunic_er_regions:
        region = Region(region_name, player, multiworld)
        multiworld.regions.append(region)


# create the static connections between the more granular regions
def create_static_cxns(world: TunicWorld, ability_unlocks: Dict[str, int]) -> None:
    for cxn in er_static_cxns:
        # todo: figure out if there's a good way to keep the reference to the Regions to avoid get_region
        multiworld = world.multiworld
        player = world.player
        origin_region = multiworld.get_region(cxn.origin, player)
        dest_region = multiworld.get_region(cxn.destination, player)
        if cxn.reqs:
            origin_region.connect(dest_region, f"{cxn.origin} -> {cxn.destination}",
                                  create_static_cxn_rule(cxn.reqs, cxn.region_reqs,
                                                         world, player, ability_unlocks))
            if cxn.reverse:
                dest_region.connect(origin_region, f"{cxn.destination} -> {cxn.origin}",
                                    create_static_cxn_rule(cxn.reqs, cxn.region_reqs,
                                                           world, player, ability_unlocks))
        # if there's no requirements, just create the connection without the rules field
        else:
            origin_region.connect(dest_region, f"{cxn.origin} -> {cxn.destination}")
            if cxn.reverse:
                dest_region.connect(origin_region, f"{cxn.destination} -> {cxn.origin}")

    # connect to the victory spot manually for finer control over the victory condition
    spirit_arena = world.multiworld.get_region("Spirit Arena", world.player)
    victory = world.multiworld.get_region("Spirit Arena Victory", world.player)
    spirit_arena.connect(victory, "Overcome the Heir",
                         lambda state: (state.has(gold_hexagon, player, world.options.hexagon_goal.value) if
                                        world.options.hexagon_quest else
                                        state.has_all({red_hexagon, green_hexagon, blue_hexagon}, player)))


def create_static_cxn_rule(or_reqs: List[List[str]], region_reqs: List[str], world: TunicWorld, player: int,
                           ability_unlocks: Dict[str, int]) -> Callable[[CollectionState], bool]:
    # items where we want to use a function instead of the name
    helpers: Dict[str, Callable[[CollectionState], bool]] = {
        "Stick": lambda state: has_stick(state, player),
        "Sword": lambda state: has_sword(state, player),
        "Prayer": lambda state: has_prayer(state, player, world.options, ability_unlocks),
        "Holy Cross": lambda state: has_hc(state, player, world.options, ability_unlocks),
    }

    requirements = {}
    for and_reqs in or_reqs:
        items_required = tuple(item for item in and_reqs if item not in helpers)
        helpers_required = tuple(helpers[item] for item in and_reqs if item in helpers)
        requirements[items_required] = helpers_required

    return lambda state: any(all((state.has_all(items_req, player), *[helper for helper in helpers_req],
                                  *[lambda: er_can_reach(region, world.multiworld, player) for region in region_reqs]))
                             for items_req, helpers_req in requirements.items())


def has_prayer(state: CollectionState, player: int, options: TunicOptions, ability_unlocks: Dict[str, int]) -> bool:
    return has_ability(state, player, prayer, options, ability_unlocks)


def has_hc(state: CollectionState, player: int, options: TunicOptions, ability_unlocks: Dict[str, int]) -> bool:
    return has_ability(state, player, holy_cross, options, ability_unlocks)


def has_stick(state: CollectionState, player: int) -> bool:
    return state.has("Stick", player, 1) or state.has("Sword Upgrade", player, 1)


def er_can_reach(region_name: str, multiworld: MultiWorld, player: int) -> Callable[[CollectionState], bool]:
    region = multiworld.get_region(region_name, player)
    return lambda state: state.can_reach(region)


# key is the region you have, value is the regions you get for having it
# so that we aren't being excessively careful with the granular regions
dependent_regions: Dict[Tuple[str, ...], List[str]] = {
    ("Overworld", "Overworld Belltower", "Overworld Laurels", "Overworld Southeast Cross Door", "Overworld Temple Door",
     "Overworld Fountain Cross Door", "Overworld Town Portal", "Overworld Spawn Portal"):
         ["Overworld", "Overworld Belltower", "Overworld Laurels", "Overworld Ruined Hall Door",
          "Overworld Southeast Cross Door", "Overworld Old House Door", "Overworld Temple Door",
          "Overworld Fountain Cross Door", "Overworld Town Portal", "Overworld Spawn Portal"],
    ("Old House Front",): ["Old House Front", "Old House Back"],
    ("Furnace Fuse", "Furnace Ladder Area", "Furnace Walking Path"):
        ["Furnace Fuse", "Furnace Ladder Area", "Furnace Walking Path"],
    ("Sealed Temple", "Sealed Temple Rafters"): ["Sealed Temple", "Sealed Temple Rafters"],
    ("Forest Belltower Upper",): ["Forest Belltower Upper", "Forest Belltower Main", "Forest Belltower Lower"],
    ("Forest Belltower Main",): ["Forest Belltower Main", "Forest Belltower Lower"],
    ("East Forest", "East Forest Dance Fox Spot", "East Forest Portal"):
        ["East Forest", "East Forest Dance Fox Spot", "East Forest Portal"],
    ("Forest Grave Path Main", "Forest Grave Path Upper"):
        ["Forest Grave Path Main", "Forest Grave Path Upper",
         "Forest Grave Path by Grave", "Forest Hero's Grave"],
    ("Forest Grave Path by Grave", "Forest Hero's Grave"):
        ["Forest Grave Path by Grave", "Forest Hero's Grave"],
    ("Bottom of the Well Front", "Bottom of the Well Back"): ["Bottom of the Well Front", "Bottom of the Well Back"],
    ("Dark Tomb Entry Point", "Dark Tomb Main", "Dark Tomb Dark Exit"):
        ["Dark Tomb Entry Point", "Dark Tomb Main", "Dark Tomb Dark Exit"],
    ("Dark Tomb Checkpoint", "Well Boss"): ["Dark Tomb Checkpoint", "Well Boss"],
    ("West Garden", "West Garden Laurels Exit", "West Garden after Boss", "West Garden Hero's Grave"):
        ["West Garden", "West Garden Laurels Exit", "West Garden after Boss", "West Garden Hero's Grave"],
    ("Ruined Atoll", "Ruined Atoll Lower Entry Area", "Ruined Atoll Frog Mouth", "Ruined Atoll Portal"):
        ["Ruined Atoll", "Ruined Atoll Lower Entry Area", "Ruined Atoll Frog Mouth", "Ruined Atoll Portal"],
    ("Frog's Domain",): ["Frog's Domain", "Frog's Domain Back"],
    ("Library Exterior Ladder", "Library Exterior Tree"):
        ["Library Exterior Ladder", "Library Exterior Tree"],
    ("Library Hall", "Library Hero's Grave"): ["Library Hall", "Library Hero's Grave"],
    ("Library Lab", "Library Lab Lower", "Library Portal"): ["Library Lab", "Library Lab Lower", "Library Portal"],
    ("Fortress Courtyard Upper",):
        ["Fortress Courtyard Upper", "Fortress Exterior from East Forest", "Fortress Exterior from Overworld",
         "Fortress Exterior near cave", "Fortress Courtyard"],
    ("Fortress Exterior from East Forest", "Fortress Exterior from Overworld",
     "Fortress Exterior near cave", "Fortress Courtyard"):
        ["Fortress Exterior from East Forest", "Fortress Exterior from Overworld",
         "Fortress Exterior near cave", "Fortress Courtyard"],
    ("Beneath the Vault Front", "Beneath the Vault Back"): ["Beneath the Vault Front", "Beneath the Vault Back"],
    ("Fortress East Shortcut Upper",): ["Fortress East Shortcut Upper", "Fortress East Shortcut Lower"],
    ("Eastern Vault Fortress", "Eastern Vault Fortress Gold Door"):
        ["Eastern Vault Fortress", "Eastern Vault Fortress Gold Door"],
    ("Fortress Grave Path", "Fortress Grave Path Dusty Entrance", "Fortress Hero's Grave"):
        ["Fortress Grave Path", "Fortress Grave Path Dusty Entrance", "Fortress Hero's Grave"],
    ("Fortress Arena", "Fortress Arena Portal"): ["Fortress Arena", "Fortress Arena Portal"],
    ("Lower Mountain", "Lower Mountain Stairs"): ["Lower Mountain", "Lower Mountain Stairs"],
    ("Monastery Front", "Monastery Back", "Monastery Hero's Grave"):
        ["Monastery Front", "Monastery Back", "Monastery Hero's Grave"],
    ("Quarry", "Quarry Portal", "Lower Quarry"): ["Quarry", "Quarry Portal", "Lower Quarry", "Lower Quarry Zig Door"],
    ("Monastery Rope",): ["Monastery Rope", "Quarry", "Quarry Portal", "Lower Quarry", "Lower Quarry Zig Door"],
    ("Rooted Ziggurat Upper Front", "Rooted Ziggurat Upper Back"):
        ["Rooted Ziggurat Upper Front", "Rooted Ziggurat Upper Back"],
    ("Rooted Ziggurat Middle Top",): ["Rooted Ziggurat Middle Top", "Rooted Ziggurat Middle Bottom"],
    ("Rooted Ziggurat Lower Front", "Rooted Ziggurat Lower Back", "Rooted Ziggurat Portal Room Entrance"):
        ["Rooted Ziggurat Lower Front", "Rooted Ziggurat Lower Back", "Rooted Ziggurat Portal Room Entrance"],
    ("Rooted Ziggurat Portal", "Rooted Ziggurat Portal Room Exit"):
        ["Rooted Ziggurat Portal", "Rooted Ziggurat Portal Room Exit"],
    ("Swamp", "Swamp to Cathedral Treasure Room", "Swamp to Cathedral Main Entrance"):
        ["Swamp", "Swamp to Cathedral Treasure Room", "Swamp to Cathedral Main Entrance"],
    ("Back of Swamp", "Back of Swamp Laurels Area", "Swamp Hero's Grave"):
        ["Back of Swamp", "Back of Swamp Laurels Area", "Swamp Hero's Grave"],
    ("Cathedral Gauntlet Checkpoint",):
        ["Cathedral Gauntlet Checkpoint", "Cathedral Gauntlet Exit", "Cathedral Gauntlet"],
    ("Far Shore", "Far Shore to Spawn", "Far Shore to East Forest", "Far Shore to Quarry",
     "Far Shore to Fortress", "Far Shore to Library", "Far Shore to West Garden"):
        ["Far Shore", "Far Shore to Spawn", "Far Shore to East Forest", "Far Shore to Quarry",
         "Far Shore to Fortress", "Far Shore to Library", "Far Shore to West Garden"]
}


def add_dependent_regions(region: str) -> Set[str]:
    region_set = set()
    for origin_regions, destination_regions in dependent_regions.items():
        if region in origin_regions:
            # if you matched something in the first set, you get the regions in its paired set
            region_set.update(destination_regions)
            return region_set
    # if you didn't match anything in the first sets, just gives you the region
    region_set = {region}
    return region_set
