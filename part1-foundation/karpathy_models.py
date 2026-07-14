"""Load local Karpathy GPT implementations for the teaching notebooks."""

from pathlib import Path
import importlib.util


def _repo_root():
    start = Path(__file__).resolve()
    for candidate in [start.parent, *start.parents]:
        marker = candidate / "external" / "karpathy" / "nanoGPT" / "model.py"
        if marker.exists():
            return candidate
    raise FileNotFoundError("Run: git submodule update --init --recursive")


ROOT = _repo_root()
NANOGPT_MODEL = ROOT / "external" / "karpathy" / "nanoGPT" / "model.py"
_spec = importlib.util.spec_from_file_location("karpathy_nanogpt_model", NANOGPT_MODEL)
_nanogpt = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_nanogpt)

NanoGPT = _nanogpt.GPT
NanoGPTConfig = _nanogpt.GPTConfig
