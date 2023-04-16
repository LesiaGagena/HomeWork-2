import sys
from pathlib import Path

JPEG_IMAGES = []
JPG_IMAGES = []
PNG_IMAGES = []
SVG_IMAGE = []

MP4_AUDIO = []
MOV_AUDIO = []
MKV_AUDIO = []

DOC_DOCUMENT = []
EXE_DOCUMENT = []
DOCX_DOCUMENT = []
TXT_DOCUMENT = []
PDF_DOCUMENT = []
XLSX_DOCUMENT = []
PPTX_DOCUMENT = []

MP3_MUSIC = []
OGG_MUSIC = []
WAV_MUSIC = []
AMR_MUSIC = []

ARCHIVES_ZIP = []
ARCHIVES_GZ = []
ARCHIVES_TAR = []

MY_OTHER = []


REGISTER_EXTENSION = {
    'JPEG': JPEG_IMAGES,
    'JPG': JPG_IMAGES,
    'PNG': PNG_IMAGES,
    'SVG': SVG_IMAGE,

    'MOV': MOV_AUDIO,
    'MKV': MKV_AUDIO,
    'MP4': MP4_AUDIO,

    'DOC': DOC_DOCUMENT,
    'EXE': EXE_DOCUMENT,
    'DOCX': DOCX_DOCUMENT,
    'TXT': TXT_DOCUMENT,
    'PDF': PDF_DOCUMENT,
    'XLSX': XLSX_DOCUMENT,
    'PPTX': PPTX_DOCUMENT,

    'MP3': MP3_MUSIC,
    'OGG': OGG_MUSIC,
    'WAV': WAV_MUSIC,
    'AMR': AMR_MUSIC,


    'ZIP': ARCHIVES_ZIP,
    'GZ': ARCHIVES_GZ,
    'TAR': ARCHIVES_TAR

}

FOLDERS = []
EXTENSIONS = set()
UNKNOWN = set()


def get_extension(filename: str) -> str:
    return Path(filename).suffix[1:].upper()


def scan(folder: Path):
    for item in folder.iterdir():
        # Робота з папкою
        if item.is_dir():
            # Перевіряємо, щоб папка не була тією в яку ми вже складаємо файли.
            if item.name not in ('archives', 'video', 'audio', 'documents', 'images', 'other'):
                FOLDERS.append(item)
                scan(item)  # скануємо цю вкладену папку - рекурсія
            continue  # переходимо до наступного елемента в сканованій папці
        # else:
        # Робота з файлом
        ext = get_extension(item.name)  # беремо розширення файлу
        full_name = folder / item.name  # беремо повний шлях до файлу
        if not ext:
            MY_OTHER.append(full_name)
        else:
            try:
                container = REGISTER_EXTENSION[ext]
                EXTENSIONS.add(ext)
                container.append(full_name)
            except KeyError:
                UNKNOWN.add(ext)
                MY_OTHER.append(full_name)


if __name__ == '__main__':
    folder_for_scan = sys.argv[1]
    print(f'Start in folder: {folder_for_scan}')

    scan(Path(folder_for_scan))
    print(f"Images jpeg: {JPEG_IMAGES}")
    print(f"Images jpg: {JPG_IMAGES}")
    print(f"Images png: {PNG_IMAGES}")
    print(f"Images svg: {SVG_IMAGE}")

    print(f"Audio mp4: {MP4_AUDIO}")
    print(f"Audio mov: {MOV_AUDIO}")

    print(f"document doc: {DOC_DOCUMENT}")
    print(f"document exe: {EXE_DOCUMENT}")
    print(f"document docx: {DOCX_DOCUMENT}")
    print(f"document txt: {TXT_DOCUMENT}")
    print(f"document pdf: {PDF_DOCUMENT}")
    print(f"document xlsx: {XLSX_DOCUMENT}")
    print(f"document pptx: {PPTX_DOCUMENT}")

    print(f"music mp3: {MP3_MUSIC}")
    print(f"music ogg: {OGG_MUSIC}")
    print(f"music wav: {WAV_MUSIC}")
    print(f"music amr: {AMR_MUSIC}")

    print(f"arhives zip: {ARCHIVES_ZIP}")
    print(f"arhives gz: {ARCHIVES_GZ}")
    print(f"arhives tar: {ARCHIVES_TAR}")

    print('*' * 25)
    print(f'Types of file in folder: {EXTENSIONS}')
    print(f'UNKNOWN: {UNKNOWN}')
