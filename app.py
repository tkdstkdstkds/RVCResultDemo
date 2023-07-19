import gradio

# python main entry point
def main():
    # Create a gradio blocks
    app = gradio.Blocks()
    with app:
        # using python with keyword to create a gradio column
        with gradio.Column():
            # create a gradio label
            gradio.HTML("<B>rei-yumesaki訓練集原始音檔URL: <a href='https://tyc.rei-yumesaki.net/material/corpus/'>https://tyc.rei-yumesaki.net/material/corpus/</a> </B>")

            # create a gradio audio player, audio file path = ./vocal/rei-yumesaki/VOICEACTRESS100_001.wav
            gradio.Audio(value="./vocal/rei-yumesaki/VOICEACTRESS100_001.wav", label="rei-yumesaki訓練集原始音檔試聽")

            # create a gradio label
            gradio.HTML("<B>jsut來源音檔URL: <a href='https://sites.google.com/site/shinnosuketakamichi/publication/jsut'>https://sites.google.com/site/shinnosuketakamichi/publication/jsut</a> " \
                        "<br/>" \
                        "論文 Ryosuke Sonobe, Shinnosuke Takamichi and Hiroshi Saruwatari,  'JSUT corpus: free large-scale Japanese speech corpus for end-to-end speech synthesis,' arXiv preprint, 1711.00354, 2017." \
                        "</B>")
            # create a gradio audio player, audio file path = ./vocal/jsut_ver1.1/REPEAT500_set1_001.wav
            gradio.Audio(value="./vocal/jsut_ver1.1/REPEAT500_set1_001.wav", label="jsut來源音檔試聽")

            # create a gradio label
            gradio.HTML("<B>將jsut來源音檔 => rei-yumesaki的聲音: </B>")
            # create a gradio audio player, audio file path = ./vocal/jsut_to_rei-yumesaki.wav
            gradio.Audio(value="./vocal/jsut_to_rei-yumesaki.wav")

            # create a gradio label
            gradio.HTML("<B>自己(男)錄製來源音檔 </B>")
            # create a gradio audio player, audio file path = ./vocal/my-dirty-talk.wav
            gradio.Audio(value="./vocal/my-dirty-talk.wav")

            # create a gradio label
            gradio.HTML("<B>自己(男)錄製來源音檔 => rei-yumesaki的聲音: </B>")
            # create a gradio audio player, audio file path = ./vocal/my-dirty-talk_to_rei-yumesaki.wav
            gradio.Audio(value="./vocal/my-dirty-talk_to_rei-yumesaki.wav")

    
    # launch gradio app with dark theme
    app.launch()

# python main entry point
if __name__ == "__main__":
    # call main function
    main()


