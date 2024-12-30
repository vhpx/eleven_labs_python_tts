import os
import uuid
from dotenv import load_dotenv
from text_to_speech_stream import text_to_speech_stream

load_dotenv()

# Create output directory if it doesn't exist
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def main(text: str):
    audio_stream = text_to_speech_stream(text)

    # Generate unique filename
    filename = f"{uuid.uuid4()}.mp3"
    filepath = os.path.join(OUTPUT_DIR, filename)

    # Save stream to file
    with open(filepath, "wb") as f:
        f.write(audio_stream.read())

    print(f"Audio saved to: {filepath}")

    # Play audio on arduino


if __name__ == "__main__":
    main("Hello world!")
