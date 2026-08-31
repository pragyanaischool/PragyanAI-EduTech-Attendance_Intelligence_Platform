import qrcode
import uuid
from datetime import datetime, timedelta
from io import BytesIO

class QREngine:
    @staticmethod
    def generate_session_token(faculty_id: int, subject_id: int, duration_minutes: int = 10):
        """Generates a secure, time-limited tokenized QR session."""
        secure_token = str(uuid.uuid4())
        expires_at = datetime.utcnow() + timedelta(minutes=duration_minutes)
        return secure_token, expires_at

    @staticmethod
    def create_qr_image(secure_token: str) -> BytesIO:
        """Encodes the token into a high-error-correction PNG QR code image."""
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(f"https://pragyan-ai.edu/mark?token={secure_token}")
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        buffered.seek(0)
        return buffered
