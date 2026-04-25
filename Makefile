hooks:
	uv tool run prek run --all-files

upgrade:
	uv lock --upgrade

upgrade-hooks:
	uv tool run prek autoupdate
	cd {{cookiecutter.repo_name}}
	uv tool run pre-commit autoupdate