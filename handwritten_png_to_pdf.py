import re
from pathlib import Path

from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader


# ============================================================
# CONFIGURATION
# ============================================================

ROOT_DIR = Path("downloaded_notes")

# Delete PNG images after successfully creating PDF?
DELETE_IMAGES_AFTER_PDF = False

# Supported image formats
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}

# PDF page sizing
# "original" = match image dimensions
# "A4"       = fit image inside A4
PAGE_SIZE_MODE = "original"

# PDF quality
JPEG_QUALITY = 95


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def natural_sort_key(path):
    """
    Sort files numerically.

    Example:
        page_1.png
        page_2.png
        page_10.png

    Instead of:
        page_1.png
        page_10.png
        page_2.png
    """

    return [
        int(text) if text.isdigit() else text.lower()
        for text in re.split(r"(\d+)", path.name)
    ]


def sanitize_filename(name):
    """
    Convert directory name into a safe PDF filename.

    Example:
        Maven Notes -> maven_notes.pdf
        Spring Boot Handbook -> spring_boot_handbook.pdf
    """

    name = name.lower().strip()

    name = re.sub(r"[^a-z0-9]+", "_", name)

    return name.strip("_")


def get_image_files(directory):
    """
    Find all supported images in a directory.
    """

    images = [
        file
        for file in directory.iterdir()
        if file.is_file()
        and file.suffix.lower() in IMAGE_EXTENSIONS
    ]

    return sorted(images, key=natural_sort_key)


def delete_files(files):
    """
    Delete image files after successful PDF generation.
    """

    for file in files:
        try:
            file.unlink()
            print(f"  Deleted: {file.name}")

        except OSError as error:
            print(f"  Error deleting {file}: {error}")


# ============================================================
# IMAGE TO PDF CONVERSION
# ============================================================

def convert_images_to_pdf(image_files, output_pdf):
    """
    Convert multiple images into a single PDF.

    Preserves:
        - Original image aspect ratio
        - Page ordering
        - Image resolution

    Returns True only when all pages are added successfully.
    """

    if not image_files:
        return False

    print(f"\nCreating PDF: {output_pdf.name}")
    print(f"Total images: {len(image_files)}")

    temp_pdf = output_pdf.with_name(
        output_pdf.stem + ".tmp.pdf"
    )

    pdf = None
    success = False

    try:
        pdf = canvas.Canvas(str(temp_pdf))

        for index, image_path in enumerate(image_files, start=1):

            with Image.open(image_path) as image:

                image.load()

                width, height = image.size

                # Handle transparency and unsupported modes
                if image.mode not in ("RGB", "L"):
                    image = image.convert("RGB")

                # ----------------------------------------
                # ORIGINAL IMAGE SIZE
                # ----------------------------------------

                if PAGE_SIZE_MODE.lower() == "original":

                    page_width = width
                    page_height = height

                    draw_width = width
                    draw_height = height

                    x = 0
                    y = 0

                # ----------------------------------------
                # A4 PAGE SIZE
                # ----------------------------------------

                elif PAGE_SIZE_MODE.upper() == "A4":

                    from reportlab.lib.pagesizes import A4

                    page_width, page_height = A4

                    scale = min(
                        page_width / width,
                        page_height / height
                    )

                    draw_width = width * scale
                    draw_height = height * scale

                    x = (page_width - draw_width) / 2
                    y = (page_height - draw_height) / 2

                else:
                    raise ValueError(
                        f"Unsupported PAGE_SIZE_MODE: {PAGE_SIZE_MODE}"
                    )

                pdf.setPageSize(
                    (page_width, page_height)
                )

                pdf.drawImage(
                    ImageReader(image),
                    x,
                    y,
                    width=draw_width,
                    height=draw_height
                )

                pdf.showPage()

                print(
                    f"  [{index}/{len(image_files)}] "
                    f"Added: {image_path.name} "
                    f"({width}x{height})"
                )

        pdf.save()
        pdf = None

        # Replace final PDF only after successful creation
        temp_pdf.replace(output_pdf)

        success = True

        print(f"\nPDF created successfully: {output_pdf}")

    except Exception as error:

        print(f"\nERROR creating {output_pdf.name}: {error}")

    finally:

        if pdf is not None:
            try:
                pdf.save()
            except Exception:
                pass

        if not success and temp_pdf.exists():
            temp_pdf.unlink()

    return success


# ============================================================
# RECURSIVE DIRECTORY PROCESSING
# ============================================================

def process_directories(root_dir):
    """
    Recursively find folders containing images.

    Generate one PDF for each directory.
    """

    root_dir = Path(root_dir)

    if not root_dir.exists():
        print(f"Directory not found: {root_dir}")
        return

    total_directories = 0
    successful_pdfs = 0
    failed_pdfs = 0

    directories = sorted(
        [root_dir] +
        [
            path
            for path in root_dir.rglob("*")
            if path.is_dir()
        ]
    )

    for directory in directories:

        image_files = get_image_files(directory)

        # Skip directories without images
        if not image_files:
            continue

        total_directories += 1

        pdf_filename = (
            sanitize_filename(directory.name) + ".pdf"
        )

        output_pdf = directory / pdf_filename

        print("\n" + "=" * 65)
        print(f"Directory: {directory}")
        print(f"Images found: {len(image_files)}")
        print(f"Output PDF: {output_pdf}")
        print("=" * 65)

        success = convert_images_to_pdf(
            image_files,
            output_pdf
        )

        if success:

            successful_pdfs += 1

            if DELETE_IMAGES_AFTER_PDF:
                delete_files(image_files)

        else:
            failed_pdfs += 1

    # --------------------------------------------------------
    # FINAL SUMMARY
    # --------------------------------------------------------

    print("\n" + "=" * 65)
    print("PDF GENERATION SUMMARY")
    print("=" * 65)

    print(f"Directories processed : {total_directories}")
    print(f"PDFs generated        : {successful_pdfs}")
    print(f"Failed conversions    : {failed_pdfs}")

    print("=" * 65)


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":

    process_directories(ROOT_DIR)