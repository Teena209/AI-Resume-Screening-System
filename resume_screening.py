print("====================================")
print("     AI RESUME SCREENING SYSTEM")
print("====================================")

candidates = [
    {"name": "John", "skills": ["Python", "Java", "SQL", "Git"], "experience": 3},
    {"name": "David", "skills": ["Python", "HTML", "CSS"], "experience": 2},
    {"name": "Alex", "skills": ["Java", "C++"], "experience": 1},
    {"name": "Sophia", "skills": ["Python", "SQL", "Git", "AWS"], "experience": 4}
]

required_skills = ["Python", "SQL", "Git"]

results = []

for candidate in candidates:
    score = 0

    for skill in required_skills:
        if skill in candidate["skills"]:
            score += 20

    score += candidate["experience"] * 10

    results.append((candidate["name"], score))

results.sort(key=lambda x: x[1], reverse=True)

print("\n===== SCREENING REPORT =====\n")

for i, (name, score) in enumerate(results, start=1):
    print(f"Rank {i}: {name} - Score {score}")

print("\nSelected Candidate:", results[0][0])