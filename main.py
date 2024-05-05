import consts.file_path

from models import *
from utils import *


def main():
    movies_list = sorted(Movie.load_from_csv(consts.file_path.movie), key=lambda x: int(x.id))
    keywords_list = sorted(Keywords.load_from_csv(consts.file_path.keywords), key=lambda x: int(x.movie_id))
    credits_list = sorted(Credits.load_from_csv(consts.file_path.credits), key=lambda x: int(x.movie_id))

    print(movies_list[0].to_json(
        fields=['id', 'title', 'overview', 'original_language', 'budget', 'popularity', 'release_date', 'runtime',
                'vote_average', 'vote_count', 'genres', 'production_countries', 'production_companies']))
    print(keywords_list[0].to_json())
    print(credits_list[0].to_json())

    save_json(movies_list, 'output_data/movies.json',
              fields=['id', 'title', 'overview', 'original_language', 'budget', 'popularity', 'release_date', 'runtime',
                      'vote_average', 'vote_count', 'genres', 'production_countries', 'production_companies'])
    save_json(keywords_list, 'output_data/keywords.json')
    save_json(credits_list, 'output_data/credits.json')


if __name__ == "__main__":
    main()
