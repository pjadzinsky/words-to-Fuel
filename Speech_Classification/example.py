from features import mfcc
from features import logfbank
import scipy.io.wavfile as wav
import pdb

pdb.set_trace()
(rate,sig) = wav.read("Spanish_Numbers/cero_0.wav")
mfcc_feat = mfcc(sig,rate)
fbank_feat = logfbank(sig,rate)

print(fbank_feat[1:3,:])
