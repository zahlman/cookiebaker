from cookiecutter.main import cookiecutter
from datetime import datetime
from pathlib import Path
import sys

_default_cookiecutter = str(Path(__file__).parent / 'default_cookiecutter')
assert ':' not in _default_cookiecutter, "please use a path without colons"


def create(*sources):
    now = datetime.now()
    cookiecutter(_default_cookiecutter, output_dir='wrapper', extra_context={
        '__full_name': 'A User',
        '__email': 'a@user.com',
        '__year': now.year,
        '__month': now.month
    })


def cli():
    return create(*sys.argv[1:])


if __name__ == '__main__':
    sys.exit(cli())
