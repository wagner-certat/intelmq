# -*- coding: utf-8 -*-
import json
import unittest

import intelmq.lib.test as test
from intelmq.bots.experts.csv.expert import CSVExpertBot


TEST_INPUT1 = {
    "__type": "Event",
    "destination.ip": "2001:DB8::BB2B:F258",
    "destination.port": 22,
}

TEST_OUTPUT1 = """destination.ip
2001:DB8::BB2B:F258"""
TEST_OUTPUT2 = """;22"""


class TestCSVExpertBot(test.BotTestCase, unittest.TestCase):

    @classmethod
    def set_bot(cls):
        cls.bot_reference = CSVExpertBot
        cls.sysconfig = {"fieldnames": "destination.ip", "header": True}

    def test_conversion(self):
        self.input_message = TEST_INPUT1
        self.run_bot()
        expected = TEST_INPUT1.copy()
        expected['output'] = json.dumps(TEST_OUTPUT1)
        self.assertMessageEqual(0, expected)

    def test_conversion2(self):
        self.input_message = TEST_INPUT1
        self.sysconfig = {"fieldnames": "classification.taxonomy,destination.port",
                          "delimiter": ";"}
        self.run_bot()
        expected = TEST_INPUT1.copy()
        expected['output'] = json.dumps(TEST_OUTPUT2)
        self.assertMessageEqual(0, expected)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
