import tomllib
from src.core.constants import PROJECT_ROOT_PATH





class PoetryConfig:
    version: str = '0.0.1'
    project_name: str = 'template-fastapi-sqlalchemy-mysql'
    description: str = 'fastapi Project'

    # def __init__(self):
    #     with open(PROJECT_ROOT_PATH/'pyproject.toml', 'r') as f:
    #         config: dict = tomllib.load(f)
    #         try:
    #             self.project_name = config.get('tool').get('poetry').get('name')
    #             self.version = config.get('tool').get('poetry').get('version')
    #             self.description = config.get('tool').get('poetry').get('description')
    #         except AttributeError:
    #             pass

poetry_config: PoetryConfig = PoetryConfig()



