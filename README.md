# Proyecto:
# Procesamiento de sonido

## Objetivo general:  
Determinar el beneficio de los algoritmos de filtrado de ruido en la identificación biométrica de personas usando sonido de pasos.  

## Objetivos específicos: 
- Conocer el estado del arte de la identificación biométrica usando el sonido de pasos. 
- Aplicar sistemas de procesamiento de sonido para degradar las señales de pasos con ruidos de diversos tipos y niveles.
- Implementar diversos tipos de filtros de ruido desarrollados recientemente, para determinar su capacidad con las señales degradadas. 
- Aplicar sistemas de clasificación a las señales degradadas, para determinar de forma comparativa los beneficios de los distintos filtros.

## Experimentos:

Se entrena el modelo con los audios que tienen un SNR=10 (Menor cantidad de ruido)

El clasificador a utilizar es un **SVM**.

Para cada ruido:

1. Babble:
	1.  MMSE:
		- SNR = -10:
	2.  Spectral sub:
		- SNR = -10:
	3.  Wiener
		- SNR = -10:
2. Rudio Blanco:
	1.  MMSE:
		- SNR = -10:
	2.  Spectral sub:
		- SNR = -10:
	3.  Wiener
		- SNR = -10:
3. Oficina:
	1.  MMSE:
		- SNR = -10:
	2.  Spectral sub:
		- SNR = -10:
	3.  Wiener
		- SNR = -10:

python3 ../pyAudioAnalysis/audioAnalysis.py trainClassifier -i dataset/pasos_babble_carolina_joseline_michelle/mmse/original/snr_10/carolina/train/carolina/ dataset/pasos_babble_carolina_joseline_michelle/mmse/original/snr_10/joseline/train/joseline/ --method svm -o trained_models/original_snr_10


./evaluate_model.py --class1 dataset/pasos_babble_carolina_joseline_michelle/mmse/original/snr_-10/carolina/test/carolina --class2 dataset/pasos_babble_carolina_joseline_michelle/mmse/original/snr_-10/joseline/test/joseline --model trained_models/original_snr_10 --pos_class carolina