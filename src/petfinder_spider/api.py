from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional
from pathlib import Path

from .utils.seed import set_seed
from .utils.io import save_jsonl, save_json
from .data.loaders import load_dataset
from .pipelines import dual_debias as pl_dual
from .pipelines import baseline as pl_base

@dataclass
class ModelCfg:
    backend: str = "hf"  # "openai" or "hf"
    name: str = "meta-llama/Llama-3.1-8B-Instruct"
    temperature: float = 0.0
    max_new_tokens: int = 256

@dataclass
class ExpCfg:
    name: str = "dual_debias"
    output_dir: str = "outputs/dual_debias"
    seed: int = 42
    save_artifacts: bool = True

@dataclass
class RunResult:
    predictions: List[Dict[str, Any]]
    metrics: Dict[str, Any]
    out_dir: Optional[Path] = None
    extras: Dict[str, Any] = field(default_factory=dict)

def run_dual_debias(
    data_path: str,
    model: ModelCfg = ModelCfg(),
    exp: ExpCfg = ExpCfg(),
    pipeline_params: Dict[str, Any] = field(default_factory=dict)
) -> RunResult:
    set_seed(exp.seed)
    out_dir = Path(exp.output_dir); out_dir.mkdir(parents=True, exist_ok=True)
    rows = load_dataset(data_path)
    preds, metrics, extras = pl_dual.run_pipeline(rows, out_dir, model_cfg=model.__dict__, params=pipeline_params)
    if exp.save_artifacts:
        save_jsonl(out_dir / "predictions.jsonl", preds)
        save_json(out_dir / "metrics.json", metrics)
        for k, v in extras.items():
            save_json(out_dir / f"{k}.json", v)
    return RunResult(predictions=preds, metrics=metrics, out_dir=out_dir, extras=extras)

def run_baseline(
    data_path: str,
    model: ModelCfg = ModelCfg(),
    exp: ExpCfg = ExpCfg(name="baseline", output_dir="outputs/baseline"),
    baseline_params: Dict[str, Any] = field(default_factory=dict)
) -> RunResult:
    set_seed(exp.seed)
    out_dir = Path(exp.output_dir); out_dir.mkdir(parents=True, exist_ok=True)
    rows = load_dataset(data_path)
    preds, metrics = pl_base.run_pipeline(rows, out_dir, model_cfg=model.__dict__, baseline_params=baseline_params)
    if exp.save_artifacts:
        save_jsonl(out_dir / "predictions.jsonl", preds)
        save_json(out_dir / "metrics.json", metrics)
    return RunResult(predictions=preds, metrics=metrics, out_dir=out_dir)
