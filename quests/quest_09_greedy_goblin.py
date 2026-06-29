gold = 27
friends = 4

each_gets = gold // friends    # floor division — whole number result
goblin_keeps = gold % friends  # modulo — the leftover remainder

print(f"Each friend gets {each_gets} gold pieces.")
print(f"The goblin keeps {goblin_keeps} gold pieces.")
