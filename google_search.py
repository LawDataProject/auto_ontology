import argparse,os,pdb,requests,sys
from pprint import pprint


sys.path.append(os.path.abspath('/opt/Programs/project'))
from project_utils import project_utils as pu

def main(entry):
	jfile = pu.get_json(entry)

	return jfile

if __name__=="__main__":
	
	defaults = {'mode': 'full'}
	# Parse input arguments and check.
	parser = argparse.ArgumentParser(
		description="Script that retrieves google search results for entry word.")
	parser.add_argument(
		"--entry",
		required=True,
		type=str,
		help=("Word you wish to search on Google."))
	

	args = parser.parse_args()

	main(args.entry)