import tkinter as tk
from pypresence import Presence
import time
import webbrowser
import requests

url = "https://backend.karusa.fr/livingroomrpc/"

version_actuelle = "1.0.0"
response = requests.post(url)

if response.text == version_actuelle:
    RPC = Presence(client_id="777992628045611072")

    def launch_rpc():
        RPC.connect()
        RPC.update(
            details="Serveur communautaire",
            state="Chill, discussion, rencontre amicale et plus encore !",
            large_image="livingroom",
            large_text="Living Room 🎀",
            buttons=[
                {"label": "Rejoindre le serveur !", "url": "https://discord.gg/LivingRoom"},
                {"label": "Voir le site !", "url": "https://panel.karusa.fr/"}
            ],
            start=time.time(),
        )

    def stop_rpc():
        RPC.close()

    def main():
        root = tk.Tk()
        root.title("RPC Living Room")
        root.iconbitmap(default='icon.ico')
        root.geometry("300x200")
        root.minsize(300, 200)
        root.maxsize(300, 200)
        root.config(bg="#2C2F33")

        label = tk.Label(root, text="RPC Living Room", font=("Helvetica", 20), bg="#2C2F33", fg="white")
        label.pack(pady=10)

        btn_launch_rpc = tk.Button(root, text="Lancer le RPC", command=launch_rpc)
        btn_launch_rpc.pack(pady=10)

        btn_stop_rpc = tk.Button(root, text="Arrêter le RPC", command=stop_rpc)
        btn_stop_rpc.pack(pady=5)

        label2 = tk.Label(root, text="Par karusa_", font=("Helvetica", 10), bg="#2C2F33", fg="#cf00ba")
        label2.bind("<Button-1>", lambda e: webbrowser.open_new("https://discord.com/users/299572401975328769"))
        label2.pack(pady=10)

        root.mainloop()

    if __name__ == "__main__":
        main()

else:
    root = tk.Tk()
    root.title("Mise à jour requise")
    
    root.iconbitmap(default='icon.ico')
    root.geometry("500x100")
    root.minsize(500, 100)
    root.maxsize(500, 100)
    root.config(bg="#2C2F33")

    label = tk.Label(root, text="Une nouvelle version est disponible !", font=("Helvetica", 20), bg="#2C2F33", fg="white")
    label.pack(pady=10)

    def download():
        webbrowser.open_new("https://panel.karusa.fr/download/LivingRoomRPC_Setup.exe")
        root.destroy()

    btn_download = tk.Button(root, text="Télécharger", command=download)
    btn_download.pack(pady=10)

    root.mainloop()
