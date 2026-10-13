import base64
import re
import time
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

URL = "https://amanviews.in/notes"

# NOTES = [
#     "Java Fundamentals",
#     "Java Collections Handbook",
#     "Java Important Interview Programs",
# ]


# NOTES = [
#     "Spring Boot Handbook",
#     "Spring JPA and JWT",
#     "Spring Boot Annotation Notes",
#     "Kafka & RabitMQ Handbook",
#     "Redis Handbook",
#     "MongoDB Handbook",
#     "PostgreSQL Handbook",
#     "JUnit and Mockito Notes",
#     "Django Notes",
#     "Maven Notes",
#     "Top 30 Backend Concepts",
#     "Top 50 Spring boot interview Questions",
#     "Kafka Top 30 interview Questions",
#     "Top 20 git concepts",
#     "Top 30 Spring boot concepts",
#     "NodeJs and ExpressJs",
#     "Kafka Cheat Sheet",
# ]
# NOTES = ["JavaScript interview questions", "Data Structures Notes",
# "Top 70 DSA Coding Problems",] 

# NOTES = [
#     # ============================================================
#     # 1. BACKEND DEVELOPMENT FUNDAMENTALS
#     # ============================================================
#     "Top 30 Backend Concepts",

#     # ============================================================
#     # 2. SPRING BOOT / SPRING FRAMEWORK
#     # ============================================================
#     "Spring Boot Handbook",
#     "Spring Boot Annotation Notes",
#     "Top 30 Spring boot concepts",
#     "Spring JPA and JWT",
#     "Top 50 Spring boot interview Questions",

#     # ============================================================
#     # 3. DATABASES
#     # ============================================================
#     "PostgreSQL Handbook",
#     "MongoDB Handbook",
#     "Redis Handbook",

#     # ============================================================
#     # 4. APACHE KAFKA / MESSAGE BROKERS
#     # ============================================================
#     "Kafka & RabitMQ Handbook",
#     "Kafka Cheat Sheet",
#     "Kafka Top 30 interview Questions",

#     # ============================================================
#     # 5. TESTING FRAMEWORKS
#     # ============================================================
#     "JUnit and Mockito Notes",

#     # ============================================================
#     # 6. BUILD TOOLS
#     # ============================================================
#     "Maven Notes",

#     # ============================================================
#     # 7. NODE.JS / EXPRESS.JS
#     # ============================================================
#     "NodeJs and ExpressJs",

#     # ============================================================
#     # 8. PYTHON BACKEND DEVELOPMENT
#     # ============================================================
#     "Django Notes",

#     # ============================================================
#     # 9. VERSION CONTROL
#     # ============================================================
#     "Top 20 git concepts",
# ]

# NOTES = [
#     # ============================================================
#     # 1. JAVA
#     # ============================================================
#     "Introdution to Java",
#     "Java Fundamentals",
#     "Java Collections Handbook",
#     "Java Collection Shortcuts",
#     "Java Steams and Lambda Expressions",
#     "Java Important Interview Programs",
#     "Java Star Pattern",
#     "Java Top 20 Trick Interview Questions",
#     "Top 50 Java interview Questions",
#     "Java Cheat Sheet complete",

#     # ============================================================
#     # 2. PYTHON
#     # ============================================================
#     "Python Quick Handbook",
#     "Python OOPs & Collections Notes",
#     "Pandas with Python",
#     "Python Start Patterns",
#     "Top 30 Python Coding Questions",
#     "Top 30 Python interview questions",
#     "Top 50 Python Interview Questions",
#     "Python Cheat Sheet",
#     "Python Cheat Sheet Notes",
#     "Python Revision Sheet",

#     # ============================================================
#     # 3. C / C++
#     # ============================================================
#     "C Programming",
#     "C++ Handbook",
#     "OOPS Concept in C++",

#     # ============================================================
#     # 4. OBJECT-ORIENTED PROGRAMMING
#     # ============================================================
#     "OOPS Concepts",
#     "Top 50 OOPS interview questions",

#     # ============================================================
#     # 5. JAVASCRIPT / TYPESCRIPT
#     # ============================================================
#     "JavaScript Handwritten Notes",
#     "Java Script Full Handbook",
#     "Top 50 JavaScript interview questions",
#     "TypeScript Notes",

#     # ============================================================
#     # 6. WEB DEVELOPMENT / FRONTEND
#     # ============================================================
#     "Web Development Notes",
#     "React Js",
#     "Top 30 ReactJs interview Questions",
#     "Tailwind CSS Notes",

#     # ============================================================
#     # 7. NODE.JS
#     # ============================================================
#     "Node Js",

#     # ============================================================
#     # 8. GO LANGUAGE
#     # ============================================================
#     "Go language notes",

#     # ============================================================
#     # 9. CODING / PLACEMENT PREPARATION
#     # ============================================================
#     "Top 40 TCS NQT problems",

#     # ============================================================
#     # 10. MATHEMATICS / ENGINEERING
#     # ============================================================
#     "Trigonometry",
#     "Engineering Physics 1 (part 1)",
#     "Electronic Devices and Circuits Part 2",
# ]

# NOTES = [
#     # ============================================================
#     # 1. FUNDAMENTALS & COMPLEXITY ANALYSIS
#     # ============================================================
#     "Data Structures Notes",
#     "Time Complexity",

#     # ============================================================
#     # 2. SORTING & SEARCHING ALGORITHMS
#     # ============================================================
#     "Sorting & Searching Notes",

#     # ============================================================
#     # 3. DSA CODING PATTERNS
#     # ============================================================
#     "DSA Coding Patterns",

#     # ============================================================
#     # 4. ARRAYS & STRINGS
#     # ============================================================
#     "Top 30 Array and String Interview Coding Problems",

#     # ============================================================
#     # 5. STACKS & QUEUES
#     # ============================================================
#     "Top 30 Stack and Queue Problems",

#     # ============================================================
#     # 6. TREES & GRAPHS
#     # ============================================================
#     "Tree & Graph Handbook",
#     "Top 30 Tree and Graph Problems",

#     # ============================================================
#     # 7. INTERVIEW CODING PRACTICE
#     # ============================================================
#     "Top 70 DSA Coding Problems",

#     # ============================================================
#     # 8. REVISION & QUICK REFERENCE
#     # ============================================================
#     "DSA Revision Sheet",
# ]

# NOTES = [
#     # ============================================================
#     # 1. SYSTEM DESIGN FUNDAMENTALS
#     # ============================================================
#     "System Design Handbook",
#     "Top 20 system design concepts",

#     # ============================================================
#     # 2. OBJECT-ORIENTED DESIGN PRINCIPLES
#     # ============================================================
#     "SOLID Principle Handbook",

#     # ============================================================
#     # 3. LOW-LEVEL DESIGN (LLD)
#     # ============================================================
#     "Low-Level Design (LLD)",

#     # ============================================================
#     # 4. PRACTICAL LLD CASE STUDIES
#     # ============================================================
#     "Splitwise LLD",

#     # ============================================================
#     # 5. SYSTEM DESIGN INTERVIEW PREPARATION
#     # ============================================================
#     "Top 50 System Design Questions",
# ]

# NOTES = [
#     # ============================================================
#     # 1. SOFTWARE TESTING FUNDAMENTALS
#     # ============================================================
#     # "Complete Manual Testing Notes",

#     # # ============================================================
#     # # 2. SELENIUM AUTOMATION
#     # # ============================================================
#     # "Selenium Notes",
#     # "Testng Notes",
#     # "Top 165 real Selenium Interview Questions",

#     # # ============================================================
#     # # 3. PLAYWRIGHT AUTOMATION
#     # # ============================================================
#     # "Playwright Handbook",
#     # "Playwright Framework",
#     # "Playwright Cheat Sheet",
#     # "Playwright Top 35 Questions",

#     # ============================================================
#     # 4. API TESTING & AUTOMATION
#     # ============================================================
#     "Postman Notes",
#     "REST Assured Notes",
#     "Karate Automation",

#     # ============================================================
#     # 5. UNIT TESTING & MOCKING
#     # ============================================================
#     "JUnit and Mockito Notes",
#     "Api Mocking Using Mockito",

#     # ============================================================
#     # 6. PERFORMANCE & LOAD TESTING
#     # ============================================================
#     "Performance Testing & Load Runner",

#     # ============================================================
#     # 7. MOBILE TEST AUTOMATION
#     # ============================================================
#     "Appium notes",

#     # ============================================================
#     # 8. AI-POWERED TESTING
#     # ============================================================
#     "Introduction to AI for QA",
#     "Playwright MCP Notes",
# ]

# NOTES = [
#     # ============================================================
#     # 1. AI FUNDAMENTALS
#     # ============================================================
#     "AI for Developers Notes",
#     "Top 20 AI Engineering Concepts",

#     # ============================================================
#     # 2. MACHINE LEARNING
#     # ============================================================
#     "Machine Learning for Developer Notes",

#     # ============================================================
#     # 3. GENERATIVE AI & LLM INTEGRATION
#     # ============================================================
#     "Gen AI Api for Developers",

#     # ============================================================
#     # 4. RETRIEVAL-AUGMENTED GENERATION (RAG)
#     # ============================================================
#     "RAG for Developers",
#     "RAG MAG CAG",

#     # ============================================================
#     # 5. MODEL CONTEXT PROTOCOL (MCP)
#     # ============================================================
#     "MCP for Developers",

#     # ============================================================
#     # 6. AI AGENTS & AGENTIC AI
#     # ============================================================
#     "AI Agent For Developers",

#     # ============================================================
#     # 7. ADDITIONAL AI MODEL CONCEPTS
#     # ============================================================
#     "JEV Model",
# ]

NOTES = [
    "Java Cheat Sheet complete",
    #"JavaScript interview questions",
    "Top 50 JavaScript interview questions",
]

OUTPUT_DIR = Path("downloaded_notes")
OUTPUT_DIR.mkdir(exist_ok=True)

WAIT_SECONDS = 30


def create_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(60)

    return driver


def safe_filename(name):
    return re.sub(r'[\\/:*?"<>|]', "_", name).strip()


def get_page_info(driver):
    """
    Waits until the preview navigation contains
    a valid page count.

    Examples:
        1 / ...
        1 / 58
        2 / 58

    Returns:
        (current_page, total_pages)
    """

    def wait_for_page_count(driver):

        navigation = driver.find_element(
            By.CSS_SELECTOR,
            ".note-preview-navigation span"
        )

        text = navigation.get_attribute("textContent").strip()

        # Match only complete page counts
        match = re.fullmatch(
            r"(\d+)\s*/\s*(\d+)",
            text
        )

        if match:
            current_page = int(match.group(1))
            total_pages = int(match.group(2))

            if 1 <= current_page <= total_pages:
                return current_page, total_pages

        # Selenium will retry until the condition succeeds
        return False

    return WebDriverWait(
        driver,
        60,
        poll_frequency=0.5
    ).until(wait_for_page_count)


def wait_for_page_image(driver, note_name, page_number, timeout=8):
    """
    Waits for the image corresponding to the current page.

    Returns:
        WebElement if image is available.
        None if no image is found.

    Handles promotional pages such as:
        "Get All Notes"
    """

    expected_alt = f"{note_name} - Page {page_number}"

    def image_ready(driver):

        images = driver.find_elements(
            By.CSS_SELECTOR,
            'img[src^="blob:"]'
        )

        for image in images:

            if image.get_attribute("alt") != expected_alt:
                continue

            ready = driver.execute_script(
                """
                const img = arguments[0];

                return img.complete &&
                       img.naturalWidth > 0 &&
                       img.naturalHeight > 0;
                """,
                image
            )

            if ready:
                return image

        return False

    try:
        return WebDriverWait(
            driver,
            timeout,
            poll_frequency=0.3
        ).until(image_ready)

    except TimeoutException:
        return None
def get_preview_image(driver):
    """
    Finds the currently displayed preview image.
    """

    return WebDriverWait(driver, WAIT_SECONDS).until(
        lambda d: next(
            (
                img
                for img in d.find_elements(
                    By.CSS_SELECTOR,
                    'img[src^="blob:"]'
                )
                if img.is_displayed()
                and d.execute_script(
                    "return arguments[0].complete "
                    "&& arguments[0].naturalWidth > 0;",
                    img
                )
            ),
            None
        )
    )


def download_blob_image(driver, image_element, output_file):
    """
    Retrieves the original image bytes from the browser.

    No screenshot is taken.
    No resizing or recompression is performed.
    """

    image_data = driver.execute_async_script(
        """
        const image = arguments[0];
        const callback = arguments[arguments.length - 1];

        async function download() {
            try {
                const response = await fetch(image.src);

                if (!response.ok) {
                    throw new Error(
                        "HTTP error: " + response.status
                    );
                }

                const blob = await response.blob();

                const reader = new FileReader();

                reader.onloadend = function() {
                    callback({
                        success: true,
                        data: reader.result,
                        type: blob.type,
                        width: image.naturalWidth,
                        height: image.naturalHeight
                    });
                };

                reader.onerror = function() {
                    callback({
                        success: false,
                        error: "FileReader failed"
                    });
                };

                reader.readAsDataURL(blob);

            } catch (error) {
                callback({
                    success: false,
                    error: error.toString()
                });
            }
        }

        download();
        """,
        image_element
    )

    if not image_data["success"]:
        raise RuntimeError(image_data["error"])

    encoded = image_data["data"].split(",", 1)[1]

    binary_data = base64.b64decode(encoded)

    output_file.write_bytes(binary_data)

    return {
        "size": len(binary_data),
        "width": image_data["width"],
        "height": image_data["height"],
        "type": image_data["type"]
    }


def click_next(driver, previous_page):

    next_button = WebDriverWait(
        driver,
        WAIT_SECONDS
    ).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                '//div[contains(@class, "note-preview-navigation")]'
                '//button[contains(normalize-space(.), "Next")]'
            )
        )
    )

    if not next_button.is_enabled():
        return False

    driver.execute_script(
        "arguments[0].click();",
        next_button
    )

    def page_changed(driver):

        elements = driver.find_elements(
            By.CSS_SELECTOR,
            ".note-preview-navigation span"
        )

        if not elements:
            return False

        text = elements[0].get_attribute(
            "textContent"
        ).strip()

        match = re.fullmatch(
            r"(\d+)\s*/\s*(\d+)",
            text
        )

        if not match:
            return False

        current_page = int(match.group(1))

        return current_page > previous_page

    WebDriverWait(
        driver,
        30,
        poll_frequency=0.3
    ).until(page_changed)

    return True

def close_preview(driver):
    """
    Attempts to close the preview dialog.
    """

    selectors = [
        'button[aria-label="Close"]',
        'button[aria-label="Close preview"]',
        '.note-preview-close',
    ]

    for selector in selectors:
        buttons = driver.find_elements(
            By.CSS_SELECTOR,
            selector
        )

        for button in buttons:
            if button.is_displayed():
                button.click()
                return

    # Fallback: Escape
    from selenium.webdriver.common.keys import Keys

    webdriver.ActionChains(driver).send_keys(
        Keys.ESCAPE
    ).perform()


def download_note(driver, note_name):

    print(f"\n{'=' * 60}")
    print(f"Processing: {note_name}")
    print(f"{'=' * 60}")

    folder = OUTPUT_DIR / safe_filename(note_name)
    folder.mkdir(parents=True, exist_ok=True)

    # Open preview
    preview_button = WebDriverWait(
        driver,
        WAIT_SECONDS
    ).until(
        EC.element_to_be_clickable(
            (
                By.CSS_SELECTOR,
                f'button.note-preview-button'
                f'[aria-label="Preview {note_name}"]'
            )
        )
    )

    driver.execute_script(
        "arguments[0].click();",
        preview_button
    )

    current_page, total_pages = get_page_info(driver)

    print(f"Total pages: {total_pages}")

    downloaded = 0
    skipped = 0

    while current_page <= total_pages:

        print(
            f"\nProcessing page "
            f"{current_page}/{total_pages}"
        )

        # Wait for image
        image = wait_for_page_image(
            driver,
            note_name,
            current_page,
            timeout=8
        )

        # Handle promotional or missing-image pages
        if image is None:

            print(
                f"  ⚠ No image available on page "
                f"{current_page}. Skipping."
            )

            skipped += 1

        else:

            output_file = folder / (
                f"page_{current_page:03d}.png"
            )

            if (
                output_file.exists()
                and output_file.stat().st_size > 0
            ):

                print(
                    f"  Already exists: "
                    f"{output_file.name}"
                )

            else:

                try:

                    result = download_blob_image(
                        driver,
                        image,
                        output_file
                    )

                    downloaded += 1

                    print(
                        f"  Saved: {output_file.name} | "
                        f"{result['width']}x"
                        f"{result['height']} | "
                        f"{result['size'] / 1024:.2f} KB"
                    )

                except Exception as error:

                    print(
                        f"  ⚠ Download failed for "
                        f"page {current_page}: {error}"
                    )

                    skipped += 1

        # Stop after final page
        if current_page >= total_pages:
            break

        previous_page = current_page

        try:

            moved = click_next(
                driver,
                previous_page
            )

            if not moved:
                print(
                    "  Next button disabled. "
                    "Stopping preview."
                )
                break

            current_page, total_pages = get_page_info(
                driver
            )

        except TimeoutException:

            print(
                "  ⚠ Navigation timeout. "
                "Stopping current note."
            )
            break

    print(f"\n{'=' * 60}")
    print(f"Completed: {note_name}")
    print(f"Downloaded: {downloaded}")
    print(f"Skipped: {skipped}")
    print(f"{'=' * 60}")

    close_preview(driver)

    time.sleep(1)

def main():
    driver = create_driver()

    try:
        driver.get(URL)

        for note in NOTES:
            try:
                download_note(driver, note)

            except Exception as error:
                print(
                    f"ERROR downloading {note}: {error}"
                )

                # Return to a clean state.
                driver.get(URL)

        print("\nAll processing completed.")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()