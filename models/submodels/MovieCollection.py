from dataclasses import dataclass


@dataclass
class MovieCollection:
    id: str
    name: str
    poster_path: str
    backdrop_path: str
