import unittest
from unittest.mock import Mock, patch

from app.lib.utils.base_packages import (
    BASE_FONTS_PACKAGES,
    BASE_PACKAGES,
    GNOME_APPS,
    KDE_PLASMA_APPS,
    PACKAGES_TO_REMOVE,
    BasePackages,
)


class TestBasePackages(unittest.TestCase):
    def setUp(self):
        """Set up the test environment before each test."""
        self.mock_logger = Mock()
        self.mock_system = Mock()
        self.mock_desktop = Mock()
        self.base_packages = BasePackages(
            logger=self.mock_logger,
            system=self.mock_system,
            desktop=self.mock_desktop,
        )

    def test_install_base_packages_for_kde(self):
        """
        Test that the correct packages are installed when the desktop environment is KDE.
        """
        # Arrange: Simulate that the desktop environment is KDE
        self.mock_desktop.is_kde.return_value = True

        # Act: Call the method to install base packages
        self.base_packages.install_base_packages()

        # Assert: Verify that the system's install_packages method was called with the correct lists
        self.mock_system.install_packages.assert_any_call(BASE_PACKAGES)
        self.mock_system.install_packages.assert_any_call(BASE_FONTS_PACKAGES)
        self.mock_system.install_packages.assert_any_call(KDE_PLASMA_APPS)
        self.assertEqual(self.mock_system.install_packages.call_count, 3)

    def test_install_base_packages_for_gnome(self):
        """
        Test that the correct packages are installed when the desktop environment is GNOME.
        """
        # Arrange: Simulate that the desktop environment is not KDE (i.e., GNOME)
        self.mock_desktop.is_kde.return_value = False

        # Act: Call the method to install base packages
        self.base_packages.install_base_packages()

        # Assert: Verify that the system's install_packages method was called with the correct lists
        self.mock_system.install_packages.assert_any_call(BASE_PACKAGES)
        self.mock_system.install_packages.assert_any_call(BASE_FONTS_PACKAGES)
        self.mock_system.install_packages.assert_any_call(GNOME_APPS)
        self.assertEqual(self.mock_system.install_packages.call_count, 3)

    def test_remove_unused_packages(self):
        """
        Test that the remove_packages method is called with the correct list of packages.
        """
        # Act: Call the method to remove unused packages
        self.base_packages.remove_unnused_packages()

        # Assert: Verify that the system's remove_packages method was called with the correct list
        self.mock_system.remove_packages.assert_called_once_with(PACKAGES_TO_REMOVE)


if __name__ == "__main__":
    unittest.main()
