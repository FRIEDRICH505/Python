favorite_languages = {
'piet': 'python',
'koos': 'c',
}
friends = ['piet', 'koos']
for name in favorite_languages.keys():
    print(name.title())
if name in friends:
    language = favorite_languages[name].title()
print(f"\t{name.title()}, I see you love {language}!")