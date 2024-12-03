from pathlib import Path
from tkinter import Tk, Canvas, Text, Button, PhotoImage, messagebox

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = str(OUTPUT_PATH) + "/assets/frame0"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def coletar_teclas():
    def start_camera():
        exit_key = entry_1.get("1.0", "end").strip()
        left_key = entry_2.get("1.0", "end").strip()
        right_key = entry_3.get("1.0", "end").strip()
        jump_key = entry_4.get("1.0", "end").strip()

        if not (exit_key and left_key and right_key and jump_key):
            messagebox.showwarning("Campos obrigatórios", "Todos os campos de teclas devem ser preenchidos.")
            return None

        window.quit()
        return exit_key, left_key, right_key, jump_key

    window = Tk()
    window.geometry("600x600")
    window.configure(bg="#2A2A2A")

    canvas = Canvas(
        window,
        bg="#2A2A2A",
        height=600,
        width=600,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)

    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: start_camera(),
        relief="flat",
        bg="#2A2A2A"
    )
    button_1.place(x=187.0, y=503.0, width=226.0, height=52.0)

    canvas.create_rectangle(0.0, 0.0, 600.0, 57.0, fill="#0D7910", outline="")
    canvas.create_text(
        600.0 / 2,
        57.0 / 2,
        anchor="center",
        text="Kinect Indie",
        fill="#FFFFFF",
        
        font=("Jersey25 Regular", 40 * -1)
)

    canvas.create_text(164.0, 105.0, anchor="nw", text="Exit key", fill="#B3B3B3", font=("Inter", 16 * -1))
    entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
    canvas.create_image(300.0, 155.0, image=entry_image_1)
    entry_1 = Text(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
    entry_1.place(x=172.0, y=135.0, width=256.0, height=38.0)

    canvas.create_text(164.0, 199.0, anchor="nw", text="Left key", fill="#B3B3B3", font=("Inter", 16 * -1))
    entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
    canvas.create_image(300.0, 249.0, image=entry_image_2)
    entry_2 = Text(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
    entry_2.place(x=172.0, y=229.0, width=256.0, height=38.0)

    canvas.create_text(164.0, 293.0, anchor="nw", text="Right key", fill="#B3B3B3", font=("Inter", 16 * -1))
    entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
    canvas.create_image(300.0, 343.0, image=entry_image_3)
    entry_3 = Text(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
    entry_3.place(x=172.0, y=323.0, width=256.0, height=38.0)

    canvas.create_text(164.0, 387.0, anchor="nw", text="Jump key", fill="#B3B3B3", font=("Inter", 16 * -1))
    entry_image_4 = PhotoImage(file=relative_to_assets("entry_4.png"))
    canvas.create_image(300.0, 437.0, image=entry_image_4)
    entry_4 = Text(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
    entry_4.place(x=172.0, y=417.0, width=256.0, height=38.0)

    window.resizable(False, False)
    window.mainloop()
    window.quit()
    return start_camera()
