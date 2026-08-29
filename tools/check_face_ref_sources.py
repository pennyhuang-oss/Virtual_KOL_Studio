#!/usr/bin/env python3
"""Validate the provenance, files, hashes and readouts for new face references."""

import hashlib
import json
import struct
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "review/batch3_face_refs/SOURCES.json"
READOUT = ROOT / "pilot/face_refs_readout.json"
PLAN = ROOT / "pilot/batch3_faces_v2.json"
EXPECTED = {f"ref_{n:02d}" for n in range(16, 24)}
EXPECTED_ASSIGNMENTS = {
    "emma-kao": "ref_16",
    "somi-oh": "ref_18",
    "peggy-lee": "ref_19",
    "miu-shiraishi": "ref_20",
    "sydney-leong": "ref_21",
    "nanami-fujiwara": "ref_22",
    "kanon-komori": "ref_23",
}


def image_dimensions(path: Path) -> tuple[int, int]:
    with path.open("rb") as fh:
        header = fh.read(24)
        if header[:8] == b"\x89PNG\r\n\x1a\n" and header[12:16] == b"IHDR":
            return struct.unpack(">II", header[16:24])
        if header[:2] != b"\xff\xd8":
            raise ValueError("unsupported image header")
        fh.seek(2)
        while True:
            byte = fh.read(1)
            if not byte:
                break
            if byte != b"\xff":
                continue
            marker = fh.read(1)
            while marker == b"\xff":
                marker = fh.read(1)
            if marker in {b"\xd8", b"\xd9"}:
                continue
            length_bytes = fh.read(2)
            if len(length_bytes) != 2:
                break
            length = struct.unpack(">H", length_bytes)[0]
            if marker in {bytes([code]) for code in range(0xC0, 0xC4)} | {
                bytes([code]) for code in range(0xC5, 0xC8)
            } | {bytes([code]) for code in range(0xC9, 0xCC)} | {
                bytes([code]) for code in range(0xCD, 0xD0)
            }:
                data = fh.read(5)
                if len(data) != 5:
                    break
                height, width = struct.unpack(">HH", data[1:5])
                return width, height
            fh.seek(length - 2, 1)
    raise ValueError("JPEG dimensions not found")


def main() -> int:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    readout = json.loads(READOUT.read_text(encoding="utf-8"))["refs"]
    plan = json.loads(PLAN.read_text(encoding="utf-8"))
    personas = plan["personas"]
    refs = manifest["references"]
    errors = []

    if set(refs) != EXPECTED:
        errors.append(f"manifest IDs differ: expected={sorted(EXPECTED)} got={sorted(refs)}")
    if manifest["provenance_policy"].get("input_images") != []:
        errors.append("new synthetic references must declare an empty input_images list")
    if manifest["provenance_policy"].get("real_person_or_public_figure_reference") is not False:
        errors.append("real-person/public-figure reference flag must be false")

    seen_hashes = set()
    for ref_id, item in sorted(refs.items()):
        path = ROOT / item["file"]
        if not path.is_file():
            errors.append(f"{ref_id}: missing file {item['file']}")
            continue
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if digest != item["sha256"]:
            errors.append(f"{ref_id}: sha256 mismatch")
        if digest in seen_hashes:
            errors.append(f"{ref_id}: duplicate image hash")
        seen_hashes.add(digest)
        try:
            dims = list(image_dimensions(path))
        except ValueError as exc:
            errors.append(f"{ref_id}: {exc}")
        else:
            if dims != item["dimensions_px"]:
                errors.append(f"{ref_id}: dimensions {dims} != {item['dimensions_px']}")
            if min(dims) < 1000:
                errors.append(f"{ref_id}: short edge below 1000 px")
        if item.get("usability") != "high":
            errors.append(f"{ref_id}: manifest usability is not high")
        if readout.get(ref_id, {}).get("usability") != "high":
            errors.append(f"{ref_id}: missing matching high-usability readout")

    for persona, expected_ref in EXPECTED_ASSIGNMENTS.items():
        assigned = personas[persona]["refs_v2"]["FACE_SHAPE_AND_JAW"]
        if assigned != expected_ref:
            errors.append(f"{persona}: expected {expected_ref}, got {assigned}")
    if personas["wendy-yeo"]["refs_v2"]["FACE_SHAPE_AND_JAW"] != "ref_11":
        errors.append("wendy-yeo must retain ref_11 per H-02")
    excluded = {
        ref_id
        for ref_id, note in plan.get("ref_notes", {}).items()
        if note.get("excluded_from_FACE_SHAPE_AND_JAW")
    }
    for persona, data in personas.items():
        assigned = (data.get("refs_v2") or data["refs"])["FACE_SHAPE_AND_JAW"]
        if assigned in excluded:
            errors.append(f"{persona}: excluded face-shape source {assigned} is assigned")

    if errors:
        for error in errors:
            print("✗", error)
        print(f"HARD FAIL: {len(errors)} reference-source error(s)")
        return 1
    print("✓ 8/8 new references: files, hashes, dimensions, provenance and readouts pass")
    return 0


if __name__ == "__main__":
    sys.exit(main())
