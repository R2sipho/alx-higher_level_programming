$.ajax({
  url: 'https://swapi.co/api/people/5/?format=json',
  success: function (data, status) {
    $('#character').text(data.name);
  }
});

