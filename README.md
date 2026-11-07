# Wind-Turbine-Dataset

This repository distributes two semantic segmentation datasets for wind turbines used in **EdgeAwareUNet: A Lightweight Semantic Segmentation Network for Wind Turbine Extraction from Satellite Imagery** (submitted to *Computers & Geosciences*):

- **WTS (Wind Turbine Satellite-image Dataset)** — satellite imagery with pixel-level annotations for small-target wind-turbine segmentation.
- **WTA (Wind Turbine Aerial-image Dataset)** — UAV-captured imagery used as an additional validation set.

## Repository layout

```text
Wind-Turbine-Dataset/
├── WTS_dataset/
│   ├── LICENSE              # CC BY 4.0 (applies to WTS)
│   ├── Readme.txt
│   └── test/
│       ├── img/             # 110 images
│       ├── label_1D/        # 110 single-channel masks
│       ├── label_3D/        # 110 colored masks
│       └── viz/             # 110 overlay visualizations
└── WTA_dataset/
    ├── LICENSE              # Apache License 2.0 (applies to WTA)
    ├── Readme.txt
    ├── train/               # 189 images (img, label_1D, label_3D)
    └── test/                # 35 images (img, label_1D, label_3D)
```

Image and mask files share matching stems. `label_1D` stores single-channel class-index masks, `label_3D` stores colored RGB masks, and `viz` stores image–mask overlays for inspection.

## Data sources and derivative-work statement

### WTS (derivative dataset)

WTS is a derivative work built from publicly available sources:

1. **Power Plant Satellite Imagery Dataset** (Figshare), licensed under **CC BY 4.0**:
   https://figshare.com/articles/dataset/Power_Plant_Satellite_Imagery_Dataset/5307364
2. **Wind Turbine Detection** (Kaggle), licensed under **CC BY 4.0**:
   https://www.kaggle.com/datasets/saurabhshahane/wind-turbine-obj-detection

The present study further filtered the source imagery, added and selected patches, and produced the original pixel-level semantic segmentation masks. The underlying imagery remains the work of the original providers; the manual annotations and curation are contributed by the EdgeAwareUNet authors. The WTS directory, including the annotations, is distributed under **CC BY 4.0** (see `WTS_dataset/LICENSE`).

### WTA (redistributed dataset)

WTA originates from the **WTA/TLA** dataset by Zampokas et al.:

- Repository: https://github.com/gzamps/wta_tla_dataset
- DOI: https://doi.org/10.1109/ICUAS54217.2022.9836096

WTA is redistributed here under its original **Apache License 2.0** (see `WTA_dataset/LICENSE`). Copyright and attribution for WTA remain with the original authors. The duplicate-handling changes documented below follow the original dataset notes.

## Licensing summary

| Component | License | Attribution |
|---|---|---|
| WTS imagery and annotations | CC BY 4.0 | Original Figshare/Kaggle providers + this work |
| WTA imagery and annotations | Apache License 2.0 | Zampokas et al. (WTA/TLA) |

There is no single repository-wide license; use the license located inside each dataset directory.

## Reuse and citation requirements

You may reuse, adapt, and redistribute these datasets under the terms of the applicable license. When using **WTS**, please cite both the original source datasets and the EdgeAwareUNet paper, and indicate any changes you made. When using **WTA**, please cite the original WTA/TLA paper and retain the Apache 2.0 notice.

### EdgeAwareUNet paper (submitted)

```bibtex
@article{edgeawareunet2026,
  title  = {EdgeAwareUNet: A Lightweight Semantic Segmentation Network for Wind Turbine Extraction from Satellite Imagery},
  author = {Li, Shibao and Liu, Xiaochen and Gu, Zhaozhi and Gu, Liang and Tian, Haoran},
  journal= {Computers \& Geosciences},
  note   = {submitted},
  year   = {2026}
}
```

### WTA/TLA source paper

```bibtex
@inproceedings{za2022wtatla,
  author    = {Zampokas, Georgios and Skartados, Evangelos and Alexiou, Dimitrios and Tsiakas, Kosmas and Tzanakis, Ioannis and Roussos, Nikolaos and Giakoumis, Dimitrios and Kostavelis, Ioannis and Bouganis, Christos-Savvas and Tzovaras, Dimitrios},
  booktitle = {2022 International Conference on Unmanned Aircraft Systems (ICUAS)},
  title     = {WTA/TLA: A UAV-captured Dataset for Semantic Segmentation of Energy Infrastructure},
  year      = {2022},
  doi       = {10.1109/ICUAS54217.2022.9836096}
}
```

## WTA duplicate-handling notes

1. `envB_06t` is a duplicate of `envB_01`. Action: moved `envB_06t` to the training dataset.
2. `envB_09t` is a duplicate of `envB_31`. Action: moved `envB_09t` to the training dataset.
3. `envB_07t` is highly similar to `envB_07`. Action: swapped `envB_09` and `envB_07t` between training and test sets.
4. `envA_10t` is highly similar to `envA_74`. Action: swapped `envA_34` and `envA_10t` between training and test sets.
