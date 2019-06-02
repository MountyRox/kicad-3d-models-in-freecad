
# -*- coding: utf8 -*-
#!/usr/bin/python
#
# This is derived from a cadquery script for generating QFP/GullWings models in X3D format.
#
# from https://bitbucket.org/hyOzd/freecad-macros
# author hyOzd
#

## file of parametric definitions

import collections
from collections import namedtuple

destination_dir="/Relay_THT.3dshapes"
# destination_dir="./"
old_footprints_dir="Relay_THT.pretty"
footprints_dir="Relay_THT.pretty"
##footprints_dir=None #to exclude importing of footprints

##enabling optional/default values to None
def namedtuple_with_defaults(typename, field_names, default_values=()):

    T = collections.namedtuple(typename, field_names)
    T.__new__.__defaults__ = (None,) * len(T._fields)
    if isinstance(default_values, collections.Mapping):
        prototype = T(**default_values)
    else:
        prototype = T(*default_values)
    T.__new__.__defaults__ = tuple(prototype)
    return T

Params = namedtuple_with_defaults("Params", [
	'modelName',		#modelName
	'roundbelly',		# If belly of caseing should be round (or flat)
	'L',				# package length
	'W',			   	# package width
	'H',				# package height
	'rim',				# If a rim should be added to the belly
	'pinpadsize',		# pin diameter or pad size
	'pinpadh',			# pin length, pad height
	'pintype',			# Casing type
	'rotation',			# Rotation if required
	'pin1corner',		# Left upp corner relationsship to pin 1
	'pin',				# pin pitch
	'A1',				# package board seperation
	'corner',			# If top should be cut
	'show_top',			# If top should be visible or not
	'body_color_key',	# Body colour
	'body_top_color_key',	# Body top colour
	'pin_color_key',	# Pin colour
	'dest_dir_prefix'	# Destination directory
])

all_params = {
    
    'Relay_SPST_SANYOU_SRD_Series_Form_A': Params(   # ModelName
        #
        # http://www.sanyourelay.ca/public/products/pdf/SRD.pdf
        #
        modelName = 'Relay_SPST_SANYOU_SRD_Series_Form_A',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 19.6,  # Package length
        W  = 15.4,  # Package width
        H  = 15.5,  # Package height
        A1 = 0.1,   # Package board seperation
        rim = (0.5, 0.5, 0.38),  # If a rim should be created at the bottom
        pin = ((0.0, 0.0, 'rect', 0.3, 1.0), (2.0, 6.0, 'rect', 0.5, 0.5), (14.2, 6.0, 'rect', 1.0, 0.3), (2.0, -6.0, 'rect', 0.5, 0.5)),  # Pin placement
        pin1corner = (-1.3, -7.7),  # Left up corner relationsship to pin 1
        pinpadh    = 3.5,           # Pin length, pad height
        pinpadsize = 1.0,           # Pin diameter or pad size
        show_top   = 0,             # If top should be visible or not
        corner     = 'none',        # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,             # If belly of caseing should be round (or flat)
        rotation   = 0,             # If belly of caseing should be round (or flat)
        body_color_key     = 'blue body',       # Body color
        body_top_color_key = 'blue body',       # Body top color
        pin_color_key      = 'metal grey pins', # Pin color
        dest_dir_prefix    = '../Relay_THT.3dshapes'  # Destination directory
        ),
    
    'Relay_SPST_SANYOU_SRD_Series_Form_B': Params(   # ModelName
        #
        # http://www.sanyourelay.ca/public/products/pdf/SRD.pdf
        #
        modelName = 'Relay_SPST_SANYOU_SRD_Series_Form_B',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 19.6,  # Package length
        W  = 15.4,  # Package width
        H  = 15.5,  # Package height
        A1 = 0.1,   # Package board seperation
        rim = (0.5, 0.5, 0.38),  # If a rim should be created at the bottom
        pin = ((0.0, 0.0, 'rect', 0.3, 1.0), (2.0, 6.0, 'rect', 0.5, 0.5), (14.2, -6.0, 'rect', 1.0, 0.3), (2.0, -6.0, 'rect', 0.5, 0.5)),  # Pin placement
        pin1corner = (-1.3, -7.7),  # Left up corner relationsship to pin 1
        pinpadh    = 3.5,           # Pin length, pad height
        pinpadsize = 1.0,           # Pin diameter or pad size
        show_top   = 0,             # If top should be visible or not
        corner     = 'none',        # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,             # If belly of caseing should be round (or flat)
        rotation   = 0,             # If belly of caseing should be round (or flat)
        body_color_key     = 'blue body',       # Body color
        body_top_color_key = 'blue body',       # Body top color
        pin_color_key      = 'metal grey pins', # Pin color
        dest_dir_prefix    = '../Relay_THT.3dshapes'  # Destination directory
        ),
    
    'Relay_SPDT_SANYOU_SRD_Series_Form_C': Params(   # ModelName
        #
        # http://www.sanyourelay.ca/public/products/pdf/SRD.pdf
        #
        modelName = 'Relay_SPDT_SANYOU_SRD_Series_Form_C',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 19.6,  # Package length
        W  = 15.4,  # Package width
        H  = 15.5,  # Package height
        A1 = 0.1,   # Package board seperation
        rim = (0.5, 0.5, 0.38),  # If a rim should be created at the bottom
        pin = ((0.0, 0.0, 'rect', 0.3, 1.0), (2.0, 6.0, 'rect', 0.5, 0.5), (14.2, 6.0, 'rect', 1.0, 0.3), (14.2, -6.0, 'rect', 1.0, 0.3), (2.0, -6.0, 'rect', 0.5, 0.5)),  # Pin placement
        pin1corner = (-1.3, -7.7),  # Left up corner relationsship to pin 1
        pinpadh    = 3.5,           # Pin length, pad height
        pinpadsize = 1.0,           # Pin diameter or pad size
        show_top   = 0,             # If top should be visible or not
        corner     = 'none',        # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,             # If belly of caseing should be round (or flat)
        rotation   = 0,             # If belly of caseing should be round (or flat)
        body_color_key     = 'blue body',       # Body color
        body_top_color_key = 'blue body',       # Body top color
        pin_color_key      = 'metal grey pins', # Pin color
        dest_dir_prefix    = '../Relay_THT.3dshapes'  # Destination directory
        ),
    
    'Relay_SPDT_Omron-G5LE-1': Params(   # ModelName
        #
        # http://www.sanyourelay.ca/public/products/pdf/SRD.pdf
        #
        modelName = 'Relay_SPDT_Omron-G5LE-1',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 16.5,  # Package length
        W  = 22.5,  # Package width
        H  = 19.0,  # Package height
        A1 = 0.1,   # Package board seperation
        rim = (2.0, 2.0, 0.5),  # If a rim should be created at the bottom
        pin = ((0.0, 0.0, 'rect', 1.2, 0.2), (-6.0, 2.0, 'rect', 0.4, 1.0), (-6.0, 14.2, 'rect', 0.4, 1.0), (6.0, 14.2, 'rect', 0.4, 1.0), (6.0, 2.0, 'rect', 0.4, 1.0)),  # Pin placement
        pin1corner = (-8.25, -2.55),  # Left up corner relationsship to pin 1
        pinpadh    = 3.5,           # Pin length, pad height
        pinpadsize = 1.0,           # Pin diameter or pad size
        show_top   = 0,             # If top should be visible or not
        corner     = 'none',        # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,             # If belly of caseing should be round (or flat)
        rotation   = 0,             # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',       # Body color
        body_top_color_key = 'black body',       # Body top color
        pin_color_key      = 'metal grey pins', # Pin color
        dest_dir_prefix    = '../Relay_THT.3dshapes'  # Destination directory
        ),
}

