from unittest import TestCase
from mppsolar import mpputils


class test_mppcommands(TestCase):
    def testOne(self):
        mp = mpputils.mppUtils('/dev/ttyUSB0')
        mp.getKnownCommands()
        return True
