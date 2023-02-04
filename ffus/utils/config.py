import typing as t
from functools import lru_cache
from os import environ, getenv
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()


class ConfigMeta(type):
    def resolve_value(cls, value: str) -> t.Any:
        _map: t.Dict[str, t.Callable[[str], t.Any]] = {
            "bool": bool,
            "int": int,
            "float": float,
            "str": str,
            "file": lambda x: Path(x).read_text().strip("\n"),
            "list": lambda x: [
                cls.resolve_value(i.strip()) for i in x.split(",")
            ],
            "set": lambda x: set(
                [cls.resolve_value(i.strip()) for i in x.split(",")]
            ),
        }

        return _map[(v := value.split(":", maxsplit=1))[0]](v[1])

    @lru_cache()
    def __getattr__(cls, name) -> t.Any:
        try:
            return cls.resolve_value(environ[name] or getenv([name]))
        except KeyError:
            raise AttributeError(f'"{name}" is not a key in Config')

    def __getitem__(cls, name: str) -> t.Any:
        return cls.__getattr__(name)


class Config(metaclass=ConfigMeta):
    pass
