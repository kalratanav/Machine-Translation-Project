import os

save_data: data/wmt/run/example
## Where the vocab(s) will be written
src_vocab: data/wmt/run/example.vocab.src
tgt_vocab: data/wmt/run/example.vocab.tgt

# Corpus opts:
data:
    commoncrawl:
        path_src: os.path.abspath('C:\Users\k0912315\github-classroom\SLHSCS\fall-semester-project-2021-kalratanav\src.training.txt')
        path_tgt: os.path.abspath('C:\Users\k0912315\github-classroom\SLHSCS\fall-semester-project-2021-kalratanav\tgt.training.txt')
        transforms: [sentencepiece, filtertoolong]
        weight: 23
    """"europarl:
        path_src: data/wmt/europarl-v7.de-en.en
        path_tgt: data/wmt/europarl-v7.de-en.de
        transforms: [sentencepiece, filtertoolong]
        weight: 19
    news_commentary:
        path_src: data/wmt/news-commentary-v11.de-en.en
        path_tgt: data/wmt/news-commentary-v11.de-en.de
        transforms: [sentencepiece, filtertoolong]
        weight: 3
    valid:
        path_src: data/wmt/valid.en
        path_tgt: data/wmt/valid.de
        transforms: [sentencepiece]""""


src_subword_model: data/wmt/wmtende.model
tgt_subword_model: data/wmt/wmtende.model
src_subword_nbest: 1
src_subword_alpha: 0.0
tgt_subword_nbest: 1
tgt_subword_alpha: 0.0

src_seq_length: 150
tgt_seq_length: 150

skip_empty_level: silent