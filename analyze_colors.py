#!/usr/bin/env python3
"""Analyze nail art photos to extract dominant colors, brightness, contrast, and texture info."""

import os
import json
from pathlib import Path
from collections import Counter

try:
    from PIL import Image
    import numpy as np
    HAS_PIL = True
except ImportError:
    HAS_PIL = False

PHOTO_DIR = Path(r"/mnt/c/Users/Home/vault/projects/missoula-nail-art/Pictures/Sage's artwork for the website and Nail's nail art")

def rgb_to_hex(r, g, b):
    return f"#{r:02x}{g:02x}{b:02x}"

def quantize_color(r, g, b, step=32):
    """Quantize color to reduce palette size."""
    return (r // step * step, g // step * step, b // step * step)

def color_category(r, g, b):
    """Categorize a color."""
    h, s, v = rgb_to_hsv(r, g, b)
    if v < 30:
        return "black"
    if s < 25 and v > 200:
        return "white"
    if s < 25:
        return "gray"
    if h < 15 or h >= 345:
        return "red/pink"
    if h < 45:
        return "orange/gold"
    if h < 70:
        return "yellow"
    if h < 160:
        return "green"
    if h < 260:
        return "blue/teal"
    if h < 345:
        return "purple/violet"
    return "red/pink"

def rgb_to_hsv(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    v = mx * 100
    diff = mx - mn
    if mx == 0:
        s = 0
    else:
        s = (diff / mx) * 100
    if mx == mn:
        h = 0
    elif mx == r:
        h = 60 * ((g - b) / diff) % 360
    elif mx == g:
        h = 60 * ((b - r) / diff + 2)
    else:
        h = 60 * ((r - g) / diff + 4)
    if h < 0:
        h += 360
    return h, s, v

def analyze_image(filepath):
    """Analyze a single image for color palette, brightness, saturation."""
    img = Image.open(filepath).convert("RGB")
    
    # Resize for speed
    img_small = img.resize((150, 150), Image.LANCZOS)
    pixels = np.array(img_small)
    
    # Flatten
    h, w, _ = pixels.shape
    flat = pixels.reshape(-1, 3)
    
    # Quantize and count
    quantized = [quantize_color(r, g, b, step=24) for r, g, b in flat]
    color_counts = Counter(quantized)
    
    # Top 10 colors
    top_colors = color_counts.most_common(10)
    top_hex = [(rgb_to_hex(r, g, b), count, color_category(r, g, b)) 
               for (r, g, b), count in top_colors]
    
    # Color category distribution
    cat_counts = Counter()
    for r, g, b in flat[::4]:  # sample every 4th pixel
        cat_counts[color_category(r, g, b)] += 1
    
    # Average brightness and saturation
    total = len(flat)
    avg_brightness = np.mean(flat) / 255 * 100
    saturations = []
    hues = []
    for r, g, b in flat[::4]:
        h, s, v = rgb_to_hsv(r, g, b)
        saturations.append(s)
        if s > 15:  # only count saturated colors
            hues.append(h)
    
    avg_saturation = sum(saturations) / len(saturations) if saturations else 0
    
    # Detect if image has metallic/chrome (high brightness variance in small areas)
    # Detect sparkle/glitter (high frequency brightness changes)
    
    # Detect dark vs light overall
    dark_pct = sum(1 for r, g, b in flat if (r + g + b) / 3 < 60) / total * 100
    bright_pct = sum(1 for r, g, b in flat if (r + g + b) / 3 > 200) / total * 100
    
    # Detect highly saturated areas
    high_sat_pct = sum(1 for r, g, b in flat[::4] if rgb_to_hsv(r, g, b)[1] > 60) / len(flat[::4]) * 100
    
    return {
        "filename": os.path.basename(filepath),
        "top_colors": top_hex,
        "color_categories": dict(cat_counts.most_common()),
        "avg_brightness": round(avg_brightness, 1),
        "avg_saturation": round(avg_saturation, 1),
        "dark_pct": round(dark_pct, 1),
        "bright_pct": round(bright_pct, 1),
        "high_sat_pct": round(high_sat_pct, 1),
        "dominant_hue_range": f"{min(hues):.0f}-{max(hues):.0f}" if hues else "none",
    }

if HAS_PIL:
    results = []
    jpg_files = sorted(PHOTO_DIR.glob("*.jpg"))
    print(f"Found {len(jpg_files)} images\n")
    
    all_categories = Counter()
    all_top_hex = Counter()
    brightnesses = []
    saturations = []
    high_sat_pcts = []
    dark_pcts = []
    bright_pcts = []
    
    for f in jpg_files:
        try:
            r = analyze_image(f)
            results.append(r)
            print(f"--- {r['filename']} ---")
            print(f"  Top colors: {r['top_colors'][:5]}")
            print(f"  Categories: {r['color_categories']}")
            print(f"  Brightness: {r['avg_brightness']}% | Saturation: {r['avg_saturation']}%")
            print(f"  Dark: {r['dark_pct']}% | Bright: {r['bright_pct']}% | High Sat: {r['high_sat_pct']}%")
            print()
            
            for cat, cnt in r['color_categories'].items():
                all_categories[cat] += cnt
            for hex_c, cnt, cat in r['top_colors'][:3]:
                all_top_hex[hex_c] += cnt
            brightnesses.append(r['avg_brightness'])
            saturations.append(r['avg_saturation'])
            high_sat_pcts.append(r['high_sat_pct'])
            dark_pcts.append(r['dark_pct'])
            bright_pcts.append(r['bright_pct'])
        except Exception as e:
            print(f"Error with {f}: {e}")
    
    print("\n" + "="*60)
    print("AGGREGATE ANALYSIS")
    print("="*60)
    print(f"\nOverall Color Category Distribution:")
    for cat, cnt in all_categories.most_common():
        pct = cnt / sum(all_categories.values()) * 100
        print(f"  {cat}: {pct:.1f}%")
    
    print(f"\nTop Aggregated Hex Colors (across all images):")
    for hex_c, cnt in all_top_hex.most_common(15):
        print(f"  {hex_c}: {cnt}")
    
    print(f"\nAvg Brightness: {sum(brightnesses)/len(brightnesses):.1f}%")
    print(f"Avg Saturation: {sum(saturations)/len(saturations):.1f}%")
    print(f"Avg High-Sat Area: {sum(high_sat_pcts)/len(high_sat_pcts):.1f}%")
    print(f"Avg Dark Area: {sum(dark_pcts)/len(dark_pcts):.1f}%")
    print(f"Avg Bright Area: {sum(bright_pcts)/len(bright_pcts):.1f}%")
    
    # Save results
    with open(PHOTO_DIR / "analysis_results.json", "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nDetailed results saved to analysis_results.json")
else:
    print("PIL/numpy not available. Installing...")
    import subprocess
    subprocess.run(["pip", "install", "Pillow", "numpy"], check=True)
    print("Installed. Re-run the script.")