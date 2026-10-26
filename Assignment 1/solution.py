def validate_records(records, required_keys):
	"""Raise an informative exception if records are not a usable list of keyed records."""
	if not isinstance(records, list):
		raise TypeError("records must be a list")

	if not records:
		raise ValueError("records cannot be empty")

	seen = set()

	for record in records:
		if not isinstance(record, dict):
			raise TypeError("all items must be dictionaries")

		for key in required_keys:
			if key not in record:
				raise KeyError(f"Missing key: {key}")

		pair = (record["state"], record["date"])
		if pair in seen:
			raise ValueError(f"Duplicate (state,date): {pair}")

		seen.add(pair)
