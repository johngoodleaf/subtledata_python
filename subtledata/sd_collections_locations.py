__author__ = 'gsibble'

from base_types import SDFirstClassCollection

from sd_location import SDLocation

class SDLocationCollection(SDFirstClassCollection):

    def __init__(self, parent):
        super(SDLocationCollection, self).__init__(parent)

    @property
    def all(self):


        #Get all locations via swagger
        self._swagger_locations = self._swagger_locations_api.getAllLocations(self._api_key, use_cache=self._use_cache)

        return [SDLocation(parent=self, location_id=location.location_id, fetch=False, initial_data=location) for location in self._swagger_locations]


    def get(self, location_id, use_cache=True, include_menu=False):
        if not self._use_cache:
            use_cache = False

        return SDLocation(self, location_id, include_menu, use_cache)

    def filter(self, name=None, postal_code=None):

        return []

    def near(self, latitude, longitude, radius):

        return []

    def create(self):
        pass
