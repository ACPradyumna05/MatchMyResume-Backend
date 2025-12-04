import fitz
from PIL import Image
import pytesseract
import io

class PDFParser:
    def parse(self, pdf_bytes: bytes) -> str:
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        texts = []
        for page in doc:
            t = page.get_text().strip()
            texts.append(t)
        combined = "\n".join(texts).strip()
        print("\n\n===== PARSED RESUME TEXT =====\n")
        print(combined)
        print("\n===== END PARSED TEXT =====\n\n")
        if len(combined) > 50:
            return combined

        ocr_texts = []
        for page in doc:
            pix = page.get_pixmap()
            img = Image.open(io.BytesIO(pix.tobytes("png"))).convert("RGB")
            ocr_texts.append(pytesseract.image_to_string(img))
        

        return "\n".join(ocr_texts).strip()
