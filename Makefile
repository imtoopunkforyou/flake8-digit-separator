# === Сonfiguration ===
MAKEFLAGS += --silent
make:
	cat -n ./Makefile

# === Dev ===
lint:
	poetry run flake8 ./flake8_digit_separator ./tests \
	&& poetry run mypy ./flake8_digit_separator --no-pretty
pre-commit:
	poetry run isort ./flake8_digit_separator ./tests \
	&& make lint \
	&& make test
test-collect:
	poetry run pytest ./tests/ --collect-only
test:
	poetry run pytest ./tests/ 
py:
	poetry run python
fds:
	poetry run flake8 --select FDS ./

# === Aliases ===
pc: pre-commit
t: test