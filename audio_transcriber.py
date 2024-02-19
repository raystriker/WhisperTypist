import torch
from transformers import pipeline
from transformers.utils import is_flash_attn_2_available


def transcribe(wav_file):
    """
    A function that transcribes the speech from a given WAV file using the OpenAI whisper-medium model.

    Parameters:
    wav_file (str): The path to the WAV file to be transcribed.

    Returns:
    str: The transcribed text from the speech in the WAV file.
    """
    pipe = pipeline(
        "automatic-speech-recognition",
        model="openai/whisper-medium",
        torch_dtype=torch.float16,
        device="cuda",  # or mps for Mac devices
        model_kwargs={
            "attn_implementation": "flash_attention_2"
        } if is_flash_attn_2_available() else {
            "attn_implementation": "sdpa"
        },
    )

    outputs = pipe(wav_file,
                   chunk_length_s=30,
                   batch_size=24,
                   return_timestamps=False)

    print(outputs['text'])
    return outputs['text']
