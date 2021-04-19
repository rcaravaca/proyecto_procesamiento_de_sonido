#!/usr/bin/env python3

import sys
import scipy.io.wavfile as wav
import argparse
import os
import numpy as np
import matplotlib.pyplot as plt
import sklearn as slk
from scipy import stats


sys.path.append('MMSE_STSA')
import main as mmse

def check_args(args):
	# if not os.path.exists(args.datasets_dir):
	# 	os.makedirs(args.datasets_dir)
	assert args.num_FFT >= 1, 'number of FFT size must be larger than or equal to one'
	assert args.hop_size < args.num_FFT, 'hop size must be smaller than number of FFT size'
	return args

def parse_args():
	parser = argparse.ArgumentParser(description='MMSE-STSA Speech Enhancement')
	# parser.add_argument('--datasets_dir', type=str, default='datasets/',
	# 					help='')
	# parser.add_argument('--input_clean', type=str, default='datasets/clean.wav',
	# 					help='datasets/clean_file_name.wav')
	parser.add_argument('--input_noisy', type=str, default='datasets/noisy_white_3dB.wav',
						help='datasets/noisy_file_name.wav')
	parser.add_argument('--output_file', type=str, default='datasets/clean_estimated_MMSE_STSA_test.wav',
						help='datasets/output_file_name.wav')
	parser.add_argument('--num_FFT', type=int, default='256',
						help='')
	parser.add_argument('--hop_size', type=int, default='128',
						help='')
	parser.add_argument('--window', type=str, default='hamming',
						help='')
	return check_args(parser.parse_args())

def normalize(signal):

	max_val = np.max(np.abs(signal))
	return signal/max_val



def plot_signals(noisy_test, signal_reconstructed_clean):


	noisy_test_norm = normalize(noisy_test)
	signal_reconstructed_clean_norm = normalize(signal_reconstructed_clean)

	plt.subplot(2,2,1)
	plt.plot(noisy_test_norm)
	plt.grid(True)
	plt.title("Senal con ruido")
	plt.subplot(2,2,2)
	plt.plot(signal_reconstructed_clean_norm)
	plt.grid(True)
	plt.title("Senal filtrada")
	plt.subplot(2,2,3)
	plt.specgram(noisy_test)
	plt.title("Espectrograma de senal con ruido")
	plt.subplot(2,2,4)
	plt.specgram(signal_reconstructed_clean)	
	plt.title("Espectrograma de senal filtrada")
	plt.show()

if __name__ == '__main__':
	args = parse_args()

	PATH_ROOT = os.getcwd() 
	path_noisy_test = os.path.join(PATH_ROOT , args.input_noisy)
	output_path_estimated_noisy_test = os.path.join(PATH_ROOT , args.output_file)
	sr, noisy_test = wav.read(path_noisy_test)
	noisy_test = np.float32(noisy_test)
	NFFT = args.num_FFT
	hop_length_sample = args.hop_size
	winfunc = args.window

	signal_reconstructed_clean, sr = mmse.MMSE_STSA(path_noisy_test, output_path_estimated_noisy_test, sr, noisy_test, NFFT, hop_length_sample, winfunc )

	plot_signals(noisy_test, signal_reconstructed_clean)

	#mmse.plot_signals(noisy_test,signal_reconstructed_clean,sr,NFFT,hop_length_sample)
