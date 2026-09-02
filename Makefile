.PHONY: test verify

test:
	python3 -m pytest tests/ -q

verify: test
