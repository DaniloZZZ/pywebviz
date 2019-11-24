export get_nb_name=()->
  window.location.href.match(/nb_name=(.+)&?/)?[1]

