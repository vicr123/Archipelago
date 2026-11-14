from enum import StrEnum


class GoalCondition(StrEnum):
    PLAY_STONES = "Obtain the PLAY Stones"
    DIE_TO_CASTLE_TRAP_ROOM = "Die to the Castle Trap Room at least once"
    SWIM_3000_METERS = "Swim 3000 meters"