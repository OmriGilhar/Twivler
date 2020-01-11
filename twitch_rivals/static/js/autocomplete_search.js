 $('#autocomplete1').autocomplete({
    serviceUrl: '/search/names',
      dataType: 'json',
      onSearchComplete: function (query, suggestions) {
        console.log(query);
      }
    });

  $('#autocomplete2').autocomplete({
      serviceUrl: '/search/songs',
      dataType: 'json',
      onSearchComplete: function (query, suggestions) {
        console.log(query);
      }
  });
