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
curl --output <保存先のPATH> -X POST -F img=@./<元の画像のPATH> localhost:8080/v1/gray/
```

### クエリパラメーター

- `?gamma=1.0`
  - デフォルトは2.2
  - 省略可能（省略された場合はgamma=2.2になる）

## 等倍したリサイズ画像の作成

### リクエスト

```
curl --output <保存先の画像のPATH> -X POST -F img=@./<元の画像のPATH> localhost:8080/v1/resize/same-size/<size>/
```

- `<size>` はfloatを指定

## サイズを指定したリサイズ画像の作成

### リクエスト

```
curl --output <保存先の画像のPATH> -X POST -F img=@./<元の画像のPATH> localhost:8080/v1/resize/designation-size/<x_size>*<y_size>/
```

- `<x_size>` と `<y_size>` はintを指定

## ２値化画像の作成

### リクエスト

```
curl --output <保存先の画像のPATH> -X POST -F img=@./<元の画像のPATH> localhost:8080/v1/binarization/<threshold>/
```

- `<threshold>` はintを指定

## 適応的閾値処理を用いた2値化画像の作成

### リクエスト

```
curl --output <保存先の画像のPATH> -X POST -F img=@./<元の画像のPATH> localhost:8080/v1/adaptive/binarization/<block_size>/<mean_c>/
```

- `<block_size>` と `<mean_c>` はintを指定
  - `<block_size>` は奇数である必要がある

## エッジ検出処理を用いた画像の作成

### リクエスト

```
curl --output <保存先の画像のPATH> -X POST -F img=@./<元の画像のPATH> localhost:8080/v1/edge-detection/<threshold_max>/<threshold_min>/
```

- `<threshold_max>` と `<threshold_min>` はintを指定
  - `<threshold_max> > <threshold_min>` である必要がある

## 指定範囲の平均ぼかし処理を用いた画像の作成

### リクエスト

```
curl --output <保存先の画像のPATH> -X POST -F img=@./<元の画像のPATH> localhost:8080/v1/blur/average/<x>/<y>/
```

- `<x>` と `<y>` はintを指定

## ガウシアンフィルタのぼかし処理を用いた画像の作成

### リクエスト

```
curl --output <保存先の画像のPATH> -X POST -F img=@./<元の画像のPATH> localhost:8080/v1/blur/gaussian/<x>/<y>/<sigma>/
```

- `<x>` と `<y>` と `<sigma>` はintを指定
  - `<x>` と `<y>` は奇数である必要がある

## 中央値ぼかし処理を用いた画像の作成

### リクエスト

```
curl --output <保存先の画像のPATH> -X POST -F img=@./Lenna.jpg localhost:8080/v1/blur/median/<median_numeric>/
```

- `<median_numeric>` はintを指定
  - `<median_numeric>` は奇数である必要がある
