#!/usr/bin/env python3
import os
import random
import sys
import time


# --- CONFIGURATION ---
# Define your exam path layout.
# Key: Level identifier, Value: Folder name containing the exercises for that level
LEVELS_CONFIG = {
    1: "level_1",
    2: "level_2",
    3: "level_3",
    4: "level_4",
    5: "level_5",
    6: "level_6"
}

# The name of the subject file inside the exercise directory
SUBJECT_FILE_NAME = "subject.txt"
# Where the user will write their code during the simulated exam
RENDERING_DIR = "rendu"

class ExamSession:
    def __init__(self):
        self.levels = sorted(list(LEVELS_CONFIG.keys()))
        self.current_level_index = 1
        self.selected_exercises = {}
        self.start_time = time.time()

        # Prepare the simulated environment
        self._setup_rendu()
        self._pool_exercises()

    def _setup_rendu(self):
        """Creates a clean 'rendu' directory at the start of the exam."""
        if not os.path.exists(RENDERING_DIR):
            os.makedirs(RENDERING_DIR)
        print(
                "✨ Exam environment initialized. Your work "
                f"directory is: ./{RENDERING_DIR}/\n"
        )

    def _pool_exercises(self):
        """Pre-selects a random exercise for each configured level."""
        for lvl, folder in LEVELS_CONFIG.items():
            if not os.path.isdir(folder):
                print(
                        f"\tWarning: Folder '{folder}' for "
                        f"level {lvl} not found. Skipping."
                )
                continue

            # Get all subdirectories (exercises) inside the level folder
            exercises = [
                    ex for ex in os.listdir(folder) 
                    if os.path.isdir(os.path.join(folder, ex))
            ]

            if exercises:
                self.selected_exercises[lvl] = random.choice(exercises)
            else:
                print(f"\tWarning: No exercises found inside '{folder}'.")

    def display_subject(self, lvl, ex_name):
        """Finds and displays the content of the subject file."""
        lvl_folder = LEVELS_CONFIG[lvl]
        subject_path = os.path.join(lvl_folder, ex_name, SUBJECT_FILE_NAME)

        print("\n" + "="*60)
        print(f" LEVEL {lvl} - Exercise: {ex_name} ")
        print("="*60 + "\n")

        if os.path.exists(subject_path):
            with open(subject_path, "r", encoding="utf-8") as f:
                print(f.read())
        else:
            # Fallback if subject.txt doesn't exist
            print(f"❌ Subject file not found at: {subject_path}")
            print(
                    f"Please create your solution inside "
                    f"./{RENDERING_DIR}/{ex_name}/"
            )

        print("\n" + "="*60 + "\n")

    def check_exercise(self, lvl, ex_name):
        """
        PLACEHOLDER FOR CORRECTION
        This is where you will implement scalable automated checks later.
        """
        print(f"🔍 Grading Level {lvl}: {ex_name}...")

        # Simulating user input verification for now
        # When you implement correction, you can replace this prompt with subprocess compilation/execution
        user_input = input("Did your code compile and match perfectly? (yes/no): ").strip().lower()
        if user_input in ['y', 'yes']:
            return True
        return False

    def start(self):
        print("=========================================")
        print("        42 EXAM RANK 03 SIMULATOR        ")
        print("=========================================\n")

        while self.current_level_index < len(self.levels):
            current_lvl = self.levels[self.current_level_index]

            if current_lvl not in self.selected_exercises:
                print(f"Skipping Level {current_lvl} (No exercises configured).")
                self.current_level_index += 1
                continue

            ex_name = self.selected_exercises[current_lvl]

            # Guide the student where to place their files
            os.makedirs(os.path.join(RENDERING_DIR, ex_name), exist_ok=True)

            while True:
                elapsed = time.strftime("%H:%M:%S", time.gmtime(time.time() - self.start_time))
                print(f"[Time elapsed: {elapsed}]")
                self.display_subject(current_lvl, ex_name)

                print("Options:")
                print("  [1] Submit / Grade exercise")
                print("  [2] Re-read subject")
                print("  [3] Forfeit / Exit Exam")

                choice = input("\nWhat do you want to do? (1-3): ").strip()

                if choice == '1':
                    success = self.check_exercise(current_lvl, ex_name)
                    if success:
                        print(f"\n🟩 SUCCESS! You passed Level {current_lvl}.\n")
                        self.current_level_index += 1
                        break # Break inner loop to progress to next level
                    else:
                        print(f"\n🟥 FAIL! Try again. Check your code in ./{RENDERING_DIR}/{ex_name}/\n")
                elif choice == '2':
                    continue
                elif choice == '3':
                    print("\n👋 Exiting exam simulator. Better luck next time!")
                    sys.exit(0)
                else:
                    print("\n❌ Invalid choice.")

        print("=========================================")
        print("🎉 CONGRATULATIONS! You passed the exam! 🎉")
        print("=========================================")

if __name__ == "__main__":
    try:
        session = ExamSession()
        session.start()
    except KeyboardInterrupt:
        print("\n\n👋 Exam interrupted. Exiting.")
        sys.exit(0)
