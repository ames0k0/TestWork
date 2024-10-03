import os
from hashlib import md5
from pathlib import Path
from datetime import datetime

from fastapi import UploadFile

from src.config import settings


async def save_resume_file(file: UploadFile) -> Path:
    """ Saving the file to `PROJECT_STATICFILES_DIR`

    Returns the saved filepath
    """
    # XXX: same filename will rewire the old one
    filename = md5(
        f"{file.filename} {datetime.now()}".encode()
    ).hexdigest()
    file_ext = os.path.splitext(file.filename)[-1]
    filepath = settings.PROJECT_RESUME_FILES_DIR / (filename + file_ext)

    with open(filepath, "wb") as ftw:
        ftw.write(await file.read())

    return filepath