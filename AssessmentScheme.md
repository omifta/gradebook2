An assessment scheme determines marks for class activities. There are a number of standard assessment schemes in common use that should be supported by default, but there are also more exotic assessment schemes that individual teachers prefer.

Sometimes teachers make single-student exceptions to the marking scheme, e.g. a student who misses a midterm for a good might have the marks for that moved to the final exam. But in the same course there might be students who miss the midterm for no good reason, and so they do not get the benefit of a more highly-weighted final exam.

There needs to be some mechanism for allowing motivated teachers to create their own marking scheme. For example, perhaps an on-screen textbox could be provided wherein the teacher enters their assessment scheme for a course using Python. Variables representing activities and students could be provided in a standard way. Default marking schemes could be written in this way, so that it would be easy for teachers to see examples of how to make their own.

## Mapping Score Functions ##

One possible way to give GB users a relatively easy way to write their own scoring and related functions is to support a "function mapping" model, where the user writes mapping functions to be applied to lists of students and their marks. Users then don't have to worry about loops (unless their marking scheme contains a loop).

Suppose a student's marks are stored as a list of vectors, e.g.
```
students = [[9, 20, 31], [10, 15, 33], [10, 18, 29]]
```

Each sublist is the marks the students received on three different assessed activities. The weighting and what each activity is out of comes from the corresponding assignment objects.

To calculate a score for an individual student, suppose the teacher has this function (which is representative of a typical weighted-average marking scheme):
```
def score(s):
   return 0.25*s[0]/10 + 0.25*s[1]/20, 0.5*s[2]/35
```

In Python we can easily apply this function to all student marks:
```
marks = [score(s) for s in students]
```
Letter grades can also be calculated with a mapping function, e.g.
```
def letter_grade(raw_mark):
   m = int(ceiling(100 * raw_mark))
   if mark >= 95:
      return 'A+'
   elif 90 <= mark < 95:
      return 'A'
   elif 85 <= mark < 90:
      return 'A-'
   elif 80 <= mark < 85:
      return 'B+'
   elif 75 <= mark < 80:
      return 'B'
   elif 70 <= mark < 75:
      return 'B-'
   elif 65 <= mark < 70:
      return 'C+'
   elif 60 <= mark < 65:
      return 'C'
   elif 55 <= mark < 60:
      return 'C-'
   elif 50 <= mark < 55:
      return 'D'
   elif mark < 50:
      return 'F'
```
Thus:
```
final_grades = [letter_grade(m) for m in marks]
```
Or it could be done all in one step:
```
final_grades = [letter_grade(score(s)) for s in students]
```

Allowing the user to enter code they've written raises security and integrity issues, e.g.  the user's code might crash the program, or even try to do something malicious like access data it shouldn't know about. These issues must be taken into consideration in the design of this facility.