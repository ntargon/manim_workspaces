from manimlib.imports import *

class KochCurve(Scene):
    def construct(self):
        txt = TextMobject("Koch Curve").to_edge(UP)
        self.play(Write(txt))

        n = 4
        r = 3
        theta = np.pi/6

        mbj1 = Mobject()
        for i in reversed(range(3)):
            mbj1.add(Line(self.compToPos(r*np.exp(1j*(theta + (np.pi*2/3*i)))), self.compToPos(r*np.exp(1j*(theta + (np.pi*2/3*(i-1)))))))
        self.play(FadeIn(mbj1))

        for i in range(n):
            mbj2 = self.step(mbj1)
            self.play(ReplacementTransform(mbj1, mbj2))
            mbj1 = mbj2

    def step(self, mbj):
        nxt_mbj = Mobject()

        for l in mbj:
            z0 = l.start[0] + l.start[1]*1j
            z1 = l.end[0] + l.end[1]*1j
            z = z1 - z0
            nxt_mbj.add(Line(self.compToPos(z0), self.compToPos(z0 + z/3)))
            nxt_mbj.add(Line(self.compToPos(z0 + z/3), self.compToPos(z0 + z/3*(1 + np.exp((np.pi/3)*1j)))))
            nxt_mbj.add(Line(self.compToPos(z0 + z/3*(1 + np.exp((np.pi/3)*1j))), self.compToPos(z0 + z*2/3)))
            nxt_mbj.add(Line(self.compToPos(z0 + z*2/3), self.compToPos(z1)))

        return nxt_mbj

    def compToPos(self, z):
        return (z.real, z.imag, 0)