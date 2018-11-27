Palette generator for VoxelShop

## About

This script extracts dominant colors of a illustration and generates a color palette for [VoxelShop](https://github.com/simlu/voxelshop).

For example, the script generates the following palette from the following icon.

![](https://github.com/nekketsuuu/palette-generator/blob/master/img/nekketsuuu.jpg)

↓

![](https://github.com/nekketsuuu/palette-generator/blob/master/img/palette.png)

## Prerequisites

* cv2
* numpy
* sklearn (for k-means)

## Usage

The following command generates a 10x16 palette `<prefix>_result.png`.

```
python main.py <imgpath>
```

## License

[CC-BY 3.0 Unported](https://creativecommons.org/licenses/by/3.0/deed.en)
