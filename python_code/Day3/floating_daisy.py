# -*- coding: utf-8 -*-
"""A draggable, always-on-top floating daisy for Windows."""

import math
import random
import tkinter as tk


class FloatingDaisyApp:
    """Draw and manage the borderless floating daisy window."""

    WIDTH = 380
    HEIGHT = 260
    SKY_BLUE = "#BFE8F7"

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("悬浮小雏菊")
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)
        self.root.configure(bg=self.SKY_BLUE)
        self.root.resizable(False, False)

        # Start near the top-center of the primary screen.
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        start_x = max(0, (screen_width - self.WIDTH) // 2)
        start_y = max(0, min(8, screen_height - self.HEIGHT - 8))
        self.root.geometry(
            f"{self.WIDTH}x{self.HEIGHT}+{start_x}+{start_y}"
        )

        self.canvas = tk.Canvas(
            self.root,
            width=self.WIDTH,
            height=self.HEIGHT,
            bg=self.SKY_BLUE,
            bd=0,
            highlightthickness=0,
        )
        self.canvas.pack(fill="both", expand=True)

        self.drag_mouse_x = 0
        self.drag_mouse_y = 0
        self.drag_window_x = 0
        self.drag_window_y = 0
        self.sparkles = []
        self.animation_step = 0

        self._draw_scene()
        self._bind_controls()
        self._animate_sparkles()
        self._keep_on_top()

    def _bind_controls(self):
        """Enable left-button dragging and right-button exit."""
        for widget in (self.root, self.canvas):
            widget.bind("<ButtonPress-1>", self._start_drag)
            widget.bind("<B1-Motion>", self._drag_window)
            widget.bind("<Button-3>", self._exit_app)

        # Escape is a convenient backup exit key.
        self.root.bind("<Escape>", self._exit_app)

    def _start_drag(self, event):
        self.drag_mouse_x = event.x_root
        self.drag_mouse_y = event.y_root
        self.drag_window_x = self.root.winfo_x()
        self.drag_window_y = self.root.winfo_y()

    def _drag_window(self, event):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        new_x = self.drag_window_x + event.x_root - self.drag_mouse_x
        new_y = self.drag_window_y + event.y_root - self.drag_mouse_y

        new_x = max(0, min(new_x, screen_width - self.WIDTH))
        new_y = max(0, min(new_y, screen_height - self.HEIGHT))

        self.root.geometry(f"+{new_x}+{new_y}")

    def _exit_app(self, _event=None):
        self.root.destroy()

    def _keep_on_top(self):
        """Reassert the topmost state periodically."""
        self.root.attributes("-topmost", True)
        self.root.after(1500, self._keep_on_top)

    def _draw_scene(self):
        """Draw sparkles, stem, leaves, petals, and flower center."""
        self._draw_sparkles()

        # Soft ground shadow.
        self.canvas.create_oval(
            142, 232, 238, 246,
            fill="#9FCED9",
            outline="",
        )

        # Stem, placed behind the flower.
        self.canvas.create_line(
            190, 104, 187, 231,
            fill="#3F914C",
            width=9,
            smooth=True,
            capstyle=tk.ROUND,
        )
        self.canvas.create_line(
            187, 115, 184, 230,
            fill="#68B85B",
            width=4,
            smooth=True,
            capstyle=tk.ROUND,
        )

        # Left and right leaves.
        self.canvas.create_polygon(
            187, 171,
            166, 153,
            135, 157,
            151, 181,
            184, 190,
            fill="#5DAF55",
            outline="#398447",
            width=2,
            smooth=True,
            splinesteps=24,
        )
        self.canvas.create_line(
            181, 183, 145, 162,
            fill="#A5D77D",
            width=2,
            smooth=True,
        )
        self.canvas.create_polygon(
            188, 194,
            211, 174,
            246, 179,
            227, 205,
            189, 214,
            fill="#65B95B",
            outline="#398447",
            width=2,
            smooth=True,
            splinesteps=24,
        )
        self.canvas.create_line(
            194, 207, 235, 184,
            fill="#A5D77D",
            width=2,
            smooth=True,
        )

        # White petals with subtle blue-grey outlines.
        flower_x, flower_y = 190, 92
        for index in range(18):
            angle = -math.pi / 2 + index * (2 * math.pi / 18)
            length = 65 if index % 2 == 0 else 58
            width = 25 if index % 2 == 0 else 22
            points = self._petal_points(
                flower_x, flower_y, angle, length, width
            )
            self.canvas.create_polygon(
                points,
                fill="#FFFDF7",
                outline="#D7E7EA",
                width=2,
                smooth=True,
                splinesteps=24,
            )

        # Golden center with warm shading and highlights.
        self.canvas.create_oval(
            158, 60, 222, 124,
            fill="#E6A51B",
            outline="#C98212",
            width=3,
        )
        self.canvas.create_oval(
            164, 64, 217, 117,
            fill="#F6C933",
            outline="",
        )
        self.canvas.create_oval(
            173, 69, 188, 84,
            fill="#FFE982",
            outline="",
        )

        # Tiny center texture.
        texture_rng = random.Random(17)
        for _ in range(22):
            angle = texture_rng.random() * 2 * math.pi
            radius = math.sqrt(texture_rng.random()) * 22
            x = flower_x + math.cos(angle) * radius
            y = flower_y + math.sin(angle) * radius
            dot_radius = texture_rng.choice((1.2, 1.5, 2.0))
            color = texture_rng.choice(
                ("#D99416", "#E9AA18", "#FFD956", "#FFF09B")
            )
            self.canvas.create_oval(
                x - dot_radius,
                y - dot_radius,
                x + dot_radius,
                y + dot_radius,
                fill=color,
                outline="",
            )

    @staticmethod
    def _petal_points(cx, cy, angle, length, width):
        """Return a smooth, leaf-like petal polygon rotated around its center."""
        ux, uy = math.cos(angle), math.sin(angle)
        px, py = -uy, ux

        def point(forward, sideways):
            return (
                cx + ux * forward + px * sideways,
                cy + uy * forward + py * sideways,
            )

        return [
            *point(8, 2),
            *point(24, width * 0.48),
            *point(length * 0.72, width * 0.43),
            *point(length, 0),
            *point(length * 0.72, -width * 0.43),
            *point(24, -width * 0.48),
            *point(8, -2),
        ]

    def _draw_sparkles(self):
        """Create randomly positioned light points in the blue background."""
        rng = random.Random()
        for _ in range(30):
            x = rng.randint(18, self.WIDTH - 18)
            y = rng.randint(12, self.HEIGHT - 18)

            # Keep most points outside the flower's central area.
            if (x - 190) ** 2 + (y - 92) ** 2 < 72 ** 2:
                continue

            base_radius = rng.uniform(1.2, 3.2)
            sparkle_id = self.canvas.create_oval(
                x - base_radius,
                y - base_radius,
                x + base_radius,
                y + base_radius,
                fill="#FFFFFF",
                outline="",
            )
            self.sparkles.append(
                {
                    "id": sparkle_id,
                    "x": x,
                    "y": y,
                    "radius": base_radius,
                    "phase": rng.uniform(0, 2 * math.pi),
                    "speed": rng.uniform(0.06, 0.13),
                }
            )

    def _animate_sparkles(self):
        """Gently pulse the random light points."""
        self.animation_step += 1
        colors = ("#DDF8FF", "#ECFBFF", "#FFFFFF", "#FFF7C7")

        for sparkle in self.sparkles:
            pulse = 0.68 + 0.32 * math.sin(
                sparkle["phase"] + self.animation_step * sparkle["speed"]
            )
            radius = max(0.7, sparkle["radius"] * pulse)
            x, y = sparkle["x"], sparkle["y"]
            self.canvas.coords(
                sparkle["id"],
                x - radius,
                y - radius,
                x + radius,
                y + radius,
            )
            color_index = min(
                len(colors) - 1,
                max(0, int(pulse * len(colors))),
            )
            self.canvas.itemconfigure(
                sparkle["id"],
                fill=colors[color_index],
            )

        self.root.after(70, self._animate_sparkles)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    FloatingDaisyApp().run()
