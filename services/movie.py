from db.models import Movie


def get_movies(genres_ids=None, actors_ids=None):
    if genres_ids is None and actors_ids is None:
        return Movie.objects.all()
    elif genres_ids is not None and actors_ids is not None:
        return Movie.objects.filter(
            genres__id__in=genres_ids, actors__id__in=actors_ids)
    elif genres_ids is not None and actors_ids is None:
        return Movie.objects.filter(genres__id__in=genres_ids)
    elif genres_ids is None and actors_ids is not None:
        return Movie.objects.filter(actors__id__in=actors_ids)


def get_movie_by_id(movie_id: int):
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title, movie_description,
                 genres_ids=None, actors_ids=None):
    film = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if genres_ids is not None:
        film.genres.add(*genres_ids)
    if actors_ids is not None:
        film.actors.add(*actors_ids)
