import os
from selene import browser, have

name = "Kirill"
surname = "Semin"
email = "testemail1324@gmail.com"
phone = "9803628839"
gender = "Male"
birthDate = {'day': 20, 'month': 'January', 'year': 1999}
subjects = ["Maths", "English", "Physics", "Chemistry", "Computer Science"]
hobbies = ["Sports", "Reading"]
address = "Emlutina 13"
state = "NCR"
city = "Delhi"
imageName = "cat.jpg"

def test_success_filling_form():
    browser.open("https://demoqa.com/automation-practice-form")
    browser.element("#firstName").set_value(name)
    browser.element("#lastName").set_value(surname)
    browser.element("#userEmail").set_value(email)
    browser.all("[name='gender']").element_by(have.value(gender)).element('..').element('label').click()
    browser.element("#userNumber").set_value(phone)
    browser.element("#dateOfBirthInput").click()
    browser.element('.react-datepicker__year-select').element(f'[value="{birthDate['year']}"]').click()
    browser.element('.react-datepicker__month-select').all("option").element_by(have.text(birthDate["month"])).click()
    browser.element(f'.react-datepicker__day--0{birthDate["day"]}').click()
    for subj in subjects:
        browser.element("#subjectsInput").set_value(subj).press_enter()
    for hobby in hobbies:
        browser.all("label[for^='hobbies']").element_by(have.text(hobby)).click()
    browser.element("#uploadPicture").set_value(os.path.abspath(f"lesson_5/{imageName}"))
    browser.element("#currentAddress").set_value(address)
    browser.element("#state").click()
    browser.all("[id^='react-select']").element_by(have.text(state)).click()
    browser.element("#city").click()
    browser.all("[id^='react-select']").element_by(have.text(city)).click()
    browser.element("#submit").submit()

    browser.element('.table-responsive').all('td').should(have.texts(
            'Student Name', f"{name} {surname}",
            'Student Email', email,
            'Gender', gender,
            'Mobile', phone,
            'Date of Birth', f"{birthDate['day']} {birthDate['month']},{birthDate['year']}",
            'Subjects', ', '.join(subjects),
            'Hobbies', ', '.join(hobbies),
            'Picture', imageName,
            'Address', address,
            'State and City', f"{state} {city}"))
