# -*- coding: utf-8 -*-
"""
Converts to CSV and writes output to field `output`.
"""
import csv
import io
import json

from intelmq.lib.bot import Bot


class CSVExpertBot(Bot):

    def init(self):
        self.fieldnames = getattr(self.parameters, 'fieldnames')
        if isinstance(self.fieldnames, str):
            self.fieldnames = self.fieldnames.split(',')
        self.delimiter = getattr(self.parameters, 'delimiter', ',')
        self.header = getattr(self.parameters, 'header', False)

    def process(self):
        event = self.receive_message()
        csvfile = io.StringIO()
        writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames,
                                quoting=csv.QUOTE_MINIMAL,
                                delimiter=self.delimiter,
                                extrasaction='ignore', lineterminator=r'\n')
        if self.header:
            writer.writeheader()
        writer.writerow(event)
        a = json.dumps(csvfile.getvalue())
        print('a', repr(a))
        event.add("output", a)
        print('a in event', repr(event['output']))
        self.send_message(event)
        self.acknowledge_message()

BOT = CSVExpertBot
