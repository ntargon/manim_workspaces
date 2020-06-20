from manimlib.imports import *

class BubbleSort(Scene):
    def construct(self):

        txt = TextMobject("Bubble Sort")
        txt.to_edge(UP)
        self.play(Write(txt))

        n = 40
        bar_width = 0.1
        bar_height = 4/n
        rects = [ Rectangle(width=bar_width, height=bar_height*(i+1), stroke_color=WHITE, stroke_width=0.1, fill_opacity=1, color=WHITE) for i in range(n) ]
        VGroup(*rects).arrange(RIGHT, aligned_edge=BOTTOM, buff=0.01)

        self.add(*rects)


        def swap_x(r1, r2, run_time=1):
            r1.generate_target()
            r2.generate_target()
            r1.target.shift((r2.get_x() - r1.get_x())*RIGHT)
            r2.target.shift((r1.get_x() - r2.get_x())*RIGHT)

            self.play(
                MoveToTarget(r1),
                MoveToTarget(r2),
                run_time=run_time,
            )

        # randomize
        rect_id = list(range(n)) # rect_id[i] th rectangle is in the i-th position.
        random.shuffle(rect_id)
        for i, j in enumerate(rect_id):
            rects[j].generate_target()
            rects[j].target.shift((rects[i].get_x() - rects[j].get_x())*RIGHT)

        for rect in rects:
            rect.move_to(rect.target.get_center())

        self.wait(1)



        for i in reversed(range(1,n)):
            rects[rect_id[0]].set_color(RED)
            for j in range(i):
                if rects[rect_id[j]].height > rects[rect_id[j+1]].height:
                    swap_x(rects[rect_id[j]], rects[rect_id[j+1]], run_time=0.05)
                    rect_id[j], rect_id[j+1] = rect_id[j+1], rect_id[j]
                else:
                    self.wait(0.05)
                    rects[rect_id[j]].set_color(WHITE)
                    rects[rect_id[j+1]].set_color(RED)

            rects[rect_id[i]].set_color(GREEN)
        rects[rect_id[0]].set_color(GREEN)

        self.wait()

