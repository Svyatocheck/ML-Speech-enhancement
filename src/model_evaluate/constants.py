
SAMPLE_RATE = 16000

WINDOW_LENGTH = 512

OVERLAP = round(0.5 * WINDOW_LENGTH)  # 50%

N_FFT = WINDOW_LENGTH

N_FEATURES = N_FFT // 2 + 1  # 257

N_SEGMENTS = 1
