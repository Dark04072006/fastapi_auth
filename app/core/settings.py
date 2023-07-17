import os

import yaml
import pathlib

from app.core.parse_env_files import AppConfig, DatabaseConfig, SecretCongig


BASE_DIR = pathlib.Path(__file__).parent.parent.parent
config_path = BASE_DIR / "config" / "dev_config.yaml"


def get_config(path):
    with open(path, 'r') as file:
        yaml_data = yaml.safe_load(file)
        return AppConfig(
            secret=SecretCongig(**yaml_data['application']['secret']),
            database=DatabaseConfig(**yaml_data['database'])
        )


config = get_config(config_path)

# DATABASE_URL = f"postgresql+asyncpg://{config.database.username}:{config.database.password}" \
#                f"@{config.database.host}:{config.database.port}/{config.database.name}"

DATABASE_URL = os.getenv('DATABASE_URL')

