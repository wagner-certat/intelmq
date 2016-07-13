# -*- coding: utf-8 -*-
"""
A collector for grabbing appropriately tagged events from MISP.

Parameters:
  - misp_url: URL of the MISP server
  - misp_key: API key for accessing MISP
  - misp_verify: true or false, check the validity of the certificate
  - misp_tag_to_process: MISP tag identifying events to be processed
  - misp_tag_processed: MISP tag identifying events that have been processed

"""
import json
import sys
from urllib.parse import urljoin

from pymisp import PyMISP

from intelmq.lib.bot import Bot
from intelmq.lib.message import Report


class MISPCollectorBot(Bot):

    def init(self):
        # Initialise MISP connection
        self.misp = PyMISP(self.parameters.misp_url,
                           self.parameters.misp_key,
                           self.parameters.misp_verify)

        # URLs used for deleting and adding MISP event tags
        self.misp_add_tag_url = urljoin(self.parameters.misp_url,
                                        'events/addTag')
        self.misp_del_tag_url = urljoin(self.parameters.misp_url,
                                        'events/removeTag')

    def process(self):
        # Grab the events from MISP
        misp_result = self.misp.search(
            tags=self.parameters.misp_tag_to_process
        )

        # Process the response and events
        if 'response' in misp_result:

            # Extract the MISP event details
            misp_events = misp_result['response']
            misp_events_details = [e['Event'] for e in misp_events]

            # Send the results to the parser
            report = Report()
            report.add('raw', json.dumps(misp_events_details, sort_keys=True))
            report.add('feed.name', self.parameters.feed)
            report.add('feed.url', self.parameters.misp_url)
            report.add('feed.accuracy', self.parameters.accuracy)
            self.send_message(report)

            # Finally, update the tags on the MISP events.
            # Note PyMISP does not currently support this so we use
            # the API URLs directly with the requests module.

            for misp_event in misp_events:
                # Remove the 'to be processed' tag
                self.misp.remove_tag(misp_event,
                                     self.parameters.misp_tag_to_process)

                # Add a 'processed' tag to the event
                self.misp.add_tag(misp_event,
                                  self.parameters.misp_tag_processed)


if __name__ == '__main__':
    bot = MISPCollectorBot(sys.argv[1])
    bot.start()
