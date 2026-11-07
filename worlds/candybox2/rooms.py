from enum import StrEnum


class CandyBox2Room(StrEnum):
    QUEST_THE_CELLAR = "THE_CELLAR"
    QUEST_THE_DESERT = "THE_DESERT"
    QUEST_THE_BRIDGE = "THE_BRIDGE"
    QUEST_THE_OCTOPUS_KING = "THE_OCTOPUS_KING"
    QUEST_THE_NAKED_MONKEY_WIZARD = "THE_NAKED_MONKEY_WIZARD"
    QUEST_THE_SEA = "THE_SEA"
    QUEST_THE_FOREST = "THE_FOREST"
    QUEST_THE_CASTLE_ENTRANCE = "THE_CASTLE_ENTRANCE"
    QUEST_THE_HOLE = "THE_HOLE"
    QUEST_THE_GIANT_NOUGAT_MONSTER = "THE_GIANT_NOUGAT_MONSTER"
    QUEST_THE_CASTLE_TRAP_ROOM = "THE_CASTLE_TRAP_ROOM"
    QUEST_THE_CASTLE_EGG_ROOM = "THE_CASTLE_EGG_ROOM"
    QUEST_HELL = "HELL"
    QUEST_THE_DEVELOPER = "THE_DEVELOPER"
    QUEST_THE_XINOPHERYDON = "THE_XINOPHERYDON"
    QUEST_THE_TEAPOT = "THE_TEAPOT"
    QUEST_THE_LEDGE_ROOM = "THE_LEDGE_ROOM"
    QUEST_THE_X_POTION = "THE_X_POTION"

    VILLAGE_SHOP = "VILLAGE_SHOP"
    VILLAGE_MINIGAME = "VILLAGE_MINIGAME"
    VILLAGE_FORGE = "VILLAGE_FORGE"
    VILLAGE_FURNISHED_HOUSE = "VILLAGE_FURNISHED_HOUSE"
    VILLAGE_QUEST_HOUSE = "VILLAGE_QUEST_HOUSE"
    SQUIRREL_TREE = "SQUIRREL_TREE"
    LONELY_HOUSE = "LONELY_HOUSE"
    DIG_SPOT = "DIG_SPOT"
    DESERT_FORTRESS = "DESERT_FORTRESS"
    POGO_STICK_SPOT = "POGO_STICK_SPOT"
    SORCERESS_HUT = "SORCERESS_HUT"
    WISHING_WELL = "WISHING_WELL"
    CAVE = "CAVE"
    PIER = "PIER"
    LIGHTHOUSE = "LIGHTHOUSE"
    HOLE = "HOLE"
    CASTLE = "CASTLE"
    CASTLE_BAKEHOUSE = "CASTLE_BAKEHOUSE"
    CASTLE_DARK_ROOM = "CASTLE_DARK_ROOM"
    DRAGON = "DRAGON"
    TOWER = "TOWER"
    LOLLIPOP_FARM = "LOLLIPOP_FARM"

    # These do not participate in ER
    VILLAGE = "VILLAGE"
    WORLD_MAP = "WORLD_MAP"


entrance_friendly_names: dict[CandyBox2Room, str] = {
    CandyBox2Room.QUEST_THE_CELLAR: "Nhiệm vụ: Hầm",
    CandyBox2Room.QUEST_THE_DESERT: "Nhiệm vụ: Sa mạc",
    CandyBox2Room.QUEST_THE_BRIDGE: "Nhiệm vụ: Cầu",
    CandyBox2Room.QUEST_THE_OCTOPUS_KING: "Nhiệm vụ: Mực vua",
    CandyBox2Room.QUEST_THE_NAKED_MONKEY_WIZARD: "Nhiệm vụ: Phù thủy Khỉ Khỏa thân",
    CandyBox2Room.QUEST_THE_SEA: "Nhiệm vụ: Đại dương",
    CandyBox2Room.QUEST_THE_FOREST: "Nhiệm vụ: Rừng",
    CandyBox2Room.QUEST_THE_CASTLE_ENTRANCE: "Nhiệm vụ: Cửa lâu đài",
    CandyBox2Room.QUEST_THE_HOLE: "Nhiệm vụ: Lỗ",
    CandyBox2Room.QUEST_THE_GIANT_NOUGAT_MONSTER: "Nhiệm vụ: Quái vật Nu-ga to lớn",
    CandyBox2Room.QUEST_THE_CASTLE_TRAP_ROOM: "Nhiệm vụ: Phòng bẩy lâu đài",
    CandyBox2Room.QUEST_THE_CASTLE_EGG_ROOM: "Nhiệm vụ: Phòng trứng lâu đài",
    CandyBox2Room.QUEST_HELL: "Nhiệm vụ: Địa ngục",
    CandyBox2Room.QUEST_THE_DEVELOPER: "Nhiệm vụ: Người phát triển",
    CandyBox2Room.QUEST_THE_XINOPHERYDON: "Nhiệm vụ: Xi-nô-phê-ri-đôn",
    CandyBox2Room.QUEST_THE_TEAPOT: "Nhiệm vụ: Bình trà",
    CandyBox2Room.QUEST_THE_LEDGE_ROOM: "Nhiệm vụ: Phòng kệ",
    CandyBox2Room.QUEST_THE_X_POTION: "Nhiệm vụ: Uống thuốc X",
    CandyBox2Room.VILLAGE_SHOP: "Thành Phố: Cửa hàng",
    CandyBox2Room.VILLAGE_MINIGAME: "Thành Phố: Nhà thứ 3",
    CandyBox2Room.VILLAGE_FORGE: "Thành Phố: Lò ren",
    CandyBox2Room.VILLAGE_FURNISHED_HOUSE: "Thành Phố: Nhà thứ 5",
    CandyBox2Room.VILLAGE_QUEST_HOUSE: "Thành Phố: Nhà cuối cùng",
    CandyBox2Room.SQUIRREL_TREE: "Bản đồ thế giới Cây sóc",
    CandyBox2Room.LONELY_HOUSE: "Bản đồ thế giới: Nhà cô độc",
    CandyBox2Room.DIG_SPOT: "Bản đồ thế giới: Chỗ đào bí mật",
    CandyBox2Room.DESERT_FORTRESS: "Bản đồ thế giới: Pháo đài sa mạc",
    CandyBox2Room.POGO_STICK_SPOT: "Bản đồ thế giới: Dãy núi",
    CandyBox2Room.SORCERESS_HUT: "Bản đồ thế giới: Lều phù thủy",
    CandyBox2Room.WISHING_WELL: "Bản đồ thế giới: Giếng ước nguyện",
    CandyBox2Room.CAVE: "Bản đồ thế giới: Hang",
    CandyBox2Room.PIER: "Bản đồ thế giới: Bến tàu",
    CandyBox2Room.LIGHTHOUSE: "Bản đồ thế giới: Hải đăng",
    CandyBox2Room.HOLE: "Bản đồ thế giới: Lỗ",
    CandyBox2Room.CASTLE: "Bản đồ thế giới: Lâu đài",
    CandyBox2Room.CASTLE_BAKEHOUSE: "Lâu đài: Lò bánh",
    CandyBox2Room.CASTLE_DARK_ROOM: "Lâu đài: Phòng tối",
    CandyBox2Room.DRAGON: "Bản đồ thế giới: Rồng",
    CandyBox2Room.TOWER: "Lâu đài: Tháp",
    CandyBox2Room.LOLLIPOP_FARM: "Bản đồ thế giới: Vườn kẹo",
    # Not required, just here to make logic easier
    CandyBox2Room.VILLAGE: "The Village",
    CandyBox2Room.WORLD_MAP: "The World Map",
}
quests: list[CandyBox2Room] = [
    CandyBox2Room.QUEST_THE_CELLAR,
    CandyBox2Room.QUEST_THE_DESERT,
    CandyBox2Room.QUEST_THE_BRIDGE,
    CandyBox2Room.QUEST_THE_OCTOPUS_KING,
    CandyBox2Room.QUEST_THE_NAKED_MONKEY_WIZARD,
    CandyBox2Room.QUEST_THE_SEA,
    CandyBox2Room.QUEST_THE_FOREST,
    CandyBox2Room.QUEST_THE_CASTLE_ENTRANCE,
    CandyBox2Room.QUEST_THE_HOLE,
    CandyBox2Room.QUEST_THE_GIANT_NOUGAT_MONSTER,
    CandyBox2Room.QUEST_THE_CASTLE_TRAP_ROOM,
    CandyBox2Room.QUEST_THE_CASTLE_EGG_ROOM,
    CandyBox2Room.QUEST_HELL,
    CandyBox2Room.QUEST_THE_DEVELOPER,
    CandyBox2Room.QUEST_THE_XINOPHERYDON,
    CandyBox2Room.QUEST_THE_TEAPOT,
    CandyBox2Room.QUEST_THE_LEDGE_ROOM,
    CandyBox2Room.QUEST_THE_X_POTION,
]

rooms: list[CandyBox2Room] = [
    CandyBox2Room.VILLAGE_SHOP,
    CandyBox2Room.VILLAGE_MINIGAME,
    CandyBox2Room.VILLAGE_FORGE,
    CandyBox2Room.VILLAGE_FURNISHED_HOUSE,
    CandyBox2Room.VILLAGE_QUEST_HOUSE,
    CandyBox2Room.SQUIRREL_TREE,
    CandyBox2Room.LONELY_HOUSE,
    CandyBox2Room.DIG_SPOT,
    CandyBox2Room.DESERT_FORTRESS,
    CandyBox2Room.POGO_STICK_SPOT,
    CandyBox2Room.SORCERESS_HUT,
    CandyBox2Room.WISHING_WELL,
    CandyBox2Room.CAVE,
    CandyBox2Room.PIER,
    CandyBox2Room.LIGHTHOUSE,
    CandyBox2Room.HOLE,
    CandyBox2Room.CASTLE,
    CandyBox2Room.CASTLE_BAKEHOUSE,
    CandyBox2Room.CASTLE_DARK_ROOM,
    CandyBox2Room.DRAGON,
    CandyBox2Room.TOWER,
]
lollipop_farm: list[CandyBox2Room] = [CandyBox2Room.LOLLIPOP_FARM]
