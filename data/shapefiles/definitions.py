from datetime import date

from django.contrib.humanize.templatetags.humanize import ordinal

import utils

SHAPEFILES = {
    # This key should be the plural name of the boundaries in this set
    'Counties': {
        # Path to a shapefile, relative to /data/shapefiles
        'file': '04_Arizona/04/tl_2010_04_county10.shp',
        # Generic singular name for an boundary of from this set
        'singular': 'County',
        # Should the singular name come first when creating canonical identifiers for this set?
        'kind_first': False,
        # Function which each feature wall be passed to in order to extract its "external_id" property
        # The utils module contains several generic functions for doing this
        'ider': utils.simple_namer(['COUNTYFP10']),
        # Function which each feature will be passed to in order to extract its "name" property
        'namer': utils.simple_namer(['NAME10']),
        # Authority that is responsible for the accuracy of this data
        'authority': 'Census',
        # Geographic extents which the boundary set encompasses
        'domain': 'Arizona',
        # Last time the source was checked for new data
        'last_updated': date(2011, 6, 18),
        # A url to the source of the data
        'href': 'http://www.census.gov/geo/www/tiger/',
        # Notes identifying any pecularities about the data, such as columns that were deleted or files which were merged
        'notes': '',
        # Encoding of the text fields in the shapefile, i.e. 'utf-8'. If this is left empty 'ascii' is assumed
        'encoding': 'utf-8',
        # SRID of the geometry data in the shapefile if it can not be inferred from an accompanying .prj file
        # This is normally not necessary and can be left undefined or set to an empty string to maintain the default behavior
        'srid': ''
    },
}