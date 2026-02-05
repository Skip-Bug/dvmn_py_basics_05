import file_operations
import random
import os
from faker import Faker
from skills_list import skills
from letters_mapping import ruinic_letters

MIN_STAT = 3
MAX_STAT = 18
NAM_NPC = 10


def main():
    os.makedirs("NPC", exist_ok=True)
    fake = Faker("ru_RU")
    runic_skills = []
    for skill in skills:
        runic_skill = skill
        for char, runic_char in ruinic_letters.items():
            runic_skill = runic_skill.replace(char, runic_char)
        runic_skills.append(runic_skill)
    for namber in range(NAM_NPC):
        basic_skills = random.sample(runic_skills, 3)
        context = {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "job": fake.job(),
            "town": fake.city(),
            "strength": random.randint(MIN_STAT, MAX_STAT),
            "agility": random.randint(MIN_STAT, MAX_STAT),
            "endurance": random.randint(MIN_STAT, MAX_STAT),
            "intelligence": random.randint(MIN_STAT, MAX_STAT),
            "luck": random.randint(MIN_STAT, MAX_STAT),
            "skill_1": basic_skills[0],
            "skill_2": basic_skills[1],
            "skill_3": basic_skills[2]
            }
        output_path = "NPC/result_{}.svg".format(namber + 1)
        file_operations.render_template("charsheet.svg", output_path, context)


if __name__ == "__main__":
    main()
