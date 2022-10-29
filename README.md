# A comprehensive experiment-based review of low-light image enhancement methods and benchmarking low-light image quality assessment
By Muhammad Tahir Rasheed, Daming Shi, Hufsa Khan

This is a tensorflow implementation of perceptual low-light image quality assessment [A comprehensive experiment-based review of low-light image enhancement methods and
benchmarking low-light image quality assessment](https://www.sciencedirect.com/science/article/abs/pii/S0165168422003607).

## Citation Information
```
@article{rasheed2022comprehensive,
  title={A comprehensive experiment-based review of low-light image enhancement methods and benchmarking low-light image quality assessment},
  author={Rasheed, Muhammad Tahir and Shi, Daming and Khan, Hufsa},
  journal={Signal Processing},
  pages={108821},
  year={2022},
  publisher={Elsevier}
}
```

## PIAQ Dataset
Download: [google drive](https://drive.google.com/file/d/1cJOUB2dp95fOyp55-7onj4Nnz65MwswJ/view?usp=sharing) (Just unzip data to current folder)

## Pre-trained Model
You can donwload the pre-trained DenseNet121 on the PIQA dataset from [google drive](https://drive.google.com/file/d/1Vh92wkYLVMSg6d1JNfpwO3Wjs__dIdqu/view?usp=sharing) and extract inside the checkpoints folder.
The pre-trained model can predict the perceputal quality of image size 256x256x3

## Testing
For the evaluation of pre-trained model on the PIQA test dataset use the following command line: 
```
> python test.py
```




