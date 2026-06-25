# Framework de Automatizacion QA - Juan Cruz Enzetti

Proyecto final integrador de automatizacion de pruebas construido con Python, Selenium WebDriver, Pytest y Requests. Incluye pruebas UI sobre Sauce Demo y pruebas API sobre Reqres.

## Tecnologias Utilizadas

- Python 3.10+
- Selenium WebDriver
- WebDriver Manager
- Pytest
- Requests
- Pytest HTML
- Pytest xdist
- Pytest rerunfailures
- Python dotenv

## Estructura del Framework

```text
project/
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/
│   ├── ui/
│   │   ├── test_login.py
│   │   ├── test_inventory.py
│   │   ├── test_cart.py
│   │   └── test_checkout.py
│   └── api/
│       ├── test_users_api.py
│       ├── test_create_user.py
│       └── test_delete_user.py
├── data/
│   └── login_data.json
├── utils/
│   ├── logger.py
│   ├── data_reader.py
│   └── api_client.py
├── reports/
│   └── screenshots/
├── logs/
├── conftest.py
├── pytest.ini
├── requirements.txt
├── README.md
└── .gitignore
```

## Instalacion

Crear y activar un entorno virtual:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

La API key de Reqres puede configurarse en un archivo `.env`:

```text
REQRES_API_KEY=free_user_3EKJqFeUD8Y2tnBD7IoxTE7Cttr
```

Si no existe `.env`, el framework usa la API key provista como valor por defecto.

## Ejecucion de Pruebas UI

```bash
pytest tests/ui -m ui
```

## Ejecucion de Pruebas API

```bash
pytest tests/api -m api
```

## Ejecucion Completa

```bash
pytest
```

## Generacion de Reportes

El archivo `pytest.ini` ya genera el reporte automaticamente:

```bash
pytest --html=reports/report.html --self-contained-html
```

El reporte queda disponible en:

```text
reports/report.html
```

Las capturas de pantalla de pruebas UI fallidas se guardan en:

```text
reports/screenshots/
```

Formato de captura:

```text
test_name_YYYYMMDD_HHMMSS.png
```

## Ejemplo de Salida

```text
tests/ui/test_login.py::test_successful_login PASSED
tests/ui/test_login.py::test_invalid_login_shows_error PASSED
tests/api/test_users_api.py::test_get_single_user PASSED
```

## Buenas Practicas Implementadas

- Page Object Model para separar tests de detalles Selenium.
- Locators centralizados en cada page object.
- Explicit waits con Expected Conditions.
- Tests sin locators ni acciones Selenium directas.
- Parametrizacion con datos externos desde JSON.
- Fixtures reutilizables para driver, base URL y API client.
- Logging centralizado en `logs/test_execution.log`.
- Screenshots automaticos ante fallos.
- Reporte HTML autocontenido.
- Separacion clara entre pruebas UI y API.
- Preparado para ejecucion paralela con `pytest-xdist`.
- `.gitignore` listo para evitar versionar artefactos temporales.

## Comandos Utiles

Ejecutar pruebas en paralelo:

```bash
pytest -n auto
```

Reintentar pruebas inestables:

```bash
pytest --reruns 2
```

Ejecutar solo smoke tests:

```bash
pytest -m smoke
```
