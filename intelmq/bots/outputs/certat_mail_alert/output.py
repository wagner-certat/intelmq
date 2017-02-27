# -*- coding: utf-8 -*-

import smtplib
import sys

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from intelmq.lib.bot import Bot


class CertatMailAlertOutputBot(Bot):

    def process(self):
        event = self.receive_message()

        msg = MIMEMultipart()
        msg['Subject'] = 'CERT.at notification VIP alerts for ASN %s' % event.get('source.asn', 'unknown')
        msg['From'] = self.parameters.from_addr
        msg['To'] = self.parameters.to_addr
        msg.preamble = '''Dear reader,
we have a special event for you which you should look at. This is the VIP alerting service.

Yours, faithfully,
the VIP alerting service
'''

        msg.attach(MIMEText(event.to_json()))

        s = smtplib.SMTP(self.parameters.mail_server)
        s.send_message(msg)
        s.quit()

        self.acknowledge_message()


BOT = CertatMailAlertOutputBot
