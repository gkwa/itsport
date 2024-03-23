import os
import pathlib

import exifread
import jinja2


def get_template(template_name):
    TEMPLATES_PATH = pathlib.Path(__file__).resolve().parent / "templates"
    loader = jinja2.FileSystemLoader(searchpath=TEMPLATES_PATH)
    env = jinja2.Environment(loader=loader)
    return env.get_template(template_name)


def render_template(template_name, data=None):
    template = get_template(template_name)

    if data:
        dir_path = data.dir
        exif_data = []
        for filename in os.listdir(dir_path):
            if filename.endswith(".png"):
                file_path = os.path.join(dir_path, filename)

                with open(file_path, "rb") as f:
                    tags = exifread.process_file(f)

                    file_data = {"filename": filename, "exif_tags": []}
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

                    exif_data.append(file_data)

        data.exif_data = exif_data

    return template.render(data=data)
