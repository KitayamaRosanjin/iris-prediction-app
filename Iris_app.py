import streamlit as st
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# タイトル
st.title("Iris 花の分類予測アプリ")
st.write("花の特徴を入力して、種類を予測します！（AIモデル使用）")

# データセットの読み込みとモデルの訓練（アプリ起動時に一度だけ実行）
@st.cache_resource  # 高速化のため
def load_model():
    iris = load_iris()
    X = iris.data
    y = iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    clf = RandomForestClassifier(random_state=42)
    clf.fit(X_train, y_train)
    # 精度を表示
    y_pred = clf.predict(X_test)
    st.write("モデルの精度:", accuracy_score(y_test, y_pred))
    st.write("詳細報告:")
    st.text(classification_report(y_test, y_pred, target_names=iris.target_names))
    return clf, iris  # 修正: iris全体を返す

clf, iris = load_model()  # 修正: irisを受け取る

# ユーザー入力（スライダーで特徴量を入力）
st.header("花の特徴を入力してください")
sepal_length = st.slider("がく片の長さ (cm)", 4.0, 8.0, 5.0)
sepal_width = st.slider("がく片の幅 (cm)", 2.0, 4.5, 3.0)
petal_length = st.slider("花びらの長さ (cm)", 1.0, 7.0, 4.0)
petal_width = st.slider("花びらの幅 (cm)", 0.1, 2.5, 1.0)

# 予測ボタン
if st.button("予測する"):
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = clf.predict(input_data)[0]
    probability = clf.predict_proba(input_data)[0]
    
    st.header("結果")
    st.write(f"予測された花の種類: **{iris.target_names[prediction]}**")  # 今度はOK
    st.write("各クラスの確率:")
    for i, name in enumerate(iris.target_names):
        st.write(f"- {name}: {probability[i]:.2%}")

# 説明
st.header("このアプリについて")
st.write("- scikit-learnで訓練したRandomForestモデルを使っています。")
st.write("- Irisデータセット（有名な機械学習のサンプルデータ）で学習。")
st.write("- 精度は100%（テストデータで）。")