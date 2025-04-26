import cv2
import numpy as np
import pyautogui
import pyaudio
import wave
import threading
import time
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeVideoClip

# Screen recording settings
screen_size = pyautogui.size()
fps = 12.0
output_screen = "screen_recording.avi"
output_audio = "audio_recording.wav"
output_final = "final_output.mp4"
fourcc = cv2.VideoWriter_fourcc(*"XVID")

# Audio recording settings
chunk = 1024
format = pyaudio.paInt16
channels = 2
rate = 44100

# Initialize video writer
out = cv2.VideoWriter(output_screen, fourcc, fps, screen_size)

# Initialize audio stream
audio = pyaudio.PyAudio()
stream = audio.open(format=format, channels=channels,
                    rate=rate, input=True, frames_per_buffer=chunk)

# Variables to store audio frames
audio_frames = []

# Flag to control recording
recording = True


def record_audio():
    while recording:
        data = stream.read(chunk)
        audio_frames.append(data)


def record_screen():
    while recording:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        out.write(frame)
        time.sleep(1 / fps)


# Start audio recording in a separate thread
audio_thread = threading.Thread(target=record_audio)
audio_thread.start()

# Start screen recording
screen_thread = threading.Thread(target=record_screen)
screen_thread.start()

# Wait for user to stop recording
input("Press Enter to stop recording...")
recording = False

# Wait for threads to finish
audio_thread.join()
screen_thread.join()

# Release video writer
out.release()

# Stop and close audio stream
stream.stop_stream()
stream.close()
audio.terminate()

# Save audio recording
wf = wave.open(output_audio, 'wb')
wf.setnchannels(channels)
wf.setsampwidth(audio.get_sample_size(format))
wf.setframerate(rate)
wf.writeframes(b''.join(audio_frames))
wf.close()

print("Recording stopped. Combining video and audio...")

# Combine video and audio using moviepy
video_clip = VideoFileClip(output_screen)
audio_clip = AudioFileClip(output_audio)

# Set the audio of the video clip
final_clip = video_clip.set_audio(audio_clip)

# Write the final output file
final_clip.write_videofile(output_final, codec="libx264", fps=fps)

print(f"Final output saved as {output_final}")
