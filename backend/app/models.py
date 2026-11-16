from dataclasses import dataclass, field
from enum import Enum
import time


class Phase(str, Enum):
    WAITING = "waiting"
    DISCUSSION = "discussion"
    VOTING = "voting"
    RESULTS = "results"


@dataclass
class Slot:
    player_id: str           # "A" | "B" | "C"
    kind: str                # "human" | "ai"  (فقط سمت سرور، هرگز به کلاینت نمی‌رود)
    joined: bool = False


@dataclass
class Message:
    player_id: str
    text: str
    round: int
    ts: float = field(default_factory=time.time)


@dataclass
class Result:
    winner: str
    counts: dict[str, int]       # جمع رأی نهایی
    tie_break: str               # "none" | "cumulative" | "random"
