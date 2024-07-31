def validate_int(question, valid_answers=["1", "2", "3"]):
	choice = input(question)
	while choice not in valid_answers:
		print(f"Votre réponse est invalide. Veuillez choisir entre {valid_answers}")
		choice = input(question)
	return int(choice)