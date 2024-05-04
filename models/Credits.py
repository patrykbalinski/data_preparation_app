import csv
import json
from dataclasses import dataclass

from models.submodels import Cast, Crew


@dataclass
class Credits:
    movie_id: int
    cast: [Cast]
    crew: [Crew]

    @classmethod
    def load_from_csv(cls, file_path):
        credits_list = []
        with open(file_path, 'r', encoding='utf8') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip the header row
            for i, row in enumerate(csv_reader):
                cast, crew, movie_id = row
                credit = cls(movie_id, cast, crew)
                credits_list.append(credit)
        return credits_list

    def to_json(self, fields: [str] = 'all'):
        if fields == 'all':
            return json.dumps(self.__dict__, indent=2)
        else:
            output_dict = {}
            for field in fields:
                output_dict[field] = self.__dict__[field]
            return json.dumps(output_dict, indent=2)
