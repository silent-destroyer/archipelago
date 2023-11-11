from typing import Dict, TYPE_CHECKING
from worlds.generic.Rules import set_rule, forbid_item
from .Rules import has_ability, has_sword

if TYPE_CHECKING:
    from . import TunicWorld
else:
    TunicWorld = object

laurels = "Hero's Laurels"
grapple = "Magic Orb"
ice_dagger = "Magic Dagger"
fire_wand = "Magic Wand"
lantern = "Lantern"
fairies = "Fairy"
coins = "Golden Coin"
prayer = "Pages 24-25 (Prayer)"
holy_cross = "Pages 42-43 (Holy Cross)"
ice_rod = "Pages 52-53 (Ice Rod)"
key = "Key"
house_key = "Old House Key"
vault_key = "Fortress Vault Key"
mask = "Scavenger Mask"
red_hexagon = "Red Questagon"
green_hexagon = "Green Questagon"
blue_hexagon = "Blue Questagon"
gold_hexagon = "Gold Questagon"


def set_er_location_rules(world: TunicWorld, ability_unlocks: Dict[str, int]) -> None:
    player = world.player
    multiworld = world.multiworld
    options = world.options
    forbid_item(multiworld.get_location("Secret Gathering Place - 20 Fairy Reward", player), fairies, player)

    # Ability Shuffle Exclusive Rules
    set_rule(multiworld.get_location("East Forest - Dancing Fox Spirit Holy Cross", player),
             lambda state: has_ability(state, player, holy_cross, options, ability_unlocks))
    set_rule(multiworld.get_location("Forest Grave Path - Holy Cross Code by Grave", player),
             lambda state: has_ability(state, player, holy_cross, options, ability_unlocks))
    set_rule(multiworld.get_location("East Forest - Golden Obelisk Holy Cross", player),
             lambda state: has_ability(state, player, holy_cross, options, ability_unlocks))
    set_rule(multiworld.get_location("Bottom of the Well - [Powered Secret Room] Chest", player),
             lambda state: (has_ability(state, player, prayer, options, ability_unlocks)
             and state.can_reach(multiworld.get_region("Furnace Fuse", player))))
    set_rule(multiworld.get_location("West Garden - [North] Behind Holy Cross Door", player),
             lambda state: has_ability(state, player, holy_cross, options, ability_unlocks))
    set_rule(multiworld.get_location("Library Hall - Holy Cross Chest", player),
             lambda state: has_ability(state, player, holy_cross, options, ability_unlocks))
    set_rule(multiworld.get_location("Eastern Vault Fortress - [West Wing] Candles Holy Cross", player),
             lambda state: has_ability(state, player, holy_cross, options, ability_unlocks))
    set_rule(multiworld.get_location("West Garden - [Central Highlands] Holy Cross (Blue Lines)", player),
             lambda state: has_ability(state, player, holy_cross, options, ability_unlocks))
    set_rule(multiworld.get_location("Quarry - [Back Entrance] Bushes Holy Cross", player),
             lambda state: has_ability(state, player, holy_cross, options, ability_unlocks))
    set_rule(multiworld.get_location("Cathedral - Secret Legend Trophy Chest", player),
             lambda state: has_ability(state, player, holy_cross, options, ability_unlocks))

    # Overworld
    set_rule(multiworld.get_location("Overworld - [Southwest] Grapple Chest Over Walkway", player),
             lambda state: state.has_any({grapple, laurels}, player))
    set_rule(multiworld.get_location("Overworld - [Southwest] West Beach Guarded By Turret 2", player),
             lambda state: state.has_any({grapple, laurels}, player))
    set_rule(multiworld.get_location("Far Shore - Secret Chest", player),
             lambda state: state.has(laurels, player))
    set_rule(multiworld.get_location("Old House - Holy Cross Chest", player),
             lambda state: has_ability(state, player, holy_cross, options, ability_unlocks))
    set_rule(multiworld.get_location("Overworld - [East] Grapple Chest", player),
             lambda state: state.has(grapple, player))
    set_rule(multiworld.get_location("Sealed Temple - Holy Cross Chest", player),
             lambda state: has_ability(state, player, holy_cross, options, ability_unlocks))
    set_rule(multiworld.get_location("Caustic Light Cave - Holy Cross Chest", player),
             lambda state: has_ability(state, player, holy_cross, options, ability_unlocks))
    set_rule(multiworld.get_location("Cube Cave - Holy Cross Chest", player),
             lambda state: has_ability(state, player, holy_cross, options, ability_unlocks))
    set_rule(multiworld.get_location("Old House - Holy Cross Door Page", player),
             lambda state: has_ability(state, player, holy_cross, options, ability_unlocks))
    set_rule(multiworld.get_location("Maze Cave - Maze Room Holy Cross", player),
             lambda state: has_ability(state, player, holy_cross, options, ability_unlocks))
    set_rule(multiworld.get_location("Old House - Holy Cross Chest", player),
             lambda state: has_ability(state, player, holy_cross, options, ability_unlocks))
    set_rule(multiworld.get_location("Patrol Cave - Holy Cross Chest", player),
             lambda state: has_ability(state, player, holy_cross, options, ability_unlocks))
    set_rule(multiworld.get_location("Ruined Passage - Holy Cross Chest", player),
             lambda state: has_ability(state, player, holy_cross, options, ability_unlocks))
    set_rule(multiworld.get_location("Hourglass Cave - Holy Cross Chest", player),
             lambda state: has_ability(state, player, holy_cross, options, ability_unlocks))
    set_rule(multiworld.get_location("Secret Gathering Place - Holy Cross Chest", player),
             lambda state: has_ability(state, player, holy_cross, options, ability_unlocks))
    set_rule(multiworld.get_location("Secret Gathering Place - 10 Fairy Reward", player),
             lambda state: state.has(fairies, player, 10))
    set_rule(multiworld.get_location("Secret Gathering Place - 20 Fairy Reward", player),
             lambda state: state.has(fairies, player, 20))
    set_rule(multiworld.get_location("Coins in the Well - 3 Coins", player), lambda state: state.has(coins, player, 3))
    set_rule(multiworld.get_location("Coins in the Well - 6 Coins", player), lambda state: state.has(coins, player, 6))
    set_rule(multiworld.get_location("Coins in the Well - 10 Coins", player),
             lambda state: state.has(coins, player, 10))
    set_rule(multiworld.get_location("Coins in the Well - 15 Coins", player),
             lambda state: state.has(coins, player, 15))

    # East Forest
    set_rule(multiworld.get_location("East Forest - Lower Grapple Chest", player),
             lambda state: state.has(grapple, player))
    set_rule(multiworld.get_location("East Forest - Lower Dash Chest", player),
             lambda state: state.has_all({grapple, laurels}, player))
    set_rule(multiworld.get_location("East Forest - Ice Rod Grapple Chest", player), lambda state: (
            state.has_all({grapple, ice_dagger, fire_wand}, player) and
            has_ability(state, player, ice_rod, options, ability_unlocks)))

    # West Garden
    set_rule(multiworld.get_location("West Garden - [North] Across From Page Pickup", player),
             lambda state: state.has(laurels, player))
    set_rule(multiworld.get_location("West Garden - [West] In Flooded Walkway", player),
             lambda state: state.has(laurels, player))
    set_rule(multiworld.get_location("West Garden - [West Lowlands] Tree Holy Cross Chest", player),
             lambda state: state.has(laurels, player) and has_ability(state, player, holy_cross, options,
                                                                      ability_unlocks))
    set_rule(multiworld.get_location("West Garden - [East Lowlands] Page Behind Ice Dagger House", player),
             lambda state: state.has(laurels, player))
    set_rule(multiworld.get_location("West Garden - [Central Lowlands] Below Left Walkway", player),
             lambda state: state.has(laurels, player))

    # Ruined Atoll
    set_rule(multiworld.get_location("Ruined Atoll - [West] Near Kevin Block", player),
             lambda state: state.has(laurels, player))
    set_rule(multiworld.get_location("Ruined Atoll - [East] Locked Room Lower Chest", player),
             lambda state: state.has_any({laurels, key}, player))
    set_rule(multiworld.get_location("Ruined Atoll - [East] Locked Room Upper Chest", player),
             lambda state: state.has_any({laurels, key}, player))

    # Frog's Domain
    set_rule(multiworld.get_location("Frog's Domain - Side Room Grapple Secret", player),
             lambda state: state.has_any({grapple, laurels}, player))
    set_rule(multiworld.get_location("Frog's Domain - Grapple Above Hot Tub", player),
             lambda state: state.has_any({grapple, laurels}, player))
    set_rule(multiworld.get_location("Frog's Domain - Escape Chest", player),
             lambda state: state.has_any({grapple, laurels}, player))

    # Eastern Vault Fortress
    set_rule(multiworld.get_location("Fortress Arena - Hexagon Red", player),
             lambda state: state.has(vault_key, player))

    # Beneath the Vault
    set_rule(multiworld.get_location("Beneath the Fortress - Bridge", player),
             lambda state: state.has_group("melee weapons", player, 1) or state.has_any({laurels, fire_wand}, player))

    # Quarry
    set_rule(multiworld.get_location("Quarry - [Central] Above Ladder Dash Chest", player),
             lambda state: state.has(laurels, player))

    # Ziggurat
    set_rule(multiworld.get_location("Rooted Ziggurat Lower - After Guarded Fuse", player),
             lambda state: has_sword(state, player) and has_ability(state, player, prayer, options, ability_unlocks))

    # Bosses
    set_rule(multiworld.get_location("Fortress Arena - Siege Engine/Vault Key Pickup", player),
             lambda state: has_sword(state, player))
    set_rule(multiworld.get_location("Librarian - Hexagon Green", player),
             lambda state: has_sword(state, player))
    set_rule(multiworld.get_location("Rooted Ziggurat Lower - Hexagon Blue", player),
             lambda state: has_sword(state, player))

    # Swamp
    set_rule(multiworld.get_location("Cathedral Gauntlet - Gauntlet Reward", player),
             lambda state: state.has(fire_wand, player) and has_sword(state, player))
    set_rule(multiworld.get_location("Swamp - [Entrance] Above Entryway", player),
             lambda state: state.has(laurels, player))
    set_rule(multiworld.get_location("Swamp - [South Graveyard] Upper Walkway Dash Chest", player),
             lambda state: state.has(laurels, player))
    set_rule(multiworld.get_location("Swamp - [South Graveyard] 4 Orange Skulls", player),
             lambda state: has_sword(state, player))

    # Hero's Grave
    set_rule(multiworld.get_location("Hero's Grave - Tooth Relic", player),
             lambda state: state.has(laurels, player))
    set_rule(multiworld.get_location("Hero's Grave - Mushroom Relic", player),
             lambda state: state.has(laurels, player))
    set_rule(multiworld.get_location("Hero's Grave - Ash Relic", player),
             lambda state: state.has(laurels, player))
    set_rule(multiworld.get_location("Hero's Grave - Flowers Relic", player),
             lambda state: state.has(laurels, player))
    set_rule(multiworld.get_location("Hero's Grave - Effigy Relic", player),
             lambda state: state.has(laurels, player))
    set_rule(multiworld.get_location("Hero's Grave - Feathers Relic", player),
             lambda state: state.has(laurels, player))
