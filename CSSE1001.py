from Course import *

class CSSE1001(Course):
    COURSE_CODE = 'CSSE1001'
    UNITS = 2
    ASSESSMENT = {
    "A1": [15, 100],
    "A2": [15, 100],
    "A3": [15, 100],
    "Final Exam": [55, 100]
    }

    def calculate_grade(self) -> int | None:
        Mark = round(self.overall_percent())
        Exam = round(self._scores.get("Final Exam")/self.ASSESSMENT.get("Final Exam")[1] * 100)
        a3 = round(self._scores.get("A3")/self.ASSESSMENT.get("A3")[1] * 100)

        if Mark >= 85 and Exam >= 80 and a3 >= 80:
            return 7
        elif Mark >= 75 and Exam >= 70:
            return 6
        elif Mark >= 65 and Exam >= 60:
            return 5
        elif Mark >= 50 and Exam >= 45:
            return 4
        elif Mark >= 45 and Exam >= 40:
            return 3
        elif Mark >= 20:
            return 2
        else:
            return 1


            

# course1 = CSSE1001()
# scores = {
#     "A1": 90,
#     "A2": 88.5,
#     "A3": 85,
#     "Final Exam": 82
# }

# course1.set_score(scores)
# print(course1.calculate_grade())