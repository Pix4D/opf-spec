import argparse
import json
import sys
from pathlib import Path


def patch_gltf(gltf_path):
    extension_to_patch = "OPF_mesh_primitive_partitioning"
    bad_key = "nodeCoordinates"
    good_key = "nodeIndices"
    gltf_obj = json.load(open(gltf_path, "r"))

    for mesh in gltf_obj.get("meshes", []):
        for primitive in mesh.get("primitives", []):
            ext_obj = primitive.get("extensions", {}).get(extension_to_patch)
            if ext_obj is None:
                continue
            if bad_key in ext_obj:
                ext_obj[good_key] = ext_obj.get(bad_key)
                del ext_obj[bad_key]

    return gltf_obj


def gltf_point_cloud_uris(opf_obj):
    for item in opf_obj.get("items", []):
        if item["type"] in ["calibration", "point_cloud"]:
            for resource in item.get("resources", []):
                if resource["format"] != "model/gltf+json":
                    continue
                yield resource["uri"]


parser = argparse.ArgumentParser(
    description="Patch OPF project with invalid OPF_mesh_primitive_partitioning extension"
)
parser.add_argument("opf_path", type=str, help="path to the opf project to patch")
args = parser.parse_args()

opf_obj = json.load(open(args.opf_path, "r"))
for gltf_uri in gltf_point_cloud_uris(opf_obj):
    gltf_path = Path(args.opf_path).parent / gltf_uri
    gltf_obj = patch_gltf(gltf_path)
    json.dump(gltf_obj, open(gltf_path, "w"), indent=2)
