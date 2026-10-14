# -*- coding: utf-8 -*-
"""Day 3 附加小项目：悬浮小雏菊（tkinter 图形界面）
A draggable, always-on-top floating daisy for Windows.

导读（这个项目把 Day1-3 的技巧综合用起来了）：
1. 类（class）封装：窗口常量（宽高/配色）和全部逻辑都收进 FloatingDaisyApp，
   避免全局变量满天飞——Day 4 学函数后回头再看会更明白；
2. tkinter 无边框窗口：overrideredirect(True) 去掉标题栏，
   attributes("-topmost") 保持置顶；没了标题栏，拖动就得自己实现；
3. 事件绑定：bind("<ButtonPress-1>") 左键按下、<B1-Motion> 按住拖动、
   <Button-3> 右键退出——GUI 程序的本质就是"等事件发生再响应"；
4. 动画循环：after(70, 回调) 递归地给自己排下一次任务，
   约 14 帧/秒地让光点闪烁（不会卡死主循环）；
5. 数据结构实战：self.sparkles 是"字典组成的列表"，
   每个字典存一颗光点的 id/位置/相位/速度——数据驱动动画的雏形。

运行方式：python floating_daisy.py（左键拖动，右键或 Esc 退出）
"""

import math
import random
import tkinter as tk


class FloatingDaisyApp:
    """Draw and manage the borderless floating daisy window."""
    # 绘制与管理这个无边框悬浮窗口（类 = 数据 + 操作数据的函数 打包在一起）

    # 类属性（常量）：尺寸与主色调集中定义，改配色只改这一处
    WIDTH = 380
    HEIGHT = 260
    SKY_BLUE = "#BFE8F7"    # 颜色用 "#RRGGBB" 十六进制写法

    def __init__(self):
        # 构造方法：创建对象时自动执行，负责"搭好整个窗口"
        self.root = tk.Tk()                   # 创建主窗口
        self.root.title("悬浮小雏菊")
        self.root.overrideredirect(True)      # 去掉系统标题栏/边框（无边框窗口）
        self.root.attributes("-topmost", True)  # 窗口永远置顶
        self.root.configure(bg=self.SKY_BLUE)
        self.root.resizable(False, False)

        # Start near the top-center of the primary screen.
        # 初始位置：屏幕顶部居中；max/min 把坐标"钳制"在屏幕范围内，防出屏
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        start_x = max(0, (screen_width - self.WIDTH) // 2)
        start_y = max(0, min(8, screen_height - self.HEIGHT - 8))
        self.root.geometry(
            f"{self.WIDTH}x{self.HEIGHT}+{start_x}+{start_y}"
        )

        self.canvas = tk.Canvas(   # Canvas 画布：用几何图形"画"出小雏菊
            self.root,
            width=self.WIDTH,
            height=self.HEIGHT,
            bg=self.SKY_BLUE,
            bd=0,
            highlightthickness=0,
        )
        self.canvas.pack(fill="both", expand=True)

        self.drag_mouse_x = 0      # 拖动开始时记录鼠标位置与窗口位置，
        self.drag_mouse_y = 0      # 之后窗口新位置 = 原位置 + 鼠标位移，
        self.drag_window_x = 0     # 这样窗口不会"跳"到鼠标处，体验更自然
        self.drag_window_y = 0
        self.sparkles = []         # 背景光点列表：每个元素是一个字典（见 _draw_sparkles）
        self.animation_step = 0

        self._draw_scene()         # 一次性画好静态画面（花、叶子、光点）
        self._bind_controls()      # 绑定鼠标/键盘事件
        self._animate_sparkles()
        self._keep_on_top()

    def _bind_controls(self):
        """Enable left-button dragging and right-button exit."""
        # 左键按下→开始拖；按住移动→窗口跟随；右键→退出。
        # 主窗口和画布都要绑，因为鼠标可能停在任一控件上
        for widget in (self.root, self.canvas):
            widget.bind("<ButtonPress-1>", self._start_drag)
            widget.bind("<B1-Motion>", self._drag_window)
            widget.bind("<Button-3>", self._exit_app)

        # Escape is a convenient backup exit key.
        self.root.bind("<Escape>", self._exit_app)

    def _start_drag(self, event):
        # 按下左键的瞬间，拍个"快照"：鼠标在哪、窗口在哪
        self.drag_mouse_x = event.x_root
        self.drag_mouse_y = event.y_root
        self.drag_window_x = self.root.winfo_x()
        self.drag_window_y = self.root.winfo_y()

    def _drag_window(self, event):
        # 拖动中：窗口新位置 = 起点位置 + (鼠标当前位置 - 鼠标起点位置)
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        new_x = self.drag_window_x + event.x_root - self.drag_mouse_x
        new_y = self.drag_window_y + event.y_root - self.drag_mouse_y

        # 边界钳制：新坐标不许超出屏幕（与 __init__ 里同样的 max/min 技巧）
        new_x = max(0, min(new_x, screen_width - self.WIDTH))
        new_y = max(0, min(new_y, screen_height - self.HEIGHT))

        self.root.geometry(f"+{new_x}+{new_y}")  # "+x+y" 语法移动窗口位置

    def _exit_app(self, _event=None):
        # destroy 销毁窗口，程序随之结束（参数前缀 _ 表示"用不到但必须接收"）
        self.root.destroy()

    def _keep_on_top(self):
        """Reassert the topmost state periodically."""
        # 有些程序会抢走置顶状态，所以每 1.5 秒重新声明一次置顶；
        # after(毫秒, 函数) 是 tkinter 的定时器，递归调用形成循环
        self.root.attributes("-topmost", True)
        self.root.after(1500, self._keep_on_top)

    def _draw_scene(self):
        """Draw sparkles, stem, leaves, petals, and flower center."""
        # 绘制顺序即图层顺序：先画的在下层（光点→影子→茎→叶→花瓣→花心）
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
        # 18 片花瓣绕花心均匀转一圈：每次角度递增 2π/18；
        # 奇偶花瓣长短/宽窄略有差异，看起来更像真花
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

    @staticmethod   # 静态方法：不依赖对象状态（用不到 self），纯数学计算
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
        # 随机撒 30 颗光点；每颗光点的属性用字典保存，动画时再逐颗取用
        rng = random.Random()
        for _ in range(30):
            x = rng.randint(18, self.WIDTH - 18)
            y = rng.randint(12, self.HEIGHT - 18)

            # Keep most points outside the flower's central area.
            # 光点离花心太近就跳过（用距离平方比较，省一次开方运算）
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
        # 动画核心：每颗光点有自己的相位(phase)和速度(speed)，
        # 用 sin 波算出当前"呼吸"强度 pulse∈[0.36,1]，同时调制半径和颜色
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

        self.root.after(70, self._animate_sparkles)  # 70ms 后再来一次，形成动画循环

    def run(self):
        self.root.mainloop()   # 进入事件主循环：程序从这里开始"活着"，直到窗口销毁


if __name__ == "__main__":
    # 只有"直接运行本文件"时才启动；被 import 时不会弹窗（Day 5 细讲）
    FloatingDaisyApp().run()
