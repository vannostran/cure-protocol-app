from pathlib import Path
from typing import BinaryIO

from backend.config.settings import (
    GOOGLE_DRIVE_ROOT,
    UPLOAD_FOLDER,
    PROCESSING_FOLDER,
    COMPLETED_FOLDER,
    FAILED_FOLDER,
)


class GoogleDriveStorage:
    def __init__(self) -> None:
        self.root_folder = GOOGLE_DRIVE_ROOT
        self.intake_folder = UPLOAD_FOLDER
        self.processing_folder = PROCESSING_FOLDER
        self.completed_folder = COMPLETED_FOLDER
        self.failed_folder = FAILED_FOLDER

    def upload_to_intake(
        self,
        filename: str,
        file_object: BinaryIO,
    ) -> str:
        """
        Upload a file to the CURE Protocol Intake folder.

        Returns the Google Drive file ID.

        Google Drive API implementation will be added after
        authentication and credentials are configured.
        """
        raise NotImplementedError(
            "Google Drive upload integration is not configured yet."
        )

    def move_to_processing(self, file_id: str) -> None:
        raise NotImplementedError

    def move_to_completed(self, file_id: str) -> None:
        raise NotImplementedError

    def move_to_failed(self, file_id: str) -> None:
        raise NotImplementedError
