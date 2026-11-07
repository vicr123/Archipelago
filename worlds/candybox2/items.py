from collections.abc import Callable
from enum import StrEnum
from typing import TYPE_CHECKING, NamedTuple

from BaseClasses import Item, ItemClassification
from .locations import extra_location_count

if TYPE_CHECKING:
    from . import CandyBox2World

# an item is something you receive

candy_box_2_base_id: int = 7665000


class CandyBox2Item(Item):
    game: str = "Candy Box 2"


class CandyBox2ItemData(NamedTuple):
    code: int | None = None
    required_amount: Callable[["CandyBox2World"], int] = lambda _: 0
    classification: ItemClassification = ItemClassification.filler
    description: str | None = None


class CandyBox2ItemName(StrEnum):
    CANDY = "Kẹo"
    LOLLIPOP = "Kẹo mút"
    CHOCOLATE_BAR = "Sô-cô-la thỏi"
    HP_BAR = "Thanh HP"
    TIME_RING = "Nhẫn thời gian"
    CANDY_MERCHANTS_HAT = "Mũ ông bán kẹo"
    LEATHER_GLOVES = "Găng tay da"
    LEATHER_BOOTS = "Giầy da"
    PROGRESSIVE_WORLD_MAP = "Bản đồ thế giới tiến bộ"
    TROLLS_BLUDGEON = "Chùy quái vật"
    DESERT_BIRD_FEATHER = "Lông chim sa mạc"
    BEGINNERS_GRIMOIRE = "Sách ma thuật sơ cấp"
    ADVANCED_GRIMOIRE = "Sách ma thuật cao cấp"
    SORCERESS_CAULDRON = "Vạc phù thúy"
    SORCERESS_HAT = "Mũ phù thúy"
    OCTOPUS_KING_CROWN = "Vương miện mực vua"
    MONKEY_WIZARD_STAFF = "Gậy của phù thủy Khỉ"
    HEART_PLUG = "Nút cám tim"
    POGO_STICK = "Gậy nhảy lò xo"
    P_STONE = "Đá P"
    L_STONE = "Đá L"
    A_STONE = "Đá A"
    Y_STONE = "Đá Y"
    WOODEN_SWORD = "Kiếm gỗ"
    IRON_AXE = "Rìu sắt"
    POLISHED_SILVER_SWORD = "Kiếm bạc được đánh bóng"
    LIGHTWEIGHT_BODY_ARMOUR = "Giáp nhẹ"
    SCYTHE = "Lưỡi hái"
    RED_ENCHANTED_GLOVES = "Găng tay làm phép đỏ"
    PINK_ENCHANTED_GLOVES = "Găng tay làm phép hồng"
    SUMMONING_TRIBAL_SPEAR = "Ngọn giáo bộ lạc kêu"
    ENCHANTED_MONKEY_WIZARD_STAFF = "Gậy của phù thủy Khỉ làm phép"
    ENCHANTED_KNIGHT_BODY_ARMOUR = "Giáp bảo vệ hiệp sĩ làm phép"
    OCTOPUS_KING_CROWN_WITH_JASPERS = "Vương miện mực vua với đá Gia-spa"
    OCTOPUS_KING_CROWN_WITH_OBSIDIAN = "Vương miện mực vua với hắc diện thạch"
    GIANT_SPOON_OF_DOOM = "Muỗng lớn dẽ sợ tại họa"
    TRIBAL_SPEAR = "Ngọn giáo bộ lạc"
    GIANT_SPOON = "Muỗng lớn dẽ sợ"
    DESERT_FORTRESS_KEY = "Chìa khoá pháo đài sa mạc"
    KNIGHT_BODY_ARMOUR = "Giáp bảo vệ hiệp sĩ"
    XINOPHERYDON_CLAW = "Móng vuốt Xi-nô-phê-ri-đôn"
    UNICORN_HORN = "Sừng kỳ lân"
    ROCKET_BOOTS = "Giày tên lửa"
    HEART_PENDANT = "Mặt dây trái tim"
    BLACK_MAGIC_GRIMOIRE = "Sách ma thuật hắc ám"
    FOUR_CHOCOLATE_BARS = "4 Sô-cô-la thỏis"
    PITCHFORK = "Nĩa"
    TWENTY_CANDIES = "20 Kẹo"
    ONE_HUNDRED_CANDIES = "100 Kẹo"
    FIVE_HUNDRED_CANDIES = "500 Kẹo"
    THREE_LOLLIPOPS = "3 Kẹo mút"
    THREE_CHOCOLATE_BARS = "3 Sô-cô-la thỏis"
    THIRD_HOUSE_KEY = "Chìa khóa nhà thứ 3"
    SPONGE = "Bọt biển"
    SHELL_POWDER = "Bột vỏ sò"
    RED_FIN = "Vây cá đỏ"
    GREEN_FIN = "Vây cá xanh"
    PURPLE_FIN = "Vây cá tím"
    LOCKED_CANDY_BOX = "Hộp kẹo khóa"
    BOOTS_OF_INTROSPECTION = "Giầy tự soi chiếu"
    PAIN_AU_CHOCOLAT = "Bánh mì sô-cô-la"
    NOTHING_WEAPON = "Không có (Vũ khí)"
    PROGRESSIVE_WEAPON = "Vũ khí tiến bộ"
    PROGRESSIVE_JUMP = "Vụ nhẩy tiến bộ"
    PROGRESSIVE_GRIMOIRE = "Sách ma thuật tiến bộ"
    TWO_PAINS_AU_CHOCOLAT = "2 Bánh mì sô-cô-la"
    ACID_RAIN_SPELL = "Phép thuật mưa a-xít"
    FIREBALL_SPELL = "Phép thuật bóng lửa"
    TELEPORT_SPELL = "Phép thuật dịch chuyển tức thời"
    ERASE_MAGIC_SPELL = "Phép thuật xóa bỏ phép thuật"
    THORNS_SHIELD_SPELL = "Phép thuật khiên gai"
    OBSIDIAN_WALL_SPELL = "Phép thuật tường hắc diện thạch"
    BLACK_DEMONS_SPELL = "Phép thuật Ác quỷ Đen"
    TALKING_CANDY = "Viên kẹo biết nói"
    FONT_TRAP = "Bẫy phông chữ"


items: dict[CandyBox2ItemName, CandyBox2ItemData] = {
    CandyBox2ItemName.CANDY: CandyBox2ItemData(candy_box_2_base_id + 0, lambda _: 0, ItemClassification.skip_balancing | ItemClassification.filler),
    CandyBox2ItemName.LOLLIPOP: CandyBox2ItemData(candy_box_2_base_id + 1, lambda _: 8, ItemClassification.progression),
    CandyBox2ItemName.CHOCOLATE_BAR: CandyBox2ItemData(
        candy_box_2_base_id + 2, lambda _: 3, ItemClassification.progression
    ),
    CandyBox2ItemName.HP_BAR: CandyBox2ItemData(
        candy_box_2_base_id + 3, lambda world: hp_bar_count(world), ItemClassification.useful
    ),
    CandyBox2ItemName.TIME_RING: CandyBox2ItemData(candy_box_2_base_id + 4, lambda _: 1),
    CandyBox2ItemName.CANDY_MERCHANTS_HAT: CandyBox2ItemData(candy_box_2_base_id + 5, lambda _: 1),
    CandyBox2ItemName.LEATHER_GLOVES: CandyBox2ItemData(
        candy_box_2_base_id + 6, lambda _: 1, ItemClassification.progression
    ),
    CandyBox2ItemName.LEATHER_BOOTS: CandyBox2ItemData(candy_box_2_base_id + 7, lambda _: 1),
    CandyBox2ItemName.PROGRESSIVE_WORLD_MAP: CandyBox2ItemData(
        candy_box_2_base_id + 8, lambda _: 7, ItemClassification.progression | ItemClassification.useful
    ),
    CandyBox2ItemName.TROLLS_BLUDGEON: CandyBox2ItemData(
        candy_box_2_base_id + 9,
        lambda world: weapon_item_count(world, 9),
        ItemClassification.progression | ItemClassification.useful,
    ),
    CandyBox2ItemName.DESERT_BIRD_FEATHER: CandyBox2ItemData(
        candy_box_2_base_id + 10, lambda world: jump_item_count(world), ItemClassification.progression
    ),
    CandyBox2ItemName.BEGINNERS_GRIMOIRE: CandyBox2ItemData(
        candy_box_2_base_id + 11,
        lambda world: grimoire_item_count(world),
        ItemClassification.progression | ItemClassification.useful,
    ),
    CandyBox2ItemName.ADVANCED_GRIMOIRE: CandyBox2ItemData(
        candy_box_2_base_id + 12, lambda world: grimoire_item_count(world), ItemClassification.progression
    ),
    CandyBox2ItemName.SORCERESS_CAULDRON: CandyBox2ItemData(
        candy_box_2_base_id + 13, lambda _: 1, ItemClassification.progression | ItemClassification.useful
    ),
    CandyBox2ItemName.SORCERESS_HAT: CandyBox2ItemData(candy_box_2_base_id + 14, lambda _: 1),
    CandyBox2ItemName.OCTOPUS_KING_CROWN: CandyBox2ItemData(
        candy_box_2_base_id + 15, lambda _: 1, ItemClassification.progression
    ),
    CandyBox2ItemName.MONKEY_WIZARD_STAFF: CandyBox2ItemData(
        candy_box_2_base_id + 16,
        lambda world: weapon_item_count(world, 16),
        ItemClassification.progression | ItemClassification.useful,
    ),
    CandyBox2ItemName.HEART_PLUG: CandyBox2ItemData(
        candy_box_2_base_id + 17, lambda _: 1, ItemClassification.progression | ItemClassification.useful
    ),
    CandyBox2ItemName.POGO_STICK: CandyBox2ItemData(
        candy_box_2_base_id + 18,
        lambda world: jump_item_count(world),
        ItemClassification.progression | ItemClassification.useful,
    ),
    CandyBox2ItemName.P_STONE: CandyBox2ItemData(candy_box_2_base_id + 19, lambda _: 1, ItemClassification.progression),
    CandyBox2ItemName.L_STONE: CandyBox2ItemData(candy_box_2_base_id + 20, lambda _: 1, ItemClassification.progression),
    CandyBox2ItemName.A_STONE: CandyBox2ItemData(candy_box_2_base_id + 21, lambda _: 1, ItemClassification.progression),
    CandyBox2ItemName.Y_STONE: CandyBox2ItemData(candy_box_2_base_id + 22, lambda _: 1, ItemClassification.progression),
    CandyBox2ItemName.WOODEN_SWORD: CandyBox2ItemData(
        candy_box_2_base_id + 23,
        lambda world: weapon_item_count(world, 23),
        ItemClassification.progression | ItemClassification.useful,
    ),
    CandyBox2ItemName.IRON_AXE: CandyBox2ItemData(
        candy_box_2_base_id + 24,
        lambda world: weapon_item_count(world, 24),
        ItemClassification.progression | ItemClassification.useful,
    ),
    CandyBox2ItemName.POLISHED_SILVER_SWORD: CandyBox2ItemData(
        candy_box_2_base_id + 25,
        lambda world: weapon_item_count(world, 25),
        ItemClassification.progression | ItemClassification.useful,
    ),
    CandyBox2ItemName.LIGHTWEIGHT_BODY_ARMOUR: CandyBox2ItemData(
        candy_box_2_base_id + 26, lambda _: 1, ItemClassification.progression | ItemClassification.useful
    ),
    CandyBox2ItemName.SCYTHE: CandyBox2ItemData(
        candy_box_2_base_id + 27,
        lambda world: weapon_item_count(world, 27),
        ItemClassification.progression | ItemClassification.useful,
    ),
    CandyBox2ItemName.RED_ENCHANTED_GLOVES: CandyBox2ItemData(
        candy_box_2_base_id + 28, lambda _: 1, ItemClassification.progression
    ),
    CandyBox2ItemName.PINK_ENCHANTED_GLOVES: CandyBox2ItemData(
        candy_box_2_base_id + 29, lambda _: 1, ItemClassification.progression | ItemClassification.useful
    ),
    CandyBox2ItemName.SUMMONING_TRIBAL_SPEAR: CandyBox2ItemData(
        candy_box_2_base_id + 30,
        lambda world: weapon_item_count(world, 30),
        ItemClassification.progression | ItemClassification.useful,
    ),
    CandyBox2ItemName.ENCHANTED_MONKEY_WIZARD_STAFF: CandyBox2ItemData(
        candy_box_2_base_id + 31,
        lambda world: weapon_item_count(world, 31),
        ItemClassification.progression | ItemClassification.useful,
    ),
    CandyBox2ItemName.ENCHANTED_KNIGHT_BODY_ARMOUR: CandyBox2ItemData(
        candy_box_2_base_id + 32, lambda _: 1, ItemClassification.progression
    ),
    CandyBox2ItemName.OCTOPUS_KING_CROWN_WITH_JASPERS: CandyBox2ItemData(
        candy_box_2_base_id + 33, lambda _: 1, ItemClassification.progression | ItemClassification.useful
    ),
    CandyBox2ItemName.OCTOPUS_KING_CROWN_WITH_OBSIDIAN: CandyBox2ItemData(
        candy_box_2_base_id + 34, lambda _: 1, ItemClassification.progression
    ),
    CandyBox2ItemName.GIANT_SPOON_OF_DOOM: CandyBox2ItemData(
        candy_box_2_base_id + 35,
        lambda world: weapon_item_count(world, 35),
        ItemClassification.progression | ItemClassification.useful,
    ),
    CandyBox2ItemName.TRIBAL_SPEAR: CandyBox2ItemData(
        candy_box_2_base_id + 36,
        lambda world: weapon_item_count(world, 36),
        ItemClassification.progression | ItemClassification.useful,
    ),
    CandyBox2ItemName.GIANT_SPOON: CandyBox2ItemData(
        candy_box_2_base_id + 37,
        lambda world: weapon_item_count(world, 37),
        ItemClassification.progression | ItemClassification.useful,
    ),
    CandyBox2ItemName.DESERT_FORTRESS_KEY: CandyBox2ItemData(
        candy_box_2_base_id + 38, lambda _: 1, ItemClassification.progression | ItemClassification.useful
    ),
    CandyBox2ItemName.KNIGHT_BODY_ARMOUR: CandyBox2ItemData(
        candy_box_2_base_id + 39, lambda _: 1, ItemClassification.progression | ItemClassification.useful
    ),
    CandyBox2ItemName.XINOPHERYDON_CLAW: CandyBox2ItemData(
        candy_box_2_base_id + 40, lambda _: 1, ItemClassification.progression | ItemClassification.useful
    ),
    CandyBox2ItemName.UNICORN_HORN: CandyBox2ItemData(
        candy_box_2_base_id + 41, lambda _: 1, ItemClassification.progression | ItemClassification.useful
    ),
    CandyBox2ItemName.ROCKET_BOOTS: CandyBox2ItemData(
        candy_box_2_base_id + 42,
        lambda world: jump_item_count(world),
        ItemClassification.progression | ItemClassification.useful,
    ),
    CandyBox2ItemName.HEART_PENDANT: CandyBox2ItemData(
        candy_box_2_base_id + 43, lambda _: 1, ItemClassification.progression | ItemClassification.useful
    ),
    CandyBox2ItemName.BLACK_MAGIC_GRIMOIRE: CandyBox2ItemData(
        candy_box_2_base_id + 44,
        lambda world: grimoire_item_count(world),
        ItemClassification.progression | ItemClassification.useful,
    ),
    CandyBox2ItemName.FOUR_CHOCOLATE_BARS: CandyBox2ItemData(
        candy_box_2_base_id + 45, lambda _: 1, ItemClassification.progression
    ),
    CandyBox2ItemName.PITCHFORK: CandyBox2ItemData(
        candy_box_2_base_id + 46, lambda _: 1, ItemClassification.progression
    ),
    CandyBox2ItemName.TWENTY_CANDIES: CandyBox2ItemData(
        candy_box_2_base_id + 47, lambda _: 1, ItemClassification.skip_balancing | ItemClassification.filler
    ),
    CandyBox2ItemName.ONE_HUNDRED_CANDIES: CandyBox2ItemData(
        candy_box_2_base_id + 48, lambda _: 1, ItemClassification.skip_balancing | ItemClassification.filler
    ),
    CandyBox2ItemName.FIVE_HUNDRED_CANDIES: CandyBox2ItemData(
        candy_box_2_base_id + 49, lambda _: 1, ItemClassification.skip_balancing | ItemClassification.filler
    ),
    CandyBox2ItemName.THREE_LOLLIPOPS: CandyBox2ItemData(
        candy_box_2_base_id + 50, lambda _: 1, ItemClassification.progression
    ),
    CandyBox2ItemName.THREE_CHOCOLATE_BARS: CandyBox2ItemData(
        candy_box_2_base_id + 51, lambda _: 2, ItemClassification.progression
    ),
    CandyBox2ItemName.THIRD_HOUSE_KEY: CandyBox2ItemData(
        candy_box_2_base_id + 52, lambda _: 1, ItemClassification.progression | ItemClassification.useful
    ),
    CandyBox2ItemName.SPONGE: CandyBox2ItemData(candy_box_2_base_id + 53, lambda _: 1, ItemClassification.progression),
    CandyBox2ItemName.SHELL_POWDER: CandyBox2ItemData(
        candy_box_2_base_id + 54, lambda _: 1, ItemClassification.progression
    ),
    CandyBox2ItemName.RED_FIN: CandyBox2ItemData(candy_box_2_base_id + 55, lambda _: 1, ItemClassification.useful),
    CandyBox2ItemName.GREEN_FIN: CandyBox2ItemData(
        candy_box_2_base_id + 56, lambda _: 1, ItemClassification.progression
    ),
    CandyBox2ItemName.PURPLE_FIN: CandyBox2ItemData(
        candy_box_2_base_id + 57, lambda _: 1, ItemClassification.progression | ItemClassification.useful
    ),
    CandyBox2ItemName.LOCKED_CANDY_BOX: CandyBox2ItemData(
        candy_box_2_base_id + 58, lambda _: 1, ItemClassification.progression
    ),
    CandyBox2ItemName.BOOTS_OF_INTROSPECTION: CandyBox2ItemData(
        candy_box_2_base_id + 59, lambda _: 1, ItemClassification.progression | ItemClassification.useful
    ),
    CandyBox2ItemName.PAIN_AU_CHOCOLAT: CandyBox2ItemData(
        candy_box_2_base_id + 60, lambda world: pain_au_chocolat_count(world, 1), ItemClassification.useful
    ),
    CandyBox2ItemName.NOTHING_WEAPON: CandyBox2ItemData(
        candy_box_2_base_id + 61,
        lambda world: weapon_item_count(world, 61),
        ItemClassification.progression | ItemClassification.useful,
    ),
    CandyBox2ItemName.PROGRESSIVE_WEAPON: CandyBox2ItemData(
        candy_box_2_base_id + 62,
        lambda world: progressive_weapon_count(world),
        ItemClassification.progression | ItemClassification.useful,
    ),
    CandyBox2ItemName.PROGRESSIVE_JUMP: CandyBox2ItemData(
        candy_box_2_base_id + 63,
        lambda world: progressive_jump_count(world),
        ItemClassification.progression | ItemClassification.useful,
    ),
    CandyBox2ItemName.PROGRESSIVE_GRIMOIRE: CandyBox2ItemData(
        candy_box_2_base_id + 64,
        lambda world: progressive_grimoire_count(world),
        ItemClassification.progression | ItemClassification.useful,
    ),
    CandyBox2ItemName.TWO_PAINS_AU_CHOCOLAT: CandyBox2ItemData(
        candy_box_2_base_id + 65, lambda world: pain_au_chocolat_count(world, 2), ItemClassification.useful
    ),
    CandyBox2ItemName.ACID_RAIN_SPELL: CandyBox2ItemData(
        candy_box_2_base_id + 66,
        lambda world: spell_item_count(world),
        ItemClassification.progression | ItemClassification.useful,
    ),
    CandyBox2ItemName.FIREBALL_SPELL: CandyBox2ItemData(
        candy_box_2_base_id + 67,
        lambda world: spell_item_count(world),
        ItemClassification.progression | ItemClassification.useful,
    ),
    CandyBox2ItemName.TELEPORT_SPELL: CandyBox2ItemData(
        candy_box_2_base_id + 68,
        lambda world: spell_item_count(world),
        ItemClassification.progression | ItemClassification.useful,
    ),
    CandyBox2ItemName.ERASE_MAGIC_SPELL: CandyBox2ItemData(
        candy_box_2_base_id + 69,
        lambda world: spell_item_count(world),
        ItemClassification.progression | ItemClassification.useful,
    ),
    CandyBox2ItemName.THORNS_SHIELD_SPELL: CandyBox2ItemData(
        candy_box_2_base_id + 70,
        lambda world: spell_item_count(world),
        ItemClassification.progression | ItemClassification.useful,
    ),
    CandyBox2ItemName.OBSIDIAN_WALL_SPELL: CandyBox2ItemData(
        candy_box_2_base_id + 71,
        lambda world: spell_item_count(world),
        ItemClassification.progression | ItemClassification.useful,
    ),
    CandyBox2ItemName.BLACK_DEMONS_SPELL: CandyBox2ItemData(
        candy_box_2_base_id + 72,
        lambda world: spell_item_count(world),
        ItemClassification.progression | ItemClassification.useful,
    ),
    CandyBox2ItemName.FONT_TRAP: CandyBox2ItemData(
        candy_box_2_base_id + 73, lambda world: font_trap_count(world), ItemClassification.trap
    ),

    # The talking candy is always locked to the talking candy location if required
    CandyBox2ItemName.TALKING_CANDY: CandyBox2ItemData(candy_box_2_base_id + 74, lambda world: 0, ItemClassification.progression),
}

filler_items: list[str] = [CandyBox2ItemName.CANDY.value, CandyBox2ItemName.TWENTY_CANDIES.value]

item_groups = {
    "Sô-cô-la thỏis": {
        CandyBox2ItemName.CHOCOLATE_BAR.value,
        CandyBox2ItemName.THREE_CHOCOLATE_BARS.value,
        CandyBox2ItemName.FOUR_CHOCOLATE_BARS.value
    },
    "Lollipops": {
        CandyBox2ItemName.LOLLIPOP.value,
        CandyBox2ItemName.LOLLIPOP.value,
    },
    "Candies": {
        CandyBox2ItemName.CANDY.value,
        CandyBox2ItemName.TWENTY_CANDIES.value,
        CandyBox2ItemName.ONE_HUNDRED_CANDIES.value,
        CandyBox2ItemName.FIVE_HUNDRED_CANDIES.value,
    }
}

def weapon_item_count(world: "CandyBox2World", weapon: int):
    if world.starting_weapon == weapon:
        # We start with this weapon, so none of these are required
        return 0

    if world.starting_weapon == -1:
        # We are using Progressive Weapons, so no weapons will be added to the pool
        return 0

    return 1


def progressive_weapon_count(world: "CandyBox2World"):
    if world.starting_weapon == -1:
        return 11

    # Progressive Weapons are disabled
    return 0


def progressive_grimoire_count(world: "CandyBox2World"):
    if world.grimoires == 1:  # Progressive Grimoires
        return 3

    # Progressive Grimoires are disabled
    return 0


def grimoire_item_count(world: "CandyBox2World"):
    if world.grimoires == 0:  # Individual Grimoires
        return 1

    return 0


def spell_item_count(world: "CandyBox2World"):
    if world.grimoires == 2:  # Individual Spells
        return 1

    return 0


def jump_item_count(world: "CandyBox2World"):
    if world.progressive_jump:
        return 0

    return 1


def progressive_jump_count(world: "CandyBox2World"):
    if world.progressive_jump:
        return 3

    # Progressive Jump is disabled
    return 0


def hp_bar_count(world: "CandyBox2World"):
    if world.options.randomise_hp_bar:
        return 1

    return 0


def pain_au_chocolat_count(world: "CandyBox2World", value: int):
    if value == 1:
        return 10 - world.pains_au_chocolat

    if value == 2:
        return world.pains_au_chocolat - 5

    return 0


def font_trap_count(world: "CandyBox2World"):
    return world.font_traps

def create_items(world: "CandyBox2World"):
    for name, data in items.items():
        required_amount = data.required_amount(world)
        for _ in range(required_amount):
            world.multiworld.itempool.append(world.create_item(name.value))

    extra_location_num = -extra_location_count(world)
    if extra_location_num > 0:
        # Generate the required number of filler items
        for i in range(extra_location_num):
            world.multiworld.itempool.append(world.create_filler())
