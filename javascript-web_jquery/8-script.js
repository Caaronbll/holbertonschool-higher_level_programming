$('document').ready(function () {
    const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
    $.get(url, function (data) {
        $.each(data.results, function (i, movie) {
            $('#list_movies').appeend('<li>' + movie.title + '</li>');
        });
    });
});