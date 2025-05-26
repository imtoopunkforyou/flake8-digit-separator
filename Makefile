# === Сonfiguration ===
MAKEFLAGS += --silent
make:
	cat -n ./Makefile

# === Dev ===
lint:
	poetry run flake8 ./flake8_digit_separator ./tests \
	&& poetry run mypy ./flake8_digit_separator
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
	poetry run flake8 --select FDS ./flake8_digit_separator

# === Aliases ===
pc: pre-commit
t: test