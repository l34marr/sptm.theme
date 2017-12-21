# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from sptm.theme.testing import SPTM_THEME_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that sptm.theme is properly installed."""

    layer = SPTM_THEME_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if sptm.theme is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'sptm.theme'))

    def test_browserlayer(self):
        """Test that ISptmThemeLayer is registered."""
        from sptm.theme.interfaces import (
            ISptmThemeLayer)
        from plone.browserlayer import utils
        self.assertIn(ISptmThemeLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = SPTM_THEME_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['sptm.theme'])

    def test_product_uninstalled(self):
        """Test if sptm.theme is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'sptm.theme'))

    def test_browserlayer_removed(self):
        """Test that ISptmThemeLayer is removed."""
        from sptm.theme.interfaces import \
            ISptmThemeLayer
        from plone.browserlayer import utils
        self.assertNotIn(ISptmThemeLayer, utils.registered_layers())
