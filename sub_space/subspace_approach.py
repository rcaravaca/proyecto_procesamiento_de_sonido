import pyroomacoustics as pra

# import or create `noisy_signal`
denoised_signal = pra.apply_subspace(noisy_signal, frame_len=256, mu=10,
                                 lookback=10, skip=2, thresh=0.01)

''' Parameters:	
.- frame_len (int) – Frame length in samples. Note that large values (above 256) will make the 
eigendecompositions very expensive.
.- mu (float) – Enhancement factor, larger values suppress more noise but could lead to more distortion.
.- lookback (int) – How many frames to look back for covariance matrix estimation.
.- skip (int) – How many samples to skip when estimating the covariance matrices with past samples. skip=1 
will use all possible frames in the estimation.
.- thresh (float) – Threshold to distinguish between (signal+noise) and (noise) frames. 
A high value will classify more frames as noise but might remove desired signal!
.- data_type ('float32' or 'float64') – Data type to use in the enhancement procedure. Default is ‘float32’.
'''
