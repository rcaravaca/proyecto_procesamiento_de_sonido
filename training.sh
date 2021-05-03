#!/bin/bash

clear

echo Training with pasos_oficina_carolina_joseline_michelle
# pya 

cd info/pyAudioAnalysis/pyAudioAnalysis/
# 


####
# python3 audioAnalysis.py trainClassifier -i ../../../proyecto_procesamiento_de_sonido/dataset/pasos_oficina_carolina_joseline_michelle/spect_sub/original/snr_10/carolina/train/carolina/ ../../../proyecto_procesamiento_de_sonido/dataset/pasos_oficina_carolina_joseline_michelle/spect_sub/original/snr_10/joseline/train/joseline/ --method svm -o sp-project/oficina/original_snr_10
# cd sp-project/oficina
# cp original_snr_10* ../../../../../proyecto_procesamiento_de_sonido/trained_models/oficina/
# 
# 
# python3 audioAnalysis.py trainClassifier -i ../../../proyecto_procesamiento_de_sonido/dataset/pasos_oficina_carolina_joseline_michelle/mmse/original/snr_10/carolina/train/carolina/ ../../../proyecto_procesamiento_de_sonido/dataset/pasos_oficina_carolina_joseline_michelle/mmse/original/snr_10/joseline/train/joseline/ --method svm -o sp-project/oficina/mmse/original_snr_10
# cd sp-project/oficina/mmse/
# cp original_snr_10* ../../../../../proyecto_procesamiento_de_sonido/trained_models/oficina/mmse/
##### *************************************

### mmse
python3 audioAnalysis.py trainClassifier -i ../../../proyecto_procesamiento_de_sonido/dataset/pasos_oficina_carolina_joseline_michelle/mmse/original/snr_10/carolina/train/carolina/ ../../../proyecto_procesamiento_de_sonido/dataset/pasos_oficina_carolina_joseline_michelle/mmse/original/snr_10/joseline/train/joseline/ --method svm -o sp-project/oficina/mmse/snr_10/original_snr_10
# cd sp-project/oficina/mmse/snr_10/
# cp original_snr_10* ../../../../../proyecto_procesamiento_de_sonido/trained_models/oficina/mmse/snr_10/
# 
# python3 audioAnalysis.py trainClassifier -i ../../../proyecto_procesamiento_de_sonido/dataset/pasos_oficina_carolina_joseline_michelle/mmse/original/snr_0/carolina/train/carolina/ ../../../proyecto_procesamiento_de_sonido/dataset/pasos_oficina_carolina_joseline_michelle/mmse/original/snr_0/joseline/train/joseline/ --method svm -o sp-project/oficina/mmse/snr_0/original_snr_0
# cd sp-project/oficina/mmse/snr_0/
# cp original_snr_0* ../../../../../proyecto_procesamiento_de_sonido/trained_models/oficina/mmse/snr_0/
# 
# python3 audioAnalysis.py trainClassifier -i ../../../proyecto_procesamiento_de_sonido/dataset/pasos_oficina_carolina_joseline_michelle/mmse/original/snr_5/carolina/train/carolina/ ../../../proyecto_procesamiento_de_sonido/dataset/pasos_oficina_carolina_joseline_michelle/mmse/original/snr_5/joseline/train/joseline/ --method svm -o sp-project/oficina/mmse/snr_5/original_snr_5
# cd sp-project/oficina/mmse/snr_5/
# cp original_snr_5* ../../../../../proyecto_procesamiento_de_sonido/trained_models/oficina/mmse/snr_5/
# 
# python3 audioAnalysis.py trainClassifier -i ../../../proyecto_procesamiento_de_sonido/dataset/pasos_oficina_carolina_joseline_michelle/mmse/original/snr_-5/carolina/train/carolina/ ../../../proyecto_procesamiento_de_sonido/dataset/pasos_oficina_carolina_joseline_michelle/mmse/original/snr_-5/joseline/train/joseline/ --method svm -o sp-project/oficina/mmse/snr_-5/original_snr_-5
# cd sp-project/oficina/mmse/snr_-5/
# cp original_snr_-5* ../../../../../proyecto_procesamiento_de_sonido/trained_models/oficina/mmse/snr_-5/
# 
# python3 audioAnalysis.py trainClassifier -i ../../../proyecto_procesamiento_de_sonido/dataset/pasos_oficina_carolina_joseline_michelle/mmse/original/snr_-10/carolina/train/carolina/ ../../../proyecto_procesamiento_de_sonido/dataset/pasos_oficina_carolina_joseline_michelle/mmse/original/snr_-10/joseline/train/joseline/ --method svm -o sp-project/oficina/mmse/snr_-10/original_snr_-10
# cd sp-project/oficina/mmse/snr_-10/
# cp original_snr_-10* ../../../../../proyecto_procesamiento_de_sonido/trained_models/oficina/mmse/snr_-10/

### spect_subs

# python3 audioAnalysis.py trainClassifier -i ../../../proyecto_procesamiento_de_sonido/dataset/pasos_oficina_carolina_joseline_michelle/spect_sub/original/snr_10/carolina/train/carolina/ ../../../proyecto_procesamiento_de_sonido/dataset/pasos_oficina_carolina_joseline_michelle/spect_sub/original/snr_10/joseline/train/joseline/ --method svm -o sp-project/oficina/spect_sub/snr_10/original_snr_10
# cd sp-project/oficina/spect_sub/snr_10/
# cp original_snr_10* ../../../../../proyecto_procesamiento_de_sonido/trained_models/oficina/spect_sub/snr_10/
# 
# python3 audioAnalysis.py trainClassifier -i ../../../proyecto_procesamiento_de_sonido/dataset/pasos_oficina_carolina_joseline_michelle/spect_sub/original/snr_0/carolina/train/carolina/ ../../../proyecto_procesamiento_de_sonido/dataset/pasos_oficina_carolina_joseline_michelle/spect_sub/original/snr_0/joseline/train/joseline/ --method svm -o sp-project/oficina/spect_sub/snr_0/original_snr_0
# cd sp-project/oficina/spect_sub/snr_0/
# cp original_snr_0* ../../../../../proyecto_procesamiento_de_sonido/trained_models/oficina/spect_sub/snr_0/
# 
# python3 audioAnalysis.py trainClassifier -i ../../../proyecto_procesamiento_de_sonido/dataset/pasos_oficina_carolina_joseline_michelle/spect_sub/original/snr_5/carolina/train/carolina/ ../../../proyecto_procesamiento_de_sonido/dataset/pasos_oficina_carolina_joseline_michelle/spect_sub/original/snr_5/joseline/train/joseline/ --method svm -o sp-project/oficina/spect_sub/snr_5/original_snr_5
# cd sp-project/oficina/spect_sub/snr_5/
# cp original_snr_5* ../../../../../proyecto_procesamiento_de_sonido/trained_models/oficina/spect_sub/snr_5/
# 
# python3 audioAnalysis.py trainClassifier -i ../../../proyecto_procesamiento_de_sonido/dataset/pasos_oficina_carolina_joseline_michelle/spect_sub/original/snr_-5/carolina/train/carolina/ ../../../proyecto_procesamiento_de_sonido/dataset/pasos_oficina_carolina_joseline_michelle/spect_sub/original/snr_-5/joseline/train/joseline/ --method svm -o sp-project/oficina/spect_sub/snr_-5/original_snr_-5
# cd sp-project/oficina/spect_sub/snr_-5/
# cp original_snr_-5* ../../../../../proyecto_procesamiento_de_sonido/trained_models/oficina/spect_sub/snr_-5/
# 
# python3 audioAnalysis.py trainClassifier -i ../../../proyecto_procesamiento_de_sonido/dataset/pasos_oficina_carolina_joseline_michelle/spect_sub/original/snr_-10/carolina/train/carolina/ ../../../proyecto_procesamiento_de_sonido/dataset/pasos_oficina_carolina_joseline_michelle/spect_sub/original/snr_-10/joseline/train/joseline/ --method svm -o sp-project/oficina/spect_sub/snr_-10/original_snr_-10
# cd sp-project/oficina/spect_sub/snr_-10/
# cp original_snr_-10* ../../../../../proyecto_procesamiento_de_sonido/trained_models/oficina/spect_sub/snr_-10/

### wiener

# python3 audioAnalysis.py trainClassifier -i ../../../proyecto_procesamiento_de_sonido/dataset/pasos_oficina_carolina_joseline_michelle/wiener/original/snr_10/carolina/train/carolina/ ../../../proyecto_procesamiento_de_sonido/dataset/pasos_oficina_carolina_joseline_michelle/wiener/original/snr_10/joseline/train/joseline/ --method svm -o sp-project/oficina/wiener/snr_10/original_snr_10
# cd sp-project/oficina/wiener/snr_10/
# cp original_snr_10* ../../../../../proyecto_procesamiento_de_sonido/trained_models/oficina/wiener/snr_10/
# 
# python3 audioAnalysis.py trainClassifier -i ../../../proyecto_procesamiento_de_sonido/dataset/pasos_oficina_carolina_joseline_michelle/wiener/original/snr_0/carolina/train/carolina/ ../../../proyecto_procesamiento_de_sonido/dataset/pasos_oficina_carolina_joseline_michelle/wiener/original/snr_0/joseline/train/joseline/ --method svm -o sp-project/oficina/wiener/snr_0/original_snr_0
# cd sp-project/oficina/wiener/snr_0/
# cp original_snr_0* ../../../../../proyecto_procesamiento_de_sonido/trained_models/oficina/wiener/snr_0/
# 
# python3 audioAnalysis.py trainClassifier -i ../../../proyecto_procesamiento_de_sonido/dataset/pasos_oficina_carolina_joseline_michelle/wiener/original/snr_5/carolina/train/carolina/ ../../../proyecto_procesamiento_de_sonido/dataset/pasos_oficina_carolina_joseline_michelle/wiener/original/snr_5/joseline/train/joseline/ --method svm -o sp-project/oficina/wiener/snr_5/original_snr_5
# cd sp-project/oficina/wiener/snr_5/
# cp original_snr_5* ../../../../../proyecto_procesamiento_de_sonido/trained_models/oficina/wiener/snr_5/
# 
# python3 audioAnalysis.py trainClassifier -i ../../../proyecto_procesamiento_de_sonido/dataset/pasos_oficina_carolina_joseline_michelle/wiener/original/snr_-5/carolina/train/carolina/ ../../../proyecto_procesamiento_de_sonido/dataset/pasos_oficina_carolina_joseline_michelle/wiener/original/snr_-5/joseline/train/joseline/ --method svm -o sp-project/oficina/wiener/snr_-5/original_snr_-5
# cd sp-project/oficina/wiener/snr_-5/
# cp original_snr_-5* ../../../../../proyecto_procesamiento_de_sonido/trained_models/oficina/wiener/snr_-5/
# 
# python3 audioAnalysis.py trainClassifier -i ../../../proyecto_procesamiento_de_sonido/dataset/pasos_oficina_carolina_joseline_michelle/wiener/original/snr_-10/carolina/train/carolina/ ../../../proyecto_procesamiento_de_sonido/dataset/pasos_oficina_carolina_joseline_michelle/wiener/original/snr_-10/joseline/train/joseline/ --method svm -o sp-project/oficina/wiener/snr_-10/original_snr_-10
# cd sp-project/oficina/wiener/snr_-10/
# cp original_snr_-10* ../../../../../proyecto_procesamiento_de_sonido/trained_models/oficina/wiener/snr_-10/





# 
# 
# python3 ../pyAudioAnalysis/audioAnalysis.py trainClassifier -i dataset/pasos_babble_carolina_joseline_michelle/mmse/original/snr_10/carolina/train/carolina/ dataset/pasos_babble_carolina_joseline_michelle/mmse/original/snr_10/joseline/train/joseline/ --method svm -o trained_models/original_snr_10
# 
# ./evaluate_model.py --class1 dataset/pasos_babble_carolina_joseline_michelle/mmse/original/snr_-10/carolina/test/carolina --class2 dataset/pasos_babble_carolina_joseline_michelle/mmse/original/snr_-10/joseline/test/joseline --model trained_models/original_snr_10 --pos_class carolina
