class Course():
    COURSE_CODE = 'Course'
    UNITS = 0
    ASSESSMENT = {}

    def calculate_grade(self) -> int:
        """ Calculates the grade of the class based on the score

        Returns:
            int: The grade achieved based on the scores
        """
        raise NotImplementedError
    
    def overall_percent(self) -> float:
        if self._scores == None:
            return None
        
        overall_percentage = 0
        for assessment in self.ASSESSMENT.keys():
            percent = self.ASSESSMENT.get(assessment)[0]
            out_of = self.ASSESSMENT.get(assessment)[1]
            score = self._scores.get(assessment)
            overall_percentage += (score/out_of) * (percent)
        
        return overall_percentage

    def set_score(self, scores: dict[str: float]) -> None:
        """ Sets the score of the course to the given scores

        Args:
            scores (dict[Assessment name: str, Assessment grade: float]): The scores for each assessment
        """
        self._scores = scores
    
    def get_course_code(self) -> str:
        """ Returns the course code
        """
        return self.COURSE_CODE
    
    def get_units(self) -> int:
        """ Returns the units """
        return self.UNITS
    
    def get_assessment(self) -> dict[str: tuple[int, int]]:
        """ Returns the assessment """
        return self.ASSESSMENT
