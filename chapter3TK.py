import tkinter as tk

# Membuat jendela utama
root = tk.Tk()
root.title("Multimedia Application")

# Menjalankan loop acara Tkinter
root.mainloop()

from PIL import Image, ImageTk

# Memuat gambar menggunakan Pillow
image = Image.open('gambar/gambar.jpeg')
photo = ImageTk.PhotoImage(image)

# Membuat label untuk menampilkan gambar
label = tk.Label(root, image=photo)
label.pack()

# from tkinter import filedialog
# from pydub import AudioSegment
# from pydub.playback import play

# # Definisikan fungsi untuk memutar musik
# def play_music():
#     file_path = filedialog.askopenfilename()
#     if file_path:
#         audio = AudioSegment.from_file(audio/audio.mp3)
#         play(audio)

# # Membuat tombol untuk memutar musik
# play_button = tk.Button(root, text="Play", command=play_music)
# play_button.pack()