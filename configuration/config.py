
import logging
import os
from pathlib import Path
import json
import numpy as np
import pandas as pd

ROOT_PATH = os.path.normpath(os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."))

# data
data_dir = Path(ROOT_PATH)/ "data"
model_dir = Path(ROOT_PATH) / "model"

bert_data_path = Path.home() / 'db__pytorch_pretrained_bert'
bert_vocab_path = bert_data_path / 'bert-base-chinese' / 'bert-base-chinese-vocab.txt'
bert_model_path = bert_data_path / 'bert-base-chinese'

tencent_w2v_path = Path.home() / 'db__word2vec'

roberta_model_path = bert_data_path / 'chinese_Roberta_bert_wwm_large_ext_pytorch'

bert_insurance_path = bert_data_path / 'bert_insurance'

common_data_path = Path.home() / 'db__common_dataset'
intent_data_path = Path(common_data_path) / 'intent_data'


###############################################
# log
###############################################

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(name)s -   %(message)s',
                    datefmt='%m/%d/%y %H:%M:%S',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info(f'begin progress ...')