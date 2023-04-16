from pathlib import Path
import shutil
import sys
import file_parser as parser
from normalize import normalize


# створюємо папку для медіа - фото, відео,
def handle_media(filename: Path, target_folder: Path) -> None:
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))


# Створюємо папку для audio - MP4
def handle_audio(filename: Path, target_folder: Path) -> None:
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))


# Створюємо папку для документів - EXE
def handle_doc(filename: Path, target_folder: Path) -> None:
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))


# Створюємо папку для іншого, що не єперераховане
def handle_other(filename: Path, target_folder: Path) -> None:

    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))


# Cтворюємо папку для архивних документів
def handle_arhive(filename: Path, target_folder: Path) -> None:
    target_folder.mkdir(exist_ok=True, parents=True)
    folder_for_file = target_folder / \
        normalize(filename.name.replace(filename.suffix, ''))
    folder_for_file.mkdir(exist_ok=True, parents=True)

    try:
        shutil.unpack_archive(str(filename.resolve()),
                              str(folder_for_file.resolve()))

        normalize(filename.name.replace(filename.suffix, ''))
    except shutil.ReadError:
        folder_for_file.rmdir()
        return None
    filename.unlink()


def handle_folder(folder: Path) -> None:
    try:
        folder.rmdir()
    except OSError:
        print(f'Sorry, we can not delete the folder: {folder}')


def main(folder: Path) -> None:
    parser.scan(folder)
    for file in parser.JPEG_IMAGES:
        handle_media(file, folder / 'images' / 'JPEG')
    for file in parser.JPG_IMAGES:
        handle_media(file, folder / 'images' / 'JPG')
    for file in parser.PNG_IMAGES:
        handle_media(file, folder / 'images' / 'PNG')
    for file in parser.SVG_IMAGE:
        handle_media(file, folder / 'images' / 'SVG')

    for file in parser.MP4_AUDIO:
        handle_audio(file, folder / 'audio' / 'MP4')
    for file in parser.MOV_AUDIO:
        handle_audio(file, folder / 'audio' / 'MOV')
    for file in parser.MKV_AUDIO:
        handle_audio(file, folder / 'audio' / 'MKV')

    for file in parser.EXE_DOCUMENT:
        handle_doc(file, folder / 'documrnts' / 'EXE')
    for file in parser.DOC_DOCUMENT:
        handle_doc(file, folder / 'documrnts' / 'DOC')
    for file in parser.DOCX_DOCUMENT:
        handle_doc(file, folder / 'documrnts' / 'DOCX')
    for file in parser.TXT_DOCUMENT:
        handle_doc(file, folder / 'documrnts' / 'TXT')
    for file in parser.PDF_DOCUMENT:
        handle_doc(file, folder / 'documrnts' / 'PDF')
    for file in parser.XLSX_DOCUMENT:
        handle_doc(file, folder / 'documrnts' / 'XLSX')
    for file in parser.PPTX_DOCUMENT:
        handle_doc(file, folder / 'documrnts' / 'PPTX')

    for file in parser.MP3_MUSIC:
        handle_doc(file, folder / 'documrnts' / 'MP3')
    for file in parser.OGG_MUSIC:
        handle_doc(file, folder / 'documrnts' / 'OGG')
    for file in parser.WAV_MUSIC:
        handle_doc(file, folder / 'documrnts' / 'WAV')
    for file in parser.AMR_MUSIC:
        handle_doc(file, folder / 'documrnts' / 'AMR')

    for file in parser.MY_OTHER:
        handle_other(file, folder / 'MY_OTHER')

    for file in parser.ARCHIVES_ZIP:
        handle_arhive(file, folder / 'ZIP')
    for file in parser.ARCHIVES_GZ:
        handle_arhive(file, folder / 'GZ')
    for file in parser.ARCHIVES_TAR:
        handle_arhive(file, folder / 'TAR')

    for folder in parser.FOLDERS[::-1]:
        handle_folder(folder)


if __name__ == '__main__':
    folder_for_scan = Path(sys.argv[1])
    main(folder_for_scan.resolve())
