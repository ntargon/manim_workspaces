from synthesizer import Synthesizer, Waveform, Writer

synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
wave = synth.generate_constant_wave(frequency=2*440.0, length=0.1)

writer = Writer()
writer.write_wave("sine.wav", wave)