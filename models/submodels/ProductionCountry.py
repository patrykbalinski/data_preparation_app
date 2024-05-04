from dataclasses import dataclass


@dataclass
class ProductionCountry:
    iso_3166_1: str
    name: str
