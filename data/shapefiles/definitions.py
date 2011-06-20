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
	'Area_Landmark00': {
        'file': '04_Arizona/04/tl_2009_04_arealm.shp',
        'singular': 'Area Landmark',
        'kind_first': False,
        'ider': utils.simple_namer(['AREAID']),
        'namer': utils.simple_namer(['FULLNAME']),
        'authority': 'Census',
        'domain': 'Arizona',
        'last_updated': date(2011, 6, 18),
        'href': 'http://www.census.gov/geo/www/tiger/',
        'notes': '',
        'encoding': 'utf-8',
        'srid': ''
    },
	'Area_Water00': {
        'file': '04_Arizona/04/tl_2009_04_areawater.shp',
        'singular': 'Area Water',
        'kind_first': False,
        'ider': utils.simple_namer(['HYDROID']),
        'namer': utils.simple_namer(['FULLNAME']),
        'authority': 'Census',
        'domain': 'Arizona',
        'last_updated': date(2011, 6, 18),
        'href': 'http://www.census.gov/geo/www/tiger/',
        'notes': '',
        'encoding': 'utf-8',
        'srid': ''
    },
	'BlockGroup00': {
        'file': '04_Arizona/04/tl_2009_04_bg00.shp',
        'singular': 'Block Group 00',
        'kind_first': False,
        'ider': utils.simple_namer(['BKGPIDFP00']),
        'namer': utils.simple_namer(['NAMELSAD00']),
        'authority': 'Census',
        'domain': 'Arizona',
        'last_updated': date(2011, 6, 18),
        'href': 'http://www.census.gov/geo/www/tiger/',
        'notes': '',
        'encoding': 'utf-8',
        'srid': ''
    },
	'CountySub00': {
        'file': '04_Arizona/04/tl_2009_04_cousub00.shp',
        'singular': 'County Subdivision 00',
        'kind_first': False,
        'ider': utils.simple_namer(['COSBIDFP00']),
        'namer': utils.simple_namer(['NAMELSAD00']),
        'authority': 'Census',
        'domain': 'Arizona',
        'last_updated': date(2011, 6, 18),
        'href': 'http://www.census.gov/geo/www/tiger/',
        'notes': '',
        'encoding': 'utf-8',
        'srid': ''
    },
	'Block00': {
        'file': '04_Arizona/04/tl_2009_04_tabblock00.shp',
        'singular': 'Block (Census 2000)',
        'kind_first': False,
        'ider': utils.simple_namer(['BLKIDFP00']),
        'namer': utils.simple_namer(['NAME00']),
        'authority': 'Census',
        'domain': 'Arizona',
        'last_updated': date(2011, 6, 18),
        'href': 'http://www.census.gov/geo/www/tiger/',
        'notes': '',
        'encoding': 'utf-8',
        'srid': ''
    },
	'TAZ00': {
        'file': '04_Arizona/04/tl_2009_04_taz00.shp',
        'singular': 'Census 2000 Traffic Analysis Zone',
        'kind_first': False,
        'ider': utils.simple_namer(['TAZIDFP00']),
        'namer': utils.simple_namer(['TAZCE00']),
        'authority': 'Census',
        'domain': 'Arizona',
        'last_updated': date(2011, 6, 18),
        'href': 'http://www.census.gov/geo/www/tiger/',
        'notes': '',
        'encoding': 'utf-8',
        'srid': ''
    },
	'TRACT00': {
        'file': '04_Arizona/04/tl_2009_04_tract00.shp',
        'singular': 'Census Tract (Census 2000)',
        'kind_first': False,
        'ider': utils.simple_namer(['CTIDFP00']),
        'namer': utils.simple_namer(['NAMELSAD00']),
        'authority': 'Census',
        'domain': 'Arizona',
        'last_updated': date(2011, 6, 18),
        'href': 'http://www.census.gov/geo/www/tiger/',
        'notes': '',
        'encoding': 'utf-8',
        'srid': ''
    },
	'VTD00': {
        'file': '04_Arizona/04/tl_2009_04_vtd00.shp',
        'singular': 'Voting District (Census 2000)',
        'kind_first': False,
        'ider': utils.simple_namer(['VTDIDFP00']),
        'namer': utils.simple_namer(['NAMELSAD00']),
        'authority': 'Census',
        'domain': 'Arizona',
        'last_updated': date(2011, 6, 18),
        'href': 'http://www.census.gov/geo/www/tiger/',
        'notes': '',
        'encoding': 'utf-8',
        'srid': ''
    },
}