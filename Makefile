ENV := "flasking-kedro-venv"
KEDRO_VERSION: 0.17.2

setup:
	python -m venv /venv/flasking-kedro-venv && \
	source venv/flasking-kedro-venv/bin/activate && \
	pip install kedro==$(KEDRO_VERSION) && \
	kedro install && \
	pre-commit install && \
	echo "Successfuly setup the envrionment!\n"
