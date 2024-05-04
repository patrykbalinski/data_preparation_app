import consts.file_path
from models.Movie import Movie


def main():
    movies_list = Movie.load_from_csv(consts.file_path.movie)
    print(movies_list[0].to_json(fields=['id', 'title', 'original_title', 'genres']))


if __name__ == "__main__":
    main()
