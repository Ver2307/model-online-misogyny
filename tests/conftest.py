import pandas as pd
import pytest

from src.text.utils import contractions
from tests.domain_objects_for_testing import create_dataframe_of_labeled_tweets


@pytest.fixture
def contractions_mapping() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "contraction": list(contractions().keys()),
            "unpacked": list(contractions().values()),
        }
    )


@pytest.fixture
def labeled_tweets() -> pd.DataFrame:
    return create_dataframe_of_labeled_tweets()
