#!/bin/bash
python run_feature_extraction.py --meta_root meta-data --cache_root debug/tmp --topic_label_root cache_data --voice_root voice_data \
  --topic_tree iptc --languages zh-CN,zh-HK,zh-TW --num_sentence 10 \
  --features mfcc,spectral,rms,f0 \
  --out_dir debug/feature_data