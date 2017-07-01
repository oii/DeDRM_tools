#!/usr/bin/env python
# -*- coding: utf-8 -*-


__license__   = 'GPL v3'
__docformat__ = 'restructuredtext en'


# Released under the terms of the GNU General Public Licence, version 3
# <http://www.gnu.org/licenses/>
#
# All credit given to i♥cabbages and The Dark Reverser for the original standalone scripts.
# We had the much easier job of converting them to a calibre plugin.
#
# This plugin is meant to decrypt eReader PDBs, Adobe Adept ePubs, Barnes & Noble ePubs,
# Adobe Adept PDFs, Amazon Kindle and Mobipocket files without having to
# install any dependencies... other than having calibre installed, of course.
#
# Configuration:
# Check out the plugin's configuration settings by clicking the "Customize plugin"
# button when you have the "DeDRM" plugin highlighted (under Preferences->
# Plugins->File type plugins). Once you have the configuration dialog open, you'll
# see a Help link on the top right-hand side.
#
# Revision history:
#   6.0.0 - Initial release
#   6.0.1 - Bug Fixes for Windows App, Kindle for Mac and Windows Adobe Digital Editions
#   6.0.2 - Restored call to Wine to get Kindle for PC keys, added for ADE
#   6.0.3 - Fixes for Kindle for Mac and Windows non-ascii user names
#   6.0.4 - Fixes for stand-alone scripts and applications
#           and pdb files in plugin and initial conversion of prefs.
#   6.0.5 - Fix a key issue
#   6.0.6 - Fix up an incorrect function call
#   6.0.7 - Error handling for incomplete PDF metadata
#   6.0.8 - Fixes a Wine key issue and topaz support
#   6.0.9 - Ported to work with newer versions of Calibre (moved to Qt5). Still supports older Qt4 versions.
#   6.1.0 - Fixed multiple books import problem and PDF import with no key problem
#   6.2.0 - Support for getting B&N key from nook Study log. Fix for UTF-8 filenames in Adobe ePubs.
#           Fix for not copying needed files. Fix for getting default Adobe key for PDFs
#   6.2.1 - Fix for non-ascii Windows user names
#   6.2.2 - Added URL method for B&N/nook books
#   6.3.0 - Added in Kindle for Android serial number solution
#   6.3.1 - Version number bump for clarity
#   6.3.2 - Fixed Kindle for Android help file
#   6.3.3 - Bug fix for Kindle for PC support
#   6.3.4 - Fixes for Kindle for Android, Linux, and Kobo 3.17
#   6.3.5 - Fixes for Linux, and Kobo 3.19 and more logging
#   6.3.6 - Fixes for ADE ePub and PDF introduced in 6.3.5
#   6.4.0 - Updated for new Kindle for PC encryption
#   6.4.1 - Fix for some new tags in Topaz ebooks.
#   6.4.2 - Fix for more new tags in Topaz ebooks and very small Topaz ebooks
#   6.4.3 - Fix for error that only appears when not in debug mode
#           Also includes fix for Macs with bonded ethernet ports
#   6.5.0 - Big update to Macintosh app
#           Fix for some more 'new' tags in Topaz ebooks.
#           Fix an error in wineutils.py
#   6.5.1 - Updated version number, added PDF check for DRM-free documents
#   6.5.2 - Another Topaz fix
#   6.5.3 - Warn about KFX files explicitly
#   6.5.4 - Mac App Fix, improve PDF decryption, handle latest tcl changes in ActivePython


"""
Decrypt DRMed ebooks.
"""

PLUGIN_NAME = "DeDRM"
PLUGIN_VERSION_TUPLE = (6, 5, 4)
PLUGIN_VERSION = ".".join([str(str(x)) for x in PLUGIN_VERSION_TUPLE])
