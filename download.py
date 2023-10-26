from argparse import ArgumentParser
from huggingface_hub import snapshot_download

def init_parser():
	parser = ArgumentParser(description='Script to download HF models on to local system')
	parser.add_argument('-r','--repo', help='repo to clone', required=True)
	args = vars(parser.parse_args())
	return args

def download_hf_repo(repo_id: str):
	snapshot_download(repo_id=repo_id)
	# file should be stored in ~/.cache/huggingface/hub/


if __name__ == '__main__':
	args = init_parser()
	download_hf_repo(args['repo'])
