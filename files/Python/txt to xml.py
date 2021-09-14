# time to clean up the data

filename = "../../text/01_Harry Potter und der Stein der Weisen.txt"


def open_transcript(filename):
    with open (filename, "r", encoding='utf-8') as f:
        transcript = f.read()
    return transcript

def clean_transcript(transcript):
    if "--------" in transcript:
        transcript=transcript.replace("\n\n-------------------------------------------------------------------\n", "")
    transcript = transcript.replace("\n\n\n\n\n", "")
    transcript = transcript.split("\n\n___________________________________________")
    return transcript

def header_metadata(header):
    header = header.split("\n\n")
    metadata = header[3:]
    new_metadata = []
    for meta in metadata:
        if ":" in meta:
                meta = meta.split(":\t")[0]
                new_metadata.append(meta)
        else:
            meta = meta.split(" ")[0]
            new_metadata.append(meta)
    extra = header[:3]
    editor = new_metadata
    return extra, editor

def transcript_separate(transcript):
    transcript = transcript.replace("_\n", "")
    segments = transcript.split("\n\n")
    return segments

def clean_segments(segments):
    cleaned = []
    for segment in segments:
        segment = segment.replace("\n", " ").replace(" ?", "?")
        cleaned.append(segment)
    return cleaned

"""
def segment_metadata(segments):
    new = []
    for segment in segments:
        if ": " in segment:
            name, dialogue = segment.split(": ")
        else:
            name, dialogue = segment.split(":")
        name = name.strip()
        new.append([name, dialogue])
    return new
"""

"""
def speakers(segments):
    names = []
    for segment in segments:
        names.append(segment[0])
    names = set(names)
    return names
"""

def write_xml(xmlfile, header, segments):
    info = ["editor"]
    with open(xmlfile, "w", encoding='UTF-8') as f:
        f.write("<?xml version='1.0' encoding='UTF-8' standalone='no' ?>")
        f.write("<body>\n")
        f.write("<header>\n")
        f.write("<docinfo>\n")
        x=0
        for data in header[0]:
            f.write(f"{data}\n")
        f.write("</docinfo>\n")
        for data in header[1:]:
            f.write(f"<{info[x]}>{data}</{info[x]}>\n")
            x=x+1
        f.write("</header>\n")
        f.write("<transcript>\n")
        for segment in segments[1:]:
            f.write(f"<segment>{segment}</segment>\n")
        f.write("</transcript>\n")
        f.write("</body>\n")

transcript = open_transcript(filename)
transcript = clean_transcript(transcript)
header, transcript = transcript
header = header_metadata(header)
segments = transcript_separate(transcript)
segments = clean_segments(segments)
#segments = segment_metadata(segments)
#speakers = speakers(segments)
write_xml("HarryPotter1.xml", header, segments)