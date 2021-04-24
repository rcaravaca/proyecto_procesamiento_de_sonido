from pyroomacoustics.denoise import apply_iterative_wiener, IterativeWiener
import pyroomacoustics as pra
import numpy as np
from progress.bar import IncrementalBar

def wiener_filter(noisy_signal=None, frame_len=512, lpc_order=20, iterations=2, alpha=0.8, thresh=0.01):
	if noisy_signal.all()==None:
		return None
	return apply_iterative_wiener(noisy_signal, frame_len, lpc_order, iterations, alpha, thresh)

def wiener_filter2(noisy_signal=None, frame_len=512, lpc_order=20, iterations=2, alpha=0.8, thresh=0.01):

	scnr = IterativeWiener(frame_len, lpc_order, iterations, alpha, thresh)

	# derived parameters
	hop = frame_len // 2
	window_a = pra.hann(frame_len)
	window_s = pra.transform.stft.compute_synthesis_window(window_a, hop)
	stft = pra.transform.STFT(
		frame_len,
		hop=hop,
		analysis_window=window_a,
		synthesis_window=window_s,
		streaming=True,
	)
	speech_psd = np.ones(hop + 1)  # initialize PSD
	noise_psd = 0

	processed_audio = np.zeros(noisy_signal.shape)
	n = 0
	bar = IncrementalBar('\tProcessing ... ', max=noisy_signal.shape[0]//hop)
	while noisy_signal.shape[0] - n >= hop:
		# print("-> ",n," - ",noisy_signal.shape[0])

		# to frequency domain, 50% overlap
		stft.analysis(
			noisy_signal[n : (n + hop)]
		)

		# compute Wiener output
		X = scnr.compute_filtered_output(current_frame=stft.fft_in_buffer, frame_dft=stft.X)

		# back to time domain
		processed_audio[n : n + hop] = stft.synthesis(X)

		# update step
		n += hop
		bar.next()

	bar.finish()
	print("\tDone!")



	return processed_audio