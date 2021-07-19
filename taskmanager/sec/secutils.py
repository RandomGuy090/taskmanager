import json

class Security(object):
	def makeSafe(self, elem):
		elem = self.antiXSS(elem)

		return elem

	def antiXSS(self, dicElem):
		for elem in dicElem:
			if  isinstance(dicElem[elem], str):
				dicElem[elem] = dicElem[elem].replace("'"," &#x27")
				dicElem[elem] = dicElem[elem].replace('"',"&quot")
				dicElem[elem] = dicElem[elem].replace('<',"&lt")
				dicElem[elem] = dicElem[elem].replace('>',"&gt")
		return dicElem