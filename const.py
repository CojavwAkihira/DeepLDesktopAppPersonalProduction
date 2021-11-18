import constantFunc
import string

class value(constantFunc.Constant):

     APIPath = "./api.ini"

     rootWindowTitle: string = "(Experiment by Akimoch) DeepL Translate Desktop version FreeAPI version"
     rootWindowSize: string = "1024x768"
     rootBeforeTransLabel: string = "翻訳前の言語："
     beforeLangSelList = ["自動設定","ブルガリア語","チェコ語","デンマーク語","ドイツ語","ギリシャ語","英語","スペイン語","エストニア語","フィンランド語","フランス語","ハンガリー語","イタリア語","日本","リトアニア語","ラトビア語","オランダ語","ポーランド語","ポルトガル語（すべて）","ルーマニア語","ロシア語","スロバキア語","スロベニア語","スウェーデン語","中国語"]

     translateButtonLabel: string = "\n＝＝ 翻訳 ＝＞\n"

     rootAfterTransLabel: string = "翻訳後の言語："
     afterLangSelList = ["自動設定","ブルガリア語","チェコ語","デンマーク語","ドイツ語","ギリシャ語","イギリス英語","アメリカ英語","英語(指定なし)","スペイン語","エストニア語","フィンランド語","フランス語","ハンガリー語","イタリア語","日本","リトアニア語","ラトビア語","オランダ語","ポーランド語","ポルトガル語（標準）","ポルトガル語（ブラジル）","ポルトガル語（指定なし）","ルーマニア語","ロシア語","スロバキア語","スロベニア語","スウェーデン語","中国語"]
     APIKeyButtonLabel: string = "　APIキー変更　"

     def getBeforeLangList(self):
          return self.beforeLangSelList