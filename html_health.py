def calculate_health_score(stats):

    score = 0

    if stats["depth"] <= 5:
        score += 25

    if stats["nodes"] <= 20:
        score += 25

    if stats["leaf"] >= 1:
        score += 25

    if len(stats["unique_tags"].split(",")) >= 3:
        score += 25

    return score


def health_level(score):

    if score >= 90:
        return "Excellent"

    elif score >= 70:
        return "Good"

    elif score >= 50:
        return "Average"

    return "Poor"
