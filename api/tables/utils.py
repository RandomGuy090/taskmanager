
def get_table_url(url):
	"get table id from url"

	if url.endswith("/"):
		url=url[:-1]
	spl = url.split("/")
	# url = spl[spl.index(spl[-1])-1]
	url = spl[spl.index(spl[3])]

	#makeshift
	if len(url) == 16:
		return url
	else: 
		# url = spl[spl.index(spl[-1])]
		url = spl[spl.index(spl[3])]

		return url

def get_lookup(url):
	if url.endswith("/"):
		url = url[:-1]
	print(url)
	
	url = url.rsplit("/")
	print(url)
	return str(url[-1])
