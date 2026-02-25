import subprocess

def duration(filename):
    result = subprocess.run(
        ["ffprobe","-v","error","-show_entries","format=duration",
         "-of","default=noprint_wrappers=1:nokey=1", filename],
        stdout=subprocess.PIPE
    )
    return float(result.stdout or 0)
