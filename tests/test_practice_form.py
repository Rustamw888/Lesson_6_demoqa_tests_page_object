from selene import have, command
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


class student:
    name = "Rustam"
    surname = "Tyapaev"
    email = "test@gmail.com"
    gender = "Other"
    mobile_number = "1234567890"
    birth_day = "19"
    birth_month = "11"
    birth_month_str = "December"
    birth_year = "1988"
    current_address = "ulica Pushkina dom Kolotushkina"
    state = "NCR"
    city = "Delhi"


class Gender:
    male = 'Male'
    female = 'Female'
    other = 'Other'


class Hobbies:
    sports = 'Sports'
    reading = 'Reading'
    music = 'Music'


class Subjects:
    computer_science = 'Computer Science'
    english = 'English'


class State:
    ncr = 'NCR'
    uttar_pradesh = 'Uttar Pradesh'
    haryana = 'Haryana'
    rajasthan = 'Rajasthan'


class City:
    delhi = 'Delhi'
    gurgaon = 'Gurgaon'
    noida = 'Noida'


class Months:
    january = '0', 'January'
    february = '1', 'February'
    march = '2', 'March'
    april = '3', 'April'
    may = '4', 'May'
    june = '5', 'June'
    july = '6', 'July'
    august = '7', 'August'
    september = '8', 'September'
    october = '9', 'October'
    november = '10', 'November'
    december = '11', 'December'


def resource(path):
    import Lesson_5_demoqa_tests
    Lesson_5_demoqa_tests.__file__
    from pathlib import Path
    return str(
        Path(Lesson_5_demoqa_tests.__file__)
        .parent
        .parent
        .joinpath(f'resources/{path}')
    )


def cell_of_rows(index, should_have_texts: list[str]):
    browser.element('.modal-dialog').all("table tr")[index].all('td').should(
        have.exact_texts(*should_have_texts))


def test_register_student():
    # Given
    browser.open('/automation-practice-form')

    # When
    s('#firstName').type(student.name)
    s('#lastName').type(student.surname)
    s('#userEmail').type(student.email)

    gender_group = s('#genterWrapper')
    gender_group.all('.custom-radio').element_by(have.exact_text(Gender.other)).click()

    mobile_number = s('#userNumber')
    mobile_number.type(student.mobile_number)

    s('#dateOfBirthInput').click()
    s(f'.react-datepicker__year-select').element(f'[value="{student.birth_year}"]').click()
    s(f'.react-datepicker__month-select').element(f'[value="{Months.december[0]}"]').click()
    s(f'.react-datepicker__day--0{student.birth_day}').click()

    s('#subjectsInput').type(Subjects.computer_science).press_enter()
    s('#subjectsInput').type(Subjects.english).press_enter()

    s('#hobbiesWrapper').all('.custom-checkbox').element_by(have.exact_text(Hobbies.sports)).click()
    s('#hobbiesWrapper').all('.custom-checkbox').element_by(have.exact_text(Hobbies.reading)).click()
    s('#hobbiesWrapper').all('.custom-checkbox').element_by(have.exact_text(Hobbies.music)).click()

    s('#uploadPicture').send_keys(
        resource('picture.png'))

    s('#currentAddress').type(student.current_address)

    s('#state').element('input').type(State.ncr).press_tab()
    s('#city').element('input').type(City.delhi).press_tab()
    s("#submit").perform(command.js.click)

    # Then
    cell_of_rows(index=1, should_have_texts=[
        'Student Name',
        f'{student.name} {student.surname}'
    ])
    cell_of_rows(index=2, should_have_texts=[
        'Student Email',
        student.email
    ])
    cell_of_rows(index=3, should_have_texts=[
        'Gender',
        Gender.other
    ])
    cell_of_rows(index=4, should_have_texts=[
        'Mobile',
        student.mobile_number
    ])
    cell_of_rows(index=5, should_have_texts=[
        'Date of Birth',
        f'{student.birth_day} {Months.december[1]},{student.birth_year}'
    ])
    cell_of_rows(index=6, should_have_texts=[
        'Subjects',
        f'{Subjects.computer_science}, {Subjects.english}'
    ])
    cell_of_rows(index=7, should_have_texts=[
        'Hobbies',
        f'{Hobbies.sports}, {Hobbies.reading}, {Hobbies.music}'
    ])
    cell_of_rows(index=8, should_have_texts=[
        'Picture',
        'picture.png'
    ])
    cell_of_rows(index=9, should_have_texts=[
        'Address',
        student.current_address
    ])
    cell_of_rows(index=10, should_have_texts=[
        'State and City',
        f'{State.ncr} {City.delhi}'
    ])
