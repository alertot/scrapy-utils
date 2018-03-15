from scrapy import signals


class ItemStatsExtension(object):
    """ Register field stats about scraped items. """

    def __init__(self, stats):
        self.stats = stats
        self.registry = set()

    @classmethod
    def from_crawler(cls, crawler):
        o = cls(crawler.stats)
        crawler.signals.connect(o.item_scraped, signal=signals.item_scraped)

        return o

    def item_scraped(self, item, spider):
        item_classname = item.__class__.__name__

        for field in item.fields:
            key = 'itemstats/{}/{}'.format(item_classname, field)

            # Initialize stats to also register fields with 0 ocurrences
            if item_classname not in self.registry:
                self.stats.set_value(key, 0, spider=spider)

            if field in item:
                self.stats.inc_value(key, spider=spider)

        self.registry.add(item_classname)
