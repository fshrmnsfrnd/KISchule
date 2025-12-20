def append_to_each_line(file_path: str, suffix: str) -> None:
	"""Append `suffix` to every line in the file at `file_path`.

	Preserves each line's original newline (if present). The file is
	overwritten in-place.
	"""
	with open(file_path, "r", encoding="utf-8") as f:
		lines = f.read().splitlines(True)  # keep line endings

	out_lines = []
	for line in lines:
		if line.endswith("\r\n"):
			nl = "\r\n"
			core = line[:-2]
		elif line.endswith("\n") or line.endswith("\r"):
			nl = line[-1]
			core = line[:-1]
		else:
			nl = ""
			core = line
		out_lines.append(core + suffix + nl)

	with open(file_path, "w", encoding="utf-8", newline="") as f:
		f.writelines(out_lines)


# Direktaufruf: Passe Pfad und Suffix bei Bedarf an.
append_to_each_line('Recipe_Test/step_description.csv', ';0')