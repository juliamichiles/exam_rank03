#!/usr/bin/env python3
import os
import sys
import time
import random
import importlib.util
import io


# --- CONFIGURATION ---
LEVELS_CONFIG = {
    1: ".level_1",
    2: ".level_2",
    3: ".level_3",
    4: ".level_4",
    5: ".level_5",
    6: ".level_6"
}

SUBJECT_FILE_NAME = "subject.txt"
TESTER_FILE_NAME = "main.py"
EXPECTED_FILE_NAME = "expected"
RENDERING_DIR = "rendu"

class ExamSession:
    def __init__(self):
        self.levels = sorted(list(LEVELS_CONFIG.keys()))
        self.current_level_index = 0
        self.selected_exercises = {}
        self.start_time = time.time()
        
        self._setup_rendu()
        self._pool_exercises()

    def _setup_rendu(self):
        if not os.path.exists(RENDERING_DIR):
            os.makedirs(RENDERING_DIR)
        print(f"✨ Exam environment initialized. Workspace: ./{RENDERING_DIR}/\n")

    def _pool_exercises(self):
        for lvl, folder in LEVELS_CONFIG.items():
            if not os.path.isdir(folder):
                continue
            exercises = [ex for ex in os.listdir(folder) if os.path.isdir(os.path.join(folder, ex))]
            if exercises:
                self.selected_exercises[lvl] = random.choice(exercises)

    def display_subject(self, lvl, ex_name):
        lvl_folder = LEVELS_CONFIG[lvl]
        subject_path = os.path.join(lvl_folder, ex_name, SUBJECT_FILE_NAME)
        
        print("\n" + "="*60)
        print(f" LEVEL {lvl} - Exercise: {ex_name} ")
        print("="*60 + "\n")
        
        if os.path.exists(subject_path):
            with open(subject_path, "r", encoding="utf-8") as f:
                print(f.read())
        else:
            print(f"❌ Subject file not found at: {subject_path}")
        print("\n" + "="*60 + "\n")

    def _manual_fallback(self):
        """Helper method for manual correction prompt."""
        print("ℹ️  No automated test suite found for this exercise yet.")
        user_input = input("   Did your code work and match perfectly? (yes/no): ").strip().lower()
        return user_input in ['y', 'yes']

    def check_exercise(self, lvl, ex_name):
        """Checks for main.py/expected. Runs automated test if found; otherwise falls back to manual query."""
        print(f"🔍 Grading Level {lvl}: {ex_name}...")
        
        lvl_folder = LEVELS_CONFIG[lvl]
        user_file_path = os.path.join(RENDERING_DIR, ex_name, f"{ex_name}.py")
        tester_script_path = os.path.join(lvl_folder, ex_name, TESTER_FILE_NAME)
        expected_output_path = os.path.join(lvl_folder, ex_name, EXPECTED_FILE_NAME)

        # 1. Verification: Check if user file exists at all
        if not os.path.exists(user_file_path):
            print(f"❌ Missing submission file: {user_file_path}")
            return False

        # 2. Dynamic Fallback Check: Are automated test files available?
        if not os.path.exists(tester_script_path) or not os.path.exists(expected_output_path):
            return self._manual_fallback()

        # 3. Automated Test Execution (if files exist)
        print("⚙️  Running automated test suite...")
        try:
            # Dynamic Import of User Code
            spec = importlib.util.spec_from_file_location(ex_name, user_file_path)
            user_module = importlib.util.module_from_spec(spec)
            sys.modules[ex_name] = user_module
            spec.loader.exec_module(user_module)

            # Dynamic Import of Hidden Tester Script
            t_spec = importlib.util.spec_from_file_location("tester", tester_script_path)
            tester_module = importlib.util.module_from_spec(t_spec)
            t_spec.loader.exec_module(tester_module)

            # Capture Output
            captured_output = io.StringIO()
            sys.stdout = captured_output
            
            # Execute the grading script using the user module
            tester_module.run_tests(user_module)
            
            # Restore standard output tracking
            sys.stdout = sys.__stdout__
            user_output = captured_output.getvalue().strip()

        except Exception as e:
            # Safeguard: Restore stdout if user script crashes or handles imports poorly
            sys.stdout = sys.__stdout__
            print(f"❌ Execution Crash / Syntax Error: \n{e}")
            return False

        # Compare with expected output file
        with open(expected_output_path, "r", encoding="utf-8") as f:
            expected_output = f.read().strip()

        if user_output == expected_output:
            return True
        else:
            print("\n🟥 Diff Failed!")
            print("--- Expected ---")
            print(expected_output)
            print("--- Your Output ---")
            print(user_output)
            print("----------------")
            return False

    def start(self):
        print("=========================================")
        print("        42 EXAM RANK 03 SIMULATOR        ")
        print("=========================================\n")
        
        while self.current_level_index < len(self.levels):
            current_lvl = self.levels[self.current_level_index]
            
            if current_lvl not in self.selected_exercises:
                self.current_level_index += 1
                continue
                
            ex_name = self.selected_exercises[current_lvl]
            os.makedirs(os.path.join(RENDERING_DIR, ex_name), exist_ok=True)
            
            while True:
                elapsed = time.strftime("%H:%M:%S", time.gmtime(time.time() - self.start_time))
                print(f"[Time elapsed: {elapsed}]")
                self.display_subject(current_lvl, ex_name)
                
                print("Options:")
                print("  [grademe] Submit / Grade exercise")
                print("  [skip] Skip exercise (Next level)")
                print("  [exit] Exit Exam")
                
                choice = input("\nWhat do you want to do?: ").strip()
                
                if choice == 'grademe':
                    if self.check_exercise(current_lvl, ex_name):
                        print(f"\n🟩 SUCCESS! You passed Level {current_lvl}.\n")
                        self.current_level_index += 1
                        break
                    else:
                        print(f"\n❌ FAIL! Check your work in ./{RENDERING_DIR}/{ex_name}/\n")
                elif choice == 'skip':
                    print(f"\n⏭️ Skipping Level {current_lvl}...")
                    self.current_level_index += 1
                    break
                elif choice == 'exit':
                    print("\n👋 Exiting exam simulator. Keep practicing!")
                    sys.exit(0)
                else:
                    print("\n❌ Invalid choice.")
                    
        print("=========================================")
        print("🎉 CONGRATULATIONS! You finished the exam! 🎉")
        print("=========================================")


if __name__ == "__main__":
    try:
        session = ExamSession()
        session.start()
    except KeyboardInterrupt:
        sys.stdout = sys.__stdout__ # Guarantee stdout recovery on forced exit
        print("\n\n👋 Exam interrupted. Exiting.")
        sys.exit(0)
