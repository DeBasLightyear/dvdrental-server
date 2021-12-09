import os
from dataclasses import dataclass


@dataclass(frozen=True)
class ConnectionVariables:
    user: str
    password: str
    host: str
    port: str
    name: str


def _env_var(var: str) -> str:
    value = os.environ.get(var)

    if value is None:
        msg = f'Missing value for environment variable "{var}"'
        raise Exception(msg)

    return value


def postgres_connection_variables() -> ConnectionVariables:
    """
    Provides postgres connection variables.
    """

    return ConnectionVariables(
        user=_env_var('DB_USER'),
        password=_env_var('DB_PASSWORD'),
        host=_env_var('DB_HOST'),
        port=_env_var('DB_PORT'),
        name=_env_var('DB_NAME'),
    )
