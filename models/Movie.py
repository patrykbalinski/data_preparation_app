import csv
import json
from dataclasses import dataclass

from models.submodels import MovieCollection, Genre, ProductionCompany, ProductionCountry, SpokenLanguage


@dataclass
class Movie:
    adult: str
    belongs_to_collection: MovieCollection
    budget: int
    genres: [Genre]
    homepage: str
    id: int
    imdb_id: str
    original_language: str
    original_title: str
    overview: str
    popularity: float
    poster_path: str
    production_companies: [ProductionCompany]
    production_countries: [ProductionCountry]
    release_date: str  # TODO: change to date type
    revenue: int
    runtime: float
    spoken_languages: [SpokenLanguage]
    status: str
    tagline: str
    title: str
    video: bool
    vote_average: float
    vote_count: int

    @classmethod
    def load_from_csv(cls, file_path):
        movies = []
        with open(file_path, 'r', encoding='utf8') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip the header row
            for i, row in enumerate(csv_reader):
                adult, belongs_to_collection, budget, genres, homepage, id, imdb_id, original_language, original_title, overview, popularity, poster_path, production_companies, production_countries, release_date, revenue, runtime, spoken_languages, status, tagline, title, video, vote_average, vote_count = row
                movie = cls(adult, belongs_to_collection, budget, genres, homepage, id, imdb_id, original_language, original_title, overview, popularity, poster_path, production_companies, production_countries, release_date, revenue, runtime, spoken_languages, status, tagline, title, video, vote_average, vote_count)
                movies.append(movie)
        return movies

    def to_json(self, fields: [str] = 'all'):
        if fields == 'all':
            return json.dumps(self.__dict__, indent=2)
        else:
            output_dict = {}
            for field in fields:
                output_dict[field] = self.__dict__[field]
            return json.dumps(output_dict, indent=2)
