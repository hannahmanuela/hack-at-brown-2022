from dataclasses import dataclass


@dataclass
class ESGScore:
    """Class for keeping track of an item in inventory."""

    environment: float
    social: float
    governance: float
    controversy: int
