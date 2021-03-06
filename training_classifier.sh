NOISE="oficina babble ruido_blanco"
FILTER="mmse spect_sub wiener"
SNR="snr_0 snr_-10 snr_10 snr_-5 snr_5"
CLASS="svm knn randomforest"
audio_type="original"

rm *_training_exec.sh
for noise in $NOISE; do
	for snr in $SNR; do 
		for clss in $CLASS; do 
			mkdir -p trained_models/${noise}/${audio_type}/${filter}/${clss}/${snr}/ && touch trained_models/${noise}/${audio_type}/${clss}/${snr}/foo.file
			echo "python3 pyAudioAnalysis/pyAudioAnalysis/audioAnalysis.py trainClassifier -i dataset/pasos_${noise}_carolina_joseline_michelle/${audio_type}/${snr}/carolina/train/carolina/ dataset/pasos_${noise}_carolina_joseline_michelle/${audio_type}/${snr}/joseline/train/joseline/ --method $clss -o trained_models/${noise}/${audio_type}/${filter}/${clss}/${snr}/model" >> ${noise}_training_exec.sh
		done
	done
done

audio_type="filtered"
for noise in $NOISE; do
	for snr in $SNR; do 
		for filter in $FILTER; do 
			for clss in $CLASS; do 
				mkdir -p trained_models/${noise}/${audio_type}/${filter}/${clss}/${snr}/ && touch trained_models/${noise}/${audio_type}/${filter}/${clss}/${snr}/foo.file
				echo "python3 pyAudioAnalysis/pyAudioAnalysis/audioAnalysis.py trainClassifier -i dataset/pasos_${noise}_carolina_joseline_michelle/${filter}/${audio_type}/${snr}/carolina/train/carolina/ dataset/pasos_${noise}_carolina_joseline_michelle/${filter}/${audio_type}/${snr}/joseline/train/joseline/ --method $clss -o trained_models/${noise}/${audio_type}/${filter}/${clss}/${snr}/model" >> ${noise}_training_exec.sh
			done
		done
	done
done