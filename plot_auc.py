#!/usr/bin/env python3


import matplotlib.pyplot as plt
import numpy as np



if __name__ == '__main__':

	# snr = np.array([0, -10, 10, -5, 5])

	thr = [25,50,75,100,125,150]
	AP = [5.21,52.56,68.05,74.73,77.91,79.87]
	Recall = [17.00, 60.49, 70.86, 76.39, 79.05, 80.78 ]


# 	mmse_AUC = np.array([0.8535502958579881,
# 0.6168639053254438,
# 0.9600591715976331,
# 0.6849112426035503,
# 0.9452662721893492])

# 	spect_sub_AUC = np.array([0.9792899408284024,
# 0.6893491124260355,
# 0.9585798816568049,
# 0.8313609467455622,
# 0.9985207100591716])

# 	wiener_AUC = np.array([0.970414201183432,
# 0.7292899408284024,
# 0.9600591715976331,
# 0.8624260355029587,
# 0.9437869822485208])

	# snr, mmse_AUC = zip(*sorted(zip(snr, mmse_AUC)))

	# snr = np.array([0, -10, 10, -5, 5])
	# snr, spect_sub_AUC = zip(*sorted(zip(snr, spect_sub_AUC)))

	# snr = np.array([0, -10, 10, -5, 5])
	# snr, wiener_AUC = zip(*sorted(zip(snr, wiener_AUC)))

	plt.figure()
	plt.plot(AP,1-Recall, '--o', label="AP")
	# plt.plot(thr, Recall, '--o', label="Recall")
	# plt.plot(snr, wiener_AUC, '--o', label="wiener")
	plt.grid(True)
	# plt.title("AUC vs SNR")
	plt.xlabel("Threshold/mm")
	# plt.ylabel("AUC")
	plt.legend(loc='lower right')
	plt.show()



