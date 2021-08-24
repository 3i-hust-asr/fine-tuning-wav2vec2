
1. create tokenizer:
    
    `python3 core/create_tokenizer.py --data_csv data/train.csv --path_json_output vocab.json`

2. train model:

   `python3 wav2vec2/train_model.py --path_csv_train data/train.csv --path_csv_test data/test.csv --path_vocab vocab.json --batch_size 4 --model_output my_model --num_epochs 5`

3. inference:

   `python3 wav2vec2/inference.py --path_model my_model --path_audio_test data/test.wav`
