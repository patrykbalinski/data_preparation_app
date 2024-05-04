from dataclasses import dataclass


@dataclass
class Cast:
    cast_id: int
    character: str
    credit_id: str
    gender: int
    id: int
    name: str
    order: int
    profile_path: str
