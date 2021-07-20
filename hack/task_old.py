
import argparse
import tensorflow as tf

from . import utils

def get_args():
	parser = argparse.ArgumentParser()
	
	parser.add_argument(
		'--job-dir',
		type=str,
		required=True,
		help='GCS location to write checkpoints and export models')
	parser.add_argument(
		'--train-file',
		type=str,
		required=True,
		help='Training file local or GCS')
	parser.add_argument(
		'--verbosity',
		choices=['DEBUG', 'ERROR', 'FATAL', 'INFO', 'WARN'],
		default='INFO')
	
	return parser.parse_args()


def train_and_eval(params):
	train_file_path = utils.download_files_from_gcs(params['train_file'],'train_file.txt')[0]
	print(train_file_path)


if __name__ == "__main__":
	args = get_args()
	train_and_eval(args.__dict__)