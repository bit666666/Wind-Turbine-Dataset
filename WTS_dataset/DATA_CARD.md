# WTS data card

WTS contains 871 training images and 110 test images for two-class semantic segmentation of wind turbines. Each image has a matching PNG mask in `label_1D` (0: background; 1: wind turbine) and a colored visualization in `label_3D`.

## Release and provenance

The training files were recovered from the original project archive and published as release `wts-training-2025` on 8 November 2026. Their archived modification dates are in 2025, before the 8 September 2026 cutoff used for this recovery. These are the retained historical files, not newly synthesized images or annotations. `training_manifest.csv` records original modification times, byte sizes, and SHA-256 values for the 2,613 training files. File dates record archive provenance; they do not establish image acquisition dates.

The original dataset notes describe the 871 training images as 691 retained source images, 40 background images, and 140 supplementary images. The 110 test images comprise 100 retained images and 10 supplementary images. No split was changed during this release. Image and mask stems were checked for all 871 training pairs. No byte-identical training image was found among the 110 test images; this check does not establish geographic or spatial independence.

The source records identified by the original documentation are:

- Power Plant Satellite Imagery Dataset, Figshare: https://doi.org/10.6084/m9.figshare.5307364.v1
- Wind Turbine Detection, Kaggle: https://www.kaggle.com/datasets/saurabhshahane/wind-turbine-obj-detection

Both upstream records list CC BY 4.0. The authors' original annotations are provided under CC BY 4.0; retain attribution to the source datasets and the EdgeAwareUNet authors, and indicate modifications. See `LICENSE`. Original imagery remains subject to the original providers' license and attribution requirements. The archive does not contain a complete per-image source and rights map for the supplementary patches.

## Image dimensions and preprocessing

There are 731 training images of 608 x 608 pixels and 140 supplementary images with varying dimensions. The 40 all-background training masks are 605 x 605 pixels although their images are 608 x 608 pixels; these unchanged historical masks contain only zero labels. The historical experiment code resizes both images and masks to 512 x 256 pixels. A loader must resize the mask and image to the same output size before training.

## Metadata limitations

Complete image acquisition dates, georeferencing, geographic coverage, and per-patch ground sampling distances are not available in the recovered archive. Dataset image dimensions are pixel counts, not ground sampling distance. The published split is a historical patch benchmark and is not claimed to be geographically independent. This release supplies image patches and segmentation masks, not a georeferenced regional turbine inventory.

## Related model code

https://github.com/bit666666/EdgeAwareUNet

## Download the training split

From the repository root run `python WTS_dataset/download_training.py`. All nine public release assets are required; their URLs, byte sizes, and SHA-256 values are in `TRAINING_DOWNLOADS.json`. The script extracts the training tree and verifies all 2,613 files against `training_manifest.csv`. WTA and WTS test files are already present in the Git checkout.
