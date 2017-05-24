from os.path import join

from pandas import read_csv

from sekmet import settings
from redir.models import Quotes, QuoteAuthor, QuoteCat


def keep_df():
	path_to = join(settings.BASE_DIR, "redir", "data", "quotes.csv")

	df = read_csv(filepath_or_buffer=path_to, sep=',', delimiter=None, \
		header=0, names=None, index_col=None, usecols=None, squeeze=False, prefix=None, \
        mangle_dupe_cols=True, dtype=None, engine=None, \
		converters=None, true_values=None, false_values=None, \
		skipinitialspace=False, skiprows=None, nrows=None, \
		na_values=None, keep_default_na=True, na_filter=True, \
		verbose=False, skip_blank_lines=True, parse_dates=False, \
		infer_datetime_format=False, keep_date_col=False, \
		date_parser=None, dayfirst=False, iterator=False, chunksize=None, \
		compression='infer', thousands=None, decimal='.', lineterminator=None, \
		quotechar='"', quoting=0, escapechar=None, comment=None, \
		encoding=None, dialect=None, tupleize_cols=False, \
		error_bad_lines=True, warn_bad_lines=True, skipfooter=0, \
		skip_footer=0, doublequote=True, delim_whitespace=False, \
		as_recarray=False, compact_ints=False, use_unsigned=False, \
		low_memory=False, buffer_lines=None, memory_map=False, \
		float_precision=None)
	return df


def get_cat(cat_data):
	try:
		cat = QuoteCat.objects.get(cat=cat_data)
	except:
		cat = QuoteCat.objects.create(cat=cat_data)

	return cat


def get_author(author_data):
	try:
		author = QuoteAuthor.objects.get(author=author_data)
	except:
		author = QuoteAuthor.objects.create(author=author_data)

	return author


def generate_json_quotes(save=False):
	df = keep_df()
	
	if save:
		save_to = join(settings.BASE_DIR, "static", "data", "quotes.json")
		df.to_json(path_or_buf=save_to, orient='records')

	for i in range(len(df)):
		quote_data = df.ix[i].QUOTE
		author_data = df.ix[i].AUTHOR
		cat_data = df.ix[i].GENRE
	
		cat = get_cat(cat_data=cat_data)
		author = get_author(author_data=author_data)

		try:
			quote = Quotes.objects.create(quote=quote_data, cat=cat, author=author)
			print "Quote: {} inserted".format(quote_data)
		except Exception as e:
			print e
			pass

generate_json_quotes()