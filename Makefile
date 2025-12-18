# === Сonfiguration ===
MAKEFLAGS += --silent
.PHONY: make
make:
	cat -n ./Makefile

# === Dev ===
.PHONY: lint
lint:
	poetry run ruff format ./flake8_digit_separator ./tests \
	&& poetry run ruff check ./flake8_digit_separator ./tests \
	&& poetry run flake8 ./flake8_digit_separator \
	&& poetry run mypy ./flake8_digit_separator

.PHONY: pre-commit
pre-commit:
	make lint \
	&& make test \
	&& make spell-check

.PHONY: test-collect
test-collect:
	poetry run pytest ./tests/ --collect-only

.PHONY: test
test:
	poetry run pytest ./tests/

.PHONY: cov-report
cov-report:
	poetry run pytest ./tests --cov=flake8_digit_separator --cov-report=html

.PHONY: fds
fds:
	poetry run flake8 --select FDS ./flake8_digit_separator

.PHONY: spell-check
spell-check:
	poetry run codespell flake8_digit_separator tests README.md CONTRIBUTING.md


# === Aliases ===
pc: pre-commit
t: test
