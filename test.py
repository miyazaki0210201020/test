import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
#セレクトボックスのリストを作成
pagelist = ["ヒストグラム","データ分析","page3","page4"]
#サイドバーのセレクトボックスを配置
selector=st.sidebar.selectbox( "ページ選択",pagelist)
if selector=="ヒストグラム":
    st.title("生産データ分析")
    uploaded_file=st.file_uploader("ファイルの取り込み",type="xlsx")
    if uploaded_file is not None:
        df=pd.read_excel(uploaded_file)
        st.dataframe(df)

    z_list = sorted(list(set(df["図番"])))

    z = st.selectbox(
         "図番",
         (z_list))

    x=df[(df["図番"]==z)]
    k_list = sorted(list(set(x["工程コード"])))
    k = st.selectbox(
         "工程コード",
         (k_list))

    x=df[(df["図番"]==z)&(df["工程コード"] == k)]
    t_list = sorted(list(set(x["担当コード"])))
    t = st.selectbox(
         "担当コード",
         (t_list))
    scores=df[(df["図番"]==z)&(df["工程コード"]==k)&(df["担当コード"]==t)]
    dd=scores["処理時間"]

    answer = st.button('分析開始')
    if answer == True:
        st.write(z)
        st.write(k)
        st.write(t)
        st.dataframe(scores)

        # 描画領域を用意する
        fig = plt.figure()
        ax = fig.add_subplot()
        ax.hist(dd, bins=10)
        # Matplotlib の Figure を指定して可視化する
        st.pyplot(fig)

elif selector=="データ分析":
    if st.button('ページ2ボタン'):
        st.title("データ分析")
elif selector=="page3":
    if st.button('ページ3ボタン'):
        st.title("ページ3のタイトル")
elif selector=="page4":
    if st.button('ページ4ボタン'):
        st.title("ページ4のタイトル")

