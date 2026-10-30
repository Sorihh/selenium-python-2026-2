Feature: Login feature
    Scenario: Ingresar con un nombre unico a la lobby
        Given El usuario se encuentra en la pagina de login
        When El usuario ingresa con el nombre "SORI"
        Then El nombre del usuario "SORI" aparece en el dashboard

    Scenario: Validar mensaje de error con un nombre que contiene espacios
        Given El usuario se encuentra en la pagina de login
        When El usuario intenta ingresar con un nombre con espacios "Juan Soriano"
        Then Se muestra el mensaje de error "Usa entre 3 y 20 caracteres"
        And El usuario sigue en la pagina de login