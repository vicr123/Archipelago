from collections.abc import Callable
from enum import StrEnum
from typing import TYPE_CHECKING, NamedTuple

from BaseClasses import Location
from .options import GoalConditions

if TYPE_CHECKING:
    from . import CandyBox2World


class CandyBox2LocationData(NamedTuple):
    id: int | None = None
    is_included: Callable[["CandyBox2World"], bool] = lambda _: True


class CandyBox2Location(Location):
    game: str = "Candy Box 2"


class CandyBox2LocationName(StrEnum):
    HP_BAR_UNLOCK = "Hộp kẹo: Thanh HP"
    DISAPPOINTED_EMOTE_CHOCOLATE_BAR = "Hộp kẹo: Ném 1630 kẹo"
    VILLAGE_SHOP_TOP_LOLLIPOP = "Cửa hàng: Kẹo mút trên"
    VILLAGE_SHOP_CENTRE_LOLLIPOP = "Cửa hàng: Kẹo mút giữa"
    VILLAGE_SHOP_BOTTOM_LOLLIPOP = "Cửa hàng: Kẹo mút dưới"
    VILLAGE_SHOP_CHOCOLATE_BAR = "Cửa hàng: Sô-cô-la thỏi"
    VILLAGE_SHOP_TIME_RING = "Cửa hàng: Nhẫn thời gian"
    VILLAGE_SHOP_CANDY_MERCHANTS_HAT = "Cửa hàng: Mũ ông bán kẹo"
    VILLAGE_SHOP_LEATHER_GLOVES = "Cửa hàng: Găng tay da"
    VILLAGE_SHOP_LEATHER_BOOTS = "Cửa hàng: Giầy da"
    VILLAGE_HOUSE_LOLLIPOP_ON_THE_BOOKSHELF = "Nhà thứ 5: Kẹo mút trên giá sách"
    VILLAGE_HOUSE_LOLLIPOP_IN_THE_BOOKSHELF = "Nhà thứ 5: Kẹo mút trong giá sách"
    VILLAGE_HOUSE_LOLLIPOP_UNDER_THE_RUG = "Nhà thứ 5: Kẹo mút dưới tấm thảm"
    CELLAR_QUEST_CLEARED = "Nhiệm vụ Hầm: Hoàn thành nhiệm vụ"
    DESERT_QUEST_CLEARED = "Nhiệm vụ Sa mạc: Hoàn thành nhiệm vụ"
    DESERT_BIRD_FEATHER_ACQUIRED = "Nhiệm vụ Sa mạc: Nhận lông chim sa mạc"
    TROLL_DEFEATED = "Nhiệm vụ cầu: Quái vật đánh bại"
    THE_TROLLS_BLUDGEON_ACQUIRED = "Nhiệm vụ cầu: Nhận chùy quái vật"
    CAVE_EXIT = "Hang: Lối ra"
    CAVE_CHOCOLATE_BAR = "Hang: Sô-cô-la thỏi"
    CAVE_HEART_PLUG = "Hang: Nút cám tim"
    FOREST_QUEST_CLEARED = "Nhiệm vụ Rừng: Hoàn thành nhiệm vụ"
    CASTLE_ENTRANCE_QUEST_CLEARED = "Nhiệm vụ Cửa lâu đài: Hoàn thành nhiệm vụ"
    KNIGHT_BODY_ARMOUR_ACQUIRED = "Nhiệm vụ Cửa lâu đài: Nhận giáp bảo vệ hiệp sĩ"
    GIANT_NOUGAT_MONSTER_DEFEATED = "Nhiệm vụ Quái vật Nu-ga to lớn: Quái vật Nu-ga to lớn đánh bại"
    SORCERESS_HUT_LOLLIPOP_ON_THE_SHELVES = "Lều phù thủy: Kẹo mút kín đáo"
    SORCERESS_HUT_BEGINNERS_GRIMOIRE = "Lều phù thủy: Sách ma thuật sơ cấp"
    SORCERESS_HUT_ADVANCED_GRIMOIRE = "Lều phù thủy: Sách ma thuật cao cấp"
    SORCERESS_HUT_CAULDRON = "Lều phù thủy: Vạc phù thúy"
    SORCERESS_HUT_HAT = "Lều phù thủy: Mũ phù thúy"
    OCTOPUS_KING_DEFEATED = "Nhiệm vụ Mực vua: Mực vua đánh bại"
    MONKEY_WIZARD_DEFEATED = "Nhiệm vụ Phù thủy Khỉ: Phù thủy Khỉ đánh bại"
    EGG_ROOM_QUEST_CLEARED = "Phòng trứng: Rương mở"
    DEVIL_DEFEATED = "Nhiệm vụ Địa ngục: Ác quỷ đánh bại"
    THE_DEVELOPER_DEFEATED = "Nhiệm vụ Người phát triển: Người phát triển đánh bại"
    SOLVE_CYCLOPS_PUZZLE = "Hải đăng: Giải câu đố của gã khổng lồ một mắt"
    VILLAGE_FORGE_LOLLIPOP_ON_EXHAUST_CHUTE = "Lò ren: Kẹo mút kín đáo"
    VILLAGE_FORGE_BUY_WOODEN_SWORD = "Lò ren: Kiếm gỗ"
    VILLAGE_FORGE_BUY_IRON_AXE = "Lò ren: Rìu sắt"
    VILLAGE_FORGE_BUY_POLISHED_SILVER_SWORD = "Lò ren: Kiếm bạc được đánh bóng"
    VILLAGE_FORGE_BUY_LIGHTWEIGHT_BODY_ARMOUR = "Lò ren: Giáp nhẹ"
    VILLAGE_FORGE_BUY_SCYTHE = "Lò ren: Lưỡi hái"
    ENCHANT_RED_ENCHANTED_GLOVES = "Giếng ước nguyện: Găng tay làm phép đỏ"
    ENCHANT_PINK_ENCHANTED_GLOVES = "Giếng ước nguyện: Găng tay làm phép hồng"
    ENCHANT_SUMMONING_TRIBAL_SPEAR = "Giếng ước nguyện: Ngọn giáo bộ lạc kêu"
    ENCHANT_ENCHANTED_MONKEY_WIZARD_STAFF = "Giếng ước nguyện: Gậy của phù thủy Khỉ làm phép"
    ENCHANT_ENCHANTED_KNIGHT_BODY_ARMOUR = "Giếng ước nguyện: Giáp bảo vệ hiệp sĩ làm phép"
    ENCHANT_OCTOPUS_KING_CROWN_WITH_JASPERS = "Giếng ước nguyện: Vương miện mực vua với đá Gia-spa"
    ENCHANT_OCTOPUS_KING_CROWN_WITH_OBSIDIAN = "Giếng ước nguyện: Vương miện mực vua với hắc diện thạch"
    ENCHANT_GIANT_SPOON_OF_DOOM = "Giếng ước nguyện: Muỗng lớn dẽ sợ tại họa"
    THE_HOLE_TRIBAL_WARRIOR_DEFEATED = "Lỗ: Chiến binh bộ lạc đánh bại"
    THE_HOLE_DESERT_FORTRESS_KEY_ACQUIRED = "Lỗ: Rương bên phải mở"
    THE_HOLE_HEART_PENDANT_ACQUIRED = "Lỗ: Rương bên trên mở"
    THE_HOLE_BLACK_MAGIC_GRIMOIRE_ACQUIRED = "Lỗ: Rương bên trái mở"
    THE_HOLE_FOUR_CHOCOLATE_BARS_ACQUIRED = "Lỗ: Rương bên dưới mở"
    TEAPOT_DEFEATED = "Nhiệm vụ Bình trà: Bình trà đánh bại"
    XINOPHERYDON_DEFEATED = "Nhiệm vụ Xi-nô-phê-ri-đôn: Xi-nô-phê-ri-đôn đánh bại"
    XINOPHERYDON_QUEST_UNICORN_HORN_ACQUIRED = "Nhiệm vụ Xi-nô-phê-ri-đôn: Nhận sừng kỳ lân"
    ROCKET_BOOTS_ACQUIRED = "Nhiệm vụ Phòng kệ: Rương mở"
    PITCHFORK_ACQUIRED = "Lâu đài Phòng tối: Nhận nĩa"
    THE_SQUIRRELS_FIRST_QUESTION = "Cây: Câu hỏi chú sóc thứ 1"
    THE_SQUIRRELS_SECOND_QUESTION = "Cây: Câu hỏi chú sóc thứ 2"
    THE_SQUIRRELS_THIRD_QUESTION = "Cây: Câu hỏi chú sóc thứ 3"
    THE_SQUIRRELS_FOURTH_QUESTION = "Cây: Câu hỏi chú sóc thứ 4"
    THE_SQUIRRELS_FIFTH_QUESTION = "Cây: Câu hỏi chú sóc thứ 5"
    THE_SQUIRRELS_PUZZLE = "Cây: Câu đố chú sóc"
    THE_SPONGE_ACQUIRED = "Đại dương: Nhận bọt biển"
    THE_SHELL_POWDER_ACQUIRED = "Đại dương: Nhận bột vỏ sò"
    THE_RED_FIN_ACQUIRED = "Đại dương: Nhận vây cá đỏ"
    THE_GREEN_FIN_ACQUIRED = "Đại dương: Nhận vây cá xanh"
    THE_PURPLE_FIN_ACQUIRED = "Đại dương: Nhận vây cá tím"
    X_MARKS_THE_SPOT = "Chỗ đào bí mật: Dấu X đánh dấu vị trí!"
    LOCKED_CANDY_BOX_ACQUIRED = "Nhà cô độc: Nhận hộp kẹo khóa"
    YOURSELF_DEFEATED = "Nhiệm vụ Uống thuốc X: Đánh bại chính mình"
    BAKE_PAIN_AU_CHOCOLAT_1 = "Lò bánh lâu đài: Nướng bánh mì sô-cô-la 1 lần"
    BAKE_PAIN_AU_CHOCOLAT_2 = "Lò bánh lâu đài: Nướng bánh mì sô-cô-la 2 lần"
    BAKE_PAIN_AU_CHOCOLAT_3 = "Lò bánh lâu đài: Nướng bánh mì sô-cô-la 3 lần"
    BAKE_PAIN_AU_CHOCOLAT_4 = "Lò bánh lâu đài: Nướng bánh mì sô-cô-la 4 lần"
    BAKE_PAIN_AU_CHOCOLAT_5 = "Lò bánh lâu đài: Nướng bánh mì sô-cô-la 5 lần"
    POGO_STICK = "Dãy núi: Gậy nhảy lò xo"
    TALKING_CANDY = "Tháp: Lấy viên kẹo biết nói"

    # Message to future me and Aren: I am so sorry.
    LOLLIPOP_FARM_EXTRA_1 = "Vườn kẹo mút: Trồng 1 kẹo mút"
    LOLLIPOP_FARM_EXTRA_2 = "Vườn kẹo mút: Trồng 2 kẹo mút"
    LOLLIPOP_FARM_EXTRA_3 = "Vườn kẹo mút: Trồng 3 kẹo mút"
    LOLLIPOP_FARM_EXTRA_4 = "Vườn kẹo mút: Trồng 4 kẹo mút"
    LOLLIPOP_FARM_EXTRA_5 = "Vườn kẹo mút: Trồng 5 kẹo mút"
    LOLLIPOP_FARM_EXTRA_6 = "Vườn kẹo mút: Trồng 6 kẹo mút"
    LOLLIPOP_FARM_EXTRA_7 = "Vườn kẹo mút: Trồng 7 kẹo mút"
    LOLLIPOP_FARM_EXTRA_8 = "Vườn kẹo mút: Trồng 8 kẹo mút"
    LOLLIPOP_FARM_EXTRA_9 = "Vườn kẹo mút: Trồng 9 kẹo mút"
    LOLLIPOP_FARM_EXTRA_10 = "Vườn kẹo mút: Trồng 10 kẹo mút"
    LOLLIPOP_FARM_EXTRA_11 = "Vườn kẹo mút: Trồng 11 kẹo mút"
    LOLLIPOP_FARM_EXTRA_12 = "Vườn kẹo mút: Trồng 12 kẹo mút"
    LOLLIPOP_FARM_EXTRA_13 = "Vườn kẹo mút: Trồng 13 kẹo mút"
    LOLLIPOP_FARM_EXTRA_14 = "Vườn kẹo mút: Trồng 14 kẹo mút"
    LOLLIPOP_FARM_EXTRA_15 = "Vườn kẹo mút: Trồng 15 kẹo mút"
    LOLLIPOP_FARM_EXTRA_16 = "Vườn kẹo mút: Trồng 16 kẹo mút"
    LOLLIPOP_FARM_EXTRA_17 = "Vườn kẹo mút: Trồng 17 kẹo mút"
    LOLLIPOP_FARM_EXTRA_18 = "Vườn kẹo mút: Trồng 18 kẹo mút"
    LOLLIPOP_FARM_EXTRA_19 = "Vườn kẹo mút: Trồng 19 kẹo mút"
    LOLLIPOP_FARM_EXTRA_20 = "Vườn kẹo mút: Trồng 20 kẹo mút"
    LOLLIPOP_FARM_EXTRA_21 = "Vườn kẹo mút: Trồng 21 kẹo mút"
    LOLLIPOP_FARM_EXTRA_22 = "Vườn kẹo mút: Trồng 22 kẹo mút"
    LOLLIPOP_FARM_EXTRA_23 = "Vườn kẹo mút: Trồng 23 kẹo mút"
    LOLLIPOP_FARM_EXTRA_24 = "Vườn kẹo mút: Trồng 24 kẹo mút"
    LOLLIPOP_FARM_EXTRA_25 = "Vườn kẹo mút: Trồng 25 kẹo mút"
    LOLLIPOP_FARM_EXTRA_26 = "Vườn kẹo mút: Trồng 26 kẹo mút"
    LOLLIPOP_FARM_EXTRA_27 = "Vườn kẹo mút: Trồng 27 kẹo mút"
    LOLLIPOP_FARM_EXTRA_28 = "Vườn kẹo mút: Trồng 28 kẹo mút"
    LOLLIPOP_FARM_EXTRA_29 = "Vườn kẹo mút: Trồng 29 kẹo mút"
    LOLLIPOP_FARM_EXTRA_30 = "Vườn kẹo mút: Trồng 30 kẹo mút"
    LOLLIPOP_FARM_EXTRA_31 = "Vườn kẹo mút: Trồng 31 kẹo mút"
    LOLLIPOP_FARM_EXTRA_32 = "Vườn kẹo mút: Trồng 32 kẹo mút"
    LOLLIPOP_FARM_EXTRA_33 = "Vườn kẹo mút: Trồng 33 kẹo mút"
    LOLLIPOP_FARM_EXTRA_34 = "Vườn kẹo mút: Trồng 34 kẹo mút"
    LOLLIPOP_FARM_EXTRA_35 = "Vườn kẹo mút: Trồng 35 kẹo mút"
    LOLLIPOP_FARM_EXTRA_36 = "Vườn kẹo mút: Trồng 36 kẹo mút"
    LOLLIPOP_FARM_EXTRA_37 = "Vườn kẹo mút: Trồng 37 kẹo mút"
    LOLLIPOP_FARM_EXTRA_38 = "Vườn kẹo mút: Trồng 38 kẹo mút"
    LOLLIPOP_FARM_EXTRA_39 = "Vườn kẹo mút: Trồng 39 kẹo mút"
    LOLLIPOP_FARM_EXTRA_40 = "Vườn kẹo mút: Trồng 40 kẹo mút"
    LOLLIPOP_FARM_EXTRA_41 = "Vườn kẹo mút: Trồng 41 kẹo mút"
    LOLLIPOP_FARM_EXTRA_42 = "Vườn kẹo mút: Trồng 42 kẹo mút"
    LOLLIPOP_FARM_EXTRA_43 = "Vườn kẹo mút: Trồng 43 kẹo mút"
    LOLLIPOP_FARM_EXTRA_44 = "Vườn kẹo mút: Trồng 44 kẹo mút"
    LOLLIPOP_FARM_EXTRA_45 = "Vườn kẹo mút: Trồng 45 kẹo mút"
    LOLLIPOP_FARM_EXTRA_46 = "Vườn kẹo mút: Trồng 46 kẹo mút"
    LOLLIPOP_FARM_EXTRA_47 = "Vườn kẹo mút: Trồng 47 kẹo mút"
    LOLLIPOP_FARM_EXTRA_48 = "Vườn kẹo mút: Trồng 48 kẹo mút"
    LOLLIPOP_FARM_EXTRA_49 = "Vườn kẹo mút: Trồng 49 kẹo mút"
    LOLLIPOP_FARM_EXTRA_50 = "Vườn kẹo mút: Trồng 50 kẹo mút"
    LOLLIPOP_FARM_EXTRA_51 = "Vườn kẹo mút: Trồng 51 kẹo mút"
    LOLLIPOP_FARM_EXTRA_52 = "Vườn kẹo mút: Trồng 52 kẹo mút"
    LOLLIPOP_FARM_EXTRA_53 = "Vườn kẹo mút: Trồng 53 kẹo mút"
    LOLLIPOP_FARM_EXTRA_54 = "Vườn kẹo mút: Trồng 54 kẹo mút"
    LOLLIPOP_FARM_EXTRA_55 = "Vườn kẹo mút: Trồng 55 kẹo mút"
    LOLLIPOP_FARM_EXTRA_56 = "Vườn kẹo mút: Trồng 56 kẹo mút"
    LOLLIPOP_FARM_EXTRA_57 = "Vườn kẹo mút: Trồng 57 kẹo mút"
    LOLLIPOP_FARM_EXTRA_58 = "Vườn kẹo mút: Trồng 58 kẹo mút"
    LOLLIPOP_FARM_EXTRA_59 = "Vườn kẹo mút: Trồng 59 kẹo mút"
    LOLLIPOP_FARM_EXTRA_60 = "Vườn kẹo mút: Trồng 60 kẹo mút"
    LOLLIPOP_FARM_EXTRA_61 = "Vườn kẹo mút: Trồng 61 kẹo mút"
    LOLLIPOP_FARM_EXTRA_62 = "Vườn kẹo mút: Trồng 62 kẹo mút"
    LOLLIPOP_FARM_EXTRA_63 = "Vườn kẹo mút: Trồng 63 kẹo mút"
    LOLLIPOP_FARM_EXTRA_64 = "Vườn kẹo mút: Trồng 64 kẹo mút"
    LOLLIPOP_FARM_EXTRA_65 = "Vườn kẹo mút: Trồng 65 kẹo mút"
    LOLLIPOP_FARM_EXTRA_66 = "Vườn kẹo mút: Trồng 66 kẹo mút"
    LOLLIPOP_FARM_EXTRA_67 = "Vườn kẹo mút: Trồng 67 kẹo mút"
    LOLLIPOP_FARM_EXTRA_68 = "Vườn kẹo mút: Trồng 68 kẹo mút"
    LOLLIPOP_FARM_EXTRA_69 = "Vườn kẹo mút: Trồng 69 kẹo mút"
    LOLLIPOP_FARM_EXTRA_70 = "Vườn kẹo mút: Trồng 70 kẹo mút"
    LOLLIPOP_FARM_EXTRA_71 = "Vườn kẹo mút: Trồng 71 kẹo mút"
    LOLLIPOP_FARM_EXTRA_72 = "Vườn kẹo mút: Trồng 72 kẹo mút"
    LOLLIPOP_FARM_EXTRA_73 = "Vườn kẹo mút: Trồng 73 kẹo mút"
    LOLLIPOP_FARM_EXTRA_74 = "Vườn kẹo mút: Trồng 74 kẹo mút"
    LOLLIPOP_FARM_EXTRA_75 = "Vườn kẹo mút: Trồng 75 kẹo mút"
    LOLLIPOP_FARM_EXTRA_76 = "Vườn kẹo mút: Trồng 76 kẹo mút"
    LOLLIPOP_FARM_EXTRA_77 = "Vườn kẹo mút: Trồng 77 kẹo mút"
    LOLLIPOP_FARM_EXTRA_78 = "Vườn kẹo mút: Trồng 78 kẹo mút"
    LOLLIPOP_FARM_EXTRA_79 = "Vườn kẹo mút: Trồng 79 kẹo mút"
    LOLLIPOP_FARM_EXTRA_80 = "Vườn kẹo mút: Trồng 80 kẹo mút"
    LOLLIPOP_FARM_EXTRA_81 = "Vườn kẹo mút: Trồng 81 kẹo mút"
    LOLLIPOP_FARM_EXTRA_82 = "Vườn kẹo mút: Trồng 82 kẹo mút"
    LOLLIPOP_FARM_EXTRA_83 = "Vườn kẹo mút: Trồng 83 kẹo mút"
    LOLLIPOP_FARM_EXTRA_84 = "Vườn kẹo mút: Trồng 84 kẹo mút"
    LOLLIPOP_FARM_EXTRA_85 = "Vườn kẹo mút: Trồng 85 kẹo mút"
    LOLLIPOP_FARM_EXTRA_86 = "Vườn kẹo mút: Trồng 86 kẹo mút"
    LOLLIPOP_FARM_EXTRA_87 = "Vườn kẹo mút: Trồng 87 kẹo mút"
    LOLLIPOP_FARM_EXTRA_88 = "Vườn kẹo mút: Trồng 88 kẹo mút"
    LOLLIPOP_FARM_EXTRA_89 = "Vườn kẹo mút: Trồng 89 kẹo mút"
    LOLLIPOP_FARM_EXTRA_90 = "Vườn kẹo mút: Trồng 90 kẹo mút"
    LOLLIPOP_FARM_EXTRA_91 = "Vườn kẹo mút: Trồng 91 kẹo mút"
    LOLLIPOP_FARM_EXTRA_92 = "Vườn kẹo mút: Trồng 92 kẹo mút"
    LOLLIPOP_FARM_EXTRA_93 = "Vườn kẹo mút: Trồng 93 kẹo mút"
    LOLLIPOP_FARM_EXTRA_94 = "Vườn kẹo mút: Trồng 94 kẹo mút"
    LOLLIPOP_FARM_EXTRA_95 = "Vườn kẹo mút: Trồng 95 kẹo mút"
    LOLLIPOP_FARM_EXTRA_96 = "Vườn kẹo mút: Trồng 96 kẹo mút"
    LOLLIPOP_FARM_EXTRA_97 = "Vườn kẹo mút: Trồng 97 kẹo mút"
    LOLLIPOP_FARM_EXTRA_98 = "Vườn kẹo mút: Trồng 98 kẹo mút"
    LOLLIPOP_FARM_EXTRA_99 = "Vườn kẹo mút: Trồng 99 kẹo mút"
    LOLLIPOP_FARM_EXTRA_100 = "Vườn kẹo mút: Trồng 100 kẹo mút"
    LOLLIPOP_FARM_EXTRA_101 = "Vườn kẹo mút: Trồng 1000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_102 = "Vườn kẹo mút: Trồng 2000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_103 = "Vườn kẹo mút: Trồng 3000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_104 = "Vườn kẹo mút: Trồng 4000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_105 = "Vườn kẹo mút: Trồng 5000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_106 = "Vườn kẹo mút: Trồng 6000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_107 = "Vườn kẹo mút: Trồng 7000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_108 = "Vườn kẹo mút: Trồng 8000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_109 = "Vườn kẹo mút: Trồng 9000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_110 = "Vườn kẹo mút: Trồng 10000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_111 = "Vườn kẹo mút: Trồng 11000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_112 = "Vườn kẹo mút: Trồng 12000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_113 = "Vườn kẹo mút: Trồng 13000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_114 = "Vườn kẹo mút: Trồng 14000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_115 = "Vườn kẹo mút: Trồng 15000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_116 = "Vườn kẹo mút: Trồng 16000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_117 = "Vườn kẹo mút: Trồng 17000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_118 = "Vườn kẹo mút: Trồng 18000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_119 = "Vườn kẹo mút: Trồng 19000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_120 = "Vườn kẹo mút: Trồng 20000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_121 = "Vườn kẹo mút: Trồng 21000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_122 = "Vườn kẹo mút: Trồng 22000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_123 = "Vườn kẹo mút: Trồng 23000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_124 = "Vườn kẹo mút: Trồng 24000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_125 = "Vườn kẹo mút: Trồng 25000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_126 = "Vườn kẹo mút: Trồng 26000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_127 = "Vườn kẹo mút: Trồng 27000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_128 = "Vườn kẹo mút: Trồng 28000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_129 = "Vườn kẹo mút: Trồng 29000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_130 = "Vườn kẹo mút: Trồng 30000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_131 = "Vườn kẹo mút: Trồng 31000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_132 = "Vườn kẹo mút: Trồng 32000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_133 = "Vườn kẹo mút: Trồng 33000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_134 = "Vườn kẹo mút: Trồng 34000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_135 = "Vườn kẹo mút: Trồng 35000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_136 = "Vườn kẹo mút: Trồng 36000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_137 = "Vườn kẹo mút: Trồng 37000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_138 = "Vườn kẹo mút: Trồng 38000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_139 = "Vườn kẹo mút: Trồng 39000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_140 = "Vườn kẹo mút: Trồng 40000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_141 = "Vườn kẹo mút: Trồng 41000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_142 = "Vườn kẹo mút: Trồng 42000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_143 = "Vườn kẹo mút: Trồng 43000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_144 = "Vườn kẹo mút: Trồng 44000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_145 = "Vườn kẹo mút: Trồng 45000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_146 = "Vườn kẹo mút: Trồng 46000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_147 = "Vườn kẹo mút: Trồng 47000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_148 = "Vườn kẹo mút: Trồng 48000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_149 = "Vườn kẹo mút: Trồng 49000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_150 = "Vườn kẹo mút: Trồng 50000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_151 = "Vườn kẹo mút: Trồng 51000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_152 = "Vườn kẹo mút: Trồng 52000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_153 = "Vườn kẹo mút: Trồng 53000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_154 = "Vườn kẹo mút: Trồng 54000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_155 = "Vườn kẹo mút: Trồng 55000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_156 = "Vườn kẹo mút: Trồng 56000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_157 = "Vườn kẹo mút: Trồng 57000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_158 = "Vườn kẹo mút: Trồng 58000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_159 = "Vườn kẹo mút: Trồng 59000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_160 = "Vườn kẹo mút: Trồng 60000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_161 = "Vườn kẹo mút: Trồng 61000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_162 = "Vườn kẹo mút: Trồng 62000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_163 = "Vườn kẹo mút: Trồng 63000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_164 = "Vườn kẹo mút: Trồng 64000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_165 = "Vườn kẹo mút: Trồng 65000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_166 = "Vườn kẹo mút: Trồng 66000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_167 = "Vườn kẹo mút: Trồng 67000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_168 = "Vườn kẹo mút: Trồng 68000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_169 = "Vườn kẹo mút: Trồng 69000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_170 = "Vườn kẹo mút: Trồng 70000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_171 = "Vườn kẹo mút: Trồng 71000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_172 = "Vườn kẹo mút: Trồng 72000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_173 = "Vườn kẹo mút: Trồng 73000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_174 = "Vườn kẹo mút: Trồng 74000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_175 = "Vườn kẹo mút: Trồng 75000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_176 = "Vườn kẹo mút: Trồng 76000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_177 = "Vườn kẹo mút: Trồng 77000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_178 = "Vườn kẹo mút: Trồng 78000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_179 = "Vườn kẹo mút: Trồng 79000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_180 = "Vườn kẹo mút: Trồng 80000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_181 = "Vườn kẹo mút: Trồng 81000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_182 = "Vườn kẹo mút: Trồng 82000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_183 = "Vườn kẹo mút: Trồng 83000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_184 = "Vườn kẹo mút: Trồng 84000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_185 = "Vườn kẹo mút: Trồng 85000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_186 = "Vườn kẹo mút: Trồng 86000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_187 = "Vườn kẹo mút: Trồng 87000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_188 = "Vườn kẹo mút: Trồng 88000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_189 = "Vườn kẹo mút: Trồng 89000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_190 = "Vườn kẹo mút: Trồng 90000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_191 = "Vườn kẹo mút: Trồng 91000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_192 = "Vườn kẹo mút: Trồng 92000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_193 = "Vườn kẹo mút: Trồng 93000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_194 = "Vườn kẹo mút: Trồng 94000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_195 = "Vườn kẹo mút: Trồng 95000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_196 = "Vườn kẹo mút: Trồng 96000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_197 = "Vườn kẹo mút: Trồng 97000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_198 = "Vườn kẹo mút: Trồng 98000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_199 = "Vườn kẹo mút: Trồng 99000 kẹo mút"
    LOLLIPOP_FARM_EXTRA_200 = "Vườn kẹo mút: Trồng 100000 kẹo mút"
    THE_SEA_EXTRA_1 = "Đại dương: Bơi 50m"
    THE_SEA_EXTRA_2 = "Đại dương: Bơi 100m"
    THE_SEA_EXTRA_3 = "Đại dương: Bơi 150m"
    THE_SEA_EXTRA_4 = "Đại dương: Bơi 200m"
    THE_SEA_EXTRA_5 = "Đại dương: Bơi 250m"
    THE_SEA_EXTRA_6 = "Đại dương: Bơi 300m"
    THE_SEA_EXTRA_7 = "Đại dương: Bơi 350m"
    THE_SEA_EXTRA_8 = "Đại dương: Bơi 400m"
    THE_SEA_EXTRA_9 = "Đại dương: Bơi 450m"
    THE_SEA_EXTRA_10 = "Đại dương: Bơi 500m"
    THE_SEA_EXTRA_11 = "Đại dương: Bơi 550m"
    THE_SEA_EXTRA_12 = "Đại dương: Bơi 600m"
    THE_SEA_EXTRA_13 = "Đại dương: Bơi 650m"
    THE_SEA_EXTRA_14 = "Đại dương: Bơi 700m"
    THE_SEA_EXTRA_15 = "Đại dương: Bơi 750m"
    THE_SEA_EXTRA_16 = "Đại dương: Bơi 800m"
    THE_SEA_EXTRA_17 = "Đại dương: Bơi 850m"
    THE_SEA_EXTRA_18 = "Đại dương: Bơi 900m"
    THE_SEA_EXTRA_19 = "Đại dương: Bơi 950m"
    THE_SEA_EXTRA_20 = "Đại dương: Bơi 1000m"
    THE_SEA_EXTRA_21 = "Đại dương: Bơi 1050m"
    THE_SEA_EXTRA_22 = "Đại dương: Bơi 1100m"
    THE_SEA_EXTRA_23 = "Đại dương: Bơi 1150m"
    THE_SEA_EXTRA_24 = "Đại dương: Bơi 1200m"
    THE_SEA_EXTRA_25 = "Đại dương: Bơi 1250m"
    THE_SEA_EXTRA_26 = "Đại dương: Bơi 1300m"
    THE_SEA_EXTRA_27 = "Đại dương: Bơi 1350m"
    THE_SEA_EXTRA_28 = "Đại dương: Bơi 1400m"
    THE_SEA_EXTRA_29 = "Đại dương: Bơi 1450m"
    THE_SEA_EXTRA_30 = "Đại dương: Bơi 1500m"
    THE_SEA_EXTRA_31 = "Đại dương: Bơi 1550m"
    THE_SEA_EXTRA_32 = "Đại dương: Bơi 1600m"
    THE_SEA_EXTRA_33 = "Đại dương: Bơi 1650m"
    THE_SEA_EXTRA_34 = "Đại dương: Bơi 1700m"
    THE_SEA_EXTRA_35 = "Đại dương: Bơi 1750m"
    THE_SEA_EXTRA_36 = "Đại dương: Bơi 1800m"
    THE_SEA_EXTRA_37 = "Đại dương: Bơi 1850m"
    THE_SEA_EXTRA_38 = "Đại dương: Bơi 1900m"
    THE_SEA_EXTRA_39 = "Đại dương: Bơi 1950m"
    THE_SEA_EXTRA_40 = "Đại dương: Bơi 2000m"
    THE_SEA_EXTRA_41 = "Đại dương: Bơi 2050m"
    THE_SEA_EXTRA_42 = "Đại dương: Bơi 2100m"
    THE_SEA_EXTRA_43 = "Đại dương: Bơi 2150m"
    THE_SEA_EXTRA_44 = "Đại dương: Bơi 2200m"
    THE_SEA_EXTRA_45 = "Đại dương: Bơi 2250m"
    THE_SEA_EXTRA_46 = "Đại dương: Bơi 2300m"
    THE_SEA_EXTRA_47 = "Đại dương: Bơi 2350m"
    THE_SEA_EXTRA_48 = "Đại dương: Bơi 2400m"
    THE_SEA_EXTRA_49 = "Đại dương: Bơi 2450m"
    THE_SEA_EXTRA_50 = "Đại dương: Bơi 2500m"
    THE_SEA_EXTRA_51 = "Đại dương: Bơi 2550m"
    THE_SEA_EXTRA_52 = "Đại dương: Bơi 2600m"
    THE_SEA_EXTRA_53 = "Đại dương: Bơi 2650m"
    THE_SEA_EXTRA_54 = "Đại dương: Bơi 2700m"
    THE_SEA_EXTRA_55 = "Đại dương: Bơi 2750m"
    THE_SEA_EXTRA_56 = "Đại dương: Bơi 2800m"
    THE_SEA_EXTRA_57 = "Đại dương: Bơi 2850m"
    THE_SEA_EXTRA_58 = "Đại dương: Bơi 2900m"
    THE_SEA_EXTRA_59 = "Đại dương: Bơi 2950m"
    THE_SEA_EXTRA_60 = "Đại dương: Bơi 3000m"
    THE_SEA_EXTRA_61 = "Đại dương: Bơi 3050m"
    THE_SEA_EXTRA_62 = "Đại dương: Bơi 3100m"
    THE_SEA_EXTRA_63 = "Đại dương: Bơi 3150m"
    THE_SEA_EXTRA_64 = "Đại dương: Bơi 3200m"
    THE_SEA_EXTRA_65 = "Đại dương: Bơi 3250m"
    THE_SEA_EXTRA_66 = "Đại dương: Bơi 3300m"
    THE_SEA_EXTRA_67 = "Đại dương: Bơi 3350m"
    THE_SEA_EXTRA_68 = "Đại dương: Bơi 3400m"
    THE_SEA_EXTRA_69 = "Đại dương: Bơi 3450m"
    THE_SEA_EXTRA_70 = "Đại dương: Bơi 3500m"
    THE_SEA_EXTRA_71 = "Đại dương: Bơi 3550m"
    THE_SEA_EXTRA_72 = "Đại dương: Bơi 3600m"
    THE_SEA_EXTRA_73 = "Đại dương: Bơi 3650m"
    THE_SEA_EXTRA_74 = "Đại dương: Bơi 3700m"
    THE_SEA_EXTRA_75 = "Đại dương: Bơi 3750m"
    THE_SEA_EXTRA_76 = "Đại dương: Bơi 3800m"
    THE_SEA_EXTRA_77 = "Đại dương: Bơi 3850m"
    THE_SEA_EXTRA_78 = "Đại dương: Bơi 3900m"
    THE_SEA_EXTRA_79 = "Đại dương: Bơi 3950m"
    THE_SEA_EXTRA_80 = "Đại dương: Bơi 4000m"


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
    CandyBox2LocationName.POGO_STICK: CandyBox2LocationData(500),
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
    CandyBox2LocationName.SORCERESS_HUT_BEGINNERS_GRIMOIRE: CandyBox2LocationData(1801),
    CandyBox2LocationName.SORCERESS_HUT_ADVANCED_GRIMOIRE: CandyBox2LocationData(1802),
    CandyBox2LocationName.SORCERESS_HUT_CAULDRON: CandyBox2LocationData(1803),
    CandyBox2LocationName.SORCERESS_HUT_HAT: CandyBox2LocationData(1804),
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
    CandyBox2LocationName.THE_HOLE_BLACK_MAGIC_GRIMOIRE_ACQUIRED: CandyBox2LocationData(3703),
    CandyBox2LocationName.THE_HOLE_FOUR_CHOCOLATE_BARS_ACQUIRED: CandyBox2LocationData(3704),
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
    CandyBox2LocationName.TALKING_CANDY: CandyBox2LocationData(5000),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_1: CandyBox2LocationData(100000),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_2: CandyBox2LocationData(100001),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_3: CandyBox2LocationData(100002),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_4: CandyBox2LocationData(100003),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_5: CandyBox2LocationData(100004),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_6: CandyBox2LocationData(100005),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_7: CandyBox2LocationData(100006),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_8: CandyBox2LocationData(100007),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_9: CandyBox2LocationData(100008),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_10: CandyBox2LocationData(100009),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_11: CandyBox2LocationData(100010),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_12: CandyBox2LocationData(100011),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_13: CandyBox2LocationData(100012),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_14: CandyBox2LocationData(100013),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_15: CandyBox2LocationData(100014),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_16: CandyBox2LocationData(100015),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_17: CandyBox2LocationData(100016),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_18: CandyBox2LocationData(100017),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_19: CandyBox2LocationData(100018),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_20: CandyBox2LocationData(100019),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_21: CandyBox2LocationData(100020),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_22: CandyBox2LocationData(100021),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_23: CandyBox2LocationData(100022),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_24: CandyBox2LocationData(100023),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_25: CandyBox2LocationData(100024),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_26: CandyBox2LocationData(100025),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_27: CandyBox2LocationData(100026),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_28: CandyBox2LocationData(100027),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_29: CandyBox2LocationData(100028),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_30: CandyBox2LocationData(100029),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_31: CandyBox2LocationData(100030),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_32: CandyBox2LocationData(100031),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_33: CandyBox2LocationData(100032),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_34: CandyBox2LocationData(100033),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_35: CandyBox2LocationData(100034),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_36: CandyBox2LocationData(100035),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_37: CandyBox2LocationData(100036),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_38: CandyBox2LocationData(100037),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_39: CandyBox2LocationData(100038),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_40: CandyBox2LocationData(100039),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_41: CandyBox2LocationData(100040),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_42: CandyBox2LocationData(100041),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_43: CandyBox2LocationData(100042),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_44: CandyBox2LocationData(100043),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_45: CandyBox2LocationData(100044),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_46: CandyBox2LocationData(100045),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_47: CandyBox2LocationData(100046),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_48: CandyBox2LocationData(100047),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_49: CandyBox2LocationData(100048),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_50: CandyBox2LocationData(100049),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_51: CandyBox2LocationData(100050),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_52: CandyBox2LocationData(100051),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_53: CandyBox2LocationData(100052),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_54: CandyBox2LocationData(100053),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_55: CandyBox2LocationData(100054),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_56: CandyBox2LocationData(100055),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_57: CandyBox2LocationData(100056),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_58: CandyBox2LocationData(100057),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_59: CandyBox2LocationData(100058),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_60: CandyBox2LocationData(100059),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_61: CandyBox2LocationData(100060),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_62: CandyBox2LocationData(100061),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_63: CandyBox2LocationData(100062),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_64: CandyBox2LocationData(100063),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_65: CandyBox2LocationData(100064),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_66: CandyBox2LocationData(100065),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_67: CandyBox2LocationData(100066),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_68: CandyBox2LocationData(100067),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_69: CandyBox2LocationData(100068),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_70: CandyBox2LocationData(100069),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_71: CandyBox2LocationData(100070),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_72: CandyBox2LocationData(100071),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_73: CandyBox2LocationData(100072),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_74: CandyBox2LocationData(100073),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_75: CandyBox2LocationData(100074),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_76: CandyBox2LocationData(100075),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_77: CandyBox2LocationData(100076),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_78: CandyBox2LocationData(100077),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_79: CandyBox2LocationData(100078),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_80: CandyBox2LocationData(100079),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_81: CandyBox2LocationData(100080),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_82: CandyBox2LocationData(100081),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_83: CandyBox2LocationData(100082),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_84: CandyBox2LocationData(100083),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_85: CandyBox2LocationData(100084),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_86: CandyBox2LocationData(100085),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_87: CandyBox2LocationData(100086),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_88: CandyBox2LocationData(100087),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_89: CandyBox2LocationData(100088),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_90: CandyBox2LocationData(100089),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_91: CandyBox2LocationData(100090),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_92: CandyBox2LocationData(100091),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_93: CandyBox2LocationData(100092),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_94: CandyBox2LocationData(100093),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_95: CandyBox2LocationData(100094),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_96: CandyBox2LocationData(100095),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_97: CandyBox2LocationData(100096),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_98: CandyBox2LocationData(100097),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_99: CandyBox2LocationData(100098),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_100: CandyBox2LocationData(100099),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_101: CandyBox2LocationData(100100),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_102: CandyBox2LocationData(100101),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_103: CandyBox2LocationData(100102),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_104: CandyBox2LocationData(100103),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_105: CandyBox2LocationData(100104),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_106: CandyBox2LocationData(100105),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_107: CandyBox2LocationData(100106),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_108: CandyBox2LocationData(100107),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_109: CandyBox2LocationData(100108),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_110: CandyBox2LocationData(100109),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_111: CandyBox2LocationData(100110),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_112: CandyBox2LocationData(100111),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_113: CandyBox2LocationData(100112),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_114: CandyBox2LocationData(100113),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_115: CandyBox2LocationData(100114),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_116: CandyBox2LocationData(100115),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_117: CandyBox2LocationData(100116),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_118: CandyBox2LocationData(100117),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_119: CandyBox2LocationData(100118),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_120: CandyBox2LocationData(100119),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_121: CandyBox2LocationData(100120),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_122: CandyBox2LocationData(100121),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_123: CandyBox2LocationData(100122),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_124: CandyBox2LocationData(100123),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_125: CandyBox2LocationData(100124),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_126: CandyBox2LocationData(100125),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_127: CandyBox2LocationData(100126),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_128: CandyBox2LocationData(100127),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_129: CandyBox2LocationData(100128),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_130: CandyBox2LocationData(100129),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_131: CandyBox2LocationData(100130),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_132: CandyBox2LocationData(100131),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_133: CandyBox2LocationData(100132),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_134: CandyBox2LocationData(100133),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_135: CandyBox2LocationData(100134),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_136: CandyBox2LocationData(100135),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_137: CandyBox2LocationData(100136),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_138: CandyBox2LocationData(100137),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_139: CandyBox2LocationData(100138),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_140: CandyBox2LocationData(100139),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_141: CandyBox2LocationData(100140),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_142: CandyBox2LocationData(100141),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_143: CandyBox2LocationData(100142),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_144: CandyBox2LocationData(100143),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_145: CandyBox2LocationData(100144),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_146: CandyBox2LocationData(100145),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_147: CandyBox2LocationData(100146),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_148: CandyBox2LocationData(100147),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_149: CandyBox2LocationData(100148),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_150: CandyBox2LocationData(100149),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_151: CandyBox2LocationData(100150),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_152: CandyBox2LocationData(100151),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_153: CandyBox2LocationData(100152),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_154: CandyBox2LocationData(100153),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_155: CandyBox2LocationData(100154),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_156: CandyBox2LocationData(100155),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_157: CandyBox2LocationData(100156),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_158: CandyBox2LocationData(100157),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_159: CandyBox2LocationData(100158),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_160: CandyBox2LocationData(100159),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_161: CandyBox2LocationData(100160),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_162: CandyBox2LocationData(100161),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_163: CandyBox2LocationData(100162),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_164: CandyBox2LocationData(100163),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_165: CandyBox2LocationData(100164),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_166: CandyBox2LocationData(100165),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_167: CandyBox2LocationData(100166),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_168: CandyBox2LocationData(100167),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_169: CandyBox2LocationData(100168),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_170: CandyBox2LocationData(100169),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_171: CandyBox2LocationData(100170),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_172: CandyBox2LocationData(100171),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_173: CandyBox2LocationData(100172),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_174: CandyBox2LocationData(100173),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_175: CandyBox2LocationData(100174),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_176: CandyBox2LocationData(100175),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_177: CandyBox2LocationData(100176),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_178: CandyBox2LocationData(100177),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_179: CandyBox2LocationData(100178),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_180: CandyBox2LocationData(100179),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_181: CandyBox2LocationData(100180),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_182: CandyBox2LocationData(100181),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_183: CandyBox2LocationData(100182),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_184: CandyBox2LocationData(100183),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_185: CandyBox2LocationData(100184),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_186: CandyBox2LocationData(100185),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_187: CandyBox2LocationData(100186),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_188: CandyBox2LocationData(100187),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_189: CandyBox2LocationData(100188),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_190: CandyBox2LocationData(100189),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_191: CandyBox2LocationData(100190),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_192: CandyBox2LocationData(100191),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_193: CandyBox2LocationData(100192),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_194: CandyBox2LocationData(100193),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_195: CandyBox2LocationData(100194),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_196: CandyBox2LocationData(100195),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_197: CandyBox2LocationData(100196),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_198: CandyBox2LocationData(100197),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_199: CandyBox2LocationData(100198),
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_200: CandyBox2LocationData(100199),
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
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_9,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_10,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_11,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_12,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_13,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_14,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_15,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_16,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_17,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_18,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_19,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_20,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_21,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_22,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_23,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_24,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_25,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_26,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_27,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_28,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_29,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_30,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_31,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_32,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_33,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_34,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_35,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_36,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_37,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_38,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_39,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_40,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_41,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_42,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_43,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_44,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_45,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_46,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_47,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_48,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_49,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_50,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_51,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_52,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_53,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_54,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_55,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_56,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_57,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_58,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_59,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_60,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_61,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_62,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_63,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_64,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_65,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_66,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_67,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_68,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_69,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_70,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_71,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_72,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_73,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_74,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_75,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_76,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_77,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_78,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_79,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_80,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_81,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_82,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_83,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_84,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_85,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_86,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_87,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_88,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_89,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_90,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_91,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_92,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_93,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_94,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_95,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_96,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_97,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_98,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_99,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_100,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_101,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_102,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_103,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_104,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_105,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_106,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_107,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_108,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_109,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_110,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_111,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_112,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_113,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_114,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_115,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_116,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_117,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_118,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_119,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_120,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_121,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_122,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_123,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_124,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_125,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_126,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_127,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_128,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_129,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_130,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_131,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_132,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_133,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_134,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_135,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_136,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_137,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_138,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_139,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_140,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_141,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_142,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_143,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_144,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_145,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_146,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_147,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_148,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_149,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_150,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_151,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_152,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_153,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_154,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_155,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_156,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_157,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_158,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_159,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_160,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_161,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_162,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_163,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_164,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_165,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_166,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_167,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_168,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_169,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_170,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_171,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_172,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_173,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_174,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_175,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_176,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_177,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_178,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_179,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_180,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_181,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_182,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_183,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_184,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_185,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_186,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_187,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_188,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_189,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_190,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_191,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_192,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_193,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_194,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_195,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_196,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_197,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_198,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_199,
    CandyBox2LocationName.LOLLIPOP_FARM_EXTRA_200,
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

def generate_filter_categories():
    lollipop_farm = lollipop_farm_filler_locations.copy()
    the_sea = the_sea_filler_locations.copy()

    return [
        # Make the lollipop farm more likely
        lollipop_farm,
        lollipop_farm,
        the_sea
    ]

def extra_location_count(world: "CandyBox2World"):
    extras = 0
    extras += world.font_traps

    if world.grimoires == 2:
        # Individual spells add extra locations for each extra spell that can be obtained
        extras += 4

    if world.options.goal_conditions.value[GoalConditions.PLAY_STONES] == 0:
        # We don't have the talking candy location, but we still have the item
        extras -= 1

    return extras
