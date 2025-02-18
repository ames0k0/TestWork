import io

import pydub
from fastapi import UploadFile

from app import config


def convert_wav_to_mp3(file: bytes) -> bytes:
    """Конвертирует `.wav` в `.mp3`

    Возвращает байты конвертированного файла
    """
    audio_export = io.BytesIO()

    audio_segment = pydub.AudioSegment.from_wav(
        file=io.BytesIO(file),
    )
    audio_segment.export(
        audio_export,
        format=config.SUPPORTED_RECORD_EXPORT_FILE_FORMAT,
    )

    return audio_export.getvalue()
