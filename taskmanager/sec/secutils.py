import json

class Security(object):
	def make_safe(self, elem):
		elem = self.anti_xss(elem)

		return elem

	def anti_xss(self, dic_elem):
		for elem in dic_elem:
			if  isinstance(dic_elem[elem], str):
				dic_elem[elem] = dic_elem[elem].replace("'"," &#x27")
				dic_elem[elem] = dic_elem[elem].replace('"',"&quot")
				dic_elem[elem] = dic_elem[elem].replace('<',"&lt")
				dic_elem[elem] = dic_elem[elem].replace('>',"&gt")
		return dic_elem