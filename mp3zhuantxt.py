import os
from pydub import AudioSegment
from moviepy.editor import VideoFileClip

media_path = r"D:\下载\videoplayback.m4a"  # 支持所有音频格式和常见视频格式

# 自动生成wav和txt文件名
base, ext = os.path.splitext(media_path)
wav_path = base + ".wav"
txt_path = base + ".txt"

# 判断是否为视频格式
video_exts = ['.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv']
if ext.lower() in video_exts:
    # 提取音频
    audio_path = base + "_audio_tmp.mp3"
    try:
        clip = VideoFileClip(media_path)
        clip.audio.write_audiofile(audio_path)
        media_path_for_pydub = audio_path
    except Exception as e:
        raise ValueError(f"无法提取视频中的音频，错误信息：{e}")
else:
    media_path_for_pydub = media_path

# 自动识别并读取音频（支持所有pydub支持的格式）
try:
    audio = AudioSegment.from_file(media_path_for_pydub)
except Exception as e:
    raise ValueError(f"无法读取音频文件，错误信息：{e}")

audio = audio.set_channels(1).set_frame_rate(16000)
audio.export(wav_path, format="wav")

# 如果有临时音频文件，处理完后删除
if ext.lower() in video_exts and os.path.exists(audio_path):
    os.remove(audio_path)

# ...existing code...
要求:简述