from card import Card

from collections import defaultdict
from ctabustracker import CTABusTracker

class CTATracker(Card):
    def __init__(self, config):
        self.cta = CTABusTracker(config.get("key"))
        self.stops = config.get("stops")

    def load(self):
        data = defaultdict(list)

        for stop, routes in self.stops.items():
            p = self.cta.get_stop_predictions(stop)

            for item in p:
                if item["route_id"] not in routes: continue

                data[item["stop_name"]].append({
                    "time": item['prediction'].strftime("%s"),
                    "dist": item['distance_to_destination']
                })

        return data
