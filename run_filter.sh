
if [[ $# -eq 0 ]] ; then
	echo 'SH_ERROR: No arguments'
	exit 1
else

	mkdir $1/original
	mkdir $1/filtered

	for file in $(ls $1/*lin*); do
		file_name=`ls $file | sed 's/.wav//g'` 
		aux_name=`ls $file | sed 's/.wav/_.wav/g'`
		output_file=`ls $file | sed 's/.wav/_filtered/g'`
		echo "SH_INFO: Working on audio file: $file"
		echo "SH_INFO: Running filters!"
		./proyecto_ps.py --filter_type $2 --input_noisy $file --output_file ${output_file}.wav --num_FFT 1024
		echo "SH_INFO: Running SOX for original signal!"
		sox $file $aux_name trim 0 5 : newfile : restart
		echo "SH_INFO: Running SOX for filtered signal"
		sox ${output_file}.wav ${output_file}_.wav trim 0 5 : newfile : restart
		mv ${output_file}*.wav $1/filtered
		mv ${file_name}_*.wav $1/original
		
		echo ""
	done

	echo "SH_INFO: Moving to each dir by SNR!" 

	mkdir $1/original/snr_-10
	mkdir $1/original/snr_-5
	mkdir $1/original/snr_0
	mkdir $1/original/snr_5
	mkdir $1/original/snr_10
	mkdir $1/filtered/snr_-10
	mkdir $1/filtered/snr_-5
	mkdir $1/filtered/snr_0
	mkdir $1/filtered/snr_5
	mkdir $1/filtered/snr_10

	mkdir $1/original/snr_-10/carolina $1/original/snr_-10/joseline
	mkdir $1/original/snr_-5/carolina $1/original/snr_-5/joseline
	mkdir $1/original/snr_0/carolina $1/original/snr_0/joseline
	mkdir $1/original/snr_5/carolina $1/original/snr_5/joseline
	mkdir $1/original/snr_10/carolina $1/original/snr_10/joseline
	
	mkdir $1/filtered/snr_-10/carolina $1/filtered/snr_-10/joseline
	mkdir $1/filtered/snr_-5/carolina $1/filtered/snr_-5/joseline
	mkdir $1/filtered/snr_0/carolina $1/filtered/snr_0/joseline
	mkdir $1/filtered/snr_5/carolina $1/filtered/snr_5/joseline
	mkdir $1/filtered/snr_10/carolina $1/filtered/snr_10/joseline

	#### Carolina
	mv $1/original/*carolina*pasos_10minutossnr_-10_mix_*wav $1/original/snr_-10/carolina
	mv $1/original/*carolina*pasos_10minutossnr_-5_mix_*wav $1/original/snr_-5/carolina
	mv $1/original/*carolina*pasos_10minutossnr_0_mix_*wav $1/original/snr_0/carolina
	mv $1/original/*carolina*pasos_10minutossnr_5_mix_*wav $1/original/snr_5/carolina
	mv $1/original/*carolina*pasos_10minutossnr_10_mix_*wav $1/original/snr_10/carolina

	mv $1/filtered/*carolina*pasos_10minutossnr_-10*wav $1/filtered/snr_-10/carolina
	mv $1/filtered/*carolina*pasos_10minutossnr_-5*wav $1/filtered/snr_-5/carolina
	mv $1/filtered/*carolina*pasos_10minutossnr_0_mix_*wav $1/filtered/snr_0/carolina
	mv $1/filtered/*carolina*pasos_10minutossnr_5_mix_*wav $1/filtered/snr_5/carolina
	mv $1/filtered/*carolina*pasos_10minutossnr_10_mix_*wav $1/filtered/snr_10/carolina

	#### Joseline
	mv $1/original/*joseline*pasos_10minutossnr_-10_mix_*wav $1/original/snr_-10/joseline
	mv $1/original/*joseline*pasos_10minutossnr_-5_mix_*wav $1/original/snr_-5/joseline
	mv $1/original/*joseline*pasos_10minutossnr_0_mix_*wav $1/original/snr_0/joseline
	mv $1/original/*joseline*pasos_10minutossnr_5_mix_*wav $1/original/snr_5/joseline
	mv $1/original/*joseline*pasos_10minutossnr_10_mix_*wav $1/original/snr_10/joseline

	mv $1/filtered/*joseline*pasos_10minutossnr_-10*wav $1/filtered/snr_-10/joseline
	mv $1/filtered/*joseline*pasos_10minutossnr_-5*wav $1/filtered/snr_-5/joseline
	mv $1/filtered/*joseline*pasos_10minutossnr_0_mix_*wav $1/filtered/snr_0/joseline
	mv $1/filtered/*joseline*pasos_10minutossnr_5_mix_*wav $1/filtered/snr_5/joseline
	mv $1/filtered/*joseline*pasos_10minutossnr_10_mix_*wav $1/filtered/snr_10/joseline


fi