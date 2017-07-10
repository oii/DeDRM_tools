.PHONY: help clean setup dist release

help:
	@echo 'Usage:'
	@echo '   make clean           remove all build artifacts'
	@echo '   make setup           create python2.7 virtualenv to work in'
	@echo '   make dist            build python distributable with setuptools'
	@echo '   make release         push dedrm tools to Github'


clean:
	@rm -rf dedrm.egg-info dist venv

setup:
	virtualenv --python python2.7 venv

dist: clean setup
	source venv/bin/activate && \
	  python setup.py sdist --formats=gztar,zip

release:
	git tag v$$(python setup.py --version)
	git push --tags
	github-release release \
		--user oii \
		--repo DeDRM_tools \
		--tag v$$(python setup.py --version) \
		--pre-release
	github-release upload \
		--user oii \
		--repo DeDRM_tools \
		--tag v$$(python setup.py --version) \
		--name dedrm-$$(python setup.py --version).tar.gz \
		--file dedrm-$$(python setup.py --version).tar.gz
	github-release upload \
		--user oii \
		--repo DeDRM_tools \
		--tag v$$(python setup.py --version) \
		--name dedrm-$$(python setup.py --version).zip \
		--file dedrm-$$(python setup.py --version).zip
