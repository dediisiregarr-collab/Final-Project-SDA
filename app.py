from flask import Flask, render_template, request, send_file

from parser import tokenize
from validator import validate

from html_analyzer import unique_tags, most_used_tag

from html_report import generate_report

from error_classifier import classify_error
from semantic_checker import check_semantic_tags

from html_health import (
    calculate_health_score,
    health_level
)

from recommendation import (
    generate_recommendations
)

from tag_ranking import (
    get_tag_ranking
)

from syntax_tree import (
    build_tree,
    count_nodes,
    count_leaf_nodes,
    tree_depth,
    level_order
)

import os

app = Flask(__name__)

latest_report = ""


# =========================
# Konversi Tree ke Teks
# =========================
def tree_to_text(node, level=0):

    if node is None:
        return ""

    result = ""

    if level == 0:
        result += node.tag + "\n"
    else:
        result += ("│   " * (level - 1))
        result += "└── " + node.tag + "\n"

    for child in node.children:
        result += tree_to_text(child, level + 1)

    return result


# =========================
# Route Utama
# =========================
@app.route("/", methods=["GET", "POST"])
def index():
    
    global latest_report
    recommendations = []

    ranking = []
    
    report = []
    
    stack_history = []

    result = ""
    tree = ""

    preorder_result = []
    postorder_result = []
    level_order_result = []

    stats = {}

    html_input = ""

    status = None
    found_semantic = []
    missing_semantic = []

    recommendations = []
    ranking = []

    error_type = ""

    if request.method == "POST":

        # =========================
        # Input dari Upload File
        # =========================
        if "html_file" in request.files:

            file = request.files["html_file"]

            if file.filename != "":
                html_input = file.read().decode("utf-8")

        # =========================
        # Input dari Text Area
        # =========================
        if html_input == "":
            html_input = request.form.get("html", "")

        # =========================
        # Parsing
        # =========================
        tokens = tokenize(html_input)

        # =========================
        # Validasi
        # =========================
        valid, message, history = validate(tokens)
        
        if not valid:
            error_type = classify_error(message)
        
        
        stack_history = history

        result = message
        status = valid

        # =========================
        # Jika HTML Valid
        # =========================
        if valid:

            root = build_tree(tokens)

            tree = tree_to_text(root)
            
            

            # =========================
            # Preorder
            # =========================
            def preorder_collect(node):

                if node is None:
                    return

                preorder_result.append(node.tag)

                for child in node.children:
                    preorder_collect(child)

            # =========================
            # Postorder
            # =========================
            def postorder_collect(node):

                if node is None:
                    return

                for child in node.children:
                    postorder_collect(child)

                postorder_result.append(node.tag)

            preorder_collect(root)
            postorder_collect(root)
            level_order_result = level_order(root)
            # =========================
            # Statistik
            # =========================
            stats = {
                "nodes": count_nodes(root),
                "leaf": count_leaf_nodes(root),
                "depth": tree_depth(root)
            }
            
            # Menghitung skor kompleksitas HTML
            score = count_nodes(root) + tree_depth(root)

            stats["complexity_score"] = score

            if score <= 10:
                stats["complexity_level"] = "Simple"

            elif score <= 20:
                stats["complexity_level"] = "Medium"

            else:
                stats["complexity_level"] = "Complex"
                
            # =========================
            # Analisis HTML
            # =========================
            stats["unique_tags"] = ", ".join(unique_tags(root))
            
            tag_list = unique_tags(root)

            found_semantic, missing_semantic = check_semantic_tags(tag_list)

            most_tags, count = most_used_tag(root)

            stats["most_used_tag"] = ", ".join(most_tags)
            stats["most_used_count"] = count

            # Hitung skor kesehatan HTML
            stats["health_score"] = calculate_health_score(stats)

            stats["health_level"] = health_level(
                stats["health_score"]
            )

            recommendations = generate_recommendations(stats)

            ranking = get_tag_ranking(root)

            report = generate_report(stats)
            latest_report = f"""
            HTML VALIDATOR REPORT

            ================================

            Status : VALID

            Jumlah Node : {stats['nodes']}
            Jumlah Leaf Node : {stats['leaf']}
            Kedalaman Tree : {stats['depth']}

            Complexity Score : {stats['complexity_score']}
            Complexity Level : {stats['complexity_level']}

            Tag Terbanyak : {stats['most_used_tag']}
            Jumlah Kemunculan : {stats['most_used_count']}

            Tag Unik :
            {stats['unique_tags']}

            Traversal:

            Preorder :
            {' '.join(preorder_result)}

            Postorder :
            {' '.join(postorder_result)}

            Level Order :
            {' '.join(level_order_result)}

            ================================
            
            """
            found_semantic = found_semantic if valid else []
            missing_semantic = missing_semantic if valid else []


    return render_template(
        "index.html",
        result=result,
        tree=tree,
        preorder=" ".join(preorder_result),
        postorder=" ".join(postorder_result),
        level_order=" ".join(level_order_result),
        stats=stats,
        html_input=html_input,
        status=status,
        report=report,
        stack_history=stack_history,
        recommendations=recommendations,
        ranking=ranking,
        found_semantic=found_semantic,
        missing_semantic=missing_semantic,
        error_type=error_type
    )

@app.route("/download-report")
def download_report():

    global latest_report

    if latest_report == "":
        latest_report = "Belum ada laporan yang dibuat."

    with open("report.txt", "w", encoding="utf-8") as f:
        f.write(latest_report)

    return send_file(
        "report.txt",
        as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)