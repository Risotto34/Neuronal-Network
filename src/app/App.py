import tkinter as tk
from tkinter import colorchooser
from tkinter import ttk
import tempfile

from PIL import ImageGrab


class App:
    def __init__(
        self,
        onImageSend,
        width: int = 500,
        height: int = 500
    ):
        self.onImageSend = onImageSend

        self.width = width
        self.height = height

        self.root = tk.Tk()
        self.root.title("Circle / Cross Recognition")
        self.root.resizable(False, False)

        self.brush_size = 15
        self.brush_color = "black"

        self.last_x = None
        self.last_y = None

        self._create_interface()

    def _create_interface(self) -> None:
        main = ttk.Frame(self.root, padding=15)
        main.pack()

        title = ttk.Label(
            main,
            text="Circle / Cross Recognition",
            font=("Arial", 18, "bold")
        )
        title.pack(pady=(0, 10))

        self.canvas = tk.Canvas(
            main,
            width=self.width,
            height=self.height,
            bg="white",
            highlightthickness=0,
            highlightbackground="gray"
        )
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self._start_draw)
        self.canvas.bind("<B1-Motion>", self._draw)
        self.canvas.bind("<ButtonRelease-1>", self._stop_draw)

        controls = ttk.Frame(main)
        controls.pack(fill="x", pady=(15, 0))

        self._create_size_controls(controls)
        self._create_color_controls(controls)
        self._create_action_controls(controls)

    def _create_size_controls(self, parent: ttk.Frame) -> None:
        frame = ttk.LabelFrame(
            parent,
            text="Taille du pinceau",
            padding=10
        )
        frame.pack(fill="x", pady=(0, 10))

        self.size_label = ttk.Label(
            frame,
            text=f"{self.brush_size} px"
        )
        self.size_label.pack(side="right")

        self.size_slider = tk.Scale(
            frame,
            from_=1,
            to=50,
            orient="horizontal",
            showvalue=False,
            command=self._change_brush_size
        )
        self.size_slider.set(self.brush_size)
        self.size_slider.pack(fill="x")

    def _create_color_controls(self, parent: ttk.Frame) -> None:
        frame = ttk.LabelFrame(
            parent,
            text="Couleur du pinceau",
            padding=10
        )
        frame.pack(fill="x", pady=(0, 10))

        colors = [
            ("Noir", "black"),
        ]

        for name, color in colors:
            button = tk.Button(
                frame,
                text=name,
                bg=color,
                fg="white",
                width=8,
                command=lambda c=color: self._set_color(c)
            )
            button.pack(side="left", padx=3)

        self.color_preview = tk.Label(
            frame,
            text="  ",
            bg=self.brush_color,
            relief="solid",
            borderwidth=1
        )
        self.color_preview.pack(side="right")

    def _create_action_controls(self, parent: ttk.Frame) -> None:
        frame = ttk.Frame(parent)
        frame.pack(fill="x")

        tk.Button(
            frame,
            text="Tout effacer",
            width=15,
            command=self._clear
        ).pack(side="left", padx=3)

        tk.Button(
            frame,
            text="Gomme",
            width=15,
            command=self._activate_eraser
        ).pack(side="left", padx=3)

        tk.Button(
            frame,
            text="Envoyer",
            width=15,
            command=self._send
        ).pack(side="right", padx=3)

    def _start_draw(self, event: tk.Event) -> None:
        self.last_x = event.x
        self.last_y = event.y
        self._draw_point(event.x, event.y)

    def _draw(self, event: tk.Event) -> None:
        if self.last_x is None or self.last_y is None:
            return

        self.canvas.create_line(
            self.last_x,
            self.last_y,
            event.x,
            event.y,
            fill=self.brush_color,
            width=self.brush_size,
            capstyle=tk.ROUND,
            joinstyle=tk.ROUND
        )

        self.last_x = event.x
        self.last_y = event.y

    def _stop_draw(self, event: tk.Event) -> None:
        self.last_x = None
        self.last_y = None

    def _draw_point(self, x: int, y: int) -> None:
        radius = self.brush_size / 2

        self.canvas.create_oval(
            x - radius,
            y - radius,
            x + radius,
            y + radius,
            fill=self.brush_color,
            outline=self.brush_color
        )

    def _change_brush_size(self, value: str) -> None:
        self.brush_size = int(float(value))
        self.size_label.config(text=f"{self.brush_size} px")

    def _set_color(self, color: str) -> None:
        self.brush_color = color
        self.color_preview.config(bg=color)

    def _choose_color(self) -> None:
        color = colorchooser.askcolor(
            title="Choisir une couleur",
            initialcolor=self.brush_color
        )

        if color[1] is not None:
            self._set_color(color[1])

    def _activate_eraser(self) -> None:
        self.brush_color = "white"
        self.color_preview.config(bg="white")

    def _clear(self) -> None:
        self.canvas.delete("all")

    def _get_image(self) -> str:
        x = self.root.winfo_rootx() + self.canvas.winfo_x()
        y = self.root.winfo_rooty() + self.canvas.winfo_y()

        x2 = x + self.canvas.winfo_width()
        y2 = y + self.canvas.winfo_height()

        image = ImageGrab.grab((x, y, x2, y2))

        with tempfile.NamedTemporaryFile(
            suffix=".png",
            delete=False
        ) as file:
            image.save(file.name)
            return file.name

    def _send(self) -> None:
        image_path = self._get_image()

        if self.onImageSend:
            self.onImageSend(image_path)
        else:
            print("No image send function provided.")

    def run(self) -> None:
        self.root.mainloop()

if __name__ == "__main__":
    def on_image_send(image_path: str) -> None:
        print(f"Image sent: {image_path}")

    app = App(onImageSend=on_image_send, width=200, height=200)
    app.run()
