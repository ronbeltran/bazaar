# Bazaar

Bazaar is a random item and Heroku-ish name generator implemented in Python. This is a port of the Ruby version [bazaar][bazaar]

## Usage

	>>> from bazaar import Bazaar
	>>> for i in range(1, 11):
	...   b = Bazaar()
	...   print("https://{}.herokuapp.com".format(b.heroku))
	... 
	https://mirthful-sands-4816.herokuapp.com
	https://composed-flowers-4402.herokuapp.com
	https://jubilant-valley-5708.herokuapp.com
	https://spacial-temple-8021.herokuapp.com
	https://thriving-pond-5181.herokuapp.com
	https://divine-canopy-7081.herokuapp.com
	https://undisturbed-waterfall-9930.herokuapp.com
	https://benevolent-oasis-3268.herokuapp.com
	https://balmy-autumn-3656.herokuapp.com
	https://celestial-temple-3615.herokuapp.com
	>>> 

	>>> b = Bazaar()
	>>> b.item
	'sharpie'
	>>> b.Item
	'Sharpie'
	>>> b.adj
	'large'
	>>> b.Adj
	'Large'
	>>> b.obj
	'large sharpie'
	>>> b.Obj
	'Large Sharpie'
	>>> b.super_adj
	'tranquil'
	>>> b.Super_adj
	'Tranquil'
	>>> b.super_item
	'sands'
	>>> b.Super_item
	'Sands'
	>>> b.super_obj
	'tranquil sands'
	>>> b.Super_obj
	'Tranquil Sands'
	>>> b.heroku
	'tranquil-sands-2378'
	>>> 


## Run the tests

    python setup.py test

[bazaar]: https://github.com/raycchan/bazaar
