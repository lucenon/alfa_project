from joblib import load
from app.utils import preprocess, is_meaningful
from app.config import PIPELINE_PATH
from app.logger import logger

pipeline = None
label_dict = {0: "neutral", 1: "positive", 2: "negative"}


def load_artifacts() -> None:
    global pipeline

    if pipeline is None:
        try:
            pipeline = load(PIPELINE_PATH)
        except FileNotFoundError:
            logger.error(f"Pipeline file not found at {PIPELINE_PATH}")
            raise RuntimeError(f"Pipeline file not found at {PIPELINE_PATH}")
        except Exception as e:
            logger.error(f"Failed to deserialize pipeline: {e}")
            raise RuntimeError("Failed to deserialize pipeline") from e


def predict(input_data: str) -> dict:
    global pipeline

    if not pipeline:
        logger.error(f"Artifacts not loaded")
        raise RuntimeError("Artifacts not loaded: pipeline is empty or invalid")

    if not is_meaningful(input_data):
        return {
            "class_": "neutral",
            "label": 0,
            "model_bypassed": True
        }
    else:
        data = preprocess(input_data)
        predict_label = pipeline.predict([data])[0]
        predict_class = label_dict[predict_label]

        return {
            "class_": predict_class,
            "label": predict_label,
            "model_bypassed": False
        }
