.PHONY: help clean setup dist _check-local release

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

_check-local:
ifndef GITHUB_TOKEN
	$(error 'You must export GITHUB_TOKEN to push a new release')
endif

release: _check-local dist
	source venv/bin/activate && \
		git tag -f v$$(python setup.py --version)
	git push -f --tags
	source venv/bin/activate && \
		github-release release \
			--user oii \
			--repo DeDRM_tools \
			--tag v$$(python setup.py --version)
	source venv/bin/activate && \
		github-release upload \
			--user oii \
			--repo DeDRM_tools \
			--tag v$$(python setup.py --version) \
			--name dedrm-$$(python setup.py --version).tar.gz \
			--file dist/dedrm-$$(python setup.py --version).tar.gz
	source venv/bin/activate && \
		github-release upload \
			--user oii \
			--repo DeDRM_tools \
			--tag v$$(python setup.py --version) \
			--name dedrm-$$(python setup.py --version).zip \
			--file dist/dedrm-$$(python setup.py --version).zip
