A course is a collection of students, teachers, activities, and an assessment scheme.

A course  has a begin date, end date, and duration. This may be simply noted as "Fall 2006", say.

Course teachers are kept in special TeacherInAcourse objects to store course-specific information (e.g. notes about the course).

Students are enrolled in the course, and they are stored in special StudentInAcourse objects. They may drop the course part way through, in which case they are no longer enrolled. But for some purposes it may be useful to keep them around as having at one time been enrolled.

Courses typically have one main teacher (the head instructor), and sometimes they have teaching assistants. Some team-taught courses may have multiple instructors.

Courses have activities, such as exams and assignments. These activities are marked according to the course's assessment scheme. For example, all the activities could all be weight to add to 110% (10% bonus marks), and each activity could be out of a particular number of marks.