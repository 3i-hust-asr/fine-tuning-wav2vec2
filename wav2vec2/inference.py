import argparse
import torch
import soundfile as sf

from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor


def inference(path_audio: str) -> str:
    """
    :param path_audio:
    :return:
    """
    speech, _ = sf.read(path_audio)
    input_values = processor(speech, sampling_rate=16_000, return_tensors="pt").input_values.to('cuda')
    logits = model(input_values).logits
    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = processor.decode(predicted_ids[0])
    return transcription


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='train model wav2vec2.')
    parser.add_argument('--path_model',
                        type=str,
                        default='my_model',
                        required=False,
                        help="str - path model output")

    parser.add_argument('--path_audio_test',
                        type=str,
                        required=True,
                        help="str - path audio test")

    args = parser.parse_args()
    print('load model ....')
    processor = Wav2Vec2Processor.from_pretrained(args.path_model)
    model = Wav2Vec2ForCTC.from_pretrained(args.path_model)
    model.to("cuda")
    print(inference(args.path_audio_test))
