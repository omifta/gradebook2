## Actors ##

  * TeacherUser (possibly TAs too, but it's unclear if making such a fine distinction is worth the trouble).
  * StudentUser.
  * AdminUser (e.g. responsible for adding course, students, archiving, etc.)
  * VisitorUser (i.e. people who want a tour of the GradeBook).

## Essential Objects ##

  * ActivityObject
  * UserBase, StudentUser, TeacherUser
  * CourseObject
  * AssessmentScheme

## Teacher Features ##

  * Teacher view with easy to use "dashboard" collecting all important options.
    * **Add/remove/edit activities.** Activities have names, descriptions, marks, weightings, tags (for categorization), etc. (Should users be allowed to associate arbitrary objects with activities?)
    * **Browse and search student records in a course.** The list of student records has visual aids, such as line numbering, coloring of alternate rows, etc.
    * **Set page/report visibility.** For instance, you might not want to let students see their marks on some activity until everyone has had their mark entered. Or you might not want to let them see statistics of the overall class performance.
    * **Freeze mark changes.** For example, when a course is done, no more changes should be made to avoid the problem that the instructor does not notice the changes. These locks are not meant to be super-secure: freezing is just a way to avoid accidental changes.
  * **Protect marks from overwriting due to multiple users entering marks at the same time (which can occur with large classes).**
  * **Import classic GB CSV files.**
  * **Export CSV files (or the like) for use in Excel.**
  * **Record who marked what assignments.** This way students can more quickly talk to the marker for their assignments.
  * **Allow changes to the marking scheme for a single student.** For example, a student misses an assignment, and the weight of the assignment is added to their midterm exam. All other students keep the same weighting. Or a student might have missed the midterm and the instructor decides to add the percentage of the midterm to the percentage of the final.
  * **Provide an API for alternative marking schemes and reports.** Thus instructors who want to implement their own personal marking scheme, they can do so.
  * Teachers can apply StudentTags, such as "didNotWriteFinal" (which could be added automatically), or to help track teams, e.g. all the team members on Team LimePress could be tagged with "LimePress". Searching and sorting by tags would also be useful.
  * Enable random order of displays, which would be useful for deciding persentation orders etc.

## Student Features ##
  * Student view with courses and preferences "dashboard".
  * Automatic email/RSS notices (their choice) to students when their marks have been changed, or assignments are added, etc.
  * Simple what-if analysis to answers questions like "What % must I get on the final exam to get an overall grade of 86% or higher".
  * Provide charts showing where student stands with respect to the rest of the class. Include a way for students to see where they stand with respect to the overall class distribution.
  * Students can look back through all their previous courses to see their marks, comments, etc.

## General Features ##
  * CSS for all pages.
  * Use JavaScript when appropriate.
  * Save all edits, e.g. using SVN.
  * Keep an archive of all old courses, accessible by instructors.
  * Keeping a collection of marking schemes for people to choose from for their courses.
  * Statistics over courses, such as average enrollment, average grades, etc.

## Design Notes ##

Is it necessary to use a DB for this? Python serialization might be good enough. Performance may not be an issue since there are generally only a couple hundred students at most per course, and so a DB might not add much value.

By avoiding a DB, we avoid designing DB tables; coupling with a DB system; dealing with ORM.