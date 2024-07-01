{%- set is_open_source = cookiecutter.open_source_license != '' -%}
{%- set lower_name = cookiecutter.project_name | lower -%}
{%- set pypi_slug = lower_name | replace(' ', '_') | replace('-', '_') -%}
{%- set rtd_slug = lower_name | replace(' ', '-') | replace('_', '-') -%}
# {{ cookiecutter.project_name }} - {{ cookiecutter.project_short_description }}

{% if is_open_source -%}
[![](https://img.shields.io/pypi/v/{{ pypi_slug }}.svg)](https://pypi.python.org/pypi/{{ pypi_slug }})
[![Documentation Status](https://readthedocs.org/projects/{{ rtd_slug }}/badge/?version=latest)](https://{{ rtd_slug }}.readthedocs.io/en/latest/?version=latest)
{%- endif %}

## Installation

`pip install {{ pypi_slug }}`

## Documentation

See full documentation at https://{{ rtd_slug }}.readthedocs.io.

----

Copyright &copy; {{ cookiecutter.__year }} {{ cookiecutter.__full_name }}

{% if is_open_source -%}
This project is open source software, licensed under the terms of {{ cookiecutter.open_source_license }}.
Please see `LICENSE.txt` for details.
{%- endif %}
