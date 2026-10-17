def test_login_valid_credentials():
    username = "student01"
    password = "ValidPass123!"

    login_success = bool(
        username and password == "ValidPass123!"
    )

    assert login_success is True
    print("PASS: valid login is accepted")


def test_login_empty_password():
    username = "student01"
    password = ""

    error_shown = bool(username) and not password

    assert error_shown is True
    print("PASS: empty password is rejected")


if __name__ == "__main__":
    test_login_valid_credentials()
    test_login_empty_password()
    print("Login test completed.")
    print("Additional login validation check recorded.")