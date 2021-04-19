#!/usr/bin/env python3

"""
Created on Tue May  1 20:43:28 2018
@author: eesungkim
"""
import os
import math

import librosa
import numpy as np
import scipy.io.wavfile as wav
from utils.estnoise_ms import * 
from utils.utils import * 

def MMSE_STSA(path_noisy_test, output_path_estimated_noisy_test, sr, noisy_test, NFFT, hop_length_sample, winfunc):
	"""Speech Enhancement using A Spectral Amplitude Estimator
	"""
	
	smoothFactorDD=0.99
	maxPosteriorSNR= 100   
	minPosteriorSNR= 1
	# the variance of the speech; lambda_x(k)
	#noisy

	# print(noisy_test.dtype)
	stft_noisy_test = librosa.stft(noisy_test, n_fft=NFFT, hop_length=hop_length_sample, window=winfunc)
	magnitude_noisy_test, phase_noisy_test = divide_magphase(stft_noisy_test, power=1)
		
	pSpectrum = magnitude_noisy_test**2

	# estimate the variance of the noise using minimum statistics noise PSD estimation ; lambda_d(k). 
	estNoise = estnoisem(pSpectrum,hop_length_sample/sr)
	estNoise = estNoise
	
	aPosterioriSNR=pSpectrum/estNoise
	aPosterioriSNR=aPosterioriSNR
	aPosterioriSNR[aPosterioriSNR > maxPosteriorSNR] = maxPosteriorSNR
	aPosterioriSNR[aPosterioriSNR < minPosteriorSNR] = minPosteriorSNR

	previousGainedaPosSNR=1 
	(nFrames,nFFT2) = pSpectrum.shape				
	totalGain =[]
	for i in range(nFFT2):						 
		aPosterioriSNR_frame = aPosterioriSNR[:,i]				  
		
		#operator [2](52)
		oper=aPosterioriSNR_frame-1
		oper[oper < 0] = 0 
		smoothed_a_priori_SNR = smoothFactorDD * previousGainedaPosSNR + (1-smoothFactorDD) * oper
		
		#V for MMSE estimate ([2](8)) 
		V=smoothed_a_priori_SNR*aPosterioriSNR_frame/(1+smoothed_a_priori_SNR)

		#Calculate Gain function which results from the MMSE [2](7),(12).
		gain= smoothed_a_priori_SNR/(1+smoothed_a_priori_SNR)  
		if any(V<1):
			gain[V<1] = (math.gamma(1.5) * np.sqrt(V[V<1])) / aPosterioriSNR_frame[V<1] * np.exp(-1 * V[V<1] / 2) * ((1 + V[V<1]) * bessel(0, V[V<1] / 2) + V[V<1] * bessel(1, V[V<1] / 2))
		
		previousGainedaPosSNR = (gain**2) * aPosterioriSNR_frame
		totalGain.append(gain)
	
	totalGain=np.array(totalGain)

	magnitude_estimated_clean = totalGain.T * magnitude_noisy_test
	stft_reconstructed_clean = merge_magphase(magnitude_estimated_clean, phase_noisy_test)
	signal_reconstructed_clean =librosa.istft(stft_reconstructed_clean, hop_length=hop_length_sample, window=winfunc)
	signal_reconstructed_clean=signal_reconstructed_clean.astype('int16')
	
	# wav.write(output_path_estimated_noisy_test,sr,signal_reconstructed_clean)

	return signal_reconstructed_clean, sr

def plot_signals(noisy_test,signal_reconstructed_clean,sr,NFFT,hop_length_sample):

	signal_reconstructed_clean = np.float32(signal_reconstructed_clean)
	show_signal(noisy_test,signal_reconstructed_clean,sr)
	show_spectrogram(noisy_test, signal_reconstructed_clean,sr,NFFT,hop_length_sample)

	
if __name__ == '__main__':
	args = parse_args()
	MMSE_STSA(args)

