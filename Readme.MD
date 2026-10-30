# Taller de automatización de pruebas: Selenium + Python + Behave

**Estudiante:** Juan David Soriano
**Fecha:** 29 de octubre de 2026
**Repositorio base:** [MrM0ra/selenium-python-2026-2](https://github.com/MrM0ra/selenium-python-2026-2)

Pruebas automatizadas de front-end escritas en **Gherkin**, ejecutadas con **Behave** y **Selenium** sobre Google Chrome, siguiendo el patrón **Page Object Model (POM)**.

---

## Estructura agregada al proyecto

```
selenium-python-2026-2/
├── features/
│   ├── lobby_login.feature          # Ejercicio 1
│   ├── imdb.feature                 # Ejercicio 2
│   └── steps/
│       ├── lobby_login_steps.py
│       └── imdb_search_steps.py
├── pages/
│   ├── base_page.py                 # (del repositorio base)
│   ├── lobby_login_page.py
│   ├── lobby_dashboard_page.py
│   ├── imdb_home_page.py
│   ├── imdb_results_page.py
│   └── imdb_movie_page.py
└── evidencias/
    └── imdb_resultado.png
```

Todas las páginas heredan de `BasePage` y usan sus métodos `find_element`, `find_elements`, `click` y `enter_text`.

---

## Ejercicio 1: Lobby global

**Sitio:** https://lobby-global.vercel.app/

| Página (POM) | Elementos | Selector |
|---|---|---|
| `LobbyLoginPage` | Campo de nombre | `By.ID, "username"` |
| | Botón "Entrar a la sala" | `By.ID, "btn-login"` |
| | Mensaje de error | `By.CLASS_NAME, "error-message"` |
| `LobbyDashboardPage` | Nombres de participantes | `By.CLASS_NAME, "participant-name"` |

```gherkin
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
```

---

## Ejercicio 2: Búsqueda en IMDb

**Sitio:** https://www.imdb.com

| Página (POM) | Elementos | Selector |
|---|---|---|
| `ImdbHomePage` | Buscador | `By.ID, "suggestion-search"` |
| | Botón de búsqueda | `By.ID, "suggestion-search-button"` |
| `ImdbResultsPage` | Primer resultado de títulos | `By.CSS_SELECTOR, '[data-testid="find-results-section-title"] a.ipc-title-link-wrapper'` |
| `ImdbMoviePage` | Título | `By.CSS_SELECTOR, '[data-testid="hero__primary-text"]'` |
| | Calificación | `By.CSS_SELECTOR, '[data-testid="hero-rating-bar__aggregate-rating__score"] span'` |

```gherkin
Feature: Busqueda de peliculas en IMDb
    Scenario: Buscar una pelicula y validar su calificacion
        Given El usuario se encuentra en la pagina principal de IMDb
        When El usuario busca la pelicula "Pulp Fiction"
        And El usuario abre el primer resultado
        Then Se muestra la pagina de la pelicula "Pulp Fiction"
        And Se muestra la calificacion de la pelicula
```

La calificación se valida como un número entre 0 y 10 (no un valor fijo), porque cambia con el tiempo.

### Problemas encontrados y cómo se resolvieron

- **IMDb pedía verificación de humano:** al detectar el navegador automatizado, IMDb mostraba una verificación y el buscador nunca aparecía (`TimeoutException`). Se resolvió completando la verificación manualmente en la ventana de Chrome durante la ejecución; después la prueba continuó sola. Si vuelve a aparecer, hay que resolverla dentro de los 20 segundos de espera de `BasePage`.
- **La calificación llegaba vacía (`''`):** IMDb tiene la barra de calificación duplicada (versión escritorio y móvil) y una está oculta. Se cambió `get_rating()` para recorrer todas las coincidencias con `find_elements` y leer `textContent`, que funciona aunque el elemento esté oculto.

### Evidencia de ejecución

```bash
behave --no-capture features/imdb.feature
```

![Ejecución exitosa de la prueba de IMDb](evidencias/imdb_resultado.png)

Resultado: **1 feature passed, 1 scenario passed, 5 steps passed**, con calificación obtenida de **8,8**.

---

## Cómo ejecutar las pruebas

Requisitos: Google Chrome actualizado, `chromedriver.exe` de la misma versión en la raíz del proyecto, y:

```bash
pip install selenium behave
```

Desde la raíz del proyecto:

```bash
behave features/lobby_login.feature
behave --no-capture features/imdb.feature
```

Para verificar que todos los pasos del feature están implementados sin abrir el navegador:

```bash
behave --dry-run features/imdb.feature
```
