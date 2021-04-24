#!/usr/bin/env python3

import scipy.io.wavfile as wav
import numpy as np
import logmmse
import utils
import wiener
import sys
from datetime import datetime

sys.path.append('spectral_substraction')
import spectral_subs as ss


if __name__ == '__main__':

	args = utils.parse_args()

	sr, noisy_signal = wav.read(args.input_noisy)
	frame_len = len(noisy_signal)

	print("FILTER_INFO: FILTER TYPE:",args.filter_type)
	start_time = datetime.now()
	if args.filter_type == "mmse":
		## LOG MMSE FILTER
		data_filtered = logmmse.logmmse(noisy_signal, sr, output_file=args.output_file)

	elif args.filter_type == "spect_sub":
		## spectral subsraction
		data_filtered = ss.spectral_sub(noisy_signal, nfft=args.num_FFT)
		wav.write(args.output_file, sr, data_filtered.astype(np.int16))

	elif args.filter_type == "wiener":
		## Wiener denosing
		data_filtered = wiener.wiener_filter2(noisy_signal=noisy_signal, frame_len=args.num_FFT)
		wav.write(args.output_file, sr, data_filtered.astype(np.int16))

	else:
		print("FILTER_INFO: wrong filter_type")

	proc_time = datetime.now() - start_time
	print("FILTER_INFO: Processing time: {}".format(proc_time))

	## Plot signals
	if args.plot:
		print("FILTER_INFO: Plotting")
		utils.plot_signals(noisy_signal,data_filtered, sr, args.num_FFT)
