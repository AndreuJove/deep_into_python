from dataclasses import dataclass


@dataclass
class DataClassCard:
    suit: str
    rank: str = "paco"
