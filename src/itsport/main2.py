import logging
import pathlib

import exifread


def get_exif_data(dir_path):
    dir_path = pathlib.Path(dir_path)
    exif_data = []
    unique_tags = set()
    for file_path in dir_path.glob("*.[pP][nN][gG]"):
        logging.debug(f"Processing file: {file_path}")
        with open(file_path, "rb") as f:
            tags = exifread.process_file(f)

            file_data = {"filename": file_path.name, "exif_tags": []}
            for tag in tags.keys():
                if tag not in (
                    "JPEGThumbnail",
                    "TIFFThumbnail",
                    "Filename",
                    "EXIF MakerNote",
                ):
                    file_data["exif_tags"].append(
                        {"name": tag, "value": str(tags[tag])}
                    )
                    unique_tags.add(tag)

            exif_data.append(file_data)

    return exif_data, unique_tags


def render_output(exif_data, unique_tags):
    output = ""
    for file_data in exif_data:
        output += f"EXIF data for {file_data['filename']}:\n"
        for tag in file_data["exif_tags"]:
            output += f"  {tag['name']}: {tag['value']}\n"
        output += "\n"

    output += "Unique EXIF tags found:\n"
    for tag in sorted(unique_tags):
        output += f"- {tag}\n"

    return output
