import os
import subprocess
from tqdm import tqdm

# store the total duration in seconds
total_duration = 0

# loop through all files in the directory and its subdirectories
num_files = 0
for root, dirs, files in os.walk("."):
    num_files += len(files)

with tqdm(total=num_files, unit="file") as pbar:
    for root, dirs, files in os.walk("."):
        for file in files:
            file_path = os.path.join(root, file)
            if file_path.endswith((".mp4", ".mkv", ".avi", ".flv", ".wmv")):
                result = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                duration = float(result.stdout)
                total_duration += duration
                pbar.update(1)

# calculate the total duration in hours
total_duration_hours = total_duration / 3600

# write the result to a text file
with open("total_duration.txt", "w") as file:
    file.write(f"Total duration of all videos: {total_duration_hours:.2f} hours")

# print the result
print(f"Result written to total_duration.txt")
