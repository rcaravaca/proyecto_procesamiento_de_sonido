from pyroomacoustics.denoise import apply_iterative_wiener

def wiever_flter(noisy_signal=None, frame_len=512, lpc_order=20, iterations=2, alpha=0.8, thresh=0.01):
	if not noisy_signal:
		return None
	return apply_iterative_wiener(noisy_signal, frame_len, lpc_order, iterations, alpha, thresh)