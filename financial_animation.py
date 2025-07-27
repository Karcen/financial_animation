from manim import *


class FinancialSectorAnimation(Scene):
    """
    A detailed Manim animation explaining the paper "Linkages and Structural
    Changes in the Chinese Financial Sector, 1996-2018: A Network and
    Input-Output Approach" by Khan, Li, and Mahsud.
    """

    def construct(self):
        self.show_title()
        self.introduce_problem()
        self.explain_io_network()
        self.explain_push_pull_effects()
        self.explain_centrality_measures()
        self.explain_causative_matrix()
        self.explain_risk_coefficients()
        self.show_conclusions()
        self.show_end_screen()

    def show_title(self):
        """Scene 1: Title and introduction of the paper."""
        title = Tex(r"\textbf{Linkages and Structural Changes in the}", font_size=42)
        title2 = Tex(r"\textbf{Chinese Financial Sector (1996-2018)}", font_size=42)
        subtitle = Text("A Network and Input-Output Approach", font_size=32, slant=ITALIC)
        authors = Text("Khan, Li, and Mahsud (2024)", font_size=28)

        title_group = VGroup(title, title2, subtitle, authors).arrange(DOWN, buff=0.4)

        self.play(Write(title_group))
        self.wait(4)
        self.play(FadeOut(title_group))
        self.wait(1)

    def introduce_problem(self):
        """Scene 2: The core questions the paper addresses."""
        title = Title("Research Questions")
        q1 = Text("1. How have the financial sector's links to the economy evolved?", font_size=32)
        q2 = Text("2. What is its role in the economic network?", font_size=32)
        q3 = Text("3. How has its structure and risk profile changed over time?", font_size=32)

        questions = VGroup(q1, q2, q3).arrange(DOWN, buff=0.7, aligned_edge=LEFT).next_to(title, DOWN, buff=0.5)

        self.play(Write(title))
        self.play(Write(q1))
        self.wait(2)
        self.play(Write(q2))
        self.wait(2)
        self.play(Write(q3))
        self.wait(3)
        self.play(FadeOut(title), FadeOut(questions))
        self.wait(1)

    def explain_io_network(self):
        """Scene 3: Explaining the Input-Output table to Network concept."""
        title = Title("Methodology: From Tables to Networks")
        self.play(Write(title))

        # Explain Input-Output Table
        io_text = Text("The economy is modeled using an Input-Output (IO) Table.", font_size=30).to_edge(UP, buff=1.5)
        table_data = [
            ["", "Agri.", "Manuf.", "Finance", "Services"],
            ["Agri.", "10", "50", "5", "15"],
            ["Manuf.", "20", "40", "30", "40"],
            ["Finance", "5", "25", "10", "50"],
            ["Services", "15", "30", "40", "20"]
        ]
        table = Table(table_data, include_outer_lines=True).scale(0.5)
        table_desc = Tex(
            r"Each cell $z_{ij}$ shows the output from sector $i$ (row) \\ used as input by sector $j$ (column).").scale(
            0.7).next_to(table, DOWN)

        self.play(Write(io_text))
        self.play(Create(table), Write(table_desc))
        self.wait(4)

        # Transform to Network
        network_text = Text("This table can be visualized as a network.", font_size=30).to_edge(UP, buff=1.5)

        nodes = {
            "Agri": [-4, 2, 0], "Manuf": [-2, -2, 0],
            "Finance": [2, -2, 0], "Services": [4, 2, 0]
        }
        vertices = list(nodes.keys())
        edges = [
            ("Agri", "Manuf"), ("Manuf", "Finance"), ("Finance", "Services"),
            ("Services", "Agri"), ("Manuf", "Services")
        ]

        graph = Graph(
            vertices, edges,
            layout=nodes,
            labels=True,
            vertex_config={"color": BLUE, "radius": 0.5},
            edge_config={"color": WHITE, "stroke_width": 2}
        )
        graph_desc = Tex(r"Sectors are nodes. Transactions are weighted, directed edges.").scale(0.7).next_to(graph,
                                                                                                              DOWN)

        self.play(ReplacementTransform(io_text, network_text))
        self.play(ReplacementTransform(VGroup(table, table_desc), VGroup(graph, graph_desc)))
        self.wait(4)

        self.play(FadeOut(title), FadeOut(network_text), FadeOut(graph), FadeOut(graph_desc))
        self.wait(1)

    def explain_push_pull_effects(self):
        """Scene 4: Finding 1 - Push and Pull Effects."""
        title = Title("Finding 1: Intersectoral Linkages")
        self.play(Write(title))

        # Setup nodes
        finance_node = Circle(radius=0.8, color=YELLOW, fill_opacity=0.3).shift(DOWN * 0.5)
        finance_label = Text("Financial\nSector", font_size=24).move_to(finance_node)

        upstream_node = Circle(radius=0.6, color=BLUE).shift(LEFT * 4 + UP * 1.5)
        upstream_label = Text("Upstream\n(e.g., IT)", font_size=20).move_to(upstream_node)

        downstream_node = Circle(radius=0.6, color=GREEN).shift(RIGHT * 4 + UP * 1.5)
        downstream_label = Text("Downstream\n(e.g., Real Estate)", font_size=20).move_to(downstream_node)

        nodes_group = VGroup(finance_node, finance_label, upstream_node, upstream_label, downstream_node,
                             downstream_label)
        self.play(Create(nodes_group))

        # Pull Effects
        pull_title = Text("Pull Effects (Demand)", font_size=28, color=BLUE_C).to_edge(LEFT, buff=1).shift(DOWN * 2)
        pull_desc = Text("Financial sector 'pulls' inputs from upstream sectors.", font_size=24).next_to(pull_title,
                                                                                                         DOWN,
                                                                                                         aligned_edge=LEFT)
        pull_arrow = Arrow(upstream_node.get_right(), finance_node.get_left(), buff=0.2, color=BLUE_C)
        self.play(Write(pull_title), Create(pull_arrow))
        self.play(Write(pull_desc))
        self.wait(3)

        # Push Effects
        push_title = Text("Push Effects (Supply)", font_size=28, color=GREEN_C).to_edge(RIGHT, buff=1).shift(DOWN * 2)
        push_desc = Text("Financial sector 'pushes' services to downstream sectors.", font_size=24).next_to(push_title,
                                                                                                            DOWN,
                                                                                                            aligned_edge=LEFT)
        push_arrow = Arrow(finance_node.get_right(), downstream_node.get_left(), buff=0.2, color=GREEN_C)
        self.play(Write(push_title), Create(push_arrow))
        self.play(Write(push_desc))
        self.wait(4)

        self.play(
            FadeOut(VGroup(title, nodes_group, pull_title, pull_desc, pull_arrow, push_title, push_desc, push_arrow)))

    def explain_centrality_measures(self):
        """Scene 5: Finding 2 - Closeness and Betweenness Centrality."""
        title = Title("Finding 2: Role in the Economic Network")
        self.play(Write(title))

        # Closeness Centrality
        closeness_text = Text("Closeness Centrality: How influential is the sector?", font_size=32).next_to(title, DOWN,
                                                                                                            buff=0.5)
        self.play(Write(closeness_text))

        axes = Axes(
            x_range=[1995, 2020, 5], y_range=[0, 20000, 5000],
            x_length=10, y_length=4,
            axis_config={"include_tip": False}
        ).shift(DOWN * 1)
        x_label = axes.get_x_axis_label("Year")
        y_label = axes.get_y_axis_label("Closeness Value", edge=LEFT, direction=LEFT)

        downstream_data = [(1996, 828), (2001, 1247), (2006, 2779), (2008, 5242), (2013, 14619), (2018, 18776)]
        upstream_data = [(1996, 244), (2001, 443), (2006, 1367), (2008, 1413), (2013, 4293), (2018, 3433)]

        downstream_graph = axes.plot_line_graph(
            x_values=[d[0] for d in downstream_data],
            y_values=[d[1] for d in downstream_data],
            line_color=GREEN,
            vertex_dot_style=dict(stroke_width=3, fill_color=GREEN_C),
            add_vertex_dots=True
        )
        upstream_graph = axes.plot_line_graph(
            x_values=[d[0] for d in upstream_data],
            y_values=[d[1] for d in upstream_data],
            line_color=BLUE,
            vertex_dot_style=dict(stroke_width=3, fill_color=BLUE_C),
            add_vertex_dots=True
        )

        down_label = Text("Downstream (Supply)", color=GREEN).next_to(axes.c2p(2018, 18776), RIGHT)
        up_label = Text("Upstream (Demand)", color=BLUE).next_to(axes.c2p(2018, 3433), RIGHT)

        self.play(Create(axes), Write(x_label), Write(y_label))
        self.play(Create(downstream_graph), Write(down_label), run_time=2)
        self.play(Create(upstream_graph), Write(up_label), run_time=2)

        finding_closeness = Tex(
            r"Finding: Downstream $>$ Upstream. \\ The financial sector has strong \textbf{supply-side effects}.",
            font_size=28).to_edge(DOWN, buff=1)
        self.play(Write(finding_closeness))
        self.wait(5)
        self.play(FadeOut(
            VGroup(closeness_text, axes, x_label, y_label, downstream_graph, upstream_graph, down_label, up_label,
                   finding_closeness)))

        # Betweenness Centrality
        betweenness_text = Text("Betweenness Centrality: How important is it as an intermediary?",
                                font_size=32).next_to(title, DOWN, buff=0.5)
        self.play(Write(betweenness_text))

        nodes = {
            "A": [-4, 0, 0], "B": [4, 0, 0], "Finance": [0, 0, 0]
        }
        graph = Graph(
            list(nodes.keys()), [("A", "Finance"), ("Finance", "B")],
            layout=nodes, labels=True, vertex_config={"color": YELLOW, "radius": 0.6}
        )
        path_text = Text("It acts as a bridge for transactions between other sectors.", font_size=24).next_to(graph,
                                                                                                              DOWN)
        self.play(Create(graph), Write(path_text))

        dot = Dot(color=RED).move_to(nodes["A"])
        self.play(Create(dot))
        self.play(MoveAlongPath(dot, graph.edges[("A", "Finance")]), rate_func=linear)
        self.play(MoveAlongPath(dot, graph.edges[("Finance", "B")]), rate_func=linear)
        self.play(FadeOut(dot))

        finding_betweenness = Tex(
            r"Finding: Betweenness fluctuated, rising overall. \\ It is a crucial \textbf{network intermediary}, especially post-GFC.",
            font_size=28).to_edge(DOWN, buff=1)
        self.play(ReplacementTransform(path_text, finding_betweenness))
        self.wait(5)

        self.play(FadeOut(VGroup(title, betweenness_text, graph, finding_betweenness)))
        self.wait(1)

    def explain_causative_matrix(self):
        """Scene 6: Finding 3 - Structural Change via Causative Matrix."""
        title = Title("Finding 3: Structural Change (Causative Matrix)")
        self.play(Write(title))

        # Create the 4-quadrant grid
        axes = Axes(x_range=[-1, 1, 2], y_range=[-1, 1, 2], x_length=8, y_length=6)
        x_label = axes.get_x_axis_label(r"Sum of Off-Diagonal Elements (Feedback from others)")
        y_label = axes.get_y_axis_label(
            r"Diagonal Element, \, C_{ii} \text{ (Internal/External effect)}"
        )

        type1 = Text("Type I\nInternalized\n(More Feedback)", font_size=20, color=GREEN).move_to(axes.c2p(0.5, 0.5))
        type2 = Text("Type II\nExternalized\n(More Feedback)", font_size=20, color=BLUE).move_to(axes.c2p(0.5, -0.5))
        type3 = Text("Type III\nExternalized\n(Less Feedback)", font_size=20, color=RED).move_to(axes.c2p(-0.5, -0.5))
        type4 = Text("Type IV\nInternalized\n(Less Feedback)", font_size=20, color=ORANGE).move_to(axes.c2p(-0.5, 0.5))

        grid_group = VGroup(axes, x_label, y_label, type1, type2, type3, type4)
        self.play(Create(grid_group))

        # Animate the financial sector's position
        dot = Dot(color=YELLOW, radius=0.15)
        dot_label = Text("S36 (Finance)", font_size=20).next_to(dot, UR, buff=0.1)

        pos_1996_2006 = axes.c2p(0.4, -0.3)  # Type II
        pos_2008_2013 = axes.c2p(-0.4, 0.6)  # Type IV
        pos_2013_2018 = axes.c2p(0.6, 0.7)  # Type I

        period_text = Text("Period: 1996-2006 (Pre-GFC)", font_size=28).to_edge(UP, buff=1.5)
        self.play(Write(period_text))
        dot.move_to(pos_1996_2006)
        dot_label.next_to(dot, UR, buff=0.1)
        self.play(Create(dot), Write(dot_label))
        self.wait(3)

        period_text_2 = Text("Period: 2008-2013 (Post-GFC)", font_size=28).to_edge(UP, buff=1.5)
        self.play(ReplacementTransform(period_text, period_text_2))
        self.play(dot.animate.move_to(pos_2008_2013), dot_label.animate.next_to(dot, UR, buff=0.1))
        self.wait(3)

        period_text_3 = Text("Period: 2013-2018", font_size=28).to_edge(UP, buff=1.5)
        self.play(ReplacementTransform(period_text_2, period_text_3))
        self.play(dot.animate.move_to(pos_2013_2018), dot_label.animate.next_to(dot, UR, buff=0.1))
        self.wait(3)

        finding_causative = Tex(
            r"Finding: The financial sector shifted from \textbf{externalized} to \textbf{internalized} after the crisis.",
            font_size=28).to_edge(DOWN)
        self.play(Write(finding_causative))
        self.wait(4)

        self.play(FadeOut(VGroup(title, grid_group, dot, dot_label, period_text_3, finding_causative)))
        self.wait(1)

    def explain_risk_coefficients(self):
        """Scene 7: Finding 4 - Clustering and Symmetry Coefficients."""
        title = Title("Finding 4: Risk and Interdependence")
        self.play(Write(title))

        # Fagiolo Clustering Coefficient
        cluster_text = Text("Fagiolo Clustering: How tightly is the sector connected?", font_size=28).to_edge(UP,
                                                                                                              buff=1.5)
        axes_c = Axes(
            x_range=[1995, 2020, 5], y_range=[0, 0.08, 0.02],
            x_length=6, y_length=4, axis_config={"include_tip": False}
        ).to_edge(LEFT)
        x_label_c = axes_c.get_x_axis_label("Year")
        y_label_c = axes_c.get_y_axis_label("Clustering", edge=LEFT, direction=LEFT)

        cluster_data = [(1996, 0.073), (2001, 0.058), (2006, 0.036), (2013, 0.017), (2018, 0.015)]
        cluster_graph = axes_c.plot_line_graph(
            x_values=[d[0] for d in cluster_data], y_values=[d[1] for d in cluster_data],
            line_color=RED, add_vertex_dots=True
        )
        cluster_finding = Tex(
            r"Finding: Clustering is \textbf{decreasing}. \\ The sector is becoming less tightly linked, \\ potentially reducing direct contagion risk.",
            font_size=24).next_to(axes_c, DOWN, buff=0.5)

        self.play(Write(cluster_text))
        self.play(Create(VGroup(axes_c, x_label_c, y_label_c)))
        self.play(Create(cluster_graph))
        self.play(Write(cluster_finding))
        self.wait(4)

        # Symmetry Coefficient
        symmetry_text = Text("Symmetry: How mutual are the relationships?", font_size=28).to_edge(UP, buff=1.5)
        axes_s = Axes(
            x_range=[1995, 2020, 5], y_range=[0.1, 0.35, 0.05],
            x_length=6, y_length=4, axis_config={"include_tip": False}
        ).to_edge(RIGHT)
        x_label_s = axes_s.get_x_axis_label("Year")
        y_label_s = axes_s.get_y_axis_label("Symmetry", edge=LEFT, direction=LEFT)

        symmetry_data = [(1996, 0.298), (2001, 0.276), (2006, 0.295), (2009, 0.164), (2013, 0.217), (2018, 0.204)]
        symmetry_graph = axes_s.plot_line_graph(
            x_values=[d[0] for d in symmetry_data], y_values=[d[1] for d in symmetry_data],
            line_color=PURPLE, add_vertex_dots=True
        )
        symmetry_finding = Tex(
            r"Finding: Symmetry \textbf{fluctuates}. \\ The balance of resource exchange changes, \\ implying a dynamic risk profile.",
            font_size=24).next_to(axes_s, DOWN, buff=0.5)

        self.play(ReplacementTransform(cluster_text, symmetry_text))
        self.play(Create(VGroup(axes_s, x_label_s, y_label_s)))
        self.play(Create(symmetry_graph))
        self.play(Write(symmetry_finding))
        self.wait(5)

        self.play(FadeOut(
            VGroup(title, symmetry_text, axes_c, x_label_c, y_label_c, cluster_graph, cluster_finding, axes_s,
                   x_label_s, y_label_s, symmetry_graph, symmetry_finding)))
        self.wait(1)

    def show_conclusions(self):
        """Scene 8: Summary of Conclusions and Policy Implications."""
        title = Title("Conclusions and Policy Implications")
        self.play(Write(title))

        c1 = Text("1. The financial sector is a key driver of growth via supply-side effects.",
                  t2c={'supply-side': GREEN}, font_size=28)
        c2 = Text("2. It is a crucial intermediary, but its role shifted after the GFC.", t2c={'intermediary': YELLOW},
                  font_size=28)
        c3 = Text("3. The sector became more internalized, focusing on its own growth.", t2c={'internalized': ORANGE},
                  font_size=28)
        c4 = Text("4. Its risk profile is complex: less clustered but with fluctuating interdependence.",
                  t2c={'risk': RED}, font_size=28)

        conclusions = VGroup(c1, c2, c3, c4).arrange(DOWN, buff=0.5, aligned_edge=LEFT).next_to(title, DOWN, buff=0.5)

        policy = Tex(r"Policy Implication: Balance promoting growth with managing systemic risks.", font_size=32,
                     color=BLUE).to_edge(DOWN)

        self.play(Write(c1))
        self.wait(2)
        self.play(Write(c2))
        self.wait(2)
        self.play(Write(c3))
        self.wait(2)
        self.play(Write(c4))
        self.wait(3)
        self.play(Write(policy))
        self.wait(4)

        self.play(FadeOut(VGroup(title, conclusions, policy)))
        self.wait(1)

    def show_end_screen(self):
        """Scene 9: End screen."""
        end_text = Text("Animation created with Manim", font_size=40)
        credit_text = Text("Based on the 2024 paper by Khan, Li, and Mahsud", font_size=28, slant=ITALIC).next_to(
            end_text, DOWN)

        self.play(Write(end_text))
        self.play(Write(credit_text))
        self.wait(5)
        self.play(FadeOut(VGroup(end_text, credit_text)))
