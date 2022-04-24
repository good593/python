import re

def camel_to_snake(data: str) -> str:
  _name = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", data)

  return re.sub("([a-z0-9])([A-Z])", r"\1_\2", _name).lower()

def snake_to_camel(data: str) -> str:
  REG = r"(.*?)_([a-zA-Z])"
  pattern = re.compile(REG)

  def __camel(match):
    return match.group(1) + match.group(2).upper()

  return pattern.sub(__camel, data, 0)

