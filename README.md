# A comprehensive experiment-based review of low-light image enhancement methods and benchmarking low-light image quality assessment
By Muhammad Tahir Rasheed, Daming Shi, Hufsa Khan

This is a tensorflow implementation of perceptual low-light image quality assessment [A comprehensive experiment-based review of low-light image enhancement methods and
benchmarking low-light image quality assessment](https://pages.github.com/).

## Citation Information
```
@ARTICLE{xxx2022,
  author={Muhammad Tahir Rasheed and Daming Shi and Hufsa Khan},
  journal={Signal Processing}, 
  title={Low-light Image Enhancement}, 
  year={2022},
  doi={xyz},
}
```

## PIAQ Dataset
Download: [google drive](https://pages.github.com/) (Just unzip data to current folder)

## Pre-trained Model
You can donwload the pre-trained DenseNet121 on the PIQA dataset from [google drive](https://pages.github.com/) and extract inside the checkpoints folder.
The pre-trained model can predict the perceputal quality of image size 256x256x3

## Testing
For the evaluation of pre-trained model on the PIQA test dataset use the following command line: 
```
> python test.py
```




