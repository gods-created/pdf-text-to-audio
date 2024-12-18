from pypdf import PdfReader
from gtts import gTTS
from random import choice
from string import ascii_letters, digits
from langdetect import detect, lang_detect_exception
from loguru import logger

def generate_string() -> str:
    return ''.join(choice(ascii_letters + digits) for _ in range(30))

def detect_language(text: str) -> str:
    lang = 'en'

    try:
        lang = detect(text)

    except (lang_detect_exception.LangDetectException, Exception, ) as e:
        logger.error(str(e))
        
    finally:
        return lang

def get_text_from_pdf(file_path: str) -> str:
    reader = PdfReader(file_path)
    pages = reader.pages
    all_pages = len(pages)

    text = ''

    if all_pages == 0:
        return text
    
    for page in pages: text += page.extract_text()

    return text

def create_mp3_record(text: str) -> str:
    lang = detect_language(text)

    obj = gTTS(text=text, lang=lang, slow=False)
    filename = generate_string() + '.mp3'
    obj.save(filename)

    return 'Audio file created successfully'