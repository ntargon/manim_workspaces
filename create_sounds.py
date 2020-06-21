from synthesizer import Synthesizer, Waveform, Writer

synth = Synthesizer(osc1_waveform=Waveform.square, osc1_volume=1.0*0.5, use_osc2=False)
writer = Writer()

wave = synth.generate_constant_wave(frequency=440.0, length=0.1)
writer.write_wave("A.wav", wave)
wave = synth.generate_constant_wave(frequency=349.228, length=0.1)
writer.write_wave("F.wav", wave)
wave = synth.generate_constant_wave(frequency=391.995, length=0.1)
writer.write_wave("G.wav", wave)