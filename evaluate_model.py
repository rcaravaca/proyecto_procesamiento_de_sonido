#!/usr/bin/env python3

from pyAudioAnalysis import audioTrainTest as aT
from sklearn import metrics
import matplotlib.pyplot as plt
import os
import re

import argparse


# ./evaluate_model.py --class1 dataset/pasos_${NOISE}_carolina_joseline_michelle/$FILTER/filtered/$SNR/carolina/test/carolina --class2 dataset/pasos_${NOISE}_carolina_joseline_michelle/$FILTER/filtered/$SNR/joseline/test/joseline --model trained_models/$NOISE/$FILTER/$SNR/model --pos_class carolina


# def parse_args():
# 	parser = argparse.ArgumentParser(description='evaluate_model')

# 	parser.add_argument('--dir', type=str, help='dirname')

# 	return parser.parse_args()


if __name__ == '__main__':

	dir = os.path.dirname("trained_models/")
	# noises = os.listdir(dir)

	noises 		= ['oficina']
	# noises 	= ['ruido_blanco']
	classifiers = ["svm", "knn", "randomforest"]
	# classifiers = ["svm"]
	filters 	= ['mmse', 'spect_sub', 'wiener']
	# filters 	= ['mmse']
	snrs 		= ["snr_-10", "snr_-5", "snr_0", "snr_5", "snr_10"]

	file_csv = open("datos_round_2.csv","a")

	for clss in classifiers:

		for noise in noises:

			print("###############################################################################")
			print("INFO: Running for noise", noise)
			print("###############################################################################")

			plt.figure()
			for condition in os.listdir(str(dir) + "/" + noise):

				if condition == "original":

					snr_dic = {}
					for _snr in snrs:

						snr = int(re.sub('snr_',  '', _snr))

						print("INFO: "+str(noise)+","+str(condition)+","+str(clss)+","+str(_snr))

						class1 = os.path.dirname("dataset/pasos_" +str(noise)+"_carolina_joseline_michelle/original/"+str(_snr)+"/carolina/test/carolina/")
						class2 = os.path.dirname("dataset/pasos_" +str(noise)+"_carolina_joseline_michelle/original/"+str(_snr)+"/joseline/test/joseline/")
						model = "trained_models/"+str(noise)+"/original/"+str(clss)+"/"+str(_snr)+"/model"
						cm, thr_prre, pre, rec, thr_roc, fpr, tpr = aT.evaluate_model_for_folders([class1, class2], model, clss, "carolina", plot=False)

						TP = cm[0][0]
						TN = cm[1][1]
						FP = cm[0][1]
						FN = cm[1][0]
						accuracy = (TP + TN) / (TP + TN + FP + FN)
						print("ACC:", accuracy)

						auc = metrics.auc(fpr, tpr)
<<<<<<< HEAD
=======
						# snr_dic.update({snr: auc})
>>>>>>> e58ce1a431a72b8cb3a9e1e38ae3d59636687f3a
						snr_dic.update({snr: accuracy})

						file_csv.write(str(noise)+","+str(condition)+","+str(clss)+","+str(snr)+","+str(auc)+","+str(accuracy)+"\n")

					plt.plot(list(snr_dic.keys()),list(snr_dic.values()), '--o', label="No filter")


				elif condition == "filtered":

					for filter in filters:

						snr_dic = {}
						for _snr in snrs:
							snr = int(re.sub('snr_',  '', _snr))

							print(	"INFO: "+str(noise)+","+str(condition)+","+str(filter)+","+str(clss)+","+str(_snr))

							class1 = os.path.dirname("dataset/pasos_" +str(noise)+"_carolina_joseline_michelle/"+str(filter)+"/filtered/"+str(_snr)+"/carolina/test/carolina/")
							class2 = os.path.dirname("dataset/pasos_" +str(noise)+"_carolina_joseline_michelle/"+str(filter)+"/filtered/"+str(_snr)+"/joseline/test/joseline/")
							model = "trained_models/"+str(noise)+"/filtered/"+str(filter)+"/"+str(clss)+"/"+str(_snr)+"/model"
							cm, thr_prre, pre, rec, thr_roc, fpr, tpr = aT.evaluate_model_for_folders([class1, class2], model, clss, "carolina", plot=False)

							TP = cm[0][0]
							TN = cm[1][1]
							FP = cm[0][1]
							FN = cm[1][0]
							accuracy = (TP + TN) / (TP + TN + FP + FN)
							print("ACC:", accuracy)

							auc = metrics.auc(fpr, tpr)
<<<<<<< HEAD
=======
							# snr_dic.update({snr: auc})
>>>>>>> e58ce1a431a72b8cb3a9e1e38ae3d59636687f3a
							snr_dic.update({snr: accuracy})

							file_csv.write(str(noise)+","+str(condition)+","+str(clss)+","+str(snr)+","+str(auc)+","+str(accuracy)+"\n")

						plt.plot(list(snr_dic.keys()),list(snr_dic.values()), '--o', label=filter)

			if noise == "ruido_blanco":
				plt.title("White noise and " + str(clss) + " classifier")
			elif noise == "babble":
				plt.title("Babble noise and " + str(clss) + " classifier")
			elif noise == "oficina":
				plt.title("Office noise and " + str(clss) + " classifier")
			plt.xlabel("SNR")
<<<<<<< HEAD
			plt.ylabel("Accuracy")
			plt.ylim((0, 1.1))
			plt.grid(True)
			plt.legend()
=======
			# plt.ylabel("AUC")
			plt.ylabel("ACCURACY")
			plt.grid(True)
			plt.legend()
			# plt_name = "auc_" + str(noise) + "_" + str(clss) + ".pdf"
>>>>>>> e58ce1a431a72b8cb3a9e1e38ae3d59636687f3a
			plt_name = "accuracy_" + str(noise) + "_" + str(clss) + ".pdf"
			print("INFO: saving :", plt_name)
			plt.savefig(plt_name)


	file_csv.close()