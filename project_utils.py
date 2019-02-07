#Utility functions for nlp_tests project


import json,os,requests

def get_json(entry):
	key = os.getenv("GSEARCH_KEY")
	cx = os.getenv("GSEARCH_CX")

	url = "https://www.googleapis.com/customsearch/v1?key={}&cx={}&q={}&fields=items".format(key,cx,entry)
	r = requests.get(url)
	results_dict = r.json()
	search_results = list()
	for i in results_dict['items']:
		if i['kind']=='customsearch#result':
			snippet = i['snippet'].replace('\n','').replace('\xa0','')
			if not (('FREE detailed reports' in snippet) or ('Compare divorce attorneys serving' in snippet)):
				search_results.append(snippet)
	
	text = " ".join(search_results)
	jfile = dict()
	jfile['id'] = entry
	jfile['text'] = text

	return jfile

class bcolors:
    HEADER = '\033[95m'
    ALLE = '\033[94m'
    COMP = '\033[92m'
    POL = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'










