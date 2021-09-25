.PHONY: build build_local build_url clean

# We need python3.
# In Ubuntu the executable is called python3
# but in other systems it may simply be called python
py := $(shell which python3)

ifeq "$(py)" ""
	PY := python
else
	PY := python3
endif

build: build_local

build_local:
	$(PY) generator.py docs/api.json

build_online:
	$(PY) generator.py

clean:
	cp "pybry/__lbryd_api__.py" "pybry/lbryd_api.py"
	-rm -rf "build/"

