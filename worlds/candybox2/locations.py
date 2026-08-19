from collections.abc import Callable
from enum import StrEnum
from typing import TYPE_CHECKING, NamedTuple

from BaseClasses import Location

if TYPE_CHECKING:
    from . import CandyBox2World


class CandyBox2LocationData(NamedTuple):
    id: int | None = None
    is_included: Callable[["CandyBox2World"], bool] = lambda _: True


class CandyBox2Location(Location):
    game: str = "Candy Box 2"


class CandyBox2LocationName(StrEnum):
    HP_BAR_UNLOCK = "Candy Box: HP Bar Unlock"
    DISAPPOINTED_EMOTE_CHOCOLATE_BAR = "Candy Box: Throw 1630 candies"
    VILLAGE_SHOP_TOP_LOLLIPOP = "Shop: Top Lollipop"
    VILLAGE_SHOP_CENTRE_LOLLIPOP = "Shop: Centre Lollipop"
    VILLAGE_SHOP_BOTTOM_LOLLIPOP = "Shop: Bottom Lollipop"
    VILLAGE_SHOP_CHOCOLATE_BAR = "Shop: Chocolate Bar"
    VILLAGE_SHOP_TIME_RING = "Shop: Time Ring"
    VILLAGE_SHOP_CANDY_MERCHANTS_HAT = "Shop: Candy Merchant's Hat"
    VILLAGE_SHOP_LEATHER_GLOVES = "Shop: Leather Gloves"
    VILLAGE_SHOP_LEATHER_BOOTS = "Shop: Leather Boots"
    VILLAGE_HOUSE_LOLLIPOP_ON_THE_BOOKSHELF = "Fifth House: Lollipop on bookshelf"
    VILLAGE_HOUSE_LOLLIPOP_IN_THE_BOOKSHELF = "Fifth House: Lollipop in bookshelf"
    VILLAGE_HOUSE_LOLLIPOP_UNDER_THE_RUG = "Fifth House: Lollipop under rug"
    CELLAR_QUEST_CLEARED = "Cellar Quest: Quest Cleared"
    DESERT_QUEST_CLEARED = "Desert Quest: Quest Cleared"
    DESERT_BIRD_FEATHER_ACQUIRED = "Desert Quest: Get Desert Bird Feather"
    TROLL_DEFEATED = "Bridge Quest: Troll Defeated"
    THE_TROLLS_BLUDGEON_ACQUIRED = "Bridge Quest: Get Troll's Bludgeon"
    CAVE_EXIT = "Cave: Exit"
    CAVE_CHOCOLATE_BAR = "Cave: Chocolate Bar"
    CAVE_HEART_PLUG = "Cave: Heart Plug"
    FOREST_QUEST_CLEARED = "Forest Quest: Quest Cleared"
    CASTLE_ENTRANCE_QUEST_CLEARED = "Castle Entrance Quest: Quest Cleared"
    KNIGHT_BODY_ARMOUR_ACQUIRED = "Castle Entrance Quest: Get Knight Body Armour"
    GIANT_NOUGAT_MONSTER_DEFEATED = "Nougat Monster Quest: Giant Nougat Monster Defeated"
    SORCERESS_HUT_LOLLIPOP_ON_THE_SHELVES = "Sorceress' Hut: Inconspicuous Lollipop"
    SORCERESS_HUT_BEGINNERS_GRIMOIRE = "Sorceress' Hut: Beginner's Grimoire"
    SORCERESS_HUT_ADVANCED_GRIMOIRE = "Sorceress' Hut: Advanced Grimoire"
    SORCERESS_HUT_BEGINNERS_GRIMOIRE_FIREBALL = "Sorceress' Hut: Beginner's Grimoire - Fireball"
    SORCERESS_HUT_BEGINNERS_GRIMOIRE_ACID_RAIN = "Sorceress' Hut: Beginner's Grimoire - Acid Rain"
    SORCERESS_HUT_BEGINNERS_GRIMOIRE_TELEPORT = "Sorceress' Hut: Beginner's Grimoire - Teleport"
    SORCERESS_HUT_ADVANCED_GRIMOIRE_ERASE_MAGIC = "Sorceress' Hut: Advanced Grimoire - Erase Magic"
    SORCERESS_HUT_ADVANCED_GRIMOIRE_THORNS_SHIELD = "Sorceress' Hut: Advanced Grimoire - Thorns Shield"
    SORCERESS_HUT_CAULDRON = "Sorceress' Hut: Cauldron"
    SORCERESS_HUT_HAT = "Sorceress' Hut: Sorceress' Hat"
    OCTOPUS_KING_DEFEATED = "Octopus King Quest: Octopus King Defeated"
    MONKEY_WIZARD_DEFEATED = "Monkey Wizard Quest: Monkey Wizard Defeated"
    EGG_ROOM_QUEST_CLEARED = "Egg Room Quest: Chest Opened"
    DEVIL_DEFEATED = "Hell Quest: Devil Defeated"
    THE_DEVELOPER_DEFEATED = "Developer Quest: The Developer Defeated"
    SOLVE_CYCLOPS_PUZZLE = "Lighthouse: Solve Cyclops Puzzle"
    VILLAGE_FORGE_LOLLIPOP_ON_EXHAUST_CHUTE = "Forge: Inconspicuous Lollipop"
    VILLAGE_FORGE_BUY_WOODEN_SWORD = "Forge: Wooden Sword"
    VILLAGE_FORGE_BUY_IRON_AXE = "Forge: Iron Axe"
    VILLAGE_FORGE_BUY_POLISHED_SILVER_SWORD = "Forge: Polished Silver Sword"
    VILLAGE_FORGE_BUY_LIGHTWEIGHT_BODY_ARMOUR = "Forge: Lightweight Body Armour"
    VILLAGE_FORGE_BUY_SCYTHE = "Forge: Scythe"
    ENCHANT_RED_ENCHANTED_GLOVES = "Wishing Well: Red Enchanted Gloves"
    ENCHANT_PINK_ENCHANTED_GLOVES = "Wishing Well: Pink Enchanted Gloves"
    ENCHANT_SUMMONING_TRIBAL_SPEAR = "Wishing Well: Summoning Tribal Spear"
    ENCHANT_ENCHANTED_MONKEY_WIZARD_STAFF = "Wishing Well: Enchanted Monkey Wizard Staff"
    ENCHANT_ENCHANTED_KNIGHT_BODY_ARMOUR = "Wishing Well: Enchanted Knight Body Armour"
    ENCHANT_OCTOPUS_KING_CROWN_WITH_JASPERS = "Wishing Well: Octopus King Crown with Jaspers"
    ENCHANT_OCTOPUS_KING_CROWN_WITH_OBSIDIAN = "Wishing Well: Octopus King Crown with Obsidian"
    ENCHANT_GIANT_SPOON_OF_DOOM = "Wishing Well: Giant Spoon of Doom"
    THE_HOLE_TRIBAL_WARRIOR_DEFEATED = "Hole: Tribal Warrior Defeated"
    THE_HOLE_DESERT_FORTRESS_KEY_ACQUIRED = "Hole: Right Chest Opened"
    THE_HOLE_HEART_PENDANT_ACQUIRED = "Hole: Top Chest Opened"
    THE_HOLE_BLACK_MAGIC_GRIMOIRE_ACQUIRED = "Hole: Left Chest Opened"
    THE_HOLE_BLACK_MAGIC_GRIMOIRE_ACQUIRED_OBSIDIAN_WALL = "Hole: Left Chest Opened - Obsidian Wall"
    THE_HOLE_BLACK_MAGIC_GRIMOIRE_ACQUIRED_BLACK_DEMONS = "Hole: Left Chest Opened - Black Demons"
    THE_HOLE_FOUR_CHOCOLATE_BARS_ACQUIRED = "Hole: Bottom Chest Opened"
    TEAPOT_DEFEATED = "Teapot Quest: Teapot Defeated"
    XINOPHERYDON_DEFEATED = "Xinopherydon Quest: Xinopherydon Defeated"
    XINOPHERYDON_QUEST_UNICORN_HORN_ACQUIRED = "Xinopherydon Quest: Unicorn Horn Acquired"
    ROCKET_BOOTS_ACQUIRED = "Ledge Quest: Chest Opened"
    PITCHFORK_ACQUIRED = "Castle Dark Room: Get Pitchfork"
    THE_SQUIRRELS_FIRST_QUESTION = "A Tree: The Squirrel's first question"
    THE_SQUIRRELS_SECOND_QUESTION = "A Tree: The Squirrel's second question"
    THE_SQUIRRELS_THIRD_QUESTION = "A Tree: The Squirrel's third question"
    THE_SQUIRRELS_FOURTH_QUESTION = "A Tree: The Squirrel's fourth question"
    THE_SQUIRRELS_FIFTH_QUESTION = "A Tree: The Squirrel's fifth question"
    THE_SQUIRRELS_PUZZLE = "A Tree: The Squirrel's puzzle"
    THE_SPONGE_ACQUIRED = "The Sea: Get Sponge"
    THE_SHELL_POWDER_ACQUIRED = "The Sea: Get Shell Powder"
    THE_RED_FIN_ACQUIRED = "The Sea: Get Red Fin"
    THE_GREEN_FIN_ACQUIRED = "The Sea: Get Green Fin"
    THE_PURPLE_FIN_ACQUIRED = "The Sea: Get Purple Fin"
    X_MARKS_THE_SPOT = "Secret Treasure Spot: X marks the spot!"
    LOCKED_CANDY_BOX_ACQUIRED = "Lonely House: Locked Candy Box Acquired"
    YOURSELF_DEFEATED = "X Potion Quest: Yourself Defeated"
    BAKE_PAIN_AU_CHOCOLAT_1 = "Castle Bakehouse: Bake Pain au Chocolat 1"
    BAKE_PAIN_AU_CHOCOLAT_2 = "Castle Bakehouse: Bake Pain au Chocolat 2"
    BAKE_PAIN_AU_CHOCOLAT_3 = "Castle Bakehouse: Bake Pain au Chocolat 3"
    BAKE_PAIN_AU_CHOCOLAT_4 = "Castle Bakehouse: Bake Pain au Chocolat 4"
    BAKE_PAIN_AU_CHOCOLAT_5 = "Castle Bakehouse: Bake Pain au Chocolat 5"
    POGO_STICK = "The Mountains: Pogo Stick"
    LOLLIPOP_FARM_EXTRA_1 = "Lollipop Farm: Planted 30000 Lollipops"
    LOLLIPOP_FARM_EXTRA_2 = "Lollipop Farm: Planted 40000 Lollipops"
    LOLLIPOP_FARM_EXTRA_3 = "Lollipop Farm: Planted 50000 Lollipops"
    LOLLIPOP_FARM_EXTRA_4 = "Lollipop Farm: Planted 60000 Lollipops"
    LOLLIPOP_FARM_EXTRA_5 = "Lollipop Farm: Planted 70000 Lollipops"
    LOLLIPOP_FARM_EXTRA_6 = "Lollipop Farm: Planted 80000 Lollipops"
    LOLLIPOP_FARM_EXTRA_7 = "Lollipop Farm: Planted 90000 Lollipops"
    LOLLIPOP_FARM_EXTRA_8 = "Lollipop Farm: Planted 100000 Lollipops"
    THE_SEA_EXTRA_1 = "The Sea: Travel 50m"
    THE_SEA_EXTRA_2 = "The Sea: Travel 100m"
    THE_SEA_EXTRA_3 = "The Sea: Travel 150m"
    THE_SEA_EXTRA_4 = "The Sea: Travel 200m"
    THE_SEA_EXTRA_5 = "The Sea: Travel 250m"
    THE_SEA_EXTRA_6 = "The Sea: Travel 300m"
    THE_SEA_EXTRA_7 = "The Sea: Travel 350m"
    THE_SEA_EXTRA_8 = "The Sea: Travel 400m"
    THE_SEA_EXTRA_9 = "The Sea: Travel 450m"
    THE_SEA_EXTRA_10 = "The Sea: Travel 500m"
    THE_SEA_EXTRA_11 = "The Sea: Travel 550m"
    THE_SEA_EXTRA_12 = "The Sea: Travel 600m"
    THE_SEA_EXTRA_13 = "The Sea: Travel 650m"
    THE_SEA_EXTRA_14 = "The Sea: Travel 700m"
    THE_SEA_EXTRA_15 = "The Sea: Travel 750m"
    THE_SEA_EXTRA_16 = "The Sea: Travel 800m"
    THE_SEA_EXTRA_17 = "The Sea: Travel 850m"
    THE_SEA_EXTRA_18 = "The Sea: Travel 900m"
    THE_SEA_EXTRA_19 = "The Sea: Travel 950m"
    THE_SEA_EXTRA_20 = "The Sea: Travel 1000m"
    THE_SEA_EXTRA_21 = "The Sea: Travel 1050m"
    THE_SEA_EXTRA_22 = "The Sea: Travel 1100m"
    THE_SEA_EXTRA_23 = "The Sea: Travel 1150m"
    THE_SEA_EXTRA_24 = "The Sea: Travel 1200m"
    THE_SEA_EXTRA_25 = "The Sea: Travel 1250m"
    THE_SEA_EXTRA_26 = "The Sea: Travel 1300m"
    THE_SEA_EXTRA_27 = "The Sea: Travel 1350m"
    THE_SEA_EXTRA_28 = "The Sea: Travel 1400m"
    THE_SEA_EXTRA_29 = "The Sea: Travel 1450m"
    THE_SEA_EXTRA_30 = "The Sea: Travel 1500m"
    THE_SEA_EXTRA_31 = "The Sea: Travel 1550m"
    THE_SEA_EXTRA_32 = "The Sea: Travel 1600m"
    THE_SEA_EXTRA_33 = "The Sea: Travel 1650m"
    THE_SEA_EXTRA_34 = "The Sea: Travel 1700m"
    THE_SEA_EXTRA_35 = "The Sea: Travel 1750m"
    THE_SEA_EXTRA_36 = "The Sea: Travel 1800m"
    THE_SEA_EXTRA_37 = "The Sea: Travel 1850m"
    THE_SEA_EXTRA_38 = "The Sea: Travel 1900m"
    THE_SEA_EXTRA_39 = "The Sea: Travel 1950m"
    THE_SEA_EXTRA_40 = "The Sea: Travel 2000m"
    THE_SEA_EXTRA_41 = "The Sea: Travel 2050m"
    THE_SEA_EXTRA_42 = "The Sea: Travel 2100m"
    THE_SEA_EXTRA_43 = "The Sea: Travel 2150m"
    THE_SEA_EXTRA_44 = "The Sea: Travel 2200m"
    THE_SEA_EXTRA_45 = "The Sea: Travel 2250m"
    THE_SEA_EXTRA_46 = "The Sea: Travel 2300m"
    THE_SEA_EXTRA_47 = "The Sea: Travel 2350m"
    THE_SEA_EXTRA_48 = "The Sea: Travel 2400m"
    THE_SEA_EXTRA_49 = "The Sea: Travel 2450m"
    THE_SEA_EXTRA_50 = "The Sea: Travel 2500m"
    THE_SEA_EXTRA_51 = "The Sea: Travel 2550m"
    THE_SEA_EXTRA_52 = "The Sea: Travel 2600m"
    THE_SEA_EXTRA_53 = "The Sea: Travel 2650m"
    THE_SEA_EXTRA_54 = "The Sea: Travel 2700m"
    THE_SEA_EXTRA_55 = "The Sea: Travel 2750m"
    THE_SEA_EXTRA_56 = "The Sea: Travel 2800m"
    THE_SEA_EXTRA_57 = "The Sea: Travel 2850m"
    THE_SEA_EXTRA_58 = "The Sea: Travel 2900m"
    THE_SEA_EXTRA_59 = "The Sea: Travel 2950m"
    THE_SEA_EXTRA_60 = "The Sea: Travel 3000m"
    THE_SEA_EXTRA_61 = "The Sea: Travel 3050m"
    THE_SEA_EXTRA_62 = "The Sea: Travel 3100m"
    THE_SEA_EXTRA_63 = "The Sea: Travel 3150m"
    THE_SEA_EXTRA_64 = "The Sea: Travel 3200m"
    THE_SEA_EXTRA_65 = "The Sea: Travel 3250m"
    THE_SEA_EXTRA_66 = "The Sea: Travel 3300m"
    THE_SEA_EXTRA_67 = "The Sea: Travel 3350m"
    THE_SEA_EXTRA_68 = "The Sea: Travel 3400m"
    THE_SEA_EXTRA_69 = "The Sea: Travel 3450m"
    THE_SEA_EXTRA_70 = "The Sea: Travel 3500m"
    THE_SEA_EXTRA_71 = "The Sea: Travel 3550m"
    THE_SEA_EXTRA_72 = "The Sea: Travel 3600m"
    THE_SEA_EXTRA_73 = "The Sea: Travel 3650m"
    THE_SEA_EXTRA_74 = "The Sea: Travel 3700m"
    THE_SEA_EXTRA_75 = "The Sea: Travel 3750m"
    THE_SEA_EXTRA_76 = "The Sea: Travel 3800m"
    THE_SEA_EXTRA_77 = "The Sea: Travel 3850m"
    THE_SEA_EXTRA_78 = "The Sea: Travel 3900m"
    THE_SEA_EXTRA_79 = "The Sea: Travel 3950m"
    THE_SEA_EXTRA_80 = "The Sea: Travel 4000m"


location_descriptions: dict[CandyBox2LocationName, str] = {CandyBox2LocationName.HP_BAR_UNLOCK: ""}

locations: dict[CandyBox2LocationName, CandyBox2LocationData] = {
    CandyBox2LocationName.HP_BAR_UNLOCK: CandyBox2LocationData(1),
    CandyBox2LocationName.DISAPPOINTED_EMOTE_CHOCOLATE_BAR: CandyBox2LocationData(2),
    CandyBox2LocationName.VILLAGE_SHOP_TOP_LOLLIPOP: CandyBox2LocationData(100),
    CandyBox2LocationName.VILLAGE_SHOP_CENTRE_LOLLIPOP: CandyBox2LocationData(101),
    CandyBox2LocationName.VILLAGE_SHOP_BOTTOM_LOLLIPOP: CandyBox2LocationData(102),
    CandyBox2LocationName.VILLAGE_SHOP_CHOCOLATE_BAR: CandyBox2LocationData(103),
    CandyBox2LocationName.VILLAGE_SHOP_TIME_RING: CandyBox2LocationData(104),
    CandyBox2LocationName.VILLAGE_SHOP_CANDY_MERCHANTS_HAT: CandyBox2LocationData(105),
    CandyBox2LocationName.VILLAGE_SHOP_LEATHER_GLOVES: CandyBox2LocationData(106),
    CandyBox2LocationName.VILLAGE_SHOP_LEATHER_BOOTS: CandyBox2LocationData(107),
    CandyBox2LocationName.VILLAGE_HOUSE_LOLLIPOP_ON_THE_BOOKSHELF: CandyBox2LocationData(200),
    CandyBox2LocationName.VILLAGE_HOUSE_LOLLIPOP_IN_THE_BOOKSHELF: CandyBox2LocationData(201),
    CandyBox2LocationName.VILLAGE_HOUSE_LOLLIPOP_UNDER_THE_RUG: CandyBox2LocationData(202),
    CandyBox2LocationName.CELLAR_QUEST_CLEARED: CandyBox2LocationData(300),
    CandyBox2LocationName.DESERT_QUEST_CLEARED: CandyBox2LocationData(1100),
    CandyBox2LocationName.DESERT_BIRD_FEATHER_ACQUIRED: CandyBox2LocationData(1101),
    CandyBox2LocationName.TROLL_DEFEATED: CandyBox2LocationData(1200),
    CandyBox2LocationName.THE_TROLLS_BLUDGEON_ACQUIRED: CandyBox2LocationData(1201),
    CandyBox2LocationName.CAVE_EXIT: CandyBox2LocationData(1300),
    CandyBox2LocationName.CAVE_CHOCOLATE_BAR: CandyBox2LocationData(1301),
    CandyBox2LocationName.CAVE_HEART_PLUG: CandyBox2LocationData(1302),
    CandyBox2LocationName.FOREST_QUEST_CLEARED: CandyBox2LocationData(1400),
    CandyBox2LocationName.CASTLE_ENTRANCE_QUEST_CLEARED: CandyBox2LocationData(1500),
    CandyBox2LocationName.KNIGHT_BODY_ARMOUR_ACQUIRED: CandyBox2LocationData(1501),
    CandyBox2LocationName.GIANT_NOUGAT_MONSTER_DEFEATED: CandyBox2LocationData(1600),
    CandyBox2LocationName.SORCERESS_HUT_LOLLIPOP_ON_THE_SHELVES: CandyBox2LocationData(1800),
    CandyBox2LocationName.SORCERESS_HUT_BEGINNERS_GRIMOIRE: CandyBox2LocationData(
        1801, lambda world: grimoire_location_count(world)
    ),
    CandyBox2LocationName.SORCERESS_HUT_ADVANCED_GRIMOIRE: CandyBox2LocationData(
        1802, lambda world: grimoire_location_count(world)
    ),
    CandyBox2LocationName.SORCERESS_HUT_CAULDRON: CandyBox2LocationData(1803),
    CandyBox2LocationName.SORCERESS_HUT_HAT: CandyBox2LocationData(1804),
    CandyBox2LocationName.SORCERESS_HUT_BEGINNERS_GRIMOIRE_ACID_RAIN: CandyBox2LocationData(
        1805, lambda world: spell_location_count(world)
    ),
    CandyBox2LocationName.SORCERESS_HUT_BEGINNERS_GRIMOIRE_FIREBALL: CandyBox2LocationData(
        1806, lambda world: spell_location_count(world)
    ),
    CandyBox2LocationName.SORCERESS_HUT_BEGINNERS_GRIMOIRE_TELEPORT: CandyBox2LocationData(
        1807, lambda world: spell_location_count(world)
    ),
    CandyBox2LocationName.SORCERESS_HUT_ADVANCED_GRIMOIRE_ERASE_MAGIC: CandyBox2LocationData(
        1808, lambda world: spell_location_count(world)
    ),
    CandyBox2LocationName.SORCERESS_HUT_ADVANCED_GRIMOIRE_THORNS_SHIELD: CandyBox2LocationData(
        1809, lambda world: spell_location_count(world)
    ),
    CandyBox2LocationName.OCTOPUS_KING_DEFEATED: CandyBox2LocationData(1900),
    CandyBox2LocationName.MONKEY_WIZARD_DEFEATED: CandyBox2LocationData(2000),
    CandyBox2LocationName.EGG_ROOM_QUEST_CLEARED: CandyBox2LocationData(2100),
    CandyBox2LocationName.DEVIL_DEFEATED: CandyBox2LocationData(2300),
    CandyBox2LocationName.THE_DEVELOPER_DEFEATED: CandyBox2LocationData(2400),
    CandyBox2LocationName.SOLVE_CYCLOPS_PUZZLE: CandyBox2LocationData(2500),
    CandyBox2LocationName.VILLAGE_FORGE_LOLLIPOP_ON_EXHAUST_CHUTE: CandyBox2LocationData(2600),
    CandyBox2LocationName.VILLAGE_FORGE_BUY_WOODEN_SWORD: CandyBox2LocationData(2601),
    CandyBox2LocationName.VILLAGE_FORGE_BUY_IRON_AXE: CandyBox2LocationData(2700),
    CandyBox2LocationName.VILLAGE_FORGE_BUY_POLISHED_SILVER_SWORD: CandyBox2LocationData(2800),
    CandyBox2LocationName.VILLAGE_FORGE_BUY_LIGHTWEIGHT_BODY_ARMOUR: CandyBox2LocationData(2900),
    CandyBox2LocationName.VILLAGE_FORGE_BUY_SCYTHE: CandyBox2LocationData(3000),
    CandyBox2LocationName.ENCHANT_RED_ENCHANTED_GLOVES: CandyBox2LocationData(3100),
    CandyBox2LocationName.ENCHANT_PINK_ENCHANTED_GLOVES: CandyBox2LocationData(3101),
    CandyBox2LocationName.ENCHANT_SUMMONING_TRIBAL_SPEAR: CandyBox2LocationData(3200),
    CandyBox2LocationName.ENCHANT_ENCHANTED_MONKEY_WIZARD_STAFF: CandyBox2LocationData(3300),
    CandyBox2LocationName.ENCHANT_ENCHANTED_KNIGHT_BODY_ARMOUR: CandyBox2LocationData(3400),
    CandyBox2LocationName.ENCHANT_OCTOPUS_KING_CROWN_WITH_JASPERS: CandyBox2LocationData(3500),
    CandyBox2LocationName.ENCHANT_OCTOPUS_KING_CROWN_WITH_OBSIDIAN: CandyBox2LocationData(3501),
    CandyBox2LocationName.ENCHANT_GIANT_SPOON_OF_DOOM: CandyBox2LocationData(3600),
    CandyBox2LocationName.THE_HOLE_TRIBAL_WARRIOR_DEFEATED: CandyBox2LocationData(3700),
    CandyBox2LocationName.THE_HOLE_DESERT_FORTRESS_KEY_ACQUIRED: CandyBox2LocationData(3701),
    CandyBox2LocationName.THE_HOLE_HEART_PENDANT_ACQUIRED: CandyBox2LocationData(3702),
    CandyBox2LocationName.THE_HOLE_BLACK_MAGIC_GRIMOIRE_ACQUIRED: CandyBox2LocationData(
        3703, lambda world: grimoire_location_count(world)
    ),
    CandyBox2LocationName.THE_HOLE_FOUR_CHOCOLATE_BARS_ACQUIRED: CandyBox2LocationData(3704),
    CandyBox2LocationName.THE_HOLE_BLACK_MAGIC_GRIMOIRE_ACQUIRED_OBSIDIAN_WALL: CandyBox2LocationData(
        3705, lambda world: spell_location_count(world)
    ),
    CandyBox2LocationName.THE_HOLE_BLACK_MAGIC_GRIMOIRE_ACQUIRED_BLACK_DEMONS: CandyBox2LocationData(
        3706, lambda world: spell_location_count(world)
    ),
    CandyBox2LocationName.TEAPOT_DEFEATED: CandyBox2LocationData(3900),
    CandyBox2LocationName.XINOPHERYDON_DEFEATED: CandyBox2LocationData(4000),
    CandyBox2LocationName.XINOPHERYDON_QUEST_UNICORN_HORN_ACQUIRED: CandyBox2LocationData(4001),
    CandyBox2LocationName.ROCKET_BOOTS_ACQUIRED: CandyBox2LocationData(4100),
    CandyBox2LocationName.PITCHFORK_ACQUIRED: CandyBox2LocationData(4300),
    CandyBox2LocationName.THE_SQUIRRELS_FIRST_QUESTION: CandyBox2LocationData(4400),
    CandyBox2LocationName.THE_SQUIRRELS_SECOND_QUESTION: CandyBox2LocationData(4401),
    CandyBox2LocationName.THE_SQUIRRELS_THIRD_QUESTION: CandyBox2LocationData(4402),
    CandyBox2LocationName.THE_SQUIRRELS_FOURTH_QUESTION: CandyBox2LocationData(4403),
    CandyBox2LocationName.THE_SQUIRRELS_FIFTH_QUESTION: CandyBox2LocationData(4404),
    CandyBox2LocationName.THE_SQUIRRELS_PUZZLE: CandyBox2LocationData(4405),
    CandyBox2LocationName.THE_SPONGE_ACQUIRED: CandyBox2LocationData(4500),
    CandyBox2LocationName.THE_SHELL_POWDER_ACQUIRED: CandyBox2LocationData(4501),
    CandyBox2LocationName.THE_RED_FIN_ACQUIRED: CandyBox2LocationData(4502),
    CandyBox2LocationName.THE_GREEN_FIN_ACQUIRED: CandyBox2LocationData(4503),
    CandyBox2LocationName.THE_PURPLE_FIN_ACQUIRED: CandyBox2LocationData(4504),
    CandyBox2LocationName.X_MARKS_THE_SPOT: CandyBox2LocationData(4600),
    CandyBox2LocationName.LOCKED_CANDY_BOX_ACQUIRED: CandyBox2LocationData(4700),
    CandyBox2LocationName.YOURSELF_DEFEATED: CandyBox2LocationData(4800),
    CandyBox2LocationName.BAKE_PAIN_AU_CHOCOLAT_1: CandyBox2LocationData(4900),
    CandyBox2LocationName.BAKE_PAIN_AU_CHOCOLAT_2: CandyBox2LocationData(4901),
    CandyBox2LocationName.BAKE_PAIN_AU_CHOCOLAT_3: CandyBox2LocationData(4902),
    CandyBox2LocationName.BAKE_PAIN_AU_CHOCOLAT_4: CandyBox2LocationData(4903),
    CandyBox2LocationName.BAKE_PAIN_AU_CHOCOLAT_5: CandyBox2LocationData(4904),
    CandyBox2LocationName.POGO_STICK: CandyBox2LocationData(500),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_1: CandyBox2LocationData(100000),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_2: CandyBox2LocationData(100001),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_3: CandyBox2LocationData(100002),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_4: CandyBox2LocationData(100003),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_5: CandyBox2LocationData(100004),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_6: CandyBox2LocationData(100005),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_7: CandyBox2LocationData(100006),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_8: CandyBox2LocationData(100007),
    CandyBox2LocationName.THE_SEA_EXTRA_1: CandyBox2LocationData(101000),
    CandyBox2LocationName.THE_SEA_EXTRA_2: CandyBox2LocationData(101001),
    CandyBox2LocationName.THE_SEA_EXTRA_3: CandyBox2LocationData(101002),
    CandyBox2LocationName.THE_SEA_EXTRA_4: CandyBox2LocationData(101003),
    CandyBox2LocationName.THE_SEA_EXTRA_5: CandyBox2LocationData(101004),
    CandyBox2LocationName.THE_SEA_EXTRA_6: CandyBox2LocationData(101005),
    CandyBox2LocationName.THE_SEA_EXTRA_7: CandyBox2LocationData(101006),
    CandyBox2LocationName.THE_SEA_EXTRA_8: CandyBox2LocationData(101007),
    CandyBox2LocationName.THE_SEA_EXTRA_9: CandyBox2LocationData(101008),
    CandyBox2LocationName.THE_SEA_EXTRA_10: CandyBox2LocationData(101009),
    CandyBox2LocationName.THE_SEA_EXTRA_11: CandyBox2LocationData(101010),
    CandyBox2LocationName.THE_SEA_EXTRA_12: CandyBox2LocationData(101011),
    CandyBox2LocationName.THE_SEA_EXTRA_13: CandyBox2LocationData(101012),
    CandyBox2LocationName.THE_SEA_EXTRA_14: CandyBox2LocationData(101013),
    CandyBox2LocationName.THE_SEA_EXTRA_15: CandyBox2LocationData(101014),
    CandyBox2LocationName.THE_SEA_EXTRA_16: CandyBox2LocationData(101015),
    CandyBox2LocationName.THE_SEA_EXTRA_17: CandyBox2LocationData(101016),
    CandyBox2LocationName.THE_SEA_EXTRA_18: CandyBox2LocationData(101017),
    CandyBox2LocationName.THE_SEA_EXTRA_19: CandyBox2LocationData(101018),
    CandyBox2LocationName.THE_SEA_EXTRA_20: CandyBox2LocationData(101019),
    CandyBox2LocationName.THE_SEA_EXTRA_21: CandyBox2LocationData(101020),
    CandyBox2LocationName.THE_SEA_EXTRA_22: CandyBox2LocationData(101021),
    CandyBox2LocationName.THE_SEA_EXTRA_23: CandyBox2LocationData(101022),
    CandyBox2LocationName.THE_SEA_EXTRA_24: CandyBox2LocationData(101023),
    CandyBox2LocationName.THE_SEA_EXTRA_25: CandyBox2LocationData(101024),
    CandyBox2LocationName.THE_SEA_EXTRA_26: CandyBox2LocationData(101025),
    CandyBox2LocationName.THE_SEA_EXTRA_27: CandyBox2LocationData(101026),
    CandyBox2LocationName.THE_SEA_EXTRA_28: CandyBox2LocationData(101027),
    CandyBox2LocationName.THE_SEA_EXTRA_29: CandyBox2LocationData(101028),
    CandyBox2LocationName.THE_SEA_EXTRA_30: CandyBox2LocationData(101029),
    CandyBox2LocationName.THE_SEA_EXTRA_31: CandyBox2LocationData(101030),
    CandyBox2LocationName.THE_SEA_EXTRA_32: CandyBox2LocationData(101031),
    CandyBox2LocationName.THE_SEA_EXTRA_33: CandyBox2LocationData(101032),
    CandyBox2LocationName.THE_SEA_EXTRA_34: CandyBox2LocationData(101033),
    CandyBox2LocationName.THE_SEA_EXTRA_35: CandyBox2LocationData(101034),
    CandyBox2LocationName.THE_SEA_EXTRA_36: CandyBox2LocationData(101035),
    CandyBox2LocationName.THE_SEA_EXTRA_37: CandyBox2LocationData(101036),
    CandyBox2LocationName.THE_SEA_EXTRA_38: CandyBox2LocationData(101037),
    CandyBox2LocationName.THE_SEA_EXTRA_39: CandyBox2LocationData(101038),
    CandyBox2LocationName.THE_SEA_EXTRA_40: CandyBox2LocationData(101039),
    CandyBox2LocationName.THE_SEA_EXTRA_41: CandyBox2LocationData(101040),
    CandyBox2LocationName.THE_SEA_EXTRA_42: CandyBox2LocationData(101041),
    CandyBox2LocationName.THE_SEA_EXTRA_43: CandyBox2LocationData(101042),
    CandyBox2LocationName.THE_SEA_EXTRA_44: CandyBox2LocationData(101043),
    CandyBox2LocationName.THE_SEA_EXTRA_45: CandyBox2LocationData(101044),
    CandyBox2LocationName.THE_SEA_EXTRA_46: CandyBox2LocationData(101045),
    CandyBox2LocationName.THE_SEA_EXTRA_47: CandyBox2LocationData(101046),
    CandyBox2LocationName.THE_SEA_EXTRA_48: CandyBox2LocationData(101047),
    CandyBox2LocationName.THE_SEA_EXTRA_49: CandyBox2LocationData(101048),
    CandyBox2LocationName.THE_SEA_EXTRA_50: CandyBox2LocationData(101049),
    CandyBox2LocationName.THE_SEA_EXTRA_51: CandyBox2LocationData(101050),
    CandyBox2LocationName.THE_SEA_EXTRA_52: CandyBox2LocationData(101051),
    CandyBox2LocationName.THE_SEA_EXTRA_53: CandyBox2LocationData(101052),
    CandyBox2LocationName.THE_SEA_EXTRA_54: CandyBox2LocationData(101053),
    CandyBox2LocationName.THE_SEA_EXTRA_55: CandyBox2LocationData(101054),
    CandyBox2LocationName.THE_SEA_EXTRA_56: CandyBox2LocationData(101055),
    CandyBox2LocationName.THE_SEA_EXTRA_57: CandyBox2LocationData(101056),
    CandyBox2LocationName.THE_SEA_EXTRA_58: CandyBox2LocationData(101057),
    CandyBox2LocationName.THE_SEA_EXTRA_59: CandyBox2LocationData(101058),
    CandyBox2LocationName.THE_SEA_EXTRA_60: CandyBox2LocationData(101059),
    CandyBox2LocationName.THE_SEA_EXTRA_61: CandyBox2LocationData(101060),
    CandyBox2LocationName.THE_SEA_EXTRA_62: CandyBox2LocationData(101061),
    CandyBox2LocationName.THE_SEA_EXTRA_63: CandyBox2LocationData(101062),
    CandyBox2LocationName.THE_SEA_EXTRA_64: CandyBox2LocationData(101063),
    CandyBox2LocationName.THE_SEA_EXTRA_65: CandyBox2LocationData(101064),
    CandyBox2LocationName.THE_SEA_EXTRA_66: CandyBox2LocationData(101065),
    CandyBox2LocationName.THE_SEA_EXTRA_67: CandyBox2LocationData(101066),
    CandyBox2LocationName.THE_SEA_EXTRA_68: CandyBox2LocationData(101067),
    CandyBox2LocationName.THE_SEA_EXTRA_69: CandyBox2LocationData(101068),
    CandyBox2LocationName.THE_SEA_EXTRA_70: CandyBox2LocationData(101069),
    CandyBox2LocationName.THE_SEA_EXTRA_71: CandyBox2LocationData(101070),
    CandyBox2LocationName.THE_SEA_EXTRA_72: CandyBox2LocationData(101071),
    CandyBox2LocationName.THE_SEA_EXTRA_73: CandyBox2LocationData(101072),
    CandyBox2LocationName.THE_SEA_EXTRA_74: CandyBox2LocationData(101073),
    CandyBox2LocationName.THE_SEA_EXTRA_75: CandyBox2LocationData(101074),
    CandyBox2LocationName.THE_SEA_EXTRA_76: CandyBox2LocationData(101075),
    CandyBox2LocationName.THE_SEA_EXTRA_77: CandyBox2LocationData(101076),
    CandyBox2LocationName.THE_SEA_EXTRA_78: CandyBox2LocationData(101077),
    CandyBox2LocationName.THE_SEA_EXTRA_79: CandyBox2LocationData(101078),
    CandyBox2LocationName.THE_SEA_EXTRA_80: CandyBox2LocationData(101079),
}

lollipop_farm_filler_locations = [
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_1,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_2,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_3,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_4,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_5,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_6,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_7,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_8,
]

the_sea_filler_locations = [
    CandyBox2LocationName.THE_SEA_EXTRA_1,
    CandyBox2LocationName.THE_SEA_EXTRA_2,
    CandyBox2LocationName.THE_SEA_EXTRA_3,
    CandyBox2LocationName.THE_SEA_EXTRA_4,
    CandyBox2LocationName.THE_SEA_EXTRA_5,
    CandyBox2LocationName.THE_SEA_EXTRA_6,
    CandyBox2LocationName.THE_SEA_EXTRA_7,
    CandyBox2LocationName.THE_SEA_EXTRA_8,
    CandyBox2LocationName.THE_SEA_EXTRA_9,
    CandyBox2LocationName.THE_SEA_EXTRA_10,
    CandyBox2LocationName.THE_SEA_EXTRA_11,
    CandyBox2LocationName.THE_SEA_EXTRA_12,
    CandyBox2LocationName.THE_SEA_EXTRA_13,
    CandyBox2LocationName.THE_SEA_EXTRA_14,
    CandyBox2LocationName.THE_SEA_EXTRA_15,
    CandyBox2LocationName.THE_SEA_EXTRA_16,
    CandyBox2LocationName.THE_SEA_EXTRA_17,
    CandyBox2LocationName.THE_SEA_EXTRA_18,
    CandyBox2LocationName.THE_SEA_EXTRA_19,
    CandyBox2LocationName.THE_SEA_EXTRA_20,
    CandyBox2LocationName.THE_SEA_EXTRA_21,
    CandyBox2LocationName.THE_SEA_EXTRA_22,
    CandyBox2LocationName.THE_SEA_EXTRA_23,
    CandyBox2LocationName.THE_SEA_EXTRA_24,
    CandyBox2LocationName.THE_SEA_EXTRA_25,
    CandyBox2LocationName.THE_SEA_EXTRA_26,
    CandyBox2LocationName.THE_SEA_EXTRA_27,
    CandyBox2LocationName.THE_SEA_EXTRA_28,
    CandyBox2LocationName.THE_SEA_EXTRA_29,
    CandyBox2LocationName.THE_SEA_EXTRA_30,
    CandyBox2LocationName.THE_SEA_EXTRA_31,
    CandyBox2LocationName.THE_SEA_EXTRA_32,
    CandyBox2LocationName.THE_SEA_EXTRA_33,
    CandyBox2LocationName.THE_SEA_EXTRA_34,
    CandyBox2LocationName.THE_SEA_EXTRA_35,
    CandyBox2LocationName.THE_SEA_EXTRA_36,
    CandyBox2LocationName.THE_SEA_EXTRA_37,
    CandyBox2LocationName.THE_SEA_EXTRA_38,
    CandyBox2LocationName.THE_SEA_EXTRA_39,
    CandyBox2LocationName.THE_SEA_EXTRA_40,
    CandyBox2LocationName.THE_SEA_EXTRA_41,
    CandyBox2LocationName.THE_SEA_EXTRA_42,
    CandyBox2LocationName.THE_SEA_EXTRA_43,
    CandyBox2LocationName.THE_SEA_EXTRA_44,
    CandyBox2LocationName.THE_SEA_EXTRA_45,
    CandyBox2LocationName.THE_SEA_EXTRA_46,
    CandyBox2LocationName.THE_SEA_EXTRA_47,
    CandyBox2LocationName.THE_SEA_EXTRA_48,
    CandyBox2LocationName.THE_SEA_EXTRA_49,
    CandyBox2LocationName.THE_SEA_EXTRA_50,
    CandyBox2LocationName.THE_SEA_EXTRA_51,
    CandyBox2LocationName.THE_SEA_EXTRA_52,
    CandyBox2LocationName.THE_SEA_EXTRA_53,
    CandyBox2LocationName.THE_SEA_EXTRA_54,
    CandyBox2LocationName.THE_SEA_EXTRA_55,
    CandyBox2LocationName.THE_SEA_EXTRA_56,
    CandyBox2LocationName.THE_SEA_EXTRA_57,
    CandyBox2LocationName.THE_SEA_EXTRA_58,
    CandyBox2LocationName.THE_SEA_EXTRA_59,
    CandyBox2LocationName.THE_SEA_EXTRA_60,
    CandyBox2LocationName.THE_SEA_EXTRA_61,
    CandyBox2LocationName.THE_SEA_EXTRA_62,
    CandyBox2LocationName.THE_SEA_EXTRA_63,
    CandyBox2LocationName.THE_SEA_EXTRA_64,
    CandyBox2LocationName.THE_SEA_EXTRA_65,
    CandyBox2LocationName.THE_SEA_EXTRA_66,
    CandyBox2LocationName.THE_SEA_EXTRA_67,
    CandyBox2LocationName.THE_SEA_EXTRA_68,
    CandyBox2LocationName.THE_SEA_EXTRA_69,
    CandyBox2LocationName.THE_SEA_EXTRA_70,
    CandyBox2LocationName.THE_SEA_EXTRA_71,
    CandyBox2LocationName.THE_SEA_EXTRA_72,
    CandyBox2LocationName.THE_SEA_EXTRA_73,
    CandyBox2LocationName.THE_SEA_EXTRA_74,
    CandyBox2LocationName.THE_SEA_EXTRA_75,
    CandyBox2LocationName.THE_SEA_EXTRA_76,
    CandyBox2LocationName.THE_SEA_EXTRA_77,
    CandyBox2LocationName.THE_SEA_EXTRA_78,
    CandyBox2LocationName.THE_SEA_EXTRA_79,
    CandyBox2LocationName.THE_SEA_EXTRA_80,
]

filler_locations = [
    *lollipop_farm_filler_locations,
    *the_sea_filler_locations
]


def grimoire_location_count(world: "CandyBox2World"):
    if world.grimoires == 0 or world.grimoires == 1:  # Grimoires
        return True

    return False


def spell_location_count(world: "CandyBox2World"):
    if world.grimoires == 2:
        return True

    return False


def extra_location_count(world: "CandyBox2World"):
    return world.font_traps
