install:
	uv pip install -e .

run:
	uv run -m {{cookiecutter.package_name}}

ruff:
	uvx ruff check --fix

test:
	uvx pytest --cov=src

mypy:
	uvx mypy src/

hooks:
	uv install prek
	uv run prek install
	uv run prek run --all-files

hooks-update:
	uv run prek autoupdate