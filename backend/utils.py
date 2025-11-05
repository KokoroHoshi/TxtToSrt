# utils.py
import re

MAX_CHARS = 20
CHAR_TIMES = {
    "default": 0.2,
    "，": 0.1, "；": 0.2, "？": 0.4, "?": 0.2,
    "！": 0.2, "。": 0.3, "(": 0.1, ")": 0.1,
    "「": 0.05, "」": 0.05, ".": 0.1, "、": 0.1
}
PUNCTS = set("，；？?！。()「」.、")


def calc_time(text):
    total = 0.0
    for c in text:
        total += CHAR_TIMES.get(c, CHAR_TIMES["default"])
    return total


def split_long_line(line):
    segments = []
    current = ""
    for char in line:
        current += char
        if len(current) >= MAX_CHARS:
            match = re.search(f"[{re.escape(''.join(PUNCTS))}](?!.*[{re.escape(''.join(PUNCTS))}])", current)
            if match:
                cut_pos = match.end()
                segments.append(current[:cut_pos].strip())
                current = current[cut_pos:].strip()
            else:
                segments.append(current.strip())
                current = ""
    if current.strip():
        segments.append(current.strip())
    return segments


def split_text(text):
    lines = text.splitlines()
    segments = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if len(line) <= MAX_CHARS:
            segments.append(line)
        else:
            segments.extend(split_long_line(line))
    return segments


def generate_srt(segments):
    srt_lines = []
    current_time = 0.0

    for i, seg in enumerate(segments, start=1):
        dur = calc_time(seg)
        start = current_time
        end = current_time + dur
        current_time = end

        def fmt(t):
            h = int(t // 3600)
            m = int((t % 3600) // 60)
            s = int(t % 60)
            ms = int((t - int(t)) * 1000)
            return f"{h:02}:{m:02}:{s:02},{ms:03}"

        srt_lines.append(str(i))
        srt_lines.append(f"{fmt(start)} --> {fmt(end)}")
        srt_lines.append(seg)
        srt_lines.append("")

    return "\n".join(srt_lines)
