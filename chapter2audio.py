from pydub import AudioSegment

# Memuat file audio
audio = AudioSegment.from_file('audio/audio.mp3')

# Menyimpan file audio
audio.export('hasilaudio/result.mp3', format='mp3')

#Cutting file audio
clipped_audio = audio[:10000]  # Mendapatkan 10 detik pertama
clipped_audio.export('hasilaudio/clipped_result.mp3', format='mp3')

#mixing file audio
combined_audio = audio + clipped_audio
combined_audio.export('hasilaudio/combined_result.mp3', format='mp3')

#konvert file audio
audio.export('hasilaudio/result.wav', format='wav')

#volume file audio
louder_audio = audio - 10  # Meningkatkan volume sebesar 10dB
louder_audio.export('hasilaudio/louder_result.mp3', format='mp3')