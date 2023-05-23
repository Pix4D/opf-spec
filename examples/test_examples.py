from pathlib import Path

import pytest
from pygltflib import GLTF2
from pygltflib.validator import summary as summary_gltf
from pygltflib.validator import validate as validate_gltf

from validator.opf_validator import validate_opf


def examples_dir():
    return Path(__file__).parents[0]


@pytest.mark.parametrize("example_filename", examples_dir().glob("*.json"))
def test_examples(example_filename):
    print(f"Validating {example_filename}...")
    validate_opf(
        example_filename, exact_version=True, no_dangling=True, validate_extensions=True
    )


@pytest.mark.parametrize(
    "example_filename", (examples_dir() / "control_points").glob("*.json")
)
def test_control_point_examples(example_filename):
    print(f"Validating {example_filename}...")
    validate_opf(
        example_filename, exact_version=True, no_dangling=True, validate_extensions=True
    )


@pytest.mark.parametrize(
    "example_filename", (examples_dir() / "point_cloud").glob("*.gltf")
)
@pytest.mark.filterwarnings("ignore::UserWarning")
def test_point_cloud_examples(example_filename):
    print(f"Validating {example_filename}...")
    gltf = GLTF2().load(example_filename)
    validate_gltf(gltf)
    print(f"Successful validation of {example_filename} with summary:")
    summary_gltf(gltf)
