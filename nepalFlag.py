from manim import *    
   
class MAIN(Scene):
    def construct(self):
        ########################## section # 1 ###########################
        ################## Making the inside border ######################
        # step 1
        """
        (1) On the lower portion of a crimson cloth draw a line AB of the required length from left to right.
        """
        Step=Text("(1) On the lower portion of a crimson cloth draw a line AB")
        Step.move_to([-1.5,3.25,0])
        Step.scale(0.5)
        self.play(FadeIn(Step))

        sw = 1.4
        pointA = Dot(radius=0.1)
        pointA.move_to([-2, 0, 0])

        pointB = Dot(radius=0.1)
        pointB.move_to([2, 0, 0])

        labelA = Text("A")
        labelA.next_to(pointA, LEFT) # Position the label left of the point
        
        labelB = Text("B")
        labelB.next_to(pointB, RIGHT) # Position the label right of the point

        lineA_B = Line(start=[-2, 0, 0], end=[+2, 0, 0], color=RED, stroke_width=sw)

        self.play(Create(lineA_B), run_time=2)
        self.play(Create(pointA), Create(pointB), run_time=1.5)
        self.play(Write(labelA), run_time=1.2)
        self.play(Write(labelB), run_time=1.2)

        self.wait(1) # wait for 1 second // default is 1

        self.play(labelA.animate.scale(0.6), labelB.animate.scale(0.6))

        animations = [pointA.animate.move_to([-2,-3,0]),
                        pointB.animate.move_to([2,-3,0]),
                        labelA.animate.move_to([-2.5,-3,0]),
                        labelB.animate.move_to([2.5,-3,0]),
                        lineA_B.animate.move_to([0,-3,0])]

        # actually playing the complete translation
        self.play(*animations) 
        self.play(FadeOut(Step))

        self.wait(2)

        # step 2
        """
        (2) From A draw a line AC perpendicular to AB making AC equal to AB plus one third AB. From AC mark off D making the line AD equal to line AB. Join BD.
        """
        Step=Text("(2) From A draw a line AC perpendicular to AB\n making AC equal to AB plus one third AB.\n From AC mark off D making the line AD equal to line AB. Join BD.")
        Step.move_to([0,3.25,0])
        Step.scale(0.5)
        self.play(FadeIn(Step))

        # constructing bisector
        # move label A out of the way
        self.play(labelA.animate.move_to([[-2,-3.4,0]]))
        
        # extending line leftwards
        LineA_Aprime = DashedLine(start=[-6, -3, 0], end=[-2, -3, 0], color=RED, dash_length=0.1, stroke_width=1)

        pointA1 = Dot(radius=0.1)
        pointA1.move_to([-2,-3, 0])
        pointAprime = Dot(radius=0.1)
        pointAprime.move_to([-6, -3, 0])

        LabelAprime = Text("A\'")
        LabelAprime.scale(0.6)
        LabelAprime.next_to(pointAprime, UP) # Position the label above of the point

        self.play(Create(LineA_Aprime), Create(LabelAprime), Create(pointAprime), Create(pointA1))
        self.wait()

        # Create an arc
        arc_l = DashedVMobject(Arc(start_angle=0.50, angle=0.3, arc_center=[-6,-3,0],  radius=5, stroke_width=0.5))  # Arc from 0 to pi radians
        arc_r = DashedVMobject(Arc(start_angle=2.35, angle=0.3, arc_center=[+2,-3,0],  radius=5, stroke_width=0.5))  # Arc from 0 to pi radians

        # Show the arc on the screen
        self.play(Create(arc_l), Create(arc_r))
        pointCprime = Dot(radius=0.05)
        pointCprime.move_to([-2,0,0])
        self.play(Create(pointCprime))
        labelCprime = Text("C'")
        labelCprime.scale(0.6)
        labelCprime.next_to(pointCprime, LEFT)
        self.play(Write(labelCprime))
        self.wait(1)
        self.play(FadeOut(arc_l), FadeOut(arc_r), run_time=2)
        
        # fade unnecessary things out
        self.play(FadeOut(LineA_Aprime), FadeOut(pointAprime), FadeOut(LabelAprime), run_time=1)

        # show a line above A-B
        LineAtoCprime = Line(start=[-2,-3,0], end=[+2,-3,0], stroke_width=sw)
        self.play(Create(LineAtoCprime))

        # then remake points A and B over it
        Aredrawn = Dot(radius=0.1)
        Bredrawn = Dot(radius=0.1)
        Aredrawn.move_to([-2,-3,0])
        Bredrawn.move_to([+2,-3,0])
        self.play(Create(Aredrawn), Create(Bredrawn))
        self.wait()

        # rotates from A-B to A-C,
        self.play(Rotate(LineAtoCprime, angle=PI/2, axis=OUT, about_point=LineAtoCprime.get_start()), run_time=2, clockwise_path=True)
        self.play(ApplyMethod(LineAtoCprime.set_color, RED), run_time=1)
        self.play(ApplyMethod(LineAtoCprime.put_start_and_end_on, [-2, -3, 0], [-2, (4 * (4/3) - 3), 0]), run_time=2)
        self.wait()
        self.play(FadeOut(pointCprime), FadeOut(labelCprime), run_time=1)

        # then is extended to C where on the left is says 1 1/3 rd
        pointC = Dot(radius=0.1)
        pointC.move_to([-2, (4 * (4/3) - 3), 0])
        labelC = Text("C")
        labelC.next_to(pointC, LEFT)
        self.play(Create(pointC), Create(labelC), run_time=1)
        self.play(labelC.animate.scale(0.6), run_time=1.2)

        # rotate AB on AC and mark of D
        LineAtoDprime = Line(start=[-2,-3,0], end=[+2,-3,0], stroke_width=sw)
        LineAtoDprime.set_color(BLUE)
        pointArere = Dot(radius=0.1)
        pointBrere = Dot(radius=0.1)
        pointArere.move_to([-2,-3,0])
        pointBrere.move_to([2,-3,0])
        self.play(Create(LineAtoDprime), Create(pointArere), Create(pointBrere), run_time=1)
        self.wait()
        self.play(Rotate(LineAtoDprime, angle=PI/2, axis=OUT, about_point=LineAtoCprime.get_start()), run_time=2, clockwise_path=True)
        pointD = Dot(radius=0.1)
        pointD.move_to([-2,1,0])
        self.play(Create(pointD), run_time=1)
        labelD = Text("D")
        labelD.next_to(pointD, LEFT)
        self.play(Create(labelD), runtime=1.2)
        self.play(labelD.animate.scale(0.6))
        self.play(FadeOut(LineAtoDprime))
        self.wait(2)
        LineB_D = Line(start=LineAtoDprime.get_end(), end=[+2,-3,0], stroke_width=sw)
        LineB_D.set_color(RED)
        pointDR = Dot(radius=0.1)
        pointBR = Dot(radius=0.1)
        pointDR.move_to([-2,1,0])
        pointBR.move_to([2,-3,0])
        self.play(Create(LineB_D), Create(pointBR), Create(pointDR))
        
        self.play(FadeOut(Step))
        self.wait(2)

        # step 3
        """
        (3) From BD mark off E making BE equal to AB.
        """
        Step=Text("(3) From BD mark off E making BE equal to AB.")
        Step.move_to([-1.5,3.25,0])
        Step.scale(0.5)
        self.play(FadeIn(Step))

        # make a line from B to A
        LineB_A = Line(start=[+2,-3,0], end=[-2,-3,0], stroke_width=sw)
        LineB_A.set_color(BLUE)
        pointAtop = Dot(radius=0.1)
        pointBtop = Dot(radius=0.1)
        pointAtop.move_to([-2,-3,0])
        pointBtop.move_to([2,-3,0])
        self.play(Create(LineB_A), Create(pointAtop), Create(pointBtop))

        # rotate line until it concides with BD,
        self.play(Rotate(LineB_A, angle=-PI/4, axis=OUT, about_point=LineB_A.get_start()), run_time=2)

        # mark E
        pointE = Dot(radius=0.07)
        pointE.move_to([-2 + 1.16,-3 + 2.85,0])
        self.play(Create(pointE))
        labelE = Text("E")
        labelE.move_to([-2 + 1.16,-3 + 2.52,0])
        labelE.scale(0.5)
        self.play(Write(labelE))

        # remove line
        self.play(FadeOut(LineB_A))
        self.play(FadeOut(Step))
        self.wait(2)

        # step 4
        """
        (4) Touching E draw a line FG, starting from the point F on line AC, parallel to AB to the right hand-side. Mark off FG equal to AB.
        """
        Step=Text("(4) Touching E draw a line FG, starting from the point F on line AC,\n parallel to AB to the right hand-side.\n Mark off FG equal to AB.")
        Step.move_to([-1.5,3.25,0])
        Step.scale(0.5)
        self.play(FadeIn(Step))

        # cut arcs from E on AC, above and below
        arc_top = DashedVMobject(Arc(start_angle=2, angle=0.4, arc_center=[-2 + 1.16,-3 + 2.85,0], radius=2, stroke_width=0.75))  # Arc from 0 to pi radians
        arc_bottom = DashedVMobject(Arc(start_angle=3.90, angle=0.4, arc_center=[-2 + 1.16,-3 + 2.85,0], radius=2, stroke_width=0.75))  # Arc from 0 to pi radians
        self.play(Create(arc_top), Create(arc_bottom), run_time=1)
        
        # make points at places of intersection
        pointup = Dot(radius=0.06)
        pointlow = Dot(radius=0.06)
        pointup.move_to([-2,-3 + 2.85 + 1.63,0])
        pointlow.move_to([-2,-3 + 2.85 -1.63,0])
        self.play(Create(pointup), Create(pointlow))

        # from those points make more arcs mark a point F prime
        arc_Top = DashedVMobject(Arc(start_angle=3.6, angle=0.4, arc_center=[-2,-3 + 2.85 + 1.63,0], radius=3, stroke_width=0.75))  # Arc from 0 to pi radians
        arc_Bottom = DashedVMobject(Arc(start_angle=2.30, angle=0.4, arc_center=[-2,-3 + 2.85 - 1.63,0], radius=3, stroke_width=0.75))  # Arc from 0 to pi radians
        self.play(Create(arc_Top), Create(arc_Bottom), run_time=1)
        pointEprime = Dot(radius=0.06)
        pointEprime.move_to([[-4.5,-3 + 2.85,0]])
        labelEprime = Text("E'")
        labelEprime.next_to(pointEprime, LEFT)
        labelEprime.scale(0.5)
        self.play(Create(pointEprime))
        self.play(Write(labelEprime))

        # from that point join a dashed line from f prime to e
        LineEprime_E = DashedLine(start=[-4.5,-3 + 2.85,0], end=[-2 + 1.16,-3 + 2.85,0], dash_length=0.1, stroke_width=1)
        self.play(Create(LineEprime_E))
        pointF = Dot(radius=0.1)
        pointF.move_to([-2,-3 + 2.85,0])
        labelF = Text("F")
        labelF.next_to(pointF, UP)
        labelF.move_to([-2.4,-0.21,0])
        self.play(Create(pointF))
        self.play(Write(labelF))
        self.play(FadeOut(arc_top), FadeOut(arc_bottom), FadeOut(arc_Bottom), FadeOut(arc_Top), FadeOut(pointup), FadeOut(pointlow))
        self.play(labelF.animate.scale(0.6))
        self.play(FadeOut(pointEprime), FadeOut(LineEprime_E), FadeOut(labelEprime))
        self.play(labelF.animate.move_to([-2.6,-0.21,0]))

        # pick a solid line from A to B and place it over F until G
        LinePICK = Line(start=[-2,-3,0], end=[2,-3,0], color=BLUE, stroke_width=sw)
        self.play(Create(LinePICK))
        self.play(LinePICK.animate.move_to([0,-3 + 2.85,0]))
        pointF_n = Dot(radius=0.1)
        pointF_n.move_to([-2,-3 + 2.85,0])
        pointE1 = Dot(radius=0.07)
        pointE1.move_to([-2 + 1.16,-3 + 2.85,0])
        self.play(Create(pointE1), Create(pointF_n))
        self.play(LinePICK.animate.set_color(RED))
        
        # make G
        pointG = Dot(radius=0.1)
        pointG.move_to([2,-3 + 2.85,0])
        labelG = Text("G")
        labelG.next_to(pointG, RIGHT)
        self.play(Create(pointG))
        self.play(Create(labelG))
        self.play(labelG.animate.scale(0.6))
        self.play(FadeOut(Step))
        self.wait(2)

        # step 5
        """
        (5) Join CG.
        """
        Step=Text("(5) Join CG.")
        Step.move_to([-1.5,3.25,0])
        Step.scale(0.5)
        self.play(FadeIn(Step))

        pointG1 = Dot(radius=0.1)
        pointG1.move_to([2,-3 + 2.85,0])
        pointC1 = Dot(radius=0.1)
        pointC1.move_to([-2, (4 * (4/3) - 3), 0])
        LineC_G = Line(start=[-2, (4 * (4/3) - 3), 0],end=[2,-3 + 2.85,0], stroke_width=sw)
        LineC_G.set_color(RED)
        self.play(Create(LineC_G), Create(pointC1), Create(pointG1))
        self.play(FadeOut(Step))
        self.wait(2)

        ########################## section # 2 ###########################
        ######################## Making the Moon #########################

        # step 6
        """
        (6) From AB mark off AH making AH equal to one-fourth of line AB and starting from H draw a line HI parallel to line AC touching line CG at point I. 
        """
        Step=Text("(6) From AB mark off AH making AH equal to one-fourth of line AB \nand starting from H draw a line HI parallel to line AC\n touching line CG at point I.")
        Step.move_to([-1.5,3.25,0])
        Step.scale(0.5)
        self.play(FadeIn(Step))
        
        # bisect A B an get some point
        arcLEFT = DashedVMobject(Arc(start_angle=0.6, angle=0.4, arc_center=[-2, -3, 0], radius=3, stroke_width=0.75))  # Arc from 0 to pi radians
        arcRIGHT = DashedVMobject(Arc(start_angle=2.1, angle=0.4, arc_center=[+2, -3, 0], radius=3, stroke_width=0.75))  # Arc from 0 to pi radians
        self.play(Create(arcLEFT), Create(arcRIGHT), run_time=1)
        bisectpoint = Dot(radius=0.05)
        bisectpoint.move_to([0,-3+2.23,0])
        self.play(Create(bisectpoint))
        bisectline = DashedLine(start=[0,-3+2.23,0], end=[0,-3,0], dash_length=0.1, stroke_width=1)
        self.play(Create(bisectline))
        bisectpoint1 = Dot(radius=0.05)
        bisectpoint1.move_to([0,-3,0])
        self.play(Create(bisectpoint1))
        self.wait(2)
        self.play(FadeOut(bisectline), FadeOut(arcLEFT), FadeOut(arcRIGHT), FadeOut(bisectpoint))
 
        # bisect A and that point again to get H
        arcLEFT1 = DashedVMobject(Arc(start_angle=0.8, angle=0.4, arc_center=[-2, -3, 0], radius=2, stroke_width=0.75))  # Arc from 0 to pi radians
        arcRIGHT1 = DashedVMobject(Arc(start_angle=1.9, angle=0.4, arc_center=[0, -3, 0], radius=2, stroke_width=0.75))  # Arc from 0 to pi radians
        self.play(Create(arcLEFT1), Create(arcRIGHT1), run_time=1)
        bisectpoint2 = Dot(radius=0.05)
        bisectpoint2.move_to([-1,-3+1.732,0])
        self.play(Create(bisectpoint2))
        bisectline2 = DashedLine(start=[-1,-3+1.732,0], end=[-1,-3,0], dash_length=0.1, stroke_width=1)
        self.play(Create(bisectline2))
        bisectpoint3 = Dot(radius=0.06)
        bisectpoint3.move_to([-1,-3,0])
        self.play(Create(bisectpoint3))
        self.wait(2)
        self.play(FadeOut(bisectline2), FadeOut(arcLEFT1), FadeOut(arcRIGHT1))
        self.play(FadeOut(bisectpoint1))
        labelH = Text("H")
        labelH.move_to([-1,-3.4, 0])
        self.play(Write(labelH))
        self.play(labelH.animate.scale(0.6))

        # extend H parallel to AC until you get to CG, and mark I.
        LineH_I = DashedLine(start=[-1,-3,0], end=[-1,1.675,0], color=RED, dash_length=0.1, stroke_width=sw)
        LineH_I.set_color(RED)
        self.play(Create(LineH_I))
        self.play(FadeOut(bisectpoint2))
        pointI=Dot(radius=0.05)
        pointI.move_to([-1,1.68,0])
        self.play(Create(pointI))
        labelI=Text("I")
        labelI.move_to([-1,2,0])
        self.play(Write(labelI))
        self.play(labelI.animate.scale(0.6))
        self.play(labelI.animate.move_to([-1,2.15,0]))
        self.play(FadeOut(Step))
        self.wait(2)

        # step 7
        """
        (7) Bisect CF at J and draw a line JK parallel to AB touching CG at point K. 
        """
        Step=Text("(7) Bisect CF at J and draw a line JK parallel to AB touching CG at point K.")
        Step.move_to([-1.5,3.25,0])
        Step.scale(0.5)
        self.play(FadeIn(Step))
        
        # wait more
        # create arcs over AC on the left side
        arctop2 = DashedVMobject(Arc(start_angle=3.64, angle=0.4, arc_center=[-2, -3 + 4 + 4/3, 0], radius=1.90, stroke_width=0.75))  # Arc from 0 to pi radians
        arcbottom2 = DashedVMobject(Arc(start_angle=2.18, angle=0.4, arc_center=[-2, -3 + 2 + 2/3, 0], radius=2, stroke_width=0.75))  # Arc from 0 to pi radians
        self.play(Create(arctop2), Create(arcbottom2), run_time=1)
        bisectpoint4 = Dot(radius=0.05)
        bisectpoint4.move_to([-2-1.56+0.15,1.083,0])
        self.play(Create(bisectpoint4))
        self.play(FadeOut(arcbottom2), FadeOut(arctop2))
    
        # reduce size of D point
        self.play(labelD.animate.scale(0.65))
        self.play(labelD.animate.move_to([-2-0.3,0.8,0]))
        self.play(pointD.animate.scale(0.4), pointDR.animate.scale(0.2))

        # create point at bisection, make dashed line until CG
        LineBisector = DashedLine(start=[-2-1.56+0.1,1.08,0], end=[0,1.08,0], color=RED, dash_length=0.1, stroke_width=sw)
        self.play(Create(LineBisector))

        # make point where the dashed line intersects AC and CG
        pointJ = Dot(radius=0.03, z_index=1)
        pointK = Dot(radius=0.04)
        pointJ.move_to([-2,1.1,0])
        pointK.move_to(LineBisector.get_end())
        LineBisector2 = DashedLine(start=[-2,1.08,0], end=[0,1.08,0], color=RED, dash_length=0.1, stroke_width=sw)
        self.play(FadeOut(LineBisector), FadeOut(bisectpoint4), Create(LineBisector2))
        self.play(Create(pointJ), Create(pointK))

        # name this point J and K (small)
        labelJ = Text("J")
        labelK = Text("K")
        labelJ.move_to([-2.3,1.3,0])
        labelK.next_to(pointK, UP)
        labelJ.scale(0.5)
        labelK.scale(0.5)
        self.play(Write(labelJ), Write(labelK))
        self.play(FadeOut(Step))

        self.wait(2)

        # step 8
        """
        (8) Let L be the point where lines JK and HI cut one another.
        """
        Step=Text("(8) Let L be the point where lines JK and HI cut one another.")
        Step.move_to([-1.5,3.25,0])
        Step.scale(0.5)
        self.play(FadeIn(Step))
        
        # make point
        pointL = Dot(radius=0.03)
        pointL.set_color(GREEN)
        pointL.move_to([-2+1,1.1,0])
        self.play(Create(pointL))

        # assign label L
        labelL = Text("L")
        labelL.scale(0.6)
        labelL.move_to([-2+0.8,1.3,0])
        self.play(Write(labelL))

        self.wait()

        # move label on the bottom left as L
        self.play(labelL.animate.set_color(GREEN))
        self.play(labelL.animate.move_to([-2+0.8,1.25,0]))
        self.play(labelL.animate.scale(0.7))
        self.play(FadeOut(Step))

        self.wait()

        # step 9
        """
        (9) Join J and G. 
        """
        Step=Text("(9) Join J and G.")
        Step.move_to([-1.5,3.25,0])
        Step.scale(0.5)
        self.play(FadeIn(Step))
        
        LineJG = DashedLine(pointJ.get_center(),pointG.get_center(), color=RED, dash_length=0.1, stroke_width=sw, z_index=0)
        self.play(Create(LineJG))
        self.play(FadeOut(Step))

        self.wait(2)

        # step 10
        """
        (10) Let M be the point where line JG and HI cut one another. 
        """
        Step=Text("(10) Let M be the point where line JG and HI cut one another.")
        Step.move_to([-1.5,3.25,0])
        Step.scale(0.5)
        self.play(FadeIn(Step))

        pointM=Dot(radius=0.04)
        pointM.move_to([-1,0.79,0])
        self.play(Create(pointM))
        labelM=Text("M")
        labelM.move_to([-0.78,-3+3.90,0])
        labelM.scale(0.5)
        self.play(Write(labelM))
        self.play(labelM.animate.scale(0.7))
        self.play(FadeOut(Step))

        self.wait()

        # step 11
        """
        (11) With centre M and with a distance shortest from M to BD mark off N on the lower portion of line HI.
        """
        Step=Text("(11) With centre M and with a distance shortest from M to BD mark off N\n on the lower portion of line HI.")
        Step.move_to([-1.5,3.25,0])
        Step.scale(0.5)
        self.play(FadeIn(Step))

        # cut arcs on BD
        arctop3 = DashedVMobject(Arc(start_angle=3.0, angle=0.4, arc_center=[-1,0.79,0], radius=0.75, stroke_width=2))  # Arc from 0 to pi radians
        arcbottom3 = DashedVMobject(Arc(start_angle=4.4, angle=0.4, arc_center=[-1,0.79,0], radius=0.75, stroke_width=2))  # Arc from 0 to pi radians
        self.play(Create(arctop3), Create(arcbottom3), run_time=1)
        pointbisector1 = Dot(radius=0.03)
        pointbisector2 = Dot(radius=0.03)
        pointbisector1.move_to([-2+0.25,0.74,0])
        pointbisector2.move_to([-1-0.04,0.03,0])
        self.play(Create(pointbisector2), Create(pointbisector1))
        
        self.wait(1)

        # from those arcs cut, two more arcs to find bisector
        arctop4 = DashedVMobject(Arc(start_angle=3.85, angle=0.4, arc_center=pointbisector1.get_center(), radius=3.75, stroke_width=2))  # Arc from 0 to pi radians
        arcbottom4 = DashedVMobject(Arc(start_angle=3.65, angle=0.4, arc_center=pointbisector2.get_center(), radius=3.75, stroke_width=2))  # Arc from 0 to pi radians
        self.play(Create(arctop4), Create(arcbottom4), run_time=1)
        pointbisector3=Dot(radius=0.05)
        pointbisector3.move_to([-4.02,-2.25,0])
        self.play(Create(pointbisector3))
        self.play(FadeOut(arctop3), FadeOut(arcbottom3), FadeOut(pointbisector2), FadeOut(pointbisector1), FadeOut(arcbottom4), FadeOut(arctop4))

        # make bisector to M
        bisector_to_M = DashedLine(start=pointbisector3.get_center(), end=pointM.get_center(), color=RED, dash_length=0.1, stroke_width=sw, z_index=0)
        self.play(Create(bisector_to_M))
        pointNprime = Dot(radius=0.03)
        pointNprime.move_to([-1-0.374,0.395,0])
        self.play(Create(pointNprime))
        self.play(FadeOut(bisector_to_M), FadeOut(pointbisector3))
        linefromNprimetoM = Line(start=[-1-0.374,0.395,0], end=[-1,0.79,0], color=BLUE, z_index=0)
        self.play(Create(linefromNprimetoM))

        self.wait()

        # take distance and rotate until you cut N        
        self.play(FadeOut(pointNprime))
        self.play(Rotate(linefromNprimetoM, angle=PI/4, axis=OUT, about_point=[-1,0.79,0]), run_time=2)
        pointN = Dot(radius=0.03)
        pointN.move_to([-2+1,0.25,0])
        self.play(Create(pointN))
        self.play(FadeOut(linefromNprimetoM))
        labelN = Text("N")
        labelN.move_to([-2+1.2,0.25,0])
        labelN.scale(0.5)
        self.play(Write(labelN))
        self.play(labelN.animate.scale(0.7))
        self.play(FadeOut(Step))
        
        self.wait(2)
        # step 12
        """
        (12) Touching M and starting from O, a point on AC, draw a line from left to right parallel to AB. 
        """
        Step=Text("(12) Touching M and starting from O, a point on AC,\ndraw a line from left to right parallel to AB.")
        Step.move_to([-1.5,3.25,0])
        Step.scale(0.5)
        self.play(FadeIn(Step))

        # construct arcs on AC from M and make points
        arctop5 = DashedVMobject(Arc(start_angle=2.15, angle=0.4, arc_center=pointM.get_center(), radius=1.45, stroke_width=2))  # Arc from 0 to pi radians
        arcbottom5 = DashedVMobject(Arc(start_angle=3.74, angle=0.4, arc_center=pointM.get_center(), radius=1.45, stroke_width=2))  # Arc from 0 to pi radians
        self.play(pointF.animate.scale(0.5), pointF_n.animate.scale(0.5))
        self.play(Create(arctop5), Create(arcbottom5), run_time=1)
        self.play(labelD.animate.move_to([-2.3,1,0]))
        pointbisector4=Dot(radius=0.03)
        pointbisector4.move_to([-2,1.83,0])
        pointbisector5=Dot(radius=0.03)
        pointbisector5.move_to([-2,-0.27,0])
        self.play(Create(pointbisector4), Create(pointbisector5))
        self.play(FadeOut(arctop5), FadeOut(arcbottom5), FadeOut(pointbisector4), FadeOut(pointbisector5))

        # construct arcs from acrc-points, join them
        arctop6 = DashedVMobject(Arc(start_angle=3.75, angle=0.4, arc_center=pointbisector4.get_center(), radius=1.45, stroke_width=2))  # Arc from 0 to pi radians
        arcbottom6 = DashedVMobject(Arc(start_angle=2.14, angle=0.4, arc_center=pointbisector5.get_center(), radius=1.45, stroke_width=2))  # Arc from 0 to pi radians
        self.play(Create(arctop6), Create(arcbottom6), run_time=1)
        pointbisector6 = Dot(radius=0.04)
        pointbisector6.move_to([-3,0.79,0])
        self.play(Create(pointbisector6))
        self.play(FadeOut(arctop6), FadeOut(arcbottom6))
       
        # construct bisector, and extrapolate till O
        lineOprimeO = DashedLine(start=pointbisector6.get_center(),end=[-2,0.79,0], color=RED, dash_length=0.1, stroke_width=sw, z_index=0)
        self.play(Create(lineOprimeO))
        pointO = Dot(radius=0.05)
        pointO.move_to([-2,0.79,0])
        self.play(Create(pointO))
        self.play(FadeOut(lineOprimeO), FadeOut(pointbisector6))
        labelO=Text("O")
        labelO.scale(0.7)
        labelO.move_to([-2.29, 0.74, 0])
        self.play(Write(labelO))
        self.play(labelO.animate.scale(0.6))

        # make a dashed line from O to a little bit further of M
        lineOQ = DashedLine(start=pointO.get_center(),end=[-0.23,0.79,0], color=RED, dash_length=0.1, stroke_width=sw, z_index=0)
        self.play(Create(lineOQ))
        self.play(FadeOut(Step))

        self.wait(2)

        # step 13
        """
        (13) With centre L and radius LN draw a semi-circle on the lower portion and let P and Q be the points where it touches the line OM respectively.
        """
        Step=Text("(13) With centre L and radius LN draw a semi-circle on the lower portion\n and let P and Q be the points where it touches the line OM respectively.")
        Step.move_to([-1.5,3.25,0])
        Step.scale(0.5)
        self.play(FadeIn(Step))

        arctop7 = Arc(start_angle=PI + 0.35, angle=PI-0.70, arc_center=pointL.get_center(), radius=0.85, stroke_width=2)  # Arc from 0 to pi radians
        arctop7.set_color(WHITE)
        self.play(labelN.animate.move_to([-2+1.2,0.47,0]))
        self.play(Create(arctop7))
        self.wait()

        # make P 
        pointP = Dot(radius=0.03)
        pointP.move_to([-1.78,0.79,0])
        self.play(Create(pointP))
        self.wait()
        # make Q
        pointQ = Dot(radius=0.03)
        pointQ.move_to([-0.23,0.79,0])
        self.play(Create(pointQ))

        # make labels appear at the same time
        labelP=Text("P")
        labelQ=Text("Q")
        labelP.scale(0.3)
        labelQ.scale(0.3)
        labelP.move_to([-1.85,0.59,0])
        labelQ.move_to([-0.03,0.79,0])
        self.play(Write(labelP), Write(labelQ), run_time=1.2)
        self.play(FadeOut(Step))

        self.wait(2)

        # step 14
        """
        (14) With centre M and radius MQ draw a semi-circle on the lower portion touching P and Q. 
        """
        Step=Text("(14) With centre M and radius MQ\n draw a semi-circle on the lower portion touching P and Q.")
        Step.move_to([-1.5,3.25,0])
        Step.scale(0.5)
        self.play(FadeIn(Step))

        # make arc
        arctop8 = Arc(start_angle=PI, angle=PI, arc_center=pointM.get_center(), radius=0.77, stroke_width=2)  # Arc from 0 to pi radians
        arctop8.set_color(WHITE)
        self.play(Create(arctop8))
        self.wait()

        # make point T
        pointT=Dot(radius=0.04)
        pointT.move_to([-1,0.02,0])
        self.play(Create(pointT))
        labelT=Text("T")
        labelT.move_to([[-1.15,-0.13,0]])
        labelT.scale(0.3)
        self.play(Write(labelT))

        # fadeout uneccessary lines
        self.play(FadeOut(LineJG), FadeOut(lineOQ), FadeOut(LineBisector2))
        self.play(FadeOut(Step))

        self.wait(2)

        # step 15
        """
        (15) With centre N and radius NM draw an arc touching PNQ at R and S. Join RS. Let T be the point where RS and HI cut one another. 
        """
        Step=Text("(15) With centre N and radius NM draw an arc touching PNQ at R and S.\nJoin RS. Let T be the point where RS and HI cut one another.")
        Step.move_to([-1.5,3.25,0])
        Step.scale(0.5)
        self.play(FadeIn(Step))

        # make arc
        arctop9 = DashedVMobject(Arc(start_angle=PI/6-0.17, angle=PI/1.5 + 0.37, arc_center=pointN.get_center(), radius=0.54, stroke_width=2))  # Arc from 0 to pi radians
        arctop9.set_color(WHITE)
        self.play(Create(arctop9))
        self.wait()

        # mark points
        pointR=Dot(radius=0.045)
        pointS=Dot(radius=0.045)
        pointR.move_to([-2+0.49,0.42,0])
        pointS.move_to([-2+0.62+0.89,0.42,0])
        self.play(Create(pointR), Create(pointS))

        # assign labels S and R
        labelS=Text("S")
        labelR=Text("R")
        labelS.move_to([-2+0.52+1.25,0.22,0])
        labelR.move_to([-2+0.29,0.22,0])
        labelS.scale(0.3)
        labelR.scale(0.3)
        self.play(Write(labelS), Write(labelR))
        self.play(FadeOut(Step))

        self.wait()

        # step 16
        """
        (16) With centre T and radius TS draw a semi-circle on the upper portion of PNQ touching it at two points. 
        """
        Step=Text("(16) With centre T and radius TS draw a semi-circle\non the upper portion of PNQ touching it at two points. ")
        Step.move_to([-1.5,3.25,0])
        Step.scale(0.5)
        self.play(FadeIn(Step))

        # draw arc
        arctop10 = Arc(start_angle=PI/6 + 0.2, angle=PI/1.5 - 0.35, arc_center=pointT.get_center(), radius=0.655, stroke_width=2)  # Arc from 0 to pi radians
        self.play(Create(arctop10))
        self.play(FadeOut(Step))
        self.wait()

        # step 17
        """
        (17) With centre T and radius TM draw an arc on the upper portion of PNQ touching at two points.
        """
        Step=Text("(17) With centre T and radius TM draw an arc on the upper portion of PNQ\n touching at two points.")
        Step.move_to([-1.5,3.25,0])
        Step.scale(0.5)
        self.play(FadeIn(Step))

        # draw arc
        arctop11 = DashedVMobject(Arc(start_angle=PI/6 + 0.16, angle=PI/1.5 - 0.285, arc_center=pointT.get_center(), radius=0.78, stroke_width=2))  # Arc from 0 to pi radians
        self.play(Create(arctop11))
        self.wait()

        # FadeOut
        self.play(FadeOut(arctop9))
        self.play(FadeOut(Step))
        self.wait()

        # step 18
        """
        (18) Eight equal and similar triangles of the moon are to be made in the space lying inside the semi-circle of No. (16) and outside the arc of No. (17) of this Schedule.
        """
        Step=Text("(18) Eight equal and similar triangles of the moon are to be made\n in the space lying inside the semi-circle of No. (16) \nand outside the arc of No. (17) of this Schedule.")
        Step.move_to([-1.5,3.25,0])
        Step.scale(0.5)
        self.play(FadeIn(Step))

        # make center on right
        point_origin_zoom=Dot(radius=0.1)
        point_origin_zoom.move_to([5,-1,0])
        self.play(Create(point_origin_zoom))

        # make arcs on right
        pointRup = Dot(radius=0.06)
        pointRdown = Dot(radius=0.06)
        pointRup.move_to([6.75,0.45,0])
        pointRdown.move_to([6.47,0.25,0])
        arctop12 = DashedVMobject(Arc(start_angle=PI/6 + 0.16, angle=PI/1.5 - 0.32, arc_center=point_origin_zoom.get_center(), radius=1.9, stroke_width=2))  # Arc from 0 to pi radians
        arctop13 = DashedVMobject(Arc(start_angle=PI/6 + 0.16, angle=PI/1.5 - 0.32, arc_center=point_origin_zoom.get_center(), radius=2.3, stroke_width=2))  # Arc from 0 to pi radians
        self.play(Create(pointRup), Create(pointRdown))
        self.play(Create(arctop12), Create(arctop13))
        self.wait()

        # bisection 1st
        pointLup = Dot(radius=0.06)
        pointLdown = Dot(radius=0.06)
        pointLup.move_to([3.25,0.45,0])
        pointLdown.move_to([3.53,0.25,0])
        self.play(Create(pointLup), Create(pointLdown))
        self.wait()

        # bisection 2nd
        bisecting_arc_right_1 = DashedVMobject(Arc(start_angle=2.02, angle=0.4, arc_center=pointRup.get_center(), radius=3, stroke_width=2))  # Arc from 0 to pi radians
        bisecting_arc_left_1 = DashedVMobject(Arc(start_angle=0.70, angle=0.4, arc_center=pointLup.get_center(), radius=3, stroke_width=2))  # Arc from 0 to pi radians
        self.play(Create(bisecting_arc_left_1), Create(bisecting_arc_right_1))
        # drop dashed line
        pointprime=Dot(radius=0.06)
        pointprime.move_to([5,2.89,0])
        self.play(Create(pointprime))
        bisectorline=DashedLine(start=pointprime.get_center(), end=point_origin_zoom.get_center(), color=WHITE, dash_length=0.1, stroke_width=sw, z_index=0)
        self.play(Create(bisectorline))
        point_bisector_most_right=Dot(radius=0.09)
        point_bisector_most_right.move_to([5,-1+2.3,0])
        self.play(Create(point_bisector_most_right))
        self.play(FadeOut(pointprime), FadeOut(bisecting_arc_left_1), FadeOut(bisecting_arc_right_1))

        # bisection 3rd
        bisecting_arc_right_2 = DashedVMobject(Arc(start_angle=2.3, angle=0.4, arc_center=point_bisector_most_right.get_center(), radius=2.1, stroke_width=2))  # Arc from 0 to pi radians
        bisecting_arc_left_2 = DashedVMobject(Arc(start_angle=1.3, angle=0.4, arc_center=pointLup.get_center(), radius=2.1, stroke_width=2))  # Arc from 0 to pi radians
        self.play(Create(bisecting_arc_left_2), Create(bisecting_arc_right_2))
        point_bisector_2=Dot(radius=0.06)
        point_bisector_2.move_to([3.34,2.55,0])
        self.play(Create(point_bisector_2))
        bisectorline2 = DashedLine(start=point_bisector_2.get_center(), end=point_origin_zoom.get_center(), color=WHITE, dash_length=0.1, stroke_width=sw, z_index=0)
        self.play(Create(bisectorline2))
        point_bisector_2nd_right=Dot(radius=0.05)
        point_bisector_2nd_right.move_to([4.01,-1+2.10,0])
        self.play(Create(point_bisector_2nd_right))
        self.play(FadeOut(bisecting_arc_left_2), FadeOut(bisecting_arc_right_2), FadeOut(point_bisector_2))
        
        # bisection 4th
        bisecting_arc_right_3 = DashedVMobject(Arc(start_angle=2.3, angle=0.4, arc_center=point_bisector_2nd_right.get_center(), radius=1.9, stroke_width=2))  # Arc from 0 to pi radians
        bisecting_arc_left_3 = DashedVMobject(Arc(start_angle=1.9, angle=0.4, arc_center=pointLup.get_center(), radius=1.9, stroke_width=2))  # Arc from 0 to pi radians
        self.play(Create(bisecting_arc_left_3), Create(bisecting_arc_right_3))
        point_bisector_3=Dot(radius=0.06)
        point_bisector_3.move_to([2.42,2.14,0])
        self.play(Create(point_bisector_3))
        bisectorline3 = DashedLine(start=point_bisector_3.get_center(), end=point_origin_zoom.get_center(), color=WHITE, dash_length=0.1, stroke_width=sw, z_index=0)
        self.play(Create(bisectorline3))
        point_bisector_3rd_right=Dot(radius=0.05)
        point_bisector_3rd_right.move_to([3.555,-1+1.77,0])
        point_bisector_3rd_right_low=Dot(radius=0.05)
        point_bisector_3rd_right_low.move_to([3.78,-1+1.48,0])
        self.play(Create(point_bisector_3rd_right))
        self.play(Create(point_bisector_3rd_right_low))
        self.play(FadeOut(point_bisector_3), FadeOut(bisecting_arc_left_3), FadeOut(bisecting_arc_right_3))
        
        # last bisection
        bisecting_arc_right_4 = DashedVMobject(Arc(start_angle=2.3, angle=0.4, arc_center=point_bisector_3rd_right.get_center(), radius=2.3, stroke_width=2))  # Arc from 0 to pi radians
        bisecting_arc_left_4 = DashedVMobject(Arc(start_angle=2.1, angle=0.4, arc_center=pointLup.get_center(), radius=2.3, stroke_width=2))  # Arc from 0 to pi radians
        self.play(Create(bisecting_arc_left_4), Create(bisecting_arc_right_4))
        point_bisector_4=Dot(radius=0.06)
        point_bisector_4.move_to([1.77,2.19,0])
        self.play(Create(point_bisector_4))
        bisectorline4 = DashedLine(start=point_bisector_4.get_center(), end=point_origin_zoom.get_center(), color=WHITE, dash_length=0.1, stroke_width=sw, z_index=0)
        self.play(Create(bisectorline4))
        point_bisector_4th_right=Dot(radius=0.05)
        point_bisector_4th_right.move_to([3.37,-1+1.62,0])
        self.play(Create(point_bisector_4th_right))
        self.play(FadeOut(point_bisector_4), FadeOut(bisecting_arc_left_4), FadeOut(bisecting_arc_right_4))

        self.wait()

        # making triangle
        edge1 = Line(start=pointLdown.get_center(), end=point_bisector_4th_right.get_center())
        edge1.set_color(BLUE)
        edge2= Line(start=point_bisector_4th_right.get_center(), end=point_bisector_3rd_right_low.get_center())
        edge2.set_color(BLUE)
        self.play(Create(edge1))
        self.play(Create(edge2))

        # fading out
        self.wait(2)
        self.play(FadeOut(bisectorline), FadeOut(bisectorline2), FadeOut(bisectorline3), FadeOut(bisectorline4), FadeOut(pointLdown), FadeOut(pointLup), FadeOut(pointRup), FadeOut(pointRdown), FadeOut(point_origin_zoom), FadeOut(point_bisector_2nd_right), FadeOut(point_bisector_most_right), FadeOut(point_bisector_3rd_right), FadeOut(point_bisector_3rd_right_low), FadeOut(point_bisector_4th_right))
        self.wait(2)
        self.play(FadeOut(edge1), FadeOut(edge2), FadeOut(arctop12), FadeOut(arctop13))
        
        # making triangles in main figure
        # initialising points
        pointL1low=Dot(radius=0.02)
        pointL2low=Dot(radius=0.02)
        pointL3low=Dot(radius=0.02)
        pointL4low=Dot(radius=0.02)
        pointR1low=Dot(radius=0.02)
        pointR2low=Dot(radius=0.02)
        pointR3low=Dot(radius=0.02)
        pointR4low=Dot(radius=0.02)
        pointL1high=Dot(radius=0.02)
        pointL2high=Dot(radius=0.02)
        pointL3high=Dot(radius=0.02)
        pointL4high=Dot(radius=0.02)
        pointR1high=Dot(radius=0.02)
        pointR2high=Dot(radius=0.02)
        pointR3high=Dot(radius=0.02)
        pointR4high=Dot(radius=0.02)
        pointend=Dot(radius=0.02)

        # move to
        pointL1low.move_to([-2+0.49,0.41,0])
        pointL2low.move_to([-2+0.60,0.54,0])
        pointL3low.move_to([-2+0.72,0.63,0])
        pointL4low.move_to([-2+0.87,0.69,0])

        pointR1low.move_to([-2+1,0.70,0])
        pointR2low.move_to([-2+1.15,0.67,0])
        pointR3low.move_to([-2+1.30,0.60,0])
        pointR4low.move_to([-2+1.43,0.54,0])

        pointL1high.move_to([-2+0.47,0.60,0])
        pointL2high.move_to([-2+0.60,0.70,0])
        pointL3high.move_to([-2+0.74,0.77,0])
        pointL4high.move_to([-2+0.91,0.80,0])

        pointR1high.move_to([-2+1.10,0.79,0])
        pointR2high.move_to([-2+1.27,0.76,0])
        pointR3high.move_to([-2+1.43,0.69,0])
        pointR4high.move_to([-2+1.54,0.61,0])

        pointend.move_to([-2+0.62+0.89,0.42,0])

        self.play(Create(pointL1low),
                  Create(pointL2low),
                  Create(pointL3low),
                  Create(pointL4low),
                  Create(pointR1low),
                  Create(pointR2low),
                  Create(pointR3low),
                  Create(pointR4low),
                  Create(pointL1high),
                  Create(pointL2high),
                  Create(pointL3high),
                  Create(pointL4high),
                  Create(pointR1high),
                  Create(pointR2high),
                  Create(pointR3high),
                  Create(pointR4high))

        # connecting triangles one after the other
        self.play(Create(Line(start=pointL1low.get_center(),end=pointL1high.get_center(),color=WHITE,stroke_width=sw)))
        self.play(Create(Line(start=pointL1high.get_center(),end=pointL2low.get_center(),color=WHITE,stroke_width=sw)))
        self.play(Create(Line(start=pointL2low.get_center(),end=pointL2high.get_center(),color=WHITE,stroke_width=sw)))
        self.play(Create(Line(start=pointL2high.get_center(),end=pointL3low.get_center(),color=WHITE,stroke_width=sw)))
        self.play(Create(Line(start=pointL3low.get_center(),end=pointL3high.get_center(),color=WHITE,stroke_width=sw)))
        self.play(Create(Line(start=pointL3high.get_center(),end=pointL4low.get_center(),color=WHITE,stroke_width=sw)))
        self.play(Create(Line(start=pointL4low.get_center(),end=pointL4high.get_center(),color=WHITE,stroke_width=sw)))
        self.play(Create(Line(start=pointL4high.get_center(),end=pointR1low.get_center(),color=WHITE,stroke_width=sw)))
        self.play(Create(Line(start=pointR1low.get_center(),end=pointR1high.get_center(),color=WHITE,stroke_width=sw)))
        self.play(Create(Line(start=pointR1high.get_center(),end=pointR2low.get_center(),color=WHITE,stroke_width=sw)))
        self.play(Create(Line(start=pointR2low.get_center(),end=pointR2high.get_center(),color=WHITE,stroke_width=sw)))
        self.play(Create(Line(start=pointR2high.get_center(),end=pointR3low.get_center(),color=WHITE,stroke_width=sw)))
        self.play(Create(Line(start=pointR3low.get_center(),end=pointR3high.get_center(),color=WHITE,stroke_width=sw)))
        self.play(Create(Line(start=pointR3high.get_center(),end=pointR4low.get_center(),color=WHITE,stroke_width=sw)))
        self.play(Create(Line(start=pointR4low.get_center(),end=pointR4high.get_center(),color=WHITE,stroke_width=sw)))
        self.play(Create(Line(start=pointR4high.get_center(),end=pointend.get_center(),color=WHITE,stroke_width=sw)))
        self.wait()

        self.play(FadeOut(arctop11))
        
        self.play(pointL1low.animate.scale(0.5),
                  pointL2low.animate.scale(0.5),
                  pointL3low.animate.scale(0.5),
                  pointL4low.animate.scale(0.5),
                  pointR1low.animate.scale(0.5),
                  pointR2low.animate.scale(0.5),
                  pointR3low.animate.scale(0.5),
                  pointR4low.animate.scale(0.5),
                  pointL1high.animate.scale(0.5),
                  pointL2high.animate.scale(0.5),
                  pointL3high.animate.scale(0.5),
                  pointL4high.animate.scale(0.5),
                  pointR1high.animate.scale(0.5),
                  pointR2high.animate.scale(0.5),
                  pointR3high.animate.scale(0.5),
                  pointR4high.animate.scale(0.5))
        
        self.play(FadeOut(Step))
        
        self.wait()

        ######################## Making the Moon #########################

        # step 19
        """
        (19) Bisect line AF at U, and draw a line UV parallel to AB line touching line BE at V.
        """
        Step=Text("(19) Bisect line AF at U, and draw a line UV parallel\nto AB line touching line BE at V.")
        Step.move_to([-1.5,3.25,0])
        Step.scale(0.5)
        self.play(FadeIn(Step))

        # create arcs on either side
        bisecting_arc_topleft = DashedVMobject(Arc(start_angle=3.7, angle=0.4, arc_center=pointF.get_center(), radius=2.3, stroke_width=2))  # Arc from 0 to pi radians
        bisecting_arc_bottomleft = DashedVMobject(Arc(start_angle=2.32, angle=0.4, arc_center=pointA.get_center(), radius=2.3, stroke_width=2))  # Arc from 0 to pi radians
        bisecting_arc_topright = DashedVMobject(Arc(start_angle=5.42, angle=0.4, arc_center=pointF.get_center(), radius=2.3, stroke_width=2))  # Arc from 0 to pi radians
        bisecting_arc_bottomright = DashedVMobject(Arc(start_angle=0.5, angle=0.4, arc_center=pointA.get_center(), radius=2.3, stroke_width=2))  # Arc from 0 to pi radians
        self.play(Create(bisecting_arc_topleft), Create(bisecting_arc_bottomleft))
        self.play(Create(bisecting_arc_bottomright), Create(bisecting_arc_topright))

        # make points on arc intersections
        pointleft=Dot(radius=0.06)
        pointright=Dot(radius=0.06)
        pointleft.move_to([-3.80,-1.6,0])
        pointright.move_to([-0.2,-1.6,0])
        self.play(Create(pointleft), Create(pointright))
        lineperp = DashedLine(start=pointleft.get_center(),end=[0.6,-1.6,0], color=RED, dash_length=0.1, stroke_width=sw, z_index=0)
        self.play(Create(lineperp))
        self.play(FadeOut(bisecting_arc_topleft), FadeOut(bisecting_arc_bottomleft), FadeOut(bisecting_arc_topright), FadeOut(bisecting_arc_bottomright))

        # join with dashed line U and V
        pointU=Dot(radius=0.08)
        pointV=Dot(radius=0.08)
        pointU.move_to([-2,-1.6,0])
        pointV.move_to([0.55,-1.6,0])
        self.play(Create(pointU), Create(pointV))
        labelU=Text("U")
        labelV=Text("V")
        labelU.scale(0.7)
        labelV.scale(0.7)
        labelU.next_to(pointU,LEFT)
        labelV.next_to(pointV,RIGHT)
        self.play(FadeOut(lineperp),FadeOut(pointleft), FadeOut(pointright),Create(DashedLine(start=pointU.get_center(), end=pointV.get_center(), color=RED, dash_length=0.1, stroke_width=sw, z_index=0)))
        self.play(Create(labelU), Create(labelV))
        self.play(labelU.animate.scale(0.8), labelV.animate.scale(0.8))
        self.play(FadeOut(Step))

        self.wait(2)

        # step 20
        """
        (20) With center W, the point where HI and UN cut one another and radius MN draw a circle.
        """
        Step=Text("(20) With center W, the point where HI and UN cut one another\n and radius MN draw a circle.")
        Step.move_to([-1.5,3.25,0])
        Step.scale(0.5)
        self.play(FadeIn(Step))

        pointW=Dot(radius=0.08)
        pointW.move_to([-1,-1.6,0])
        self.play(Create(pointW))
        labelW=Text("W")
        labelW.move_to([-1.25,-1.4,0])
        labelW.scale(0.8)
        self.play(labelW.animate.scale(0.5))

        linesegment=Line(start=pointM.get_center(), end=pointN.get_center(), color=BLUE)
        self.play(Create(linesegment))
        self.play(Transform(linesegment, Line(start=pointW.get_center(), end=[-1,-2.14,0], color=BLUE), run_time=1.2))
        innerCircle = Arc(start_angle=3*PI/2, angle=2*PI, arc_center=pointW.get_center(), radius=0.54, stroke_width=sw, color=WHITE)  # Arc from 0 to pi radians
        self.play(Rotate(linesegment, angle=2*PI, axis=OUT, about_point=pointW.get_center()), Create(innerCircle), run_time=2)
        self.play(FadeOut(linesegment))
        self.play(FadeOut(Step))

        self.wait(2)

        # step 21
        """
        (21) With center W and radius LN draw a circle.
        """  
        Step=Text("(21) With center W and radius LN draw a circle.")
        Step.move_to([-1.5,3.25,0])
        Step.scale(0.5)
        self.play(FadeIn(Step))
      
        linesegment2=Line(start=pointL.get_center(), end=pointN.get_center(), color=BLUE)
        self.play(Create(linesegment2))
        self.play(Transform(linesegment2, Line(start=pointW.get_center(), end=[-1,-2.45,0], color=BLUE), run_time=1.2))
        outerCircle = DashedVMobject(Arc(start_angle=3*PI/2, angle=2*PI, arc_center=pointW.get_center(), radius=0.85, stroke_width=sw, color=WHITE))  # Arc from 0 to pi radians
        self.play(Rotate(linesegment2, angle=2*PI, axis=OUT, about_point=pointW.get_center()), Create(outerCircle), run_time=2)
        self.play(FadeOut(linesegment2))
        self.play(FadeOut(Step))

        self.wait(2)

        # step 22
        """
        (22) Twelve equal and similar triangles of the sun are to be made in the space enclosed by the circle of No (20) and No (21) with the two apexes of two triangles touching line HI.
        """
        Step=Text("(22) Twelve equal and similar triangles of the sun are to be made\n in the space enclosed by the circle of No (20) and\n No (21) with the two apexes of two triangles touching line HI.")
        Step.move_to([-1.5,3.25,0])
        Step.scale(0.5)
        self.play(FadeIn(Step))

        # show cardinal points
        point1=Dot(radius=0.05)
        point2=Dot(radius=0.05)
        point3=Dot(radius=0.05)
        point4=Dot(radius=0.05)
        point1.move_to([-0.46,-1.6,0])
        point2.move_to([-1,-1.06,0])
        point3.move_to([-1.54,-1.6,0])
        point4.move_to([-1,-2.14,0])
        self.play(Create(point1), Create(point2), Create(point3), Create(point4))

        # show line, rotate line
        radius_line = Line(start=pointW.get_center(),end=point1.get_center(), color=BLUE)
        self.play(Create(radius_line))
        self.play(Rotate(radius_line,axis=OUT,angle=-PI/3,about_point=point1.get_center()))
        pointa=Dot(radius=0.03)
        pointa.move_to([-0.74,-1.13,0])
        pointb=Dot(radius=0.03)
        pointb.move_to([-0.52,-1.34,0])
        self.play(Create(pointa))
        self.play(Transform(radius_line,Line(start=point2.get_center(),end=pointb.get_center(), color=BLUE)))
        self.play(Create(pointb))
        self.play(FadeOut(radius_line))

        # bisect first triplet, make a triangle,
        bisecting_arc_left = DashedVMobject(Arc(start_angle=PI/2-0.4, angle=0.4, arc_center=point2.get_center(), radius=4.3, stroke_width=2))  # Arc from 0 to pi radians
        bisecting_arc_right = DashedVMobject(Arc(start_angle=PI/2-0.4, angle=0.4, arc_center=pointa.get_center(), radius=4.3, stroke_width=2))  # Arc from 0 to pi radians
        self.play(Create(bisecting_arc_left), Create(bisecting_arc_right))
        pointbisector=Dot(radius=0.04)
        pointbisector.move_to([0.2,3.1,0])
        self.play(Create(pointbisector))
        self.play(FadeOut(bisecting_arc_left), FadeOut(bisecting_arc_right))
        linefrombisectortoorigin=DashedLine(start=pointbisector.get_center(), end=pointW.get_center(), color=WHITE, dash_length=0.1, stroke_width=sw, z_index=0)
        self.play(Create(linefrombisectortoorigin))
        bisectionpoint=Dot(radius=0.04)
        bisectionpoint.move_to([-0.80,-0.80,0])
        self.play(Create(bisectionpoint))
        self.play(FadeOut(linefrombisectortoorigin), FadeOut(pointbisector))
        self.play(Create(Line(start=point2.get_center(),end=bisectionpoint.get_center(),stroke_width=sw)))
        self.play(Create(Line(start=bisectionpoint.get_center(),end=pointa.get_center(),stroke_width=sw)))

        # then just make points in a circle,
        pointc=Dot(radius=0.04)
        pointd=Dot(radius=0.04)
        pointe=Dot(radius=0.04)
        pointf=Dot(radius=0.04)
        pointh=Dot(radius=0.04)
        pointi=Dot(radius=0.04)
        pointO1=Dot(radius=0.04)
        pointO2=Dot(radius=0.04)
        pointO3=Dot(radius=0.04)
        pointO4=Dot(radius=0.04)
        pointO5=Dot(radius=0.04)
        pointO6=Dot(radius=0.04)
        pointO7=Dot(radius=0.04)
        pointO8=Dot(radius=0.04)
        pointO9=Dot(radius=0.04)
        pointO10=Dot(radius=0.04)
        pointO11=Dot(radius=0.04)

        pointc.move_to([-0.51,-1.84,0]) ##
        pointd.move_to([-0.76,-2.09,0]) ##
        pointe.move_to([-1.24,-2.09,0]) ##
        pointf.move_to([-1.49,-1.84,0]) ##
        pointh.move_to([-1.49,-1.35,0]) ##
        pointi.move_to([-1.26,-1.13,0]) ##
        
        pointO1.move_to([-0.37,-1,0]) ##
        pointO2.move_to([-0.20,-1.34,0]) ##
        pointO3.move_to([-0.20,-1.86,0]) ##
        pointO4.move_to([-0.37,-2.20,0]) ##$
        pointO5.move_to([-0.74,-2.40,0]) ##
        pointO6.move_to([-1.26,-2.40,0]) ##
        pointO7.move_to([-1.64,-2.20,0]) #$
        pointO8.move_to([-1.80,-1.86,0]) ##
        pointO9.move_to([-1.80,-1.34,0]) ##
        pointO10.move_to([-1.64,-1.02,0]) # 
        pointO11.move_to([-1.26,-0.80,0]) #

        self.play(Create(pointO1))
        self.play(Create(pointO2))
        self.play(Create(pointO3))
        self.play(Create(pointc))
        self.play(Create(pointO4))
        self.play(Create(pointd))
        self.play(Create(pointO5))
        self.play(Create(pointO6))
        self.play(Create(pointe))
        self.play(Create(pointO7))
        self.play(Create(pointf))
        self.play(Create(pointO8))
        self.play(Create(pointO9))
        self.play(Create(pointh))
        self.play(Create(pointO10))
        self.play(Create(pointi))
        self.play(Create(pointO11))

        self.play(Create(Line(start=pointa.get_center(),end=pointO1.get_center(),stroke_width=sw)))
        self.play(Create(Line(start=pointO1.get_center(),end=pointb.get_center(),stroke_width=sw)))
        self.play(Create(Line(start=pointb.get_center(),end=pointO2.get_center(),stroke_width=sw)))
        self.play(Create(Line(start=pointO2.get_center(),end=point1.get_center(),stroke_width=sw)))
        self.play(Create(Line(start=point1.get_center(),end=pointO3.get_center(),stroke_width=sw)))
        self.play(Create(Line(start=pointO3.get_center(),end=pointc.get_center(),stroke_width=sw)))
        self.play(Create(Line(start=pointc.get_center(),end=pointO4.get_center(),stroke_width=sw)))
        self.play(Create(Line(start=pointO4.get_center(),end=pointd.get_center(),stroke_width=sw)))
        self.play(Create(Line(start=pointd.get_center(),end=pointO5.get_center(),stroke_width=sw)))
        self.play(Create(Line(start=pointO5.get_center(),end=point4.get_center(),stroke_width=sw)))
        self.play(Create(Line(start=point4.get_center(),end=pointO6.get_center(),stroke_width=sw)))
        self.play(Create(Line(start=pointO6.get_center(),end=pointe.get_center(),stroke_width=sw)))
        self.play(Create(Line(start=pointe.get_center(),end=pointO7.get_center(),stroke_width=sw)))
        self.play(Create(Line(start=pointO7.get_center(),end=pointf.get_center(),stroke_width=sw)))
        self.play(Create(Line(start=pointf.get_center(),end=pointO8.get_center(),stroke_width=sw)))
        self.play(Create(Line(start=pointO8.get_center(),end=point3.get_center(),stroke_width=sw)))
        self.play(Create(Line(start=point3.get_center(),end=pointO9.get_center(),stroke_width=sw)))
        self.play(Create(Line(start=pointO9.get_center(),end=pointh.get_center(),stroke_width=sw)))
        self.play(Create(Line(start=pointh.get_center(),end=pointO10.get_center(),stroke_width=sw)))
        self.play(Create(Line(start=pointO10.get_center(),end=pointi.get_center(),stroke_width=sw)))
        self.play(Create(Line(start=pointi.get_center(),end=pointO11.get_center(),stroke_width=sw)))
        self.play(Create(Line(start=pointO11.get_center(),end=point2.get_center(),stroke_width=sw)))

        # and reduce their sizes
        self.play(pointa.animate.scale(0.4),
                  pointb.animate.scale(0.4),
                  pointc.animate.scale(0.4),
                  pointd.animate.scale(0.4),
                  pointe.animate.scale(0.4),
                  pointf.animate.scale(0.4),
                  pointh.animate.scale(0.4),
                  pointi.animate.scale(0.4),
                  pointO1.animate.scale(0.4),
                  pointO2.animate.scale(0.4),
                  pointO3.animate.scale(0.4),
                  pointO4.animate.scale(0.4),
                  pointO5.animate.scale(0.4),
                  pointO6.animate.scale(0.4),
                  pointO7.animate.scale(0.4),
                  pointO8.animate.scale(0.4),
                  pointO9.animate.scale(0.4),
                  pointO10.animate.scale(0.4),
                  pointO11.animate.scale(0.4))
        
        self.wait(2)
        self.play(FadeOut(outerCircle))
        self.play(FadeOut(Step))

        self.wait(2)

        ####################### Making the Border ########################
        # step 23
        """
        (23) The width of the border will be equal to the width of TN. This will be of deep blue color and will be provided on all the sides of the flag. However, on the given angles of the flag the external angles will be equal to the internal angles.
        """
        Step=Text("(23) The width of the border will be equal to the width of TN.\nThis will be of deep blue color and will be provided on all the sides of the flag. \nHowever, on the given angles of the flag the external angles will be equal to the internal angles.")
        Step.move_to([0,3.25,0])
        Step.scale(0.5)
        self.play(FadeIn(Step))

        pointAborder=Dot(radius=0.04)
        pointBborder=Dot(radius=0.04)
        pointGborder=Dot(radius=0.04)
        pointEborder=Dot(radius=0.04)
        pointCborder=Dot(radius=0.04)
        pointAborder.move_to([-2.23,-3.23,0])
        pointBborder.move_to([2.57,-3.23,0])
        pointEborder.move_to([-0.27,-0.38,0])
        pointGborder.move_to([2.68,-0.38,0])
        pointCborder.move_to([-2.23,2.79,0])
        pickupTN=Line(start=pointT.get_center(),end=pointN.get_center(),color=BLUE)
        self.play(Create(pickupTN))
        self.play(Transform(pickupTN,Line(start=[-1,-3,0],end=[-1,-3.23,0],color=BLUE)))
        self.play(Create(pointAborder))
        self.play(Create(Line(start=pointAborder.get_center(),end=pointBborder.get_center(),stroke_width=sw,color=DARK_BLUE)))
        self.play(Create(pointBborder))
        self.play(FadeOut(pickupTN))
        self.play(Create(Line(start=pointBborder.get_center(),end=pointEborder.get_center(),stroke_width=sw,color=DARK_BLUE)))
        self.play(Create(pointEborder))
        self.play(Create(Line(start=pointEborder.get_center(),end=pointGborder.get_center(),stroke_width=sw,color=DARK_BLUE)))
        self.play(Create(pointGborder))
        self.play(Create(Line(start=pointGborder.get_center(),end=pointCborder.get_center(),stroke_width=sw,color=DARK_BLUE)))
        self.play(Create(pointCborder))
        self.play(Create(Line(start=pointCborder.get_center(),end=pointAborder.get_center(),stroke_width=sw,color=DARK_BLUE)))

        self.play(FadeOut(Step))

        self.wait(1)
        # fade everything
        self.play(FadeOut(labelU),FadeOut(labelF),FadeOut(labelO),FadeOut(labelD),FadeOut(labelJ),FadeOut(labelC),FadeOut(labelI),FadeOut(labelK),FadeOut(labelG),FadeOut(labelE),FadeOut(labelV),FadeOut(labelB),FadeOut(labelH),FadeOut(labelA),FadeOut(labelP),FadeOut(labelR),FadeOut(labelT),FadeOut(labelS),FadeOut(labelQ),FadeOut(labelN),FadeOut(labelM),FadeOut(labelL),FadeOut(labelW))
        self.play(FadeOut(pointU),FadeOut(pointF),FadeOut(pointO),FadeOut(pointD),FadeOut(pointJ),FadeOut(pointC),FadeOut(pointI),FadeOut(pointK),FadeOut(pointG),FadeOut(pointE),FadeOut(pointV),FadeOut(pointB),FadeOut(bisectpoint1),FadeOut(pointA),FadeOut(pointP),FadeOut(pointR),FadeOut(pointT),FadeOut(pointS),FadeOut(pointQ),FadeOut(pointN),FadeOut(pointM),FadeOut(pointL),FadeOut(pointW))
        self.play(FadeOut(pointAborder),FadeOut(pointBborder),FadeOut(pointEborder),FadeOut(pointCborder),FadeOut(pointGborder))

        self.wait(3)

        image_start = ImageMobject("C:\\Users\\User\\Desktop\\manim\\final_flag.png")
        image_start.set_opacity(0)
        image_start.move_to([0.1,-0.1,0])
        image_final = ImageMobject(filename_or_array="C:\\Users\\User\\Desktop\\manim\\final_flag.png")
        image_final.set_opacity(1)        
        image_final.move_to([0.1,-0.1,0])

        # Optionally, adjust position and scale
        image_start.scale(1.5)     # Scales down the image by a factor of 0.5
        # Optionally, adjust position and scale
        image_final.scale(1.5)     # Scales down the image by a factor of 0.5

        # Add the image to the scene
        self.play(Transform(image_start,image_final,run_time=6))

        self.wait(10)