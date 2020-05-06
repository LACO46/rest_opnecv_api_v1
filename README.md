# REST OpenCV API

## できること

- ガンマ補正を利用したグレースケール画像の作成

## dockerコンテナのビルド方法

```
docker build -t rest_opencv_api .
```

## 起動コマンド

```
docker run -it -p 8080:80  -v /Users/tsudzukiyoshifumi/Documents/productions/HomeSisytem/rest_opnecv_api:/home rest_opencv_api
```

## 画像について

- `<保存先の画像のPATH>` の画像の拡張子は `.png` を指定
- `<元の画像のPATH>` の画像の拡張子は `.jpg` を指定

## ガンマ補正を利用したグレースケール画像の作成

### リクエスト

```
curl --output <保存先のPATH> -X POST -F img=@<元の画像のPATH> localhost:8080/v1/gray/
```

### クエリパラメーター

- `?gamma=1.0`
  - デフォルトは2.2
  - 省略可能（省略された場合はgamma=2.2になる）

## 等倍したリサイズ画像の作成

### リクエスト

```
curl --output <保存先の画像のPATH> -X POST -F img=@<元の画像のPATH> localhost:8080/v1/resize/same-size/<size>/
```

- `<size>` はfloatを指定

## サイズを指定したリサイズ画像の作成

### リクエスト

```
curl --output <保存先の画像のPATH> -X POST -F img=@<元の画像のPATH> localhost:8080/v1/resize/designation-size/<x_size>*<y_size>/
```

- `<x_size>` と `<y_size>` はintを指定

## ２値化画像の作成

### リクエスト

```
curl --output <保存先の画像のPATH> -X POST -F img=@<元の画像のPATH> localhost:8080/v1/binarization/<threshold>/
```

- `<threshold>` はintを指定

## 適応的閾値処理を用いた2値化画像の作成

### リクエスト

```
curl --output <保存先の画像のPATH> -X POST -F img=@<元の画像のPATH> localhost:8080/v1/adaptive/binarization/<block_size>/<mean_c>/
```

- `<block_size>` と `<mean_c>` はintを指定
  - `<block_size>` は奇数である必要がある

## エッジ検出処理を用いた画像の作成

### リクエスト

```
curl --output <保存先の画像のPATH> -X POST -F img=@<元の画像のPATH> localhost:8080/v1/edge-detection/<threshold_max>/<threshold_min>/
```

- `<threshold_max>` と `<threshold_min>` はintを指定
  - `<threshold_max> > <threshold_min>` である必要がある

## 指定範囲の平均ぼかし処理を用いた画像の作成

### リクエスト

```
curl --output <保存先の画像のPATH> -X POST -F img=@<元の画像のPATH> localhost:8080/v1/blur/average/<x>/<y>/
```

- `<x>` と `<y>` はintを指定

## ガウシアンフィルタのぼかし処理を用いた画像の作成

### リクエスト

```
curl --output <保存先の画像のPATH> -X POST -F img=@<元の画像のPATH> localhost:8080/v1/blur/gaussian/<x>/<y>/<sigma>/
```

- `<x>` と `<y>` と `<sigma>` はintを指定
  - `<x>` と `<y>` は奇数である必要がある

## 中央値ぼかし処理を用いた画像の作成

### リクエスト

```
curl --output <保存先の画像のPATH> -X POST -F img=@<元の画像のPATH> localhost:8080/v1/blur/median/<median_numeric>/
```

- `<median_numeric>` はintを指定
  - `<median_numeric>` は奇数である必要がある

## バイラテラルフィルタのぼかし処理を用いた画像の作成

### リクエスト

```
curl --output <保存先の画像のPATH> -X POST -F img=@<元の画像のPATH> localhost:8080/v1/blur/bilateral/<pixel_interest>/<sigma_color>/<sigma_space>/
```

- `<pixel_interest>` と `<sigma_color>` と `<sigma_space>` はintを指定

## Convolutional Neural Network処理を用いたシャープネス画像の作成

### リクエスト

- シャープネスレベル１

```
curl --output ~/Desktop/test.png -X POST -F img=@./Lenna.jpg localhost:8080/v1/convolution-2d/<kernel>/
```

```
curl --output ~/Desktop/test.png -X POST -F img=@./Lenna.jpg localhost:8080/v1/convolution-2d/0,-1,0,0,3,0,0,-1,0/
```

- シャープネスレベル２

```
curl --output ~/Desktop/test.png -X POST -F img=@./Lenna.jpg localhost:8080/v1/convolution-2d/0,-1,0,-1,5,-1,0,-1,0/
```

- シャープネスレベル３

```
curl --output ~/Desktop/test.png -X POST -F img=@./Lenna.jpg localhost:8080/v1/convolution-2d/-1,-1,-1,-1,9,-1,-1,-1,-1/
```

- シャープネスレベル４

```
curl --output ~/Desktop/test.png -X POST -F img=@./Lenna.jpg localhost:8080/v1/convolution-2d/-1,-1,-1,-1,9,-1,-1,-1,-1/
```

- シャープネスレベル５

```
curl --output ~/Desktop/test.png -X POST -F img=@./Lenna.jpg localhost:8080/v1/convolution-2d/-1,-2,-1,-2,12,-2,-1,-2,-1/
```

- シャープネスレベル６

```
curl --output ~/Desktop/test.png -X POST -F img=@./Lenna.jpg localhost:8080/v1/convolution-2d/1,4,6,4,1,4,16,24,16,4,6,24,-476,24,6,4,16,24,16,4,1,4,6,4,1/
```

- `<kernel>` は数値を `,` で区切る必要がある
  - 例：`n,m,o,p`
- `<kernel>` の長さは、 `n^2` で表すことのできる長さである必要がある