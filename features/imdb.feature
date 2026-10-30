Feature: Busqueda de peliculas en IMDb
    Scenario: Buscar una pelicula y validar su calificacion
        Given El usuario se encuentra en la pagina principal de IMDb
        When El usuario busca la pelicula "Pulp Fiction"
        And El usuario abre el primer resultado
        Then Se muestra la pagina de la pelicula "Pulp Fiction"
        And Se muestra la calificacion de la pelicula
