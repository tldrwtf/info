# ==========================================
# TASK 5.1: Student Class
# ==========================================
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []

    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.grades.append(grade)
        else:
            print("Invalid grade")

    def grade_avg(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def info(self):
        print(f"Student: {self.name}, Age: {self.age}, Avg: {self.grade_avg():.2f}")

# ==========================================
# TASK 5.2: Encapsulation (User)
# ==========================================
class User:
    def __init__(self, username):
        self.username = username
        self._password = None # Protected

    def set_password(self, new_pass):
        if len(new_pass) >= 8:
            self._password = new_pass
            print("Password updated.")
        else:
            print("Password too short (min 8 chars).")

    def get_password(self):
        # Return masked version for security simulation
        if self._password:
            return "*" * len(self._password)
        return "No password set"

# ==========================================
# TASK 5.3: RPG Battle (Inheritance)
# ==========================================
class Character:
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk

    def attack(self, target):
        print(f"{self.name} attacks {target.name} for {self.atk} dmg!")
        target.take_damage(self.atk)

    def take_damage(self, amount):
        self.hp -= amount
        print(f"{self.name} has {self.hp} HP left.")

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, hp=100, atk=15)

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, hp=60, atk=25)
    
    def special_attack(self, target):
        dmg = self.atk * 1.5
        print(f"{self.name} casts FIREBALL on {target.name} for {dmg} dmg!")
        target.take_damage(dmg)

class EvilWizard(Character):
    def __init__(self):
        super().__init__("Voldemort", hp=150, atk=20)

    def regenerate(self):
        self.hp += 10
        print(f"{self.name} regenerates 10 HP! Now at {self.hp}.")

def battle_sim():
    hero = Warrior("Conan")
    boss = EvilWizard()
    
    round = 1
    while hero.hp > 0 and boss.hp > 0:
        print(f"\n--- Round {round} ---")
        hero.attack(boss)
        if boss.hp <= 0:
            print("Hero Wins!")
            break
            
        boss.attack(hero)
        if round % 2 == 0:
            boss.regenerate()
            
        if hero.hp <= 0:
            print("Game Over.")
            break
        round += 1

if __name__ == "__main__":
    # Student Test
    s = Student("John", 20)
    s.add_grade(90)
    s.add_grade(80)
    s.info()
    
    # RPG Test
    battle_sim()
