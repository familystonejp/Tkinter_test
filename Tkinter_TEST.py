import tkinter 

def cmdDisp( ):
    global lb2
    lb2["text"] = "クリックされました"
    print("「表示」ボタンがクリックされました")

def cmdDel( ): # 「消去」ボタンに対する処理
    global lb2
    lb2["text"] = "　　"
    print("「消去」ボタンがクリックされました")

#--- G U I の構築--- defoult
root = tkinter.Tk() # アプリケーションの最上位ウィジェット
root.title("tk01 main window") # ウィンドウのイトル
root.geometry("300x30+0+0") # ウィンドウのサイズと位置

fr = tkinter.Frame(root) # G U I 構築用のコンテナ_defoult
fr.pack () # f r をrootに配置_defoult

lb1 = tkinter.Label( fr , text="クリックしてください→") # 文字のラベル1
lb1.pack(side='left') # l b 1 をfrに配置

b1 = tkinter.Button( fr , text='表示' , command=cmdDisp ) # ボタン1
b1.pack(side='left') # b 1 をf r に配置

lb2 = tkinter.Label( fr , text="" ) # 文字のラベル2 （ 文字なし）
lb2.pack(side='left') # l b 2 をfrに配置

b2 = tkinter.Button( fr , text=' 消去' , command=cmdDel ) # ボタン2
b2.pack(side='left') # b 2 をf r に配置

 #--- アプリケーションの起動---defoult
root.mainloop ()