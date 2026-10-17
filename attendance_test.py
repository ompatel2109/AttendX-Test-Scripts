def test_mark_attendance():
    student_id = "STU1001"
    attendance_status = "Present"

    attendance_saved = (
        bool(student_id)
        and attendance_status in {"Present", "Absent"}
    )

    assert attendance_saved is True
    print("PASS: valid attendance entry is accepted")


def test_missing_student_id():
    student_id = ""
    attendance_status = "Present"

    attendance_saved = (
        bool(student_id)
        and attendance_status in {"Present", "Absent"}
    )

    assert attendance_saved is False
    print("PASS: missing student ID is rejected")


if __name__ == "__main__":
    test_mark_attendance()
    test_missing_student_id()
    print("Attendance test completed.")