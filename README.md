# REST OpenCV API

## できること

- ガンマ補正を利用したグレースケール画像の作成
- 等倍したリサイズ画像の作成
- サイズを指定したリサイズ画像の作成
- ２値化画像の作成
- 適応的閾値処理を用いた 2 値化画像の作成
- エッジ検出処理を用いた画像の作成
- 指定範囲の平均ぼかし処理を用いた画像の作成
- ガウシアンフィルタのぼかし処理を用いた画像の作成
- 中央値ぼかし処理を用いた画像の作成
- バイラテラルフィルタのぼかし処理を用いた画像の作成
- Convolutional Neural Network 処理を用いたシャープネス画像の作成

## docker コンテナのビルド方法

```
docker-compose build
```

## 起動コマンド

```
docker-compose up
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
  - デフォルトは 2.2
  - 省略可能（省略された場合は gamma=2.2 になる）

## 等倍したリサイズ画像の作成

### リクエスト

```
curl --output <保存先の画像のPATH> -X POST -F img=@<元の画像のPATH> localhost:8080/v1/resize/same-size/<size>/
```

- `<保存先の画像のPATH>` は ファイル名+拡張子 を指定する
- `<size>` は float を指定

## サイズを指定したリサイズ画像の作成

### リクエスト

```
curl --output <保存先の画像のPATH> -X POST -F img=@<元の画像のPATH> localhost:8080/v1/resize/designation-size/<x_size>*<y_size>/
```

- `<保存先の画像のPATH>` は ファイル名+拡張子 を指定する
- `<x_size>` と `<y_size>` は int を指定

## ２値化画像の作成

### リクエスト

```
curl --output <保存先の画像のPATH> -X POST -F img=@<元の画像のPATH> localhost:8080/v1/binarization/<threshold>/
```

- `<保存先の画像のPATH>` は ファイル名+拡張子 を指定する
- `<threshold>` は int を指定

## 適応的閾値処理を用いた 2 値化画像の作成

### リクエスト

```
curl --output <保存先の画像のPATH> -X POST -F img=@<元の画像のPATH> localhost:8080/v1/adaptive/binarization/<block_size>/<mean_c>/
```

- `<保存先の画像のPATH>` は ファイル名+拡張子 を指定する
- `<block_size>` と `<mean_c>` は int を指定
  - `<block_size>` は奇数である必要がある

## エッジ検出処理を用いた画像の作成

### リクエスト

```
curl --output <保存先の画像のPATH> -X POST -F img=@<元の画像のPATH> localhost:8080/v1/edge-detection/<threshold_max>/<threshold_min>/
```

- `<保存先の画像のPATH>` は ファイル名+拡張子 を指定する
- `<threshold_max>` と `<threshold_min>` は int を指定
  - `<threshold_max> > <threshold_min>` である必要がある

## 指定範囲の平均ぼかし処理を用いた画像の作成

### リクエスト

```
curl --output <保存先の画像のPATH> -X POST -F img=@<元の画像のPATH> localhost:8080/v1/blur/average/<x>/<y>/
```

- `<保存先の画像のPATH>` は ファイル名+拡張子 を指定する
- `<x>` と `<y>` は int を指定

## ガウシアンフィルタのぼかし処理を用いた画像の作成

### リクエスト

```
curl --output <保存先の画像のPATH> -X POST -F img=@<元の画像のPATH> localhost:8080/v1/blur/gaussian/<x>/<y>/<sigma>/
```

- `<保存先の画像のPATH>` は ファイル名+拡張子 を指定する
- `<x>` と `<y>` と `<sigma>` は int を指定
  - `<x>` と `<y>` は奇数である必要がある

## 中央値ぼかし処理を用いた画像の作成

### リクエスト

```
curl --output <保存先の画像のPATH> -X POST -F img=@<元の画像のPATH> localhost:8080/v1/blur/median/<median_numeric>/
```

- `<保存先の画像のPATH>` は ファイル名+拡張子 を指定する
- `<median_numeric>` は int を指定
  - `<median_numeric>` は奇数である必要がある

## バイラテラルフィルタのぼかし処理を用いた画像の作成

### リクエスト

```
curl --output <保存先の画像のPATH> -X POST -F img=@<元の画像のPATH> localhost:8080/v1/blur/bilateral/<pixel_interest>/<sigma_color>/<sigma_space>/
```

- `<保存先の画像のPATH>` は ファイル名+拡張子 を指定
- `<pixel_interest>` と `<sigma_color>` と `<sigma_space>` は int を指定

## Convolutional Neural Network 処理を用いた画像の作成

### シャープネス画像作成のリクエスト

```
curl --output <保存先の画像のPATH> -X POST -F img=@./Lenna.jpg localhost:8080/v1/convolution-2d/<kernel>/
```

- `<保存先の画像のPATH>` は ファイル名+拡張子 を指定する

### シャープネスレベル１

```
curl --output <保存先の画像のPATH> -X POST -F img=@./Lenna.jpg localhost:8080/v1/convolution-2d/0,-1,0,0,3,0,0,-1,0/
```

- `<保存先の画像のPATH>` は ファイル名+拡張子 を指定する

### シャープネスレベル２

```
curl --output <保存先の画像のPATH> -X POST -F img=@./Lenna.jpg localhost:8080/v1/convolution-2d/0,-1,0,-1,5,-1,0,-1,0/
```

- `<保存先の画像のPATH>` は ファイル名+拡張子 を指定する

### シャープネスレベル３

```
curl --output <保存先の画像のPATH> -X POST -F img=@./Lenna.jpg localhost:8080/v1/convolution-2d/-1,-1,-1,-1,9,-1,-1,-1,-1/
```

- `<保存先の画像のPATH>` は ファイル名+拡張子 を指定する

### シャープネスレベル４

```
curl --output <保存先の画像のPATH> -X POST -F img=@./Lenna.jpg localhost:8080/v1/convolution-2d/-1,-1,-1,-1,9,-1,-1,-1,-1/
```

- `<保存先の画像のPATH>` は ファイル名+拡張子 を指定する

### シャープネスレベル５

```
curl --output <保存先の画像のPATH> -X POST -F img=@./Lenna.jpg localhost:8080/v1/convolution-2d/-1,-2,-1,-2,12,-2,-1,-2,-1/
```

- `<保存先の画像のPATH>` は ファイル名+拡張子 を指定する

### シャープネスレベル６

```
curl --output <保存先の画像のPATH> -X POST -F img=@./Lenna.jpg localhost:8080/v1/convolution-2d/1,4,6,4,1,4,16,24,16,4,6,24,-476,24,6,4,16,24,16,4,1,4,6,4,1/
```

- `<保存先の画像のPATH>` は ファイル名+拡張子 を指定する
- `<kernel>` は数値を `,` で区切る必要がある
  - 例：`n,m,o,p`
- `<kernel>` の長さは、 `n^2` で表すことのできる長さである必要がある

## OCR 処理を用いた文字列抽出

### リクエスト

```
curl -X POST -F img=@<元の画像のPATH> localhost:8080/v1/ocr/jpn/
```

### レスポンス

```
{
  "word": <WORD>
}
```

- `<WORD>` は OCR で検出された文字列
