"""Dependency-free, local-only resource readers for the published skill."""
from decimal import Decimal


def seconds(value):
    if isinstance(value, str) and ':' in value:
        h, m, s = value.split(':')
        return Decimal(h)*3600 + Decimal(m)*60 + Decimal(s)
    return Decimal(str(value))


def internal_path(home, value):
    path = (home / value).resolve()
    if not path.is_relative_to(home.resolve()):
        raise ValueError('Resource path escapes skill directory: ' + value)
    if not path.is_file():
        raise FileNotFoundError(path)
    return path


def read_resource_json(home, value):
    """All release resources are local; missing files cannot fall back to research."""
    import json
    return json.loads(internal_path(home, value).read_text(encoding='utf-8-sig'))
