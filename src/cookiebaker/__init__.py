from cookiecutter.main import cookiecutter
from datetime import datetime
from pathlib import Path
import sys

_default_cookiecutter = str(Path(__file__).parent / 'default_cookiecutter')
assert ':' not in _default_cookiecutter, "please use a path without colons"


def create(name, *sources):
    now = datetime.now()
    extra_context = {
        '__project_name': name,
        '__pypi_slug': name.lower().replace(' ', '_').replace('-', '_'),
        '__rtd_slug': name.lower().replace(' ', '-').replace('_', '-'),
        '__full_name': 'A User',
        '__email': 'a@user.com',
        '__year': now.year,
        '__month': now.month
    }
    cookiecutter(_default_cookiecutter, extra_context=extra_context)


def cli():
    return create(*sys.argv[1:])


if __name__ == '__main__':
    sys.exit(cli())
