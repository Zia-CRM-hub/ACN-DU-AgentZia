#!/usr/bin/env python3
"""Build dist/AgentZ-Teams.zip (manifest + 2 generated PNG icons). Stdlib only."""
import struct, zlib, zipfile, json
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent

def png(size, fg, bg, transparent_bg=False):
    rows = []
    c, r = size / 2, size * 0.38
    for y in range(size):
        row = bytearray([0])
        for x in range(size):
            inside = (x - c) ** 2 + (y - c) ** 2 <= r * r
            bar = abs(x - c) < size * 0.07 or abs(y - c) < size * 0.07
            if inside and not bar:
                px = fg + (255,)
            else:
                px = (bg + (0,)) if transparent_bg else (bg + (255,))
            row += bytes(px)
        rows.append(bytes(row))
    def chunk(t, d):
        return struct.pack(">I", len(d)) + t + d + struct.pack(">I", zlib.crc32(t + d) & 0xFFFFFFFF)
    return (b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", size, size, 8, 6, 0, 0, 0))
            + chunk(b"IDAT", zlib.compress(b"".join(rows))) + chunk(b"IEND", b""))

(ROOT / "teams" / "color.png").write_bytes(png(192, (255, 255, 255), (31, 78, 121)))
(ROOT / "teams" / "outline.png").write_bytes(png(32, (255, 255, 255), (255, 255, 255), True))
m = json.loads((ROOT / "teams" / "manifest.json").read_text(encoding="utf-8"))
out = ROOT / "dist" / "AgentZ-Teams.zip"
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    for n in ("manifest.json", "color.png", "outline.png"):
        z.write(ROOT / "teams" / n, n)
print(f"Built {out} (app version {m['version']})")
