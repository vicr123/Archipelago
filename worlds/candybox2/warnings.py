import logging
from abc import ABC, abstractmethod
from textwrap import dedent, TextWrapper
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import CandyBox2World

class CandyBox2Warning(ABC):
    world: "CandyBox2World | None"

    def __init__(self, world: "CandyBox2World | None"):
        self.world = world

    def issue_warning(self):
        prefix = self.get_prefix()
        wrapper = TextWrapper(
            width=100,
            subsequent_indent=" " * len(prefix)
        )

        logging.warning("\n".join(wrapper.wrap(prefix + self.warning_text())))

    def get_prefix(self):
        prefix = "Candy Box 2: "

        if self.world:
            prefix += f"{self.world.player_name}: "

        prefix += f"<!> [{self.warning_code()}]"

        return prefix

    @abstractmethod
    def warning_text(self) -> str:
        return ""

    @abstractmethod
    def warning_code(self) -> str:
        return ""

    def __lt__(self, other):
        if self.world is None:
            if other.world is None:
                return False
            return True
        else:
            if other.world is None:
                return True
            return self.world.player < other.world.player


class CandyBox2UnstableApworldWarning(CandyBox2Warning):
    def __init__(self):
        super().__init__(None)

    def warning_text(self):
        warning = """
        You are generating this game using a non-stable version of the apworld.
        If you plan to play this game with an async, it is recommended that you go back
        and use the stable version. If you decide to continue anyway, when you start
        the game, bookmark the "Permalink to this version" in the bottom left corner of
        the game, and ensure you use this version to play.
        """
        return dedent(warning)

    def warning_code(self) -> str:
        return "CB2-9001"

class CandyBox2NoGoalConditionWarning(CandyBox2Warning):
    def __init__(self, world: "CandyBox2World"):
        super().__init__(world)

    def warning_text(self):
        warning = """
        The YAML has caused no goal condition to be set on the current seed.
        The goal condition to obtain the PLAY stones has been forcibly enabled. 
        """
        return dedent(warning)

    def warning_code(self) -> str:
        return "CB2-1001"