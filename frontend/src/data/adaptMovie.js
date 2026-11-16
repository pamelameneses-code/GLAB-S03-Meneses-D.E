export default function adaptMovie(record) {
  return {
    id: record.movie_id,
    title: record.original_title,
    image: record.poster_path,
    synopsis: record.overview,
    classification: record.age_rating,
    rating: record.vote_average,
    showtimes: [...record.screenings],
  }
}
