import json

class Security(object):
	def antiXSS(self, dicElem):
		for elem in dicElem:
			dicElem[elem] = dicElem[elem].replace("'"," &#x27")
			dicElem[elem] = dicElem[elem].replace('"',"&quot")
			dicElem[elem] = dicElem[elem].replace('<',"&lt")
			dicElem[elem] = dicElem[elem].replace('>',"&gt")
		return dicElem