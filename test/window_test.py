import tkinter as tk

# ウィンドウの作成
root = tk.Tk()
root.title("シンプルなウィンドウ")
root.geometry("300x200")  # 幅300px, 高さ200px

# ボタンの作成
button = tk.Button(root, text="範囲選択", command=lambda: print("ボタンが押されました"))
button.pack(expand=True)

# ウィンドウの表示
root.mainloop()
