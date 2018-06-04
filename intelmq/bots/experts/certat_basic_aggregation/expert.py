# -*- coding: utf-8 -*-
from intelmq.lib.bot import Bot
from intelmq.lib.cache import Cache


class CertatBasicAggregation(Bot):

    def init(self):
        self.cache = Cache(self.parameters.redis_cache_host,
                           self.parameters.redis_cache_port,
                           self.parameters.redis_cache_db,
                           self.parameters.redis_cache_ttl,
                           getattr(self.parameters, "redis_cache_password",
                                   None)
                           ).redis
        self.cache_key = self._Bot__bot_id

    def count_input(self):
        queue_name = self._Bot__source_pipeline.source_queue
        return self._Bot__source_pipeline.count_queued_messages(queue_name)[queue_name]

    def process(self):
        while self.cache.llen(self.cache_key) < self.parameters.minimum_count or self.count_input():
            new_message = self.receive_message()
            if self.parameters.input_field in new_message:
                self.cache.lpush(self.cache_key, new_message[self.parameters.input_field])
            self.acknowledge_message()
        event = self.new_event()
        event.add(self.parameters.output_field,
                  self.parameters.separator.join((a.decode() for a in self.cache.lrange(self.cache_key, 0, -1))))
        self.send_message(event)
        self.cache.delete(self.cache_key)


BOT = CertatBasicAggregation
