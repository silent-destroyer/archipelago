from typing import Dict, List, Callable, Set, Tuple, TYPE_CHECKING
from BaseClasses import CollectionState, Region, ItemClassification, Item, Location
from .Locations import location_table
from .Rules import prayer, holy_cross, has_sword, has_ability, red_hexagon, blue_hexagon, green_hexagon, gold_hexagon
from .Options import TunicOptions
from .ER_Data import tunic_er_regions, portal_mapping, er_static_cxns, Portal, dependent_regions

if TYPE_CHECKING:
    from . import TunicWorld
else:
    TunicWorld = object


class TunicERItem(Item):
    game: str = "Tunic"


class TunicERLocation(Location):
    game: str = "Tunic"


def create_er_regions(world: TunicWorld) -> Dict[Portal, Portal]:
    regions: Dict[str, Region] = {}
    for region_name in tunic_er_regions:
        regions[region_name] = Region(region_name, world.player, world.multiworld)
    create_static_cxns(world, regions, world.ability_unlocks)

    for location_name, location_id in world.location_name_to_id.items():
        region = regions[location_table[location_name].er_region]
        location = TunicERLocation(world.player, location_name, location_id, region)
        region.locations.append(location)

    portal_pairs = pair_portals(world)
    create_randomized_entrances(portal_pairs, regions)

    for region in regions.values():
        world.multiworld.regions.append(region)

    return portal_pairs

######################
# Static Connections #
######################


# create the static connections between the more granular regions
def create_static_cxns(world: TunicWorld, regions: Dict[str, Region], ability_unlocks: Dict[str, int]) -> None:
    for cxn in er_static_cxns:
        player = world.player
        origin_region = regions[cxn.origin]
        dest_region = regions[cxn.destination]
        if cxn.reqs:
            origin_region.connect(dest_region, f"{cxn.origin} -> {cxn.destination}",
                                  create_static_cxn_rule(cxn.reqs, cxn.region_reqs,
                                                         world, player, ability_unlocks, regions))
            if cxn.reverse:
                dest_region.connect(origin_region, f"{cxn.destination} -> {cxn.origin}",
                                    create_static_cxn_rule(cxn.reqs, cxn.region_reqs,
                                                           world, player, ability_unlocks, regions))
        # if there's no requirements, just create the connection without the rules field
        else:
            origin_region.connect(dest_region, f"{cxn.origin} -> {cxn.destination}")
            if cxn.reverse:
                dest_region.connect(origin_region, f"{cxn.destination} -> {cxn.origin}")

    # create and connect to the victory spot manually for finer control over the victory condition
    spirit_arena = regions["Spirit Arena"]
    victory_region = regions["Spirit Arena Victory"]
    victory_location = TunicERLocation(world.player, "The Heir", None, victory_region)
    victory_location.place_locked_item(TunicERItem("Victory", ItemClassification.progression, None, world.player))
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)
    victory_region.locations.append(victory_location)
    spirit_arena.connect(victory_region, "Overcome the Heir",
                         lambda state: (state.has(gold_hexagon, player, world.options.hexagon_goal.value) if
                                        world.options.hexagon_quest else
                                        state.has_all({red_hexagon, green_hexagon, blue_hexagon}, player)))


def create_static_cxn_rule(or_reqs: List[List[str]], region_reqs: List[str], world: TunicWorld, player: int,
                           ability_unlocks: Dict[str, int], regions: Dict[str, Region]) \
        -> Callable[[CollectionState], bool]:
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
                                  *[lambda: er_can_reach(region, regions) for region in region_reqs]))
                             for items_req, helpers_req in requirements.items())


def has_prayer(state: CollectionState, player: int, options: TunicOptions, ability_unlocks: Dict[str, int]) -> bool:
    return has_ability(state, player, prayer, options, ability_unlocks)


def has_hc(state: CollectionState, player: int, options: TunicOptions, ability_unlocks: Dict[str, int]) -> bool:
    return has_ability(state, player, holy_cross, options, ability_unlocks)


def has_stick(state: CollectionState, player: int) -> bool:
    return state.has("Stick", player, 1) or state.has("Sword Upgrade", player, 1)


def er_can_reach(region_name: str, regions: Dict[str, Region]) -> Callable[[CollectionState], bool]:
    region = regions[region_name]
    return lambda state: state.can_reach(region)


##################
# Portal Pairing #
##################

# pairing off portals, starting with dead ends
def pair_portals(world: TunicWorld) -> Dict[Portal, Portal]:
    # separate the portals into dead ends and non-dead ends
    portal_pairs: Dict[Portal, Portal] = {}
    dead_ends: List[Portal] = []
    two_plus: List[Portal] = []

    # create separate lists for dead ends and non-dead ends
    for portal in portal_mapping:
        if tunic_er_regions[portal.region].dead_end:
            dead_ends.append(portal)
        else:
            two_plus.append(portal)

    connected_regions: Set[str] = set()
    # todo: better start region when/if implementing random start
    start_region = "Overworld"
    connected_regions.update(add_dependent_regions(start_region))

    # we want to start by making sure every region is accessible
    non_dead_end_regions = set()
    for region_name, region_info in tunic_er_regions.items():
        if not region_info.dead_end:
            non_dead_end_regions.add(region_name)

    world.random.shuffle(two_plus)
    check_success = 0
    portal1 = None
    portal2 = None
    while len(connected_regions) < len(non_dead_end_regions):
        # find a portal in an inaccessible region
        if check_success == 0:
            for portal in two_plus:
                if portal.region not in connected_regions:
                    # if there's risk of self-locking, start over
                    if gate_before_switch(portal, two_plus):
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
                    if gate_before_switch(portal, two_plus):
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
        portal2 = Portal(name="Shop Portal", region=f"Shop Entrance {i + 1}", destination="Previous Region_")
        portal_pairs[portal1] = portal2

    # connect dead ends to random non-dead ends
    # none of the key events are in dead ends, so we don't need to do gate_before_switch
    while len(dead_ends) > 0:
        portal1 = two_plus.pop()
        portal2 = dead_ends.pop()
        portal_pairs[portal1] = portal2

    # then randomly connect the remaining portals to each other
    # every region is accessible, so gate_before_switch is not necessary
    while len(two_plus) > 1:
        portal1 = two_plus.pop()
        portal2 = two_plus.pop()
        portal_pairs[portal1] = portal2

    if len(two_plus) == 1:
        raise Exception("two plus had an odd number of portals, investigate this")

    for portal1, portal2 in portal_pairs.items():
        world.multiworld.spoiler.set_entrance(portal1.name, portal2.name, "both", world.player)

    return portal_pairs


# loop through our list of paired portals and make two-way connections
def create_randomized_entrances(portal_pairs: Dict[Portal, Portal], regions: Dict[str, Region]) \
        -> None:
    for portal1, portal2 in portal_pairs.items():
        region1 = regions[portal1.region]
        region2 = regions[portal2.region]
        region1.connect(region2, f"{portal1.name} -> {portal2.name}")
        # prevent the logic from thinking you can get to any shop-connected region from the shop
        if portal2.name != "Shop":
            region2.connect(region1, f"{portal2.name} -> {portal1.name}")


# loop through the static connections, return regions you can reach from this region
def add_dependent_regions(region_name: str) -> Set[str]:
    region_set = set()
    for origin_regions, destination_regions in dependent_regions.items():
        if region_name in origin_regions:
            # if you matched something in the first set, you get the regions in its paired set
            region_set.update(destination_regions)
            return region_set
    # if you didn't match anything in the first sets, just gives you the region
    region_set = {region_name}
    return region_set


# we're checking if an event-locked portal is being placed before the regions where its key(s) is/are
# doing this ensures the keys will not be locked behind the event-locked portal
def gate_before_switch(check_portal: Portal, two_plus: List[Portal]) -> bool:
    # the western belltower cannot be locked since you can access it with laurels
    # so we only need to make sure the forest belltower isn't locked
    if check_portal.scene_destination == "Overworld Redux, Temple_main":
        i = 0
        for portal in two_plus:
            if portal.region == "Forest Belltower Upper":
                i += 1
                break
        if i == 1:
            return True

    # fortress big gold door needs 2 scenes and one of the two upper portals of the courtyard
    elif check_portal.scene_destination == "Fortress Main, Fortress Arena_":
        i = j = k = 0
        for portal in two_plus:
            if portal.region == "Forest Courtyard Upper":
                i += 1
            if portal.scene == "Fortress Basement":
                j += 1
            if portal.scene == "Fortress Main":
                k += 1
        if i == 2 or j == 2 or k == 6:
            return True

    # fortress teleporter needs only the left fuses
    elif check_portal.scene_destination in {"Fortress Arena, Transit_teleporter_spidertank",
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
    elif check_portal.scene_destination == "Swamp Redux 2, Cathedral Redux_main":
        i = 0
        for portal in two_plus:
            if portal.region == "Swamp":
                i += 1
        if i == 4:
            return True

    # Zig portal room exit needs Zig 3 to be accessible to hit the fuse
    elif check_portal.scene_destination == "ziggurat2020_FTRoom, ziggurat2020_3":
        i = 0
        for portal in two_plus:
            if portal.scene == "ziggurat2020_3":
                i += 1
        if i == 2:
            return True

    # Quarry teleporter needs you to hit the Darkwoods fuse
    # Since it's physically in Quarry, we don't need to check for it
    elif check_portal.scene_destination == "Quarry Redux, Transit_teleporter_quarry teleporter":
        i = 0
        for portal in two_plus:
            if portal.scene == "Darkwoods Tunnel":
                i += 1
        if i == 2:
            return True

    # Same as above, but Quarry isn't guaranteed here
    elif check_portal.scene_destination == "Transit, Quarry Redux_teleporter_quarry teleporter":
        i = j = 0
        for portal in two_plus:
            if portal.scene == "Darkwoods Tunnel":
                i += 1
            if portal.scene == "Quarry Redux":
                j += 1
        if i == 2 or j == 7:
            return True

    # Need Library fuse to use this teleporter
    elif check_portal.scene_destination == "Transit, Library Lab_teleporter_library teleporter":
        i = 0
        for portal in two_plus:
            if portal.scene == "Library Lab":
                i += 1
        if i == 3:
            return True

    # Need West Garden fuse to use this teleporter
    elif check_portal.scene_destination == "Transit, Archipelagos Redux_teleporter_archipelagos_teleporter":
        i = 0
        for portal in two_plus:
            if portal.scene == "Archipelagos Redux":
                i += 1
        if i == 7:
            return True

    # false means you're good to place the portal
    return False


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
