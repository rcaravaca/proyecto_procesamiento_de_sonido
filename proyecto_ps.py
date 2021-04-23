#!/usr/bin/env python3

import scipy.io.wavfile as wav
import numpy as np
import logmmse
import utils


if __name__ == '__main__':

	args = utils.parse_args()

	sr, data = wav.read(args.input_noisy)

	## LOG MMSE FILTER
	data_filtered = logmmse.logmmse(data, sr, output_file=args.output_file)

	## Tim Sainburg Noise reduction


	## Wiener denosing


	## Plot signals
	if args.plot:
		utils.plot_signals(data,data_filtered, sr, args.num_FFT, args.hop_size)
