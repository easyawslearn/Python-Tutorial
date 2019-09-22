import textwrap

example="""This function wraps the input paragraph such that each line
in the paragraph is at most width characters long. The wrap method
returns a list of output lines."""

print("An example of text wrapping with 70 characters in line\n")
print (textwrap.fill(example,70))


print("\nAn example of text wrapping with 30 characters in line\n")
print (textwrap.fill(example,10))

print("\nAn example of text wrapping with 40 characters with start with *\n")
print (textwrap.fill(example,40,initial_indent='*'))

print("\nAn example of text wrapping with 40 characters with start with *\n")
print (textwrap.fill(example,40,subsequent_indent='*'))

example2=""" 1
                    2
                3     """
print("\nAn example of text wrapping dedent\n")
print (textwrap.dedent(example2))
