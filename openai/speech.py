from pathlib import Path
import openai

speech_file_path = Path(__file__).parent / "speech.mp3"
with openai.audio.speech.with_streaming_response.create(
        model="tts-1",
        voice="alloy",
        input="Welcome to Generative AI World!, Seshagiri",
   ) as response:
        response.stream_to_file(speech_file_path)
