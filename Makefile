# === Сonfiguration ===
MAKEFLAGS += --silent
make:
	cat -n ./Makefile

# === Dev ===
lint:
	poetry run ruff check ./flake8_digit_separator ./tests \
	&& poetry run ruff format ./flake8_digit_separator ./tests \
	&& poetry run flake8 ./flake8_digit_separator \
	&& poetry run mypy ./flake8_digit_separator
pre-commit:
	make lint \
	&& make test
test-collect:
	poetry run pytest ./tests/ --collect-only
test:
	poetry run pytest ./tests/
cov-report:
	poetry run pytest ./tests --cov=flake8_digit_separator --cov-report=html
py:
	poetry run python
fds:
	poetry run flake8 --select FDS ./flake8_digit_separator

# === Aliases ===
pc: pre-commit
t: test