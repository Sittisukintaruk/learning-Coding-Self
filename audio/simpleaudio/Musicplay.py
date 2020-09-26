import simpleaudio as sa

filename = 'Music\\anime-paradise_gintama-opening-1.mp3'
wave_obj = sa.WaveObject.from_wave_file(filename)
play_obj = wave_obj.play()
play_obj.wait_done()  # Wait until sound has finished playing