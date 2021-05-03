#!/bin/bash

clear

# spec_sub filter 
echo evaluation - spec_sub...
echo

./evaluate_model.py --class1 dataset/pasos_oficina_carolina_joseline_michelle/spect_sub/filtered/snr_0/carolina/test/carolina --class2 dataset/pasos_oficina_carolina_joseline_michelle/spect_sub/filtered/snr_0/joseline/test/joseline --model trained_models/oficina/spect_sub/snr_0/original_oficina_snr_0 --pos_class carolina > spect_sub_snr_0.auc
mv temp.html spect_sub_snr_0.html
# 
# ../../evaluate_model.py --class1 ../../dataset/pasos_oficina_carolina_joseline_michelle/spect_sub/filtered/snr_5/carolina/test/carolina --class2 ../../dataset/pasos_oficina_carolina_joseline_michelle/spect_sub/filtered/snr_5/joseline/test/joseline --model ../../trained_models/oficina/spect_sub/snr_5/original_oficina_snr_5 --pos_class carolina > spect_sub_snr_5.auc
# mv temp.html spect_sub_snr_5.html
# 
# ../../evaluate_model.py --class1 ../../dataset/pasos_oficina_carolina_joseline_michelle/spect_sub/filtered/snr_10/carolina/test/carolina --class2 ../../dataset/pasos_oficina_carolina_joseline_michelle/spect_sub/filtered/snr_10/joseline/test/joseline --model ../../trained_models/oficina/spect_sub/snr_10/original_oficina_snr_10 --pos_class carolina > spect_sub_snr_10.auc
# mv temp.html spect_sub_snr_10.html
# 
# ../../evaluate_model.py --class1 ../../dataset/pasos_oficina_carolina_joseline_michelle/spect_sub/filtered/snr_-5/carolina/test/carolina --class2 ../../dataset/pasos_oficina_carolina_joseline_michelle/spect_sub/filtered/snr_-5/joseline/test/joseline --model ../../trained_models/oficina/spect_sub/snr_-5/original_oficina_snr_-5 --pos_class carolina > spect_sub_snr_-5.auc
# mv temp.html spect_sub_snr_-5.html
# 
# ../../evaluate_model.py --class1 ../../dataset/pasos_oficina_carolina_joseline_michelle/spect_sub/filtered/snr_-10/carolina/test/carolina --class2 ../../dataset/pasos_oficina_carolina_joseline_michelle/spect_sub/filtered/snr_-10/joseline/test/joseline --model ../../trained_models/oficina/spect_sub/snr_-10/original_oficina_snr_-10 --pos_class carolina > spect_sub_snr_-10.auc
# mv temp.html spect_sub_snr_-10.html


# mmse filter
# echo evaluation - mmse...
# echo
# ../../evaluate_model.py --class1 ../../dataset/pasos_oficina_carolina_joseline_michelle/mmse/filtered/snr_0/carolina/test/carolina --class2 ../../dataset/pasos_oficina_carolina_joseline_michelle/mmse/filtered/snr_0/joseline/test/joseline --model ../../trained_models/oficina/mmse/snr_0/original_oficina_snr_0 --pos_class carolina > mmse_snr_0.auc
# mv temp.html mmse_snr_0.html
# 
# ../../evaluate_model.py --class1 ../../dataset/pasos_oficina_carolina_joseline_michelle/mmse/filtered/snr_5/carolina/test/carolina --class2 ../../dataset/pasos_oficina_carolina_joseline_michelle/mmse/filtered/snr_5/joseline/test/joseline --model ../../trained_models/oficina/mmse/snr_5/original_oficina_snr_5 --pos_class carolina > mmse_snr_5.auc
# mv temp.html mmse_snr_5.html
# 
# ../../evaluate_model.py --class1 ../../dataset/pasos_oficina_carolina_joseline_michelle/mmse/filtered/snr_10/carolina/test/carolina --class2 ../../dataset/pasos_oficina_carolina_joseline_michelle/mmse/filtered/snr_10/joseline/test/joseline --model ../../trained_models/oficina/mmse/snr_10/original_oficina_snr_10 --pos_class carolina > mmse_snr_10.auc
# mv temp.html mmse_snr_10.html
# 
# ../../evaluate_model.py --class1 ../../dataset/pasos_oficina_carolina_joseline_michelle/mmse/filtered/snr_-5/carolina/test/carolina --class2 ../../dataset/pasos_oficina_carolina_joseline_michelle/mmse/filtered/snr_-5/joseline/test/joseline --model ../../trained_models/oficina/mmse/snr_-5/original_oficina_snr_-5 --pos_class carolina > mmse_snr_-5.auc
# mv temp.html mmse_snr_-5.html
# 
# ../../evaluate_model.py --class1 ../../dataset/pasos_oficina_carolina_joseline_michelle/mmse/filtered/snr_-10/carolina/test/carolina --class2 ../../dataset/pasos_oficina_carolina_joseline_michelle/mmse/filtered/snr_-10/joseline/test/joseline --model ../../trained_models/oficina/mmse/snr_-10/original_oficina_snr_-10 --pos_class carolina > mmse_snr_-10.auc
# mv temp.html mmse_snr_-10.html
# 
# 
# 
# wiener filter
# echo evaluation - wiener...
# echo 
# ../../evaluate_model.py --class1 ../../dataset/pasos_oficina_carolina_joseline_michelle/wiener/filtered/snr_0/carolina/test/carolina --class2 ../../dataset/pasos_oficina_carolina_joseline_michelle/wiener/filtered/snr_0/joseline/test/joseline --model ../../trained_models/oficina/wiener/snr_0/original_oficina_snr_0 --pos_class carolina > wiener_snr_0.auc
# mv temp.html wiener_snr_0.html
# 
# ../../evaluate_model.py --class1 ../../dataset/pasos_oficina_carolina_joseline_michelle/wiener/filtered/snr_5/carolina/test/carolina --class2 ../../dataset/pasos_oficina_carolina_joseline_michelle/wiener/filtered/snr_5/joseline/test/joseline --model ../../trained_models/oficina/wiener/snr_5/original_oficina_snr_5 --pos_class carolina > wiener_snr_5.auc
# mv temp.html wiener_snr_5.html
# 
# ../../evaluate_model.py --class1 ../../dataset/pasos_oficina_carolina_joseline_michelle/wiener/filtered/snr_10/carolina/test/carolina --class2 ../../dataset/pasos_oficina_carolina_joseline_michelle/wiener/filtered/snr_10/joseline/test/joseline --model ../../trained_models/oficina/wiener/snr_10/original_oficina_snr_10 --pos_class carolina > wiener_snr_10.auc
# mv temp.html wiener_snr_10.html
# 
# ../../evaluate_model.py --class1 ../../dataset/pasos_oficina_carolina_joseline_michelle/wiener/filtered/snr_-5/carolina/test/carolina --class2 ../../dataset/pasos_oficina_carolina_joseline_michelle/wiener/filtered/snr_-5/joseline/test/joseline --model ../../trained_models/oficina/wiener/snr_-5/original_oficina_snr_-5 --pos_class carolina > wiener_snr_-5.auc
# mv temp.html wiener_snr_-5.html
# 
# ../../evaluate_model.py --class1 ../../dataset/pasos_oficina_carolina_joseline_michelle/wiener/filtered/snr_-10/carolina/test/carolina --class2 ../../dataset/pasos_oficina_carolina_joseline_michelle/wiener/filtered/snr_-10/joseline/test/joseline --model ../../trained_models/oficina/wiener/snr_-10/original_oficina_snr_-10 --pos_class carolina > wiener_snr_-10.auc
# mv temp.html wiener_snr_-10.html
