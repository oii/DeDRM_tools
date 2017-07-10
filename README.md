Building DeDRM Tools for OGRE
=============================

These tools are provided as is from the upstream repo maintained by Apprentice Harper.

The `ogre` branch contains minimal patches required to create a useable python package which can be
imported in the ogreclient tools.

New builds of the tools are pushed to Github releases.


Prerequisites
-------------

 * https://github.com/aktau/github-release
 * A `GITHUB_TOKEN` exported in your path (check [docs](https://github.com/aktau/github-release))


Building
--------

The included `Makefile` will build and push a new release:

   make release
