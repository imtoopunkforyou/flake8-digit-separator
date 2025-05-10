# === Сonfiguration ===
MAKEFLAGS += --silent
make:
	cat -n ./Makefile

# === Dev ===
lint:
	poetry run flake8 ./src ./tests \
	&& poetry run mypy ./src --no-pretty \
	&& poetry run nitpick fix
pre-commit:
	poetry run isort ./src ./tests \
	&& make lint \
	&& make test
test-collect:
	poetry run pytest ./tests/ --collect-only
test:
	poetry run pytest ./tests/ 

# === Aliases ===
pc: pre-commit
t: test