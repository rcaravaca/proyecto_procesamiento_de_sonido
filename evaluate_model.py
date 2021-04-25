#!/usr/bin/env python3

from pyAudioAnalysis import audioTrainTest as aT
from sklearn import metrics

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

	cm, thr_prre, pre, rec, thr_roc, fpr, tpr = aT.evaluate_model_for_folders([args.class1, args.class2], args.model, "svm", args.pos_class)

	AUC = metrics.auc(fpr, tpr)

	print("AUC:", AUC)

