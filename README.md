# REST OpenCV API

## できること

- ガンマ補正を利用したグレースケール画像の作成

## dockerのビルド方法

```
docker build -t rest_opencv_api .
```

## 起動コマンド

```
docker run -it -p 8080:80  -v /Users/tsudzukiyoshifumi/Documents/productions/HomeSisytem/rest_opnecv_api:/home rest_opencv_api
```

## ガンマ補正を利用したグレースケール画像の作成

### リクエスト

```
curl --output ~/Desktop/test.png -X POST -F img=@./Lenna.jpg localhost:8080/v1/gray/
```

### クエリパラメーター

- `?gamma=1.0`
  - デフォルトは2.2
  - 省略可能（省略された場合はgamma=2.2になる）
