$.ajax({
  url: 'https://swapi.co/api/films/?format=json',
  success: function (data) {
    data.results.forEach(film => {
      $('#list_movies').append(`<li>${film.title}</li>`);
    });
  }
});

