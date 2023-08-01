class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f"Imię: {self.name}, Nazwisko: {self.surname}"


class Teacher:
    def __init__(self, name, surname, subject, grades):
        self.name = name
        self.surname = surname
        self.subject = subject
        self.grades = grades

    def __repr__(self):
        return f"Imię: {self.name}, Nazwisko: {self.surname}, Zajęcia: {self.subject}, Klasy: {self.grades}"

class Tutor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f"Imię: {self.name}, Nazwisko: {self.surname}"


our_school = {
    "klasy": {
        "1a": {
            "uczniowie": [Student(name="Arek", surname="Bury")],
            "wychowawca": [Tutor(name="Adam", surname="Mickiewicz")]
        },
        "2a": {
            "uczniowie": [Student(name="Jan", surname="Nowak")],
            "wychowawca": [Tutor(name="Henryk", surname="Sienkiewicz")]


        },
    },
    "nauczyciele": [Teacher(name="Roman", surname="Giertych", subject="Łacina", grades=["1a", "2b"])]
}




def create_new_grade(grade):
    our_school["klasy"][grade] = {
        "uczniowie": [],
        "wychowawca": []
    }

def create_student_in_existing_grade(name, surname, grade):
    our_school["klasy"][grade]["uczniowie"].append(Student(name=name, surname=surname))

def create_new_student(name, surname, grade):
    grade_exists = our_school.get("klasy").get(grade)
    if not grade_exists:
        create_new_grade(grade)
    create_student_in_existing_grade(name, surname, grade)


def create_tutor_in_existing_grade(name, surname, grade):
    our_school["klasy"][grade]["wychowawca"].append(Tutor(name=name, surname=surname))


def create_new_tutor(name, surname, grade):
    grade_exists = our_school.get("klasy").get(grade)
    if not grade_exists:
        create_new_grade(grade)
    create_tutor_in_existing_grade(name, surname, grade)


def create_new_teacher(name, surname, subject, grades):
    our_school["nauczyciele"].append(Teacher(name=name, surname=surname, subject=subject, grades=grades))


def find_grade_by_class_number(class_number):
    for grade_number, grade in our_school["klasy"].items():
        if grade_number == class_number:
            return f"Uczniowie to: {grade['uczniowie']} wychowawca to: {grade['wychowawca']}"
    return "Niestety nie znaleziono twojej klasy"


def find_class_teachers(class_number):
    found_teachers = []
    for teacher in our_school.get("nauczyciele"):
        if class_number in teacher.grades:
            found_teachers.append(teacher)
    return found_teachers


def find_student_by_name(name, surname):
    our_text = ""
    for grade_number, grade in our_school["klasy"].items():
        for student in grade.get("uczniowie"):
            if name == student.name and surname == student.surname:
                teachers = find_class_teachers(grade_number)
                for teacher in teachers:
                    our_text += f" Nauczyciel: {teacher.name} {teacher.surname} z przedmiotem: {teacher.subject} \n"
                return our_text
    return "Niestety twoja klasa nie ma żadnych zajęć"


def find_teacher_by_name(name, surname):
    our_text = ""
    for teacher in our_school["nauczyciele"]:
        if name == teacher.name and surname == teacher.surname:
            our_text += f"{teacher.name} {teacher.surname} uczy w klasie : {teacher.grades} \n"
            return our_text
        else:
            return "Niestety nie uczysz żadnej klasy"


def find_tutor_by_name(name, surname):
    our_text = ""
    for grade_number, grade in our_school["klasy"].items():
        for tutor in grade.get("wychowawca"):
            if name == tutor.name and surname == tutor.surname:
                our_text += f" Wychowujesz uczniów klasy: {grade_number} czyli: {grade.get('uczniowie')} "
                return our_text
            else:
                return "Niestety nie jesteś wychowawcą żadnego ucznia"


initial_menu = "Witaj w swojej szkole. Podaj proszę co chcesz zrobić:\n 1.Uwtórz\n 2.Zarządzaj\n 3.Koniec\n"
create_menu = "Podaj jakiego użytkownika chcesz utworzyć:\n 1.Uczeń \n 2.Nauczyciel \n 3.Wychowawca \n 4.Koniec"
manage_menu = "Podaj kim chcesz zarządzać: \n 1.Klasa \n 2.Uczeń \n 3.Nauczyciel \n 4.Wychowawca \n 5.Koniec"
finish_program = False
while not finish_program:
    main_guess = input(initial_menu)
    if main_guess == "1":
        #wchodzimy w tryb dodawania czegokolwiek do naszej szkoly
        create_input = input(create_menu)
        if create_input == "1":
            name = input("Podaj imię ucznia")
            surname = input("Podaj nazwisko ucznia")
            grade = input("Podaj klasę ucznia")
            create_new_student(name, surname, grade)
            print(our_school)
        elif create_input == "2":
            name = input("Podaj imię nauczyciela")
            surname = input("Podaj nazwisko nauczyciela")
            subject = input("Podaj przedmiot nauczyciela")
            grades = input("Podaj klasę nuczyciela")
            create_new_teacher(name, surname, subject, grades)
            print(our_school)
        elif create_input == "3":
            name = input("Podaj imię wychowawcy")
            surname = input("Podaj nazwisko wychowawcy")
            grade = input("Podaj klasę wychowawcy")
            create_new_tutor(name, surname, grade)
            print(our_school)
        elif create_input =="4":
            finish_program=True


    elif main_guess == "2":
        manage_input = input(manage_menu)
        if manage_input == "1":
            class_number = input("Podaj nazwę klasy")
            text_to_display = find_grade_by_class_number(class_number)
            print(text_to_display)
        elif manage_input == "2":
            student_name = input("Podaj imię ucznia: ")
            student_surname = input("Podaj nazwisko ucznia: ")
            text = find_student_by_name(student_name, student_surname)
            print(text)
        elif manage_input == "3":
            teacher_name = input("Podaj imię nauczyciela: ")
            teacher_surname = input("Podaj nazwisko nauczyciela: ")
            text = find_teacher_by_name(teacher_name, teacher_surname)
            print(text)
        elif manage_input == "4":
            tutor_name = input("Podaj imię wychowawcy: ")
            tutor_surname = input("Podaj nazwisko wychowawcy: ")
            text = find_tutor_by_name(tutor_name, tutor_surname)
            print(text)
        elif manage_input == "5":
            finish_program=True


    elif main_guess == "3":
        finish_program=True
