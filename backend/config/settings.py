from pathlib import Path

APP_NAME = "CURE Protocol"

API_VERSION = "v1"

BASE_DIR = Path(__file__).resolve().parent.parent.parent

UPLOAD_FOLDER = "01 - Intake"
PROCESSING_FOLDER = "02 - Processing"
COMPLETED_FOLDER = "03 - Completed"
FAILED_FOLDER = "04 - Failed"

GOOGLE_DRIVE_ROOT = "CURE Protocol Uploads"

MAX_UPLOAD_SIZE_MB = 25

ALLOWED_FILE_TYPES = [
    ".pdf",
]
