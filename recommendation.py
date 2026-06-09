def generate_recommendations(stats):

    recommendations = []

    if stats["depth"] > 5:
        recommendations.append(
            "Kurangi nested tag yang terlalu dalam."
        )

    if stats["nodes"] > 30:
        recommendations.append(
            "Struktur HTML cukup besar, pertimbangkan pemecahan komponen."
        )

    if "header" not in stats["unique_tags"]:
        recommendations.append(
            "Pertimbangkan menggunakan tag semantic <header>."
        )

    if "main" not in stats["unique_tags"]:
        recommendations.append(
            "Pertimbangkan menggunakan tag semantic <main>."
        )

    if "footer" not in stats["unique_tags"]:
        recommendations.append(
            "Pertimbangkan menggunakan tag semantic <footer>."
        )

    if len(recommendations) == 0:
        recommendations.append(
            "Struktur HTML sudah sangat baik."
        )

    return recommendations