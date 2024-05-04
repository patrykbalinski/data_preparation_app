import csv
import json
from dataclasses import dataclass

from models.submodels import Keyword


@dataclass
class Keywords:
    movie_id: int
    keywords: [Keyword]

    @classmethod
    def load_from_csv(cls, file_path):
        keywords_list = []
        with open(file_path, 'r', encoding='utf8') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip the header row
            for i, row in enumerate(csv_reader):
                id, keywords = row
                keyword = cls(id, keywords)
                keywords_list.append(keyword)
        return keywords_list

    def to_json(self, fields: [str] = 'all'):
        if fields == 'all':
            return json.dumps(self.__dict__, indent=2)
        else:
            output_dict = {}
            for field in fields:
                output_dict[field] = self.__dict__[field]
            return json.dumps(output_dict, indent=2)
