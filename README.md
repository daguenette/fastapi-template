# FastAPI Template

This project is a FastAPI template that can be used as a starting point for other projects. It assumes the use of PostgreSQL, Alembic, SQLAlchemy, and Pydantic. The template provides a basic structure and example resource to help you quickly start developing your FastAPI application.

```
alembic/
│   ├── versions/
│   └── env.py
app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── resources/
|   |   |   ├── __init__.py
│   │   │   ├── resource1/         # Replaced with taxes as an example in the project directories
|   |   |   |   ├── __init__.py
│   │   │   │   ├── models.py
│   │   │   │   ├── schemas.py
│   │   │   │   ├── routes.py
│   │   │   │   └── operations.py
│   │   └── auth/                  # COMING SOON
|   |       ├── __init__.py
│   │       └── utils.py           # COMING SOON
│   ├── database/
│   │   ├── __init__.py
│   │   └── base.py
│   └── helper_functions/          # COMING SOON
|       ├── __init__.py
│       └── validations.py         # COMING SOON
pyproject.toml
README.md
.gitignore
```

## Getting Started

1. Enter virtual environment & install dependencies:

```bash
poetry shell
poetry install
```

2. Create a .env file in the project root with the following content:

```
DATABASE_URL="<your_db_url>"
DATABASE_DRIVERNAME="postgresql"
DATABASE_USERNAME="<your_db_username>"
DATABASE_PASSWORD="<your_db_password>"
DATABASE_HOST="<your_db_host>"
DATABASE_NAME="<your_db_name>"
DATABASE_PORT="<your_db_port>"
API_PORT="<your_api_port>"
```

3. Run the application:

```bash
poetry run start
```

The application will now be available at http://127.0.0.1:8000. Assuming 8000 was your port.


## Alembic

1. Initialize Alembic:

Navigate to your project root directory and run the following command:

```bash
poetry run alembic init alembic
```

This will create an alembic directory in your project with necessary configuration files.

2. Configure Alembic

Open alembic.ini in the project root and update the sqlalchemy.url to match your database URL. Alternatively, you can use an environment variable to load the database URL. 

```bash
sqlalchemy.url = ${DATABASE_URL}
```

Next, open alembic/env.py. Import your SQLAlchemy Base and engine objects from your project, and replace the following lines:

```python
target_metadata = None
```

```python
from app.database.base import Base
# add all new ressources models here
from app.api.ressources.ressource1.models import <classname_of_your_model>

target_metadata = Base.metadata
```

3. Generate a migration

To create a new migration, run:

```bash
poetry run alembic revision --autogenerate -m "Description of the migration"
```
Replace "Description of the migration" with a brief description of the changes made. Alembic will generate a migration script in the alembic/versions directory.

4. Review the generated migration

Before applying the migration, review the generated migration script in alembic/versions. Make sure that the upgrade() and downgrade() functions correctly represent the desired changes to your database schema.

5. Apply the migration

```bash
poetry run alembic upgrade head
```

This will apply all pending migrations up to the latest version (head).

6. Roll back a migration

If you need to undo a migration, you can use the downgrade command:

```bash
poetry run alembic downgrade -1
```

This will roll back the last applied migration. You can also specify a specific version to downgrade to by replacing -1 with the target version.

7. View migration history

To view the migration history and the current version, run:

```bash
poetry run alembic history
poetry run alembic current
```

These commands display the history of applied migrations and the current version of your database schema.

Remember to repeat steps 4 through 6 every time you make changes to your SQLAlchemy models that require a change in the database schema.

## Ressources

This template includes an example resource named resource1. The folder contains the following files:

- `models.py`: SQLAlchemy models for the resource.
- `schemas.py`: Pydantic schemas for the resource.
- `routes.py`: FastAPI routes for the resource.
- `operations.py`: The crud operations related to the resource.

To create a new resource, create a new folder inside app/api/resources and follow the same structure as resource1.

## Authentication [COMING SOON]

## Helper Functions [COMING SOON]

## Contributing

If you have any suggestions or improvements for this template, please feel free to open a pull request or create an issue. Your contributions are welcome!

## License

This project is licensed under the MIT License. See the LICENSE file for details.