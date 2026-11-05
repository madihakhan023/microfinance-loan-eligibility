"""Beginner-friendly loan eligibility checks."""

from math import isfinite


MINIMUM_AGE = 21
MINIMUM_MONTHLY_INCOME = 25_000
MINIMUM_CREDIT_SCORE = 700


def check_loan_eligibility(age, monthly_income, credit_score):
	"""Return (approved, reasons) for the supplied applicant details."""
	inputs = (
		("age", age),
		("monthly income", monthly_income),
		("credit score", credit_score),
	)

	for name, value in inputs:
		if isinstance(value, bool) or not isinstance(value, (int, float)):
			return False, [f"Invalid {name}: enter a number."]
		if not isfinite(value) or not value.is_integer() if isinstance(value, float) else False:
			return False, [f"Invalid {name}: enter a finite whole number."]
		if value < 0:
			return False, [f"Invalid {name}: value cannot be negative."]

	reasons = []
	if age < MINIMUM_AGE:
		reasons.append(f"Age must be at least {MINIMUM_AGE} years.")
	if monthly_income < MINIMUM_MONTHLY_INCOME:
		reasons.append(f"Monthly income must be at least ₹{MINIMUM_MONTHLY_INCOME:,}.")
	if credit_score < MINIMUM_CREDIT_SCORE:
		reasons.append(f"Credit score must be at least {MINIMUM_CREDIT_SCORE}.")

	if reasons:
		return False, reasons
	return True, ["Applicant meets all eligibility requirements."]
if __name__ == "__main__":

    age = int(input("Enter applicant age: "))
    income = int(input("Enter monthly income: "))
    credit_score = int(input("Enter credit score: "))

    approved, reasons = check_loan_eligibility(
        age, income, credit_score
    )

    print("\nLoan Eligibility Result:")

    if approved:
        print("APPROVED")
    else:
        print("REJECTED")

    for reason in reasons:
        print("-", reason)