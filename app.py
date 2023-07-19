import gradio

# python main entry point
def main():
    # Create a gradio blocks
    app = gradio.Blocks()
    with app:
        # using python with keyword to create a gradio column
        with gradio.Column():
            # create a gradio markdown
            gradio.Markdown("# 以下皆為AI聲音轉聲音的技術研究測試，請勿用於商業及非法用途。")

            # create a gradio markdown
            gradio.Markdown("> 音声合成（「声質の学習」「RVCによる声質変換」など、より具体的に説明しても可）には、フリー素材キャラクター「つくよみちゃん」が無料公開している音声データを使用しています。<br>"\
                            "■つくよみちゃんコーパス（CV.夢前黎）<br>" \
                            "https://tyc.rei-yumesaki.net/material/corpus/<br>")
            # create a gradio audio player, audio file path = ./vocal/rei-yumesaki/VOICEACTRESS100_001.wav
            gradio.Audio(value="./vocal/rei-yumesaki/VOICEACTRESS100_001.wav", label="rei-yumesaki訓練集原始音檔試聽", shared=False)

            gradio.Markdown("----------------------")


            # create a gradio markdown
            gradio.Markdown("## case1: 測試女性聲音轉rei-yumesaki的聲音")

            # create a gradio label
            gradio.Markdown("jsut來源音檔URL: [https://sites.google.com/site/shinnosuketakamichi/publication/jsut](https://sites.google.com/site/shinnosuketakamichi/publication/jsut)")
            gradio.Markdown("> 論文 Ryosuke Sonobe, Shinnosuke Takamichi and Hiroshi Saruwatari,  'JSUT corpus: free large-scale Japanese speech corpus for end-to-end speech synthesis,' arXiv preprint, 1711.00354, 2017.")
            # create a gradio audio player, audio file path = ./vocal/jsut_ver1.1/REPEAT500_set1_001.wav
            gradio.Audio(value="./vocal/jsut_ver1.1/REPEAT500_set1_001.wav", label="jsut來源音檔試聽", shared=False)

            # create a gradio label
            gradio.HTML("<B>將jsut來源音檔 => rei-yumesaki的聲音: </B>")
            # create a gradio audio player, audio file path = ./vocal/jsut_to_rei-yumesaki.wav
            gradio.Audio(value="./vocal/jsut_to_rei-yumesaki.wav", shared=False)


            
            gradio.Markdown("----------------------")


            # create a gradio markdown
            gradio.Markdown("## case2: 測試男性聲音轉rei-yumesaki的聲音，並同時測試呻吟聲轉出效果")

            # create a gradio label
            gradio.HTML("<B>自己(男)錄製來源音檔 </B>")
            # create a gradio audio player, audio file path = ./vocal/my-dirty-talk.wav
            gradio.Audio(value="./vocal/my-dirty-talk.wav", shared=False)

            # create a gradio label
            gradio.HTML("<B>自己(男)錄製來源音檔 => rei-yumesaki的聲音: </B>")
            # create a gradio audio player, audio file path = ./vocal/my-dirty-talk_to_rei-yumesaki.wav
            gradio.Audio(value="./vocal/my-dirty-talk_to_rei-yumesaki.wav", shared=False)

    
    # launch gradio app with dark theme
    app.launch()

# python main entry point
if __name__ == "__main__":
    # call main function
    main()


