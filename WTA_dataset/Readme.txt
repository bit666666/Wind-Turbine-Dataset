Wind Turbine Aerial-image dataset

Trian:
189 images
Test:
35 images

The links of the original paper and the dataset：
doi: 10.1109/ICUAS54217.2022.9836096
dataset: https://github.com/gzamps/wta_tla_dataset
@inproceedings{za2022wtatla,
  author={Zampokas, Georgios and Skartados, Evangelos and Alexiou, Dimitrios and Tsiakas, Kosmas and Tzanakis, Ioannis and Roussos, Nikolaos and Giakoumis,   Dimitrios and Kostavelis, Ioannis and Bouganis, Christos-Savvas and Tzovaras, Dimitrios},
  booktitle={2022 International Conference on Unmanned Aircraft Systems (ICUAS)}, 
  title={WTA/TLA: A UAV-captured Dataset for Semantic Segmentation of Energy Infrastructure}, 
  year={2022}

Three methods, namely SSIM (Structural Similarity Index), histogram similarity, and pixel similarity, are used to check whether there is duplication or high similarity between the training set and the test set.

Note the following changes:
1>'envB_06t' is a duplicate of 'envB_01'. Action: Moved envB_06t to the training dataset.
2>'envB_09t' is a duplicate of 'envB_31'. Action: Moved envB_09t to the training dataset.
3>'envB_07t' is highly similar to 'envB_07'. Actions:
    training dataset <-> test dataset.
        ' envB_09 ' <-> ' envB_07t '
4>'envA_10t' is highly similar to 'envA_74'. Actions:
    training dataset <-> test dataset.
        ' envA_34 ' <-> ' envA_10t '
