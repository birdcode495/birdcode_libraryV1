import tkinter as tk
from tkinter import filedialog
from tkVideoPlayer import TkinterVideo
from moviepy.editor import VideoFileClip

class VideoPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Player")
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        self.video_path = None
        self.volume = 1.0
        self.create_widgets()

    def create_widgets(self):
        # Open File button
        self.open_button = tk.Button(self.frame, text="Open Video", command=self.open_video)
        self.open_button.pack()

        # Volume control
        self.volume_label = tk.Label(self.frame, text="Volume")
        self.volume_label.pack()

        self.volume_slider = tk.Scale(self.frame, from_=0, to=1, resolution=0.01, orient=tk.HORIZONTAL,
                                      command=self.set_volume)
        self.volume_slider.set(self.volume)
        self.volume_slider.pack()

        # Play button
        self.play_button = tk.Button(self.frame, text="Play", command=self.play_video)
        self.play_button.pack()

    def open_video(self):
        file_path = filedialog.askopenfilename(filetypes=[("avatar", "*.mp4 *.avi *.mkv")])
        if file_path:
            self.video_path = file_path

    def set_volume(self, volume):
        self.volume = float(volume)

    def play_video(self):
        if self.video_path:
            clip = VideoFileClip(self.video_path)
            clip = clip.volumex(self.volume)
            clip.preview()

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoPlayer(root)
    root.mainloop()