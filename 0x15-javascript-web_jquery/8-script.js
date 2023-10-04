$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    const movies = data.results;
    const listMovies = $('#list_movies');
    for (let i = 0; i < movies.length; i++) {
      listMovies.append('<li>' + movies[i].title + '</li>');
    }
  });
});
