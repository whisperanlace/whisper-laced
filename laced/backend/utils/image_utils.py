# utils/image_utils.py
from typing import Tuple, Optional
from PIL import Image, ImageOps, ImageFilter
from pathlib import Path
import logging
from utils.file_utils import IMAGES_DIR

logger = logging.getLogger(__name__)

DEFAULT_MAX_SIZE = (2048, 2048)

def open_image(path: Path) -> Image.Image:
    return Image.open(path).convert("RGBA")

def resize_image(path_or_pil, max_size: Tuple[int, int] = DEFAULT_MAX_SIZE, save_as: Optional[Path] = None) -> Path:
    """
    Resize image to fit within max_size while maintaining aspect ratio.
    Accepts Path or PIL.Image. Returns path to saved resized image (overwrites if save_as provided).
    """
    if isinstance(path_or_pil, Path):
        img = open_image(path_or_pil)
    else:
        img = path_or_pil

    img.thumbnail(max_size, Image.LANCZOS)
    if save_as is None:
        save_as = Path(IMAGES_DIR) / f"resized_{Path(getattr(path_or_pil, 'name', 'image')).name}"
        save_as.parent.mkdir(parents=True, exist_ok=True)
    img.convert("RGB").save(save_as, format="JPEG", quality=92)
    logger.debug(f"Resized and saved image to {save_as}")
    return save_as

def apply_watermark(image_path: Path, watermark_path: Optional[Path] = None, opacity: float = 0.25) -> Path:
    """
    Apply watermark onto image. If watermark_path is None, skip (or use default).
    """
    if watermark_path is None:
        logger.debug("No watermark path provided, skipping watermark.")
        return image_path

    base = open_image(image_path).convert("RGBA")
    watermark = open_image(watermark_path).convert("RGBA")
    # scale watermark to 20% of base width
    w_ratio = base.width * 0.2 / watermark.width
    new_size = (int(watermark.width * w_ratio), int(watermark.height * w_ratio))
    watermark = watermark.resize(new_size, Image.ANTIALIAS)

    # set opacity
    alpha = watermark.split()[3]
    alpha = alpha.point(lambda p: int(p * opacity))
    watermark.putalpha(alpha)

    position = (base.width - watermark.width - 20, base.height - watermark.height - 20)
    base.paste(watermark, position, watermark)
    out_path = image_path.with_name(f"{image_path.stem}_wm{image_path.suffix}")
    base.convert("RGB").save(out_path, quality=92)
    logger.debug(f"Applied watermark and saved to {out_path}")
    return out_path

def fix_mirror_symmetry(image_path: Path, save_as: Optional[Path] = None) -> Path:
    """
    Simple approach: if user asked for mirrored symmetry correction, this will attempt to
    detect the center vertical axis and symmetrize left/right halves. This is heuristic and
    provided as a utility — production models may need ML-based correction.
    """
    img = open_image(image_path)
    w, h = img.size
    left = img.crop((0, 0, w // 2, h))
    right = img.crop((w - w // 2, 0, w, h))
    # mirror left to right and blend
    left_mirror = ImageOps.mirror(left)
    combined = Image.blend(left_mirror.resize(right.size), right, alpha=0.5)
    out = Image.new("RGBA", (w, h))
    out.paste(left, (0, 0))
    out.paste(combined, (w // 2, 0))
    if save_as is None:
        save_as = image_path.with_name(f"{image_path.stem}_sym{image_path.suffix}")
    out.convert("RGB").save(save_as, quality=92)
    logger.debug(f"Fixed mirror symmetry and saved to {save_as}")
    return save_as
