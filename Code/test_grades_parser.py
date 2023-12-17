from Code import grades_parser

def test_calculate_average_grade():
    test_data = [
        {'Final': '49.0'},
        {'Final': '48.0'},
        {'Final': '44.0'},
        {'Final': '47.0'},
        {'Final': '45.0'},
        {'Final': '46.0'},
        {'Final': '43.0'},
        {'Final': '50.0'},
        {'Final': '48.0'},
        {'Final': '45.0'},
    ]

    average_grade = grades_parser.calculate_average_grade(test_data)
    assert average_grade == 46.5

    empty_data = []
    average_grade_empty = grades_parser.calculate_average_grade(empty_data)
    assert average_grade_empty is None
