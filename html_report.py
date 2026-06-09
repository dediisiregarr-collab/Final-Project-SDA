def generate_report(stats):

    report = []

    report.append(
        f"Jumlah node HTML adalah {stats['nodes']}."
    )

    report.append(
        f"Jumlah leaf node adalah {stats['leaf']}."
    )

    report.append(
        f"Kedalaman tree adalah {stats['depth']}."
    )

    report.append(
        f"Tag yang paling sering muncul adalah {stats['most_used_tag']} sebanyak {stats['most_used_count']} kali."
    )

    if stats['depth'] <= 2:

        report.append(
            "Struktur HTML tergolong sederhana."
        )

    elif stats['depth'] <= 4:

        report.append(
            "Struktur HTML memiliki kompleksitas sedang."
        )

    else:

        report.append(
            "Struktur HTML tergolong kompleks karena memiliki banyak level nesting."
        )

    return report