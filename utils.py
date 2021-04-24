
import argparse
import os
import matplotlib.pyplot as plt
import librosa
import librosa.display
import numpy as np


def check_args(args):
	# if not os.path.exists(args.datasets_dir):
	# 	os.makedirs(args.datasets_dir)
	assert args.num_FFT >= 1, 'number of FFT size must be larger than or equal to one'
	return args

def parse_args():
	parser = argparse.ArgumentParser(description='MMSE-STSA Speech Enhancement')
	# parser.add_argument('--datasets_dir', type=str, default='datasets/',
	# 					help='')
	# parser.add_argument('--input_clean', type=str, default='datasets/clean.wav',
	# 					help='datasets/clean_file_name.wav')
	parser.add_argument('--filter_type', type=str, default='mmse',
						help='mmse | spect_sub | wiener')
	parser.add_argument('--input_noisy', type=str, default='datasets/noisy_white_3dB.wav',
						help='datasets/noisy_file_name.wav')
	parser.add_argument('--output_file', type=str, default='datasets/clean_estimated_MMSE_STSA_test.wav',
						help='datasets/output_file_name.wav')
	parser.add_argument('--num_FFT', type=int, default='256',
						help='')
	parser.add_argument('--window', type=str, default='hamming',
						help='')
	parser.add_argument('--plot', default=False, action=argparse.BooleanOptionalAction)

	return check_args(parser.parse_args())

def normalize(signal):

	max_val = np.max(np.abs(signal))
	return signal/max_val

def plot_signals(noisy_test, signal_reconstructed_clean, sr, NFFT):

	hop_length = NFFT//2
	noisy_test_norm = normalize(noisy_test)
	signal_reconstructed_clean_norm = normalize(signal_reconstructed_clean)

	plt.figure(figsize=(10,6))

	plt.subplot(2, 2, 1)
	librosa.display.waveplot(noisy_test_norm, sr=sr)
	plt.title('Noisy Time Signal')

	plt.subplot(2, 2, 2)
	librosa.display.waveplot(signal_reconstructed_clean_norm, sr=sr)
	plt.title('Reconstructed Clean Time Signal')

	plt.subplot(2, 2, 3)
	librosa.display.specshow(librosa.power_to_db(librosa.feature.melspectrogram(y=noisy_test_norm, sr=sr, n_fft=NFFT, hop_length=hop_length),ref=np.max),sr=sr, x_axis='time', y_axis='linear')
	#librosa.display.specshow(librosa.amplitude_to_db(origianlSpectrogram, ref_power=np.max),sr=sr, x_axis='time',y_axis='linear')
	plt.title('Noisy Spectrogram')
	plt.colorbar(format='%+02.0f dB')
	
	plt.subplot(2, 2, 4)
	librosa.display.specshow(librosa.power_to_db(librosa.feature.melspectrogram(y=signal_reconstructed_clean_norm, sr=sr, n_fft=NFFT, hop_length=hop_length),ref=np.max),sr=sr, x_axis='time', y_axis='linear')
	#librosa.display.specshow(librosa.amplitude_to_db(recnstrtSpectrogram, ref_power=np.max),sr=sr, x_axis='time', y_axis='linear')
	plt.title('Reconstructed Clean Spectrogram')
	plt.colorbar(format='%+2.0f dB')
	plt.tight_layout()
	plt.show()