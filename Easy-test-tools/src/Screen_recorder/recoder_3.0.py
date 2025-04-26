import subprocess
import threading
import time

# Output file names
output_system_audio = "system_audio.wav"
output_microphone = "microphone.wav"
output_final = "final_output.mp4"

# FFmpeg commands to record system audio and microphone
# Replace `audio_device_system` and `audio_device_microphone` with your actual device names
command_system_audio = [
    "ffmpeg",
    "-f", "dshow",  # Use `dshow` for Windows, `pulse` for Linux, `avfoundation` for macOS
    # Replace with your system audio device name
    "-i", "audio=Stereo Mix (Realtek Audio)",
    output_system_audio,
]

command_microphone = [
    "ffmpeg",
    "-f", "dshow",  # Use `dshow` for Windows, `pulse` for Linux, `avfoundation` for macOS
    # Replace with your microphone device name
    "-i", "audio=Microphone (Realtek Audio)",
    output_microphone,
]

# Function to stop FFmpeg processes


def stop_ffmpeg(process):
    process.terminate()  # Gracefully stop the FFmpeg process
    process.wait()  # Wait for the process to exit


# Start recording system audio and microphone
print("Recording system audio and microphone...")
process_system_audio = subprocess.Popen(
    command_system_audio, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
process_microphone = subprocess.Popen(
    command_microphone, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Wait for user input to stop recording
input("Press Enter to stop recording...")

# Stop the FFmpeg processes
print("Stopping recording...")
stop_ffmpeg(process_system_audio)
stop_ffmpeg(process_microphone)

print("Recording stopped. Combining system audio and microphone...")

# Combine system audio and microphone into a single file
command_combine = [
    "ffmpeg",
    "-i", output_system_audio,
    "-i", output_microphone,
    "-filter_complex", "[0:a][1:a]amerge=inputs=2[a]",  # Merge audio streams
    "-map", "[a]",
    "-ac", "2",  # Set to stereo
    output_final,
]

# Run the combine command
subprocess.run(command_combine, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

print(f"Final output saved as {output_final}")
