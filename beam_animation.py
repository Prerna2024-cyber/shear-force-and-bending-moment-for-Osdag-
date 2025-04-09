from manim import *

class MovingLoad(Scene):
    def construct(self):
        # Parameters
        L = 6
        x = 2
        a = 3
        W1 = 4
        W2 = 3

        # Beam and Supports
        beam = Line(LEFT*3, RIGHT*3, color=BLUE, stroke_width=8)
        support_A = Triangle(fill_opacity=1, color=RED).scale(0.3).next_to(beam.get_start(), DOWN, buff=0)
        support_B = Circle(fill_opacity=1, color=RED).scale(0.3).next_to(beam.get_end(), DOWN, buff=0)
        label_A = Tex("A").scale(0.6).next_to(support_A, DOWN, buff=0.1)
        label_B = Tex("B").scale(0.6).next_to(support_B, DOWN, buff=0.1)
        label_L = MathTex("L = 6m").scale(0.6).next_to(beam, DOWN, buff=0.3)

        # Weights (corrected based on symbolic positions)
        w1_pos = beam.get_start() + RIGHT * a           # W1 is 'a' units from A
        w2_pos = beam.get_start() + RIGHT * (a + x)     # W2 is at 'a + x' from A

        arrow_W1 = Arrow(w1_pos + UP*1.5, w1_pos, color=GREEN, buff=0).scale(0.6)
        arrow_W2 = Arrow(w2_pos + UP*1.1, w2_pos, color=GREEN, buff=0).scale(0.6)

        label_W1 = MathTex("W_1 = 4kN").scale(0.6).next_to(arrow_W1, UP, buff=0.2)
        label_W2 = MathTex("W_2 = 3kN").scale(0.6).next_to(arrow_W2, UP, buff=0.2)
        
        # Reaction forces
        reaction_A = Arrow(DOWN, UP*0.6, color=RED).next_to(support_A, DOWN, buff=0)
        reaction_B = Arrow(DOWN, UP*0.6, color=RED).next_to(support_B, DOWN, buff=0)
        label_RA = MathTex("R_A").scale(0.6).next_to(reaction_A, DOWN)
        label_RB = MathTex("R_B").scale(0.6).next_to(reaction_B, DOWN)
        # Horizontal reaction force at pinned support A
        reaction_Ax = Arrow(LEFT, RIGHT * 0.5, color=RED).next_to(support_A, LEFT, buff=0.05)
        label_RAx = MathTex("R_{Ax}").scale(0.6).next_to(reaction_Ax, LEFT)

        # Beam Group
        beam_group = VGroup(
            beam, support_A, support_B, label_A, label_B, label_L,
            arrow_W1, arrow_W2, label_W1, label_W2,
            reaction_A, reaction_B, label_RA, label_RB,
            reaction_Ax, label_RAx  # Add horizontal reaction
        ).scale(0.9).to_corner(RIGHT).shift(DOWN*0.5)

        # Show beam setup
        self.play(Create(beam), Create(support_A), Create(support_B))
        self.play(Write(label_A), Write(label_B), Write(label_L))
        self.play(GrowArrow(arrow_W1), GrowArrow(arrow_W2), Write(label_W1), Write(label_W2))
        self.play(GrowArrow(reaction_A), GrowArrow(reaction_B), Write(label_RA), Write(label_RB))
        self.play(GrowArrow(reaction_Ax), Write(label_RAx))  # Animate horizontal reaction
        self.wait(0.5)

        # Steps - aligned left using general variables
        step1 = Tex("1. Take moments about A:").scale(0.6)
        step1_calc = MathTex(
                              r"\sum M_A = 0", 
                              r"\Rightarrow R_B \cdot L - W_1 \cdot a - W_2 \cdot (a + x) = 0"
                            ).scale(0.6)

        step2 = Tex("2. Solve for $R_B$:").scale(0.6)
        step2_calc = MathTex(
                             r"R_B = \frac{W_1 \cdot a + W_2 \cdot (a + x)}{L}"
                            ).scale(0.6)
        
        step3 = Tex("3. Vertical equilibrium:").scale(0.6)
        step3_calc = MathTex(
                            r"\sum F_y = 0", 
                            r"\Rightarrow R_A + R_B - W_1 - W_2 = 0"
                            ).scale(0.6)

        step4 = Tex("4. Solve for $R_A$:").scale(0.6)
        step4_calc = MathTex(
                             r"R_A = W_1 + W_2 - R_B"
                            ).scale(0.6)
        steps_group = VGroup(
            step1, step1_calc, step2, step2_calc,
            step3, step3_calc, step4, step4_calc
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).scale(0.9).to_corner(UL)

        # Animate steps
        for item in steps_group:
            self.play(Write(item))
            self.wait(0.4)

        # Final boxed result
        final = VGroup(
            Tex("Final Reactions:", color=YELLOW).scale(0.7),
            MathTex("R_A = 4.5\\,kN").scale(0.6),
            MathTex("R_B = 2.5\\,kN").scale(0.6)
        ).arrange(DOWN).scale(0.9)

        box = SurroundingRectangle(final, color=YELLOW, buff=0.3)
        final_group = VGroup(final, box).to_corner(DR).shift(UP*0.3)

        self.play(Create(box), FadeIn(final))


         # NEW PAGE for SFD & BMD
        self.clear()
                # Title stays at top
        title = Tex("Shear Force and Bending Moment Diagrams").scale(0.8).to_edge(UP)

      

        # Axes for SFD and BMD
        sfd_axes = Axes(
            x_range=[0, L, 1],
            y_range=[-5, 5, 1],
            x_length=6,
            y_length=3,
            axis_config={"include_tip": False},
        ).to_edge(LEFT).shift(DOWN * 0.5)
        sfd_label = Tex("SFD").scale(0.6).next_to(sfd_axes, UP)

        bmd_axes = Axes(
            x_range=[0, L, 1],
            y_range=[-10, 10, 2],
            x_length=6,
            y_length=3,
            axis_config={"include_tip": False},
        ).to_edge(RIGHT).shift(DOWN * 0.5)
        bmd_label = Tex("BMD").scale(0.6).next_to(bmd_axes, UP)

        self.play(Create(sfd_axes), Write(sfd_label), Create(bmd_axes), Write(bmd_label))
        self.wait(1)

        # Beam points
        beam_points = [0, 2, 3, 6]
        sfd_values = [4.5, 0.5, -2.5, 0]
        bmd_values = [0, 7, 8.5, 0]

        # STEP-BY-STEP SFD BUILD
        sfd_segments = VGroup()
        for i in range(len(beam_points) - 1):
            x_vals = [beam_points[i], beam_points[i + 1]]
            y_vals = [sfd_values[i], sfd_values[i + 1]]
            
            # Explain each segment
            explanation = Tex(
                f"From x = {x_vals[0]} to {x_vals[1]}: SFD changes from {y_vals[0]} to {y_vals[1]}"
            )
            explanation.scale(0.5).to_corner(DR)
            self.play(Write(explanation))

            # Draw segment
            segment = sfd_axes.plot_line_graph(
                x_values=x_vals,
                y_values=y_vals,
                line_color=BLUE,
                vertex_dot_radius=0.05
            )
            self.play(Create(segment))
            sfd_segments.add(segment)

            # Moving dot to highlight current point
            dot = Dot(sfd_axes.c2p(x_vals[1], y_vals[1]), color=YELLOW)
            self.play(FadeIn(dot), run_time=0.3)
            self.wait(0.5)
            self.play(FadeOut(dot), FadeOut(explanation), run_time=0.3)

        self.wait(1)

        # STEP-BY-STEP BMD BUILD
        bmd_segments = VGroup()
        for i in range(len(beam_points) - 1):
            x_vals = [beam_points[i], beam_points[i + 1]]
            y_vals = [bmd_values[i], bmd_values[i + 1]]

            explanation = Tex(
                f"From x = {x_vals[0]} to {x_vals[1]}: BMD changes from {y_vals[0]} to {y_vals[1]}"
            )
            explanation.scale(0.5).to_corner(DR)
            self.play(Write(explanation))

            segment = bmd_axes.plot_line_graph(
                x_values=x_vals,
                y_values=y_vals,
                line_color=GREEN,
                vertex_dot_radius=0.05
            )
            self.play(Create(segment))
            bmd_segments.add(segment)

            dot = Dot(bmd_axes.c2p(x_vals[1], y_vals[1]), color=ORANGE)
            self.play(FadeIn(dot), run_time=0.3)
            self.wait(0.5)
            self.play(FadeOut(dot), FadeOut(explanation), run_time=0.3)

        self.wait(2)

        
