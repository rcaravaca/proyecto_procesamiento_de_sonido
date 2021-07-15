#!/usr/bin/env python3

from pyAudioAnalysis import audioTrainTest as aT
from sklearn import metrics
import matplotlib.pyplot as plt

import argparse

def parse_args():
	parser = argparse.ArgumentParser(description='evaluate_model')

	parser.add_argument('--class1', type=str, help='test/class1')
	parser.add_argument('--class2', type=str, help='test/class2')
	parser.add_argument('--model', type=str, help='model to evaluate')
	parser.add_argument('--pos_class', type=str, help='Possitive class')

	return parser.parse_args()

if __name__ == '__main__':

	args = parse_args()

	cm, thr_prre, pre, rec, thr_roc, fpr, tpr = aT.evaluate_model_for_folders([args.class1, args.class2], args.model, "svm", args.pos_class, plot=False)

	AUC = metrics.auc(fpr, tpr)

	# print("AUC:", AUC)
	# print("Prec:", pre)
	# print("thr_prre:", thr_prre)


	plt.plot(thr_prre,pre[:-1], label="Precision")
	plt.plot(thr_prre,rec[:-1], label="Recall")
	plt.title("Precision-Recall")
	plt.xlabel("Threshold")
	plt.grid(True)
	plt.legend()
	plt.tight_layout()
	# plt.autoscale(enable=None, axis="x", tight=True)
	plt.savefig('testing.pdf')  
	# plt.show()
