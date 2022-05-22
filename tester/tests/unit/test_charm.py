
import unittest
from unittest.mock import Mock

from ops.model import ActiveStatus
from ops.testing import Harness

from charm import OperatorTemplateCharm


class TestCharm(unittest.TestCase):
    def setUp(self):
        self.harness = Harness(OperatorTemplateCharm)
        self.addCleanup(self.harness.cleanup)
        self.harness.begin()

