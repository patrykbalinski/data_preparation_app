from dataclasses import dataclass


@dataclass
class Crew:
    credit_id: str
    department: str
    gender: int
    id: int
    job: str
    name: str
    profile_path: str
