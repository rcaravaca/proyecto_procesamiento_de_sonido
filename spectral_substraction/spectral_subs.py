import pyroomacoustics as pra

# import or create `noisy_signal`
def spectral_sub(noisy_signal=None, nfft=512, db_reduc=10, lookback=5, beta=20, alpha=3):
	return pra.denoise.apply_spectral_sub(noisy_signal, nfft, db_reduc, lookback, beta, alpha)
'''
Parameters:	
.- nfft (int) – FFT size. Length of gain filter, i.e. the number of frequency bins, is given by nfft//2+1.
.- db_reduc (float) – Maximum reduction in dB for each bin.
.- lookback (int) – How many frames to look back for the noise estimate.
.- beta (float) – Overestimation factor to “push” the gain filter value (at each frequency) closer to the dB reduction specified by db_reduc.
.- alpha (float, optional) – Exponent factor to modify transition behavior towards the dB reduction specified by db_reduc. Default is 1.
'''