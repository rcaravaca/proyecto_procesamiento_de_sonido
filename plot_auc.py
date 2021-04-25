#!/usr/bin/env python3


import matplotlib.pyplot as plt
import numpy as np



if __name__ == '__main__':

	snr = np.array([-10, -5, 0, 5, 10])

	mmse_AUC = np.array([0.4807692307692308, 0.4807692307692308, 0.5192307692307692, 0.5902366863905326, 0.8498520710059171])
	spect_sub_AUC = np.array([0.5547337278106509, 0.6124260355029585, 0.8032544378698225, 0.9718934911242604, 0.9970414201183433])
	wiener_AUC = np.array([0.5147928994082841, 0.6301775147928994, 0.8017751479289941, 0.9792899408284024, 1])

	plt.figure()
	plt.plot(snr, mmse_AUC, '--o', label="mmse")
	plt.plot(snr, spect_sub_AUC, '--o', label="spectral subs")
	plt.plot(snr, wiener_AUC, '--o', label="wiener")
	plt.grid(True)
	plt.title("AUC vs SNR")
	plt.xlabel("SNR")
	plt.ylabel("AUC")
	plt.legend()
	plt.show()