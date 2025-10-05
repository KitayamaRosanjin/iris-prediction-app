# Iris 花の分類予測アプリ

Streamlitで作ったシンプルなAIアプリ！ 花の特徴（がく片・花びらのサイズ）を入力すると、機械学習モデルがIrisの種類（setosa, versicolor, virginica）を予測します。Python初心者のポートフォリオプロジェクトとして作成しました。

## デモ結果例
![アプリ画面](app_screenshot.png)  <!-- ここにスクショをアップロードしてURLを貼る -->

- **入力例**: がく片長さ 5.0cm、幅 3.0cm、花びら長さ 4.0cm、幅 1.0cm
- **予測結果**: **versicolor** (94% 確率)
  - setosa: 6%
  - versicolor: 94%
  - virginica: 0%

## 機能
- ユーザー入力（スライダー）で花の特徴を調整。
- RandomForestClassifierでリアルタイム予測（確率も表示）。
- モデルの精度評価（テストデータで100%）。

## 実行方法（ローカルで動かす）
1. このリポジトリをクローン:
